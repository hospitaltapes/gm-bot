"""
🌞 gm

written by Dexter Tortoriello (@houses)
"""
import discord
from discord.utils import get
from discord.ext import commands
import time

#INTENTS MAKE IT SO get_user_named() WORKS ~ MUST ENABLE IN DEV PORTAL AS WELL.
intents = discord.Intents.default()

# Bot token from discord developers page
token = 'ODc3OTU1ODY2MjE5OTA5MTYx.YR6KHg.2C3F_osqoGUjBZ0eq_GZUWB_Ifg'

# Initializes client.
client = commands.Bot(command_prefix="--", intents=intents)  # change the prefix according to your needs


@client.event  # event decorator/wrapper
# Does something as soon as you connect to the server.
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.channel.id == 880359529068507166:
        print('🌞')
        if message.author.id == client.user.id:
            return
        if message.content.startswith('gm') or message.content.startswith('Gm'):
            time.sleep(3)
            await message.add_reaction('🌞')
        else:
            return
    else:
        return

#this runs the bot
client.run(token)
