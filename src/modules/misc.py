"""
Miscelaneous commands.
"""
# Third Party Imports
from discord.ext import commands

class Miscelaneous(commands.Cog):
    """Miscelaneous commands that don't fit with any of the other groups."""

    def __init__(self, client):
        self.client: commands.Bot = client
    
    @commands.command()
    async def about(self, ctx):
        """Show info about the bot."""

def setup(client):
    client.add_cog(Miscelaneous(client))