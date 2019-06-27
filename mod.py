import discord
from discord.ext import commands
from db import database


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, members: commands.Greedy[discord.Member], *, reason: str):
        message=""
        for member in members:
            await member.ban(reason=reason)
            message = message+"\n:white_check_mark: {}#{} Banned.".format(member.name, member.discriminator)
        await ctx.send(message)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, members: commands.Greedy[discord.Member], *, reason: str):
        message=""
        for member in members:
            await member.kick(reason=reason)
            message = message+"\n:white_check_mark: {}#{} Kicked.".format(member.name, member.discriminator)
        await ctx.send(message)
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def hackban(self, ctx, ids: commands.Greedy[int], *, reason: str):
        message=""
        for id in ids:
            guild = ctx.guild
            await guild.ban(discord.Object(id=id), reason=reason)
            message = message+"\n:white_check_mark: {} Banned.".format(id)
        await ctx.send(message)
