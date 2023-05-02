"""
🌞 gm

Replace the bot token and channel id with your own values and the bot 
will autorespond with an emoji anytime someone says gm.
"""
import discord
from discord.utils import get
from discord.ext import commands
import time


intents = discord.Intents.default()

# GET A BOT TOKEN FROM https://discord.com/developers/applications
token = 'PASTE BOT TOKEN HERE' 

# Initializes client.
client = commands.Bot(command_prefix="--", intents=intents) 


@client.event 
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    
    if message.channel.id == '880359529068507166':  # REPLACE THIS WITH THE ID OF THE CHANNEL YOU WANT TO MONITOR
        print('🌞')
        if message.author.id == client.user.id:
            return
        if message.content.startswith('gm') or message.content.startswith('Gm'):
            time.sleep(2)
            await message.add_reaction('🌞')
        else:
            return
    else:
        return

#this runs the bot
client.run(token)
