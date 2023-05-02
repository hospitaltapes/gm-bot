import discord
from discord.ext import commands
import config

intents = discord.Intents.default()
client = commands.Bot(command_prefix="--", intents=intents) 

@client.event 
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.channel.id != config.CHANNEL_ID or message.author.id == client.user.id:
        return

    content = message.content.lower()
    if content.startswith('gm'):
        await client.wait_for('message', timeout=2)
        await message.add_reaction('🌞')

client.run(config.TOKEN)
