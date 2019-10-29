"""
Debug/testing module
"""

from discord.ext import commands

class Debug(commands.Cog):
    """Commands for testing/debugging purposes."""

    def __init__(self, client):
        self.client: commands.Bot = client
    
    @commands.command()
    async def test(self, ctx, arg):
        """Test command"""
        await ctx.send(len(arg))

def setup(client):
    client.add_cog(Debug(client))