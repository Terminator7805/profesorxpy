import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'p.')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(discord.__version__)

@client.command()
async def ejemploping():
    await client.say('```async def ping \n await client.say("Pong!")```')

client.run("NDkzNzk1MjQxOTI5OTk4MzM2.DorF1g.GWKWJ6XVG95ymyKkF8is49aPcvA")
