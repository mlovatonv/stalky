import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

bot = commands.Bot(command_prefix="#")


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.content == "ping":
        response = "pong"
        await message.channel.send(response)


@bot.command(name="99")
async def hi(ctx):
    response = "choke me"
    await ctx.send(response)


@client.event
async def on_error(event, *args, **kwargs):
    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise


client.run(TOKEN)
