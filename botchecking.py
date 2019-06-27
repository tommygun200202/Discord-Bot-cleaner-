from discord.ext import commands
import discord
from db import database
import utils

class Botchecking(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_member_join(self, member: discord.Member):
		# check if the user is a confirmed bot
		if await database.bots.find_one({'_id': member.id}):
			await utils.confirmedbot_action(member)



		#check if the bot is a suspected bot
		if await utils.calculate_risk(member) > await utils.get_setting(member.guild, 'botfinder.acceptablerisk'):

			await utils.botfinder_action(member)

	@commands.command()
	async def confirmbot(self, ctx, id: int):
		if ctx.author.id in [99847272669413376, 158594933274574849, 241287492660101121]:
			database.bots.replace_one({"_id": id}, {"_id": id}, upsert=True)

			for guild in self.bot.guilds:
				user = await self.bot.fetch_user(id)
				if user in guild.members:
					member = guild.get_member(id)
					await utils.confirmedbot_action(member)
					
			await ctx.send('Added the id to the list')
