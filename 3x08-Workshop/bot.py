import discord
from discord.ext import commands
from discord.utils import get

import asyncio
import json
import time
import random

import authkey

# Initialize bot information
client = commands.Bot(command_prefix = '!')
token = authkey.authkey

# State that we have connected to discord on first contact!
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# This event happens every single time a user writes a message!
@client.event
async def on_message(message):
    # Failsafe so the bot ignores messages it types out itself
    if message.author == client.user:
        return
    print(f"{message.author.name}: {message.content}")
    await client.process_commands(message)

# [COMMAND] Simple hello to the user command
@client.command(pass_context=True)
async def hi(ctx):
    await ctx.channel.send(f"Hello {ctx.author.name}!")

client.run(token)

