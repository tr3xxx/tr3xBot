import time
import discord
from discord.ext import commands
from utils.load_cogs import load
from utils.token import token
from utils.bot_prefix import prefix

bot = commands.Bot(command_prefix=prefix(), help_command=None, intents=discord.Intents().all())

@bot.event
async def on_ready():
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot is starting...")
    await load(bot)
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Online as {0.user}".format(bot))
    
bot.run(token())

