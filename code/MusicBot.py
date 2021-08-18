import discord
import asyncio
from discord.ext import commands
from musicbotConfig import *
from discord import FFmpegPCMAudio
from pathlib import Path
#import threading

member_list = []
users = ""

@client.event
async def on_ready():
    global users
    global member_list
    for guild in client.guilds:
        for member in guild.members:
            users = member.name
            member_list.append(users)
        print(member_list)



@client.event
async def on_voice_state_update(member, before, after):
    global users, is_playing, voice, player
    if Path(f'YOUR_FILEPATH_HERE{member.name}.mp3').exists():
        if not before.channel and after.channel:
            voice = await member.voice.channel.connect()
            source = FFmpegPCMAudio(f'{member.name}.mp3')
            player = voice.play(source)
            await asyncio.sleep(8)
            await voice.disconnect()
    if Path(f'YOUR_FILEPATH_HERE{member.name}.wav').exists():
        if not before.channel and after.channel:
            voice = await member.voice.channel.connect()
            source = FFmpegPCMAudio(f'{member.name}.wav')
            player = voice.play(source)
            await asyncio.sleep(8)
            await voice.disconnect()


@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("I ain't in the voice channel you mortal")

client.run(TOKEN)
