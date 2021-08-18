import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="-", intents = intents)
TOKEN = 'YOUR_TOKEN_HERE'
