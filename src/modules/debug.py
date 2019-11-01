"""
Debug/testing module
"""
# Standard Library Imports
from typing import Optional

# Third Party Imports
from discord.ext import commands
import discord

# Local Project Imports
from utils.proxy import get_webhook

class Debug(commands.Cog):
    """Commands for testing/debugging purposes."""

    def __init__(self, client):
        self.client: commands.Bot = client
    
    @commands.command()
    async def test(self, ctx, arg):
        """Test command"""
        await ctx.send(len(arg))

    @commands.command()
    async def test_wh(self, ctx, *, content):
        wh: discord.Webhook = await get_webhook(ctx.channel, ctx.guild)
        await wh.send(content=content)


def setup(client):
    client.add_cog(Debug(client))