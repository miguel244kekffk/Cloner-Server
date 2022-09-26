import os
import discord
from discord.ext import commands
import asyncio 
import logging
import random 
from colorama import init
from colorama import Fore, Style
import requests
import json
import datetime
import random
import threading
from os import system
import random
from pystyle import Colorate, Colors, Center
import time
import threading

init()
os.system("cls" or "clear")

print('{}\n{}[>] TOKEN ↓ {}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
token = input('')
print('{}\n{}[>] PREFIX ↓ {}'.format(Fore.RESET, Fore.LIGHTBLUE_EX, Fore.RESET))
prefix = input('')
client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                      self_bot=True)

client.remove_command('help')
header = {"Authorization": f'Bot {token}'}
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

intents = discord.Intents.all()
intents.members = True

@client.event
async def on_ready():
    print('{}\n {} [/] Command :{} {}copy\n'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET, prefix))
    print('{}\n {} [ ¯\_(ツ)_/¯ ] Logged in as :{} {}\n'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET, client.user.name))


@client.command()
async def copy(ctx): 
    await ctx.message.delete()
    wow = await client.create_guild(f'cloner{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'cloner{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            print(ctx.guild.roles)
    for role in ctx.guild.roles[::-1]:
        if role.name != "Test":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print('{}\n {} [-] Created role :{} {}\n'.format(Fore.RESET, Fore.LIGHTRED_EX, Fore.RESET, prefix, role.name))
            except:
                break

client.run(token, bot=False)

#by notlow
