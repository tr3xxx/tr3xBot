import discord
import asyncio
from discord.ext import commands

class status(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        #self.status_1.start()
        self.bot.loop.create_task(status.status_(self))
    
    async def member_count(self):
        members=0
        for guild in self.bot.guilds:
            members = members + guild.member_count
        return members


    #@tasks.loop(seconds=10.0)
    @commands.Cog.listener()
    async def status_(self):
        while True:
            
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= (str(await status.member_count(self))+' people')),status=discord.Status.online)
            await asyncio.sleep(5)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=(str(len(self.bot.guilds))+' servers')),status=discord.Status.online)
            await asyncio.sleep(5)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='thelp '),status=discord.Status.online)
            await asyncio.sleep(5)

    

def setup(bot: commands.Bot):
    bot.add_cog(status(bot))