import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

from stalky import cogs

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


def main():
    bot = commands.Bot(command_prefix="$")

    cog_names = [getattr(cogs, m).__name__ for m in dir(cogs) if not m.startswith("__")]
    for cog_name in cog_names:
        bot.load_extension(cog_name)
    print(f'Cogs loaded: {", ".join(bot.cogs)}')

    @bot.event
    async def on_ready():
        print(f"{bot.user} has connected to Discord!")

    bot.run(TOKEN)


if __name__ == "__main__":
    main()
