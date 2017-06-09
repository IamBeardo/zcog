import discord
from discord.ext import commands
#from .mcoc import class_color_codes
from .utils.dataIO import dataIO
from .utils.dataIO import fileIO
from .utils import checks
from operator import itemgetter, attrgetter
from random import randint
import time
import os
import ast
import csv
import requests
import re

class Test:


    def __init__(self, bot):
        self.bot = bot
        self.data_dir = 'data/test/users/{}/'
        self.champs_file = self.data_dir + 'champs.json'
        self.champ_re = re.compile(r'champ.*\.csv')



    async def addUser(f):
        async def inner():
            pass
        pass


    @commands.command()
    async def mycom(self, user : discord.Member):
        """This does stuff!"""
        
        #Your code will go here
        await self.bot.say(user)





    async def _on_attachment(self, msg):
        channel = msg.channel
        prefixes = tuple(self.bot.settings.get_prefixes(msg.server))
        if not msg.attachments or msg.author.bot or msg.content.startswith(prefixes):
            return
        for attachment in msg.attachments:
            if self.champ_re.match(attachment['filename']):
                await self.bot.send_message(channel,
                        "Found a CSV file to import.  Load new champions?  Type 'yes'.")
                reply = await self.bot.wait_for_message(30, channel=channel,
                        author=msg.author, content='yes')
                if reply:
                    #await self._parse_champions_csv(msg, attachment)
                    await self.bot.send_message(channel, "OK fffCOOL")
                else:
                    await self.bot.send_message(channel, "Did not import!!")





#-------------- setup -------------
def check_folders():
    if not os.path.exists("data/test/users"):
        print("Creating data/test/users folder...")
        os.makedirs("data/test/users")


def setup(bot):
    check_folders()
    n = Test(bot)
    bot.add_cog(n)
    bot.add_listener(n._on_attachment, name='on_message')
