"""Main entry point for the bot."""
import os
import logging
import argparse

from discord import Bot, InteractionContextType, IntegrationType, ExtensionFailed

import dotenv

parser = argparse.ArgumentParser(description="Run the Discord bot.")
parser.add_argument("--debug", "-d", action="store_true", help="Enable debug mode.")
args = parser.parse_args()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG if args.debug else logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(stream_handler)

dotenv.load_dotenv()

bot = Bot(
    auto_sync_commands=True,
    default_command_contexts={
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel
    },
    default_command_integration_types={
        IntegrationType.user_install
    }
)

@bot.event
async def on_ready():
    """Event handler for when the bot is ready."""
    print(f"Ready as {bot.user}")

for filename in os.listdir(os.path.join(os.path.dirname(__file__), "cogs")):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
        except ExtensionFailed as e:
            print(f"Failed to load extension {filename}: {e}")

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
