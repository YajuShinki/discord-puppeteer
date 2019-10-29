"""
Miscelaneous commands.
"""
# Third Party Imports
from discord.ext import commands
from discord import Embed

class Miscelaneous(commands.Cog):
    """Miscelaneous commands that don't fit with any of the other groups."""

    def __init__(self, client):
        self.client: commands.Bot = client
    
    @commands.command()
    async def about(self, ctx):
        """Show info about the bot."""
        #TODO write about section

def setup(client):
    client.add_cog(Miscelaneous(client))