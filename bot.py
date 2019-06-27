import config
import discord
import discord.ext.commands
from botchecking import Botchecking
from settings import Settings
from mod import Mod
import utils

bot = discord.ext.commands.Bot('b!', None)

@bot.command()
async def help(ctx):
        embed=discord.Embed(title="Bot Cleaner Help", description="[] = optional, <> = needed", color=0x563d9)
        embed.add_field(name="settings", value="b!settings [settings] [value]", inline=False)
        embed.add_field(name="ban", value="b!ban <user1> [user2] [reason]", inline=False)
        embed.add_field(name="hackban", value="b!hackban <id1> [id2] [reason]", inline=False)
        embed.add_field(name="kick", value="b!kick <user1> [user2] [reason]", inline=False)
        embed.add_field(name="support", value="b!support", inline=False)
        embed.set_footer(text="Join here for support: https://discord.gg/4gD46QU")
        await ctx.send(embed=embed)

@bot.command()
async def support():
        await ctx.send("Join here for support: https://discord.gg/4gD46QU")

@bot.event
async def on_ready():
	print(bot.user.name)
	print(bot.user.id)

if __name__ == "__main__":
		bot.add_cog(Botchecking(bot))
		bot.add_cog(Settings(bot))
		bot.add_cog(Mod(bot))
		
bot.run(config.token)
