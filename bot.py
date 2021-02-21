import discord
import os
from dotenv import load_dotenv
from discord.ext import commands,tasks
from itertools import cycle

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = 'pls', intents = intents)

@client.event
async def on_ready():
    print("pokebot is ready")
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        

#################################### cog #################################################
@client.command()
@commands.has_permissions(manage_messages=True)
async def load(ctx,extensions):
    client.load_extension(f'cogs.{extensions}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def unload(ctx,extensions):
    client.unload_extension(f'cogs.{extensions}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def reload(ctx,extensions):
    client.unload_extension(f'cogs.{extensions}')
    client.load_extension(f'cogs.{extensions}')
    
##############################################################################################

load_dotenv('.env')
client.run(os.getenv('BOT_TOKEN'))