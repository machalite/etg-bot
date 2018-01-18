import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
       await client.send_message(message.channel, 'Pong!')

client.run('MzE1NDM0MDA3MjcxNTcxNDU3.DUHUdQ.HgUB_BKvaNT790BcmIn0PYrRU5A')
