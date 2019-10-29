"""
Basic commands
"""

from discord.ext import commands
from discord import Embed

class Debug(commands.Cog):
    """Basic commands for adding/removing/viewing puppets."""

    def __init__(self, client):
        self.client: commands.Bot = client
    
    @commands.command()
    async def find(self, ctx, arg):
        embed = Embed()

    @commands.command()
    async def info(self, ctx, arg):
        embed = Embed()

    @commands.command(name='list')
    async def _list(self, ctx, arg):
        embed = Embed()

    @commands.command()
    async def new(self, ctx, arg):
        embed = Embed()
    
    @commands.command()
    async def remove(self, ctx, arg):
        embed = Embed()
        
def setup(client):
    client.add_cog(Debug(client))