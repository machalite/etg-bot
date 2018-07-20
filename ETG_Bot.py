import discord
import configparser
# import asyncio
from query import search_gun, search_item, search_gundead, search_name
#
config = configparser.ConfigParser()
config.read("strings.conf")

TOKEN = config.get('settings', 'token')
GREETINGS = config.get('log', 'greetings')
PREFIX = config.get('settings', 'prefix')
COMMAND_SEARCH = PREFIX + config.get('keywords', 'search_name')
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Hello my name is ammonomicon bot !!')


@client.event
async def on_message(message):
    input_msg = message.content
    if input_msg.startswith(PREFIX + config.get('keywords', 'greet')):
        await client.send_message(message.channel, 'Say hello')
        await client.wait_for_message(author=message.author, content='hello')
        await client.send_message(message.channel, 'Hello.')
    if message.content.startswith(COMMAND_SEARCH):
        index = len(PREFIX + config.get('keywords', 'search_name')) + 1
        input_name = input_msg[index:]
        # await client.send_message(message.channel, input_name)
        names = search_name(input_name)
        if len(names) > 0:
            str_result = "```Search results for '" + input_name + "' :\n"
            str_result = str_result + "-------------------------------------\n"
            for name in names:
                str_result = str_result + name + "\n"
            str_result = str_result + "```"
        elif len(names) == 1:
            str_result = "Result for '" + input_name + "' :\n"
            str_result = str_result + "-------------------------------------\n"
        else:
            str_result = "No result for '" + input_name + "'"
        await client.send_message(message.channel, str_result)

client.run(TOKEN)
