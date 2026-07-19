"""Global application command error handling."""
import logging

from discord import ApplicationContext, Bot
from discord.ext import commands


logger = logging.getLogger("discord")


class Ping(commands.Cog):
    """Cog for handling errors in application commands."""

    def __init__(self, bot: Bot):
        """Initialize the Ping cog."""
        self.bot = bot

    @commands.slash_command(name="ping", description="Checks the bot's latency.")
    async def ping(self, ctx: ApplicationContext):
        """Respond with the bot's latency."""
        await ctx.respond(f"Latency: {self.bot.latency * 1000:.2f} ms")

def setup(bot: Bot):
    """Set up the Ping cog."""
    bot.add_cog(Ping(bot))
