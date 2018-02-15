import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Hello my name is ammonomicon bot !!')

@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        await client.send_message(message.channel, 'Say hello')
        msg = await client.wait_for_message(author=message.author, content='hello')
        await client.send_message(message.channel, 'Hello.')

client.run('MzE1NDM0MDA3MjcxNTcxNDU3.DWayYg.FxiOaWP43azdiyT4fgYwLljjZYo')
