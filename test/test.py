import discord
from discord.ext import commands
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
    
    #warInfo = {}    
    def __init__(self, bot):
        self.bot = bot
        self.data_dir = 'data/test/users/{}/'

    @commands.command(pass_context=True)
    async def renamewar(self, ctx, warName):
        pass
        old = "olddd" #self.warinfo["Name"]
        await self.bot.say(" War [{}] renamed to [{}]".format(old, warName))
        
        
    @commands.command(pass_context=True)
    async def startwar(self, ctx, warName):
        
        self.warInfo = {}

        self.warInfo["Name"] = warName
        await self.bot.say("New war created [{}]".format(warName))

    @commands.command(pass_context=True)
    async def endwar(self, ctx, warName):
        pass
    
    @commands.command(pass_context=True)
    async def mycom(self, ctx, user : discord.User = None):
        """This does stuff!"""
        if user is None:
            user=ctx.message.author
        
        #Your code will go here
        await self.bot.say(" User: {} args: {}".format(user.name, ctx.message.mentions))


    #@roster.command(pass_context=True, name='template')
    #async def _roster_template(self, ctx, *, user : discord.User = None):
    #    '''Blank CSV template for champion import'''
    #    if user is None:
    #        user=ctx.message.author
    #    message = 'Save a copy of the template (blue text):\'
        
        
        


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
    #check_folders()
    n = Test(bot)
    bot.add_cog(n)
    #bot.add_listener(n._on_attachment, name='on_message')
