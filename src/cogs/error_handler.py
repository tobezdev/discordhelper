"""Global application command error handling."""
import logging

from discord import ApplicationContext, Bot
from discord.ext import commands


logger = logging.getLogger("discord")


class ErrorHandler(commands.Cog):
    """Cog for handling errors in application commands."""

    def __init__(self, bot: Bot):
        """Initialize the ErrorHandler cog."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: ApplicationContext, error: Exception):
        """Handle errors that occur during application command execution."""
        logger.error("Error in command '%s': %s", ctx.command, str(error))
        await ctx.respond(f"An error occurred: {str(error)}", ephemeral=True)


def setup(bot: Bot):
    """Set up the ErrorHandler cog."""
    bot.add_cog(ErrorHandler(bot))
