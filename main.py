import time
import discord
from discord.ext import commands
from utils.load_cogs import load
from utils.token import token
from utils.bot_prefix import prefix
from discord.gateway import DiscordWebSocket



class MyDiscordWebSocket(DiscordWebSocket):

    async def send_as_json(self, data):
        if data.get('op') == self.IDENTIFY:
            if data.get('d', {}).get('properties', {}).get('$browser') is not None:
                data['d']['properties']['$browser'] = 'Discord Android'
                data['d']['properties']['$device'] = 'Discord Android'
        await super().send_as_json(data)


DiscordWebSocket.from_client = MyDiscordWebSocket.from_client
bot = commands.Bot(command_prefix=prefix(), help_command=None, intents=discord.Intents().all())


@bot.event
async def on_ready():
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot is starting...")
    await load(bot)
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Online as {0.user}".format(bot))
    
bot.run(token())

