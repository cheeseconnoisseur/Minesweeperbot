#thanks

import discord
import asyncio
import random
from random import randint
import pickle
import os
#from check import checker
from discord.ext import commands
from discord.ext.commands import bot
import datetime
import urllib.request
from bs4 import BeautifulSoup
#import requests
import urllib
#import yaml
import json
import math
import time
#from pytube import YouTube
#from PIL import Image
#import json
import sys


print("hi")
Client = discord.Client()
client = commands.Bot(command_prefix = "?")



#def play(level):



@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(game=discord.Game(name='your mum'))


@client.event
async def on_message(message):
    if message.content.upper().startswith('!PLAY'):
        args = message.content.split(" ")
        #play(args[1])
        if args[1] == 'easy':
            bnum = 4
            gsize = 5
        elif args[1] == 'medium':
            bnum = 8
            gsize = 6
        elif args[1] == 'hard':
            bnum = 30
            gsize = 8
        elif args[1] == 'crazy':
            bnum = 50
            gsize = 10
        print("lol")
        grid = []
        temparray=[]
        for i in range(gsize):
            temparray= []
            for j in range(gsize):
                tg = 0
                temparray.append(tg)
            grid.append(temparray)

        while (bnum is not 0):
            x = random.randint(0,gsize - 1)
            y = random.randint(0,gsize - 1)
            if grid[y][x] == 'B':
                print("oopsie")
            elif grid[y][x] == 0:
                grid[y][x] = 'B'
                bnum = bnum - 1

        #for i in range(gsize):
            #print(grid[i])

        for y in range(gsize):
            for x in range(gsize):
                if grid[y][x] == 'B':
                    print("lol")
                elif grid[y][x] is not 'B':
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if (y + i) >= 0 and (x + j) >= 0 :
                                try:
                                    if grid[y + i][x + j] == 'B':
                                        grid[y][x] = grid[y][x] + 1
                                except: pass



        #for i in range(gsize):
            #print(grid[i])
            #await client.send_message(message.channel,grid[i])

        text = ""

        for i in range(gsize):
            for j in range(gsize):
                emoji = ""
                temp = grid[i][j]
                if temp == "B": emoji = "bomb"
                if temp == 0: emoji = "white_large_square"
                if temp == 1: emoji = "one"
                if temp == 2: emoji ="two"
                if temp == 3: emoji ="three"
                if temp == 4: emoji ="four"
                if temp == 5: emoji ="five"
                if temp == 6: emoji ="six"
                if temp == 7: emoji ="seven"
                if temp == 8: emoji ="eight"
                text += "||:{}:||".format(emoji)
            text += "\n"
        await client.send_message(message.channel,text)


    if message.content.upper().startswith('!DSAY ') and message.author.id != '402062055303151627':
        args = message.content.split(" ")
        await client.send_message(message.channel, "{}".format(" ".join(args[1:])))
        await client.delete_message(message)

    if message.content.upper().startswith('!HELP'):
        await client.send_message(message.channel, "use !play and then a difficulty (easy, medium,hard,master), eg. !play easy")




client.run('token', reconnect=True)
