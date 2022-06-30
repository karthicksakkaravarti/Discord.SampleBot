import csv
import io
import logging
import typing

import discord
from asgiref.sync import sync_to_async
from discord.ext import commands


class SimpleCog(commands.Cog, name='SimpleBot'):

    def __init__(self, bot, logger=None):
        self.bot = bot
        self.logger = logger


    @commands.guild_only()
    @commands.command(help='Create New Channel')
    async def newchannel(self, ctx):
        guild_id = ctx.guild.id
        guild_name = ctx.message.guild.name
        print(guild_id)
        desc = f'Will Create New Channel. Under Implementation'
        embed = discord.Embed(description=desc)

        await ctx.send(embed=embed)
