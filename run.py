import requests
import json
import os  
from os import environ, path
import discord
from dotenv import load_dotenv
from discord.ext import commands

if(path.exists('bot.env')):
    try:
        load_dotenv(dotenv_path='bot.env')
        # settings
        Discord_bot_token = environ.get('discord_bot_token')            
        miner_ip = environ.get('miner_ip')
    except Exception as e:
        pass

else: 
    Discord_bot_token = str(os.environ['discord_bot_token'])
    miner_ip = str(os.environ['miner_ip'])

stats_url = f'http://{miner_ip}/miner.json'
height_url = "https://api.helium.io/v1/blocks/height"

def get_stats():
    h = requests.get(height_url, timeout=20)
    datah = h.json()
    actual_height = datah["data"]["height"]
    x = requests.get(stats_url, timeout=20)
    data = x.json()
    height = str(data["height"][0]).split('    ')[1]
    temp0 = data["temp0"]
    temp1 = data["temp1"]
    uptime = data["miner"]["State"]
    status = data["miner"]["Status"]
    return actual_height, height, temp0, temp1, uptime, status


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("bot is online.")

@bot.command()           
@commands.has_permissions(administrator=True)

async def stats(ctx):
    actual_height, height, temp0, temp1, uptime, status = get_stats()
    embed1 = discord.Embed(title="Bobcat Miner Stats", color=0x00F500)
    embed1.add_field(name="Status", value=str(status), inline=False)
    embed1.add_field(name="uptime", value=str(uptime), inline=False)
    embed1.add_field(name="temp1", value=str(temp1), inline=False)
    embed1.add_field(name="temp0", value=str(temp0), inline=False)
    embed1.add_field(name="Miner's height", value=str(height), inline=False)
    embed1.add_field(name="Blockchain's height", value=str(actual_height), inline=False)
    await ctx.channel.send(embed=embed1)

bot.run(Discord_bot_token)