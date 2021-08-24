import discord
import asyncio
from discord.ext import commands,tasks

class status_1(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        #self.status_1.start()
        self.bot.loop.create_task(status_1.status(self))

    #@tasks.loop(seconds=10.0)
    @commands.Cog.listener()
    async def status(self):
        while True:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="thelp "),status=discord.Status.online)
            await asyncio.sleep(5)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=("on {} Servers").format(len(self.bot.guilds))),status=discord.Status.online)
            await asyncio.sleep(5)

    #@tasks.loop(seconds=10.0)
    ##    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=("on {} Servers").format(len(self.bot.guilds))),status=discord.Status.online)

def setup(bot: commands.Bot):
    bot.add_cog(status_1(bot))