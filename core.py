import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='#', description="type #help")

@bot.event
async def on_ready():
    print (bot.user.name)
	print ("has come to kick your ass !")
	
@bot.command()