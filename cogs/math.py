import discord
from discord.ext import commands,tasks
import subprocess
import time
import os
import matplotlib.pyplot as plt


class Math(commands.Cog):

    def __init__(self,client):
        self.client=client

    #--------------commands
    @commands.command()
    async def m(self,ctx,*,arg):
        plt.text(0.11, 0.18, r'%s'%arg ,fontsize=10)
        fig = plt.gca()
        fig.axis("off")
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)
        plt.savefig('filename.png')
        await ctx.send(file=discord.File('filename.png'))

def setup(client):
    client.add_cog(Math(client))