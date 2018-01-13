import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "*")

@client.event
async def on_ready():
    print("Bot je připraven")
    
@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!HATE'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Fuck You!" % (userID))
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" (" ".join(args[1:])))
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")
    if message.content == "shit":
        await client.send_message(message.channel, ":poop:")
    if message.content == "Sex":
        await client.send_message(message.channel, ":point_right::skin-tone-5: :ok_hand::skin-tone-1: ")
    

client.run("NDAxNDI2NTA1ODU2NTgxNjMy.DTqCqQ.p1NyX3peYQz6eDrtX8fNmgrYxLo")
