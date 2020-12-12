import discord
import asyncio
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="&", intents=intents)

TOKEN = open("token.txt","r").read()

@Bot.event
async def on_ready():
    print("Uyandım artık hazırım!")

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="sohbet")
    await channel.send(f"{member} Hoş geldin lan")
@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="sohbet")
    await channel.send(f"{member} Siktir oldu gitti")

@Bot.command()
async def ordamısın(msg):
    await msg.send("Burdayım gardaş")

@Bot.command()
async def komutlar(msg):
    await msg.send("```&ordamısın``` ```&youtube``` ```&instagram``` ```&davet```")
	
@Bot.command()
async def youtube(msg):
    await msg.send("```Eklenecektir```")

@Bot.command()
async def instagram(msg):
    await msg.send("https://www.instagram.com/imustafa8/")

@Bot.command()
async def davet(msg):
    await msg.send("https://discord.gg/ru8Esxeb")
	
@Bot.command()
async def kurucular(msg):
    await msg.send("```Hybris#7718``` ```YouAreDone#3528```")

Bot.run(TOKEN)