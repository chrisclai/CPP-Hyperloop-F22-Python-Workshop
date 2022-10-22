import discord
from discord.ext import commands
from discord.utils import get

import asyncio
import json
import time
import random

# File Dependencies
import authkey

# Global Variables
numgame_start = False
numgame_answer = 0
guesses = 0
timealive = 0

# Initalize bot information
client = commands.Bot(command_prefix='!')
token = authkey.authkey

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f"{message.author.name}: {message.content}")
    await client.process_commands(message)

@client.command(pass_context=True)
async def hi(ctx):
    await ctx.channel.send(f"Hi {ctx.author.name}!")

@client.command(pass_context=True)
async def numgame(ctx, num):
    global numgame_start
    global numgame_answer
    global guesses

    if not numgame_start:
        await ctx.channel.send("No number game started yet, generating random number...")
        numgame_answer = random.randrange(0,100,1)
        print(numgame_answer)
        time.sleep(3)
        await ctx.channel.send("Number between 0-100 generated, use !numgame [arg] again to begin playing!")
        numgame_start = True
    else:
        try:
            num = int(num)
            if num > numgame_answer:
                guesses += 1
                await ctx.channel.send(f"Your number is {num}. Too high, try again! You have guessed {guesses} times.")
            elif num < numgame_answer:
                guesses += 1
                await ctx.channel.send(f"Your number is {num}. Too low, try again! You have guessed {guesses} times.")
            else:
                await ctx.channel.send(f"Your number is {num}. My number was {numgame_answer}. 🎉🎉🎉Congrats, you win!🎉🎉🎉 Your score: {guesses} guesses.")
                
                # Reset parameters
                guesses = 0
                numgame_start = False
                numgame_answer = 0
        except:
            await ctx.channel.send(f"Hey, that's not a number! Try again!")

@client.command(pass_context=True)
async def image(ctx):
    await ctx.channel.send(f"Showing image from host computer...")
    await ctx.channel.send(file=discord.File('captured.jpg'))
    await ctx.channel.send(file=discord.File('mask.jpg'))

client.run(token)