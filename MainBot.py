
from discord.ext.commands import Bot
from discord import Game
import discord
import random
import requests
import os


# def main settings
prefix = ("|")
token = 'NTMwODc3MzUwMzM0OTU1NTIx.XNN5fA.gc5Setp3m182NmUO7flcdnTJAnY'

# change main settings
client = Bot(command_prefix=prefix)
client.remove_command("help")


# Program start up
@client.event
async def on_ready():
    await client.change_presence(game = Game(name = "with femboys"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# function class
class messageFun():
    def __init__(self, message):
        self.message = message

    def url(self, strings : str, additive = None):
        url = strings + additive
        response = requests.get(url)
        return(response.json())


    async def sheriBot(self, yiffType):
        value = self.url("https://sheri.bot/api/v2/", yiffType)["url"]
        await client.send_message(self.message.channel, value)

    async def dadJoke(self):
        value = self.url("https://icanhazdadjoke.com/slack")["attachments"][0]["text"]
        await client.send_message(self.message.channel, value)


@client.event
async def on_member_join(member):
    roleMember = discord.utils.get(member.server.roles, name= 'Members')
    roleNsfw = discord.utils.get(member.server.roles, name= 'Nsfw')
    await client.add_roles(member, roleMember)
    await client.add_roles(member, roleNsfw)
    print("Added: " + str(member))


@client.event
async def on_message(message):
    extra = messageFun(message)

    print(message.author)
    print(message.content)


    # await client.send_message()

    # bot replying to self stops
    if message.author == client.user:
        return

    # print(message.author)
    # if message.author == message.author:
    #     await client.send_message(message.channel, message.content)

    #Hello
    if message.content.startswith('|hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    #Beese Churger
    elif message.content.startswith('beese churger'):
        await client.delete_message(message)
        await client.send_message(message.channel, "Welcome to Mcdownald's \n Do you want a phucking \n Beese Churger?")

        
    if message.content.startswith("|joke"):
        await extra.dadJoke()

    if message.content.startswith("|yiff"):
        await extra.sheriBot("yiff")


client.run(str(os.environ.get('BOT_TOKEN')))
