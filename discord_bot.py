import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='botfix', description='description here')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.command()
"""Description of command goes here"""
async def hello():
    await bot.say('Hello

bot.run('MzE1NDM0MDA3MjcxNTcxNDU3.DUHUdQ.HgUB_BKvaNT790BcmIn0PYrRU5A')
