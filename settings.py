from discord.ext import commands
from db import database
import utils

class Settings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def settings(self, ctx, setting: str = None, value: str = None):
		if ctx.author.Permissions.administrator:
			settingsList = ['confirmedbot.action', 'botfinder.acceptablerisk', "botfinder.action"]
			if setting and setting.lower() in settingsList:
				await utils.set_setting(ctx.guild, setting, value)
				await ctx.send(f'Successfully set {setting} to {value}')
				return
			await ctx.send("""Settings:
			confirmedBot.action,
			botFinder.acceptableRisk,
			botFinder.action,
			""")
		else:
			await ctx.send("You need to be an admin")
