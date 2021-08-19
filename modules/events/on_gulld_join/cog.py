import discord
import sqlite3
from discord.ext import commands
from config import check_log_channel, check_welcome_channel


class on_guild_join(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_guild_join(self,member):
        pass
            

def setup(bot: commands.Bot):
    bot.add_cog(on_guild_join(bot))