from db import database
import re
import config

import discord
import datetime


async def get_setting(guild: discord.Guild, setting: str):
	setting = setting.lower()
	settings = await database.servers.find_one({"_id": guild.id})

	return settings[setting.replace('.', '/')] # we have to replace . with slash to avoid making it into an object in mongo


async def set_setting(guild: discord.Guild, setting: str, value: any):
	if setting == 'botfinder.acceptablerisk':
		value = int(value)
	else:
		setting = setting.lower()
		value = value.lower()

	setting = setting.replace('.', '/') # we have to replace . with slash to avoid making it into an object in mongo
	await database.servers.update_one({"_id": guild.id}, {"$set": {setting: value}}, upsert = True)


def is_newer_than_days(user: discord.User, days: int):
	if user.created_at > datetime.datetime.utcnow() - datetime.timedelta(days=days):
		return True
	return False


def has_default_avatar(user: discord.User):
	return user.avatar == user.default_avatar

async def calculate_risk(member: discord.Member):
	risk = 0
	if re.search(config.number_regex, member.name):
		risk += 1
	if is_newer_than_days(member, 14):
		risk += 1
	if has_default_avatar(member):
		risk += 1
	if await database.names.find_one({"_id":member.name.lower().rstrip('0123456789')}):
		risk += 1
	
	return risk

async def botfinder_action(member: discord.Member):
	action = await get_setting(member.guild, 'botfinder.action')

	if action == 'ban':
		await member.ban()
		return
	if action == 'kick':
		await member.kick()
		return

async def confirmedbot_action(member: discord.Member):
	action = await get_setting(member.guild, 'confirmedbot.action')

	if action == 'ban':
		await member.ban()
		return
	elif action == 'kick':
		await member.kick()
		return
