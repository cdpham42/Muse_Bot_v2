# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 21:05:55 2018

@author: cdpha
"""

# %%

# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord

with open("token.txt") as f:
    TOKEN = f.read()

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!muse hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)