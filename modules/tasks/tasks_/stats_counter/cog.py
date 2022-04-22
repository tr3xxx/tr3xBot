import random
import discord
from discord.ext import commands,tasks

class status(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.status_.start()
        
    async def member_count(self):
        members=0
        for guild in self.bot.guilds:
            members = members + guild.member_count
        return members

    @tasks.loop(seconds=5)  
    async def status_(self):
        global x

        game = iter(
            [
                str(await status.member_count(self))+' people',
                str(len(self.bot.guilds))+' servers',
                'thelp ',
            ]
        )  
        for x in range(random.randint(1, 3)):  
            x = next(game)
            
        if x == 'thelp ':
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= x),status=discord.Status.online)
        else:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= x),status=discord.Status.online)

def setup(bot: commands.Bot):
    bot.add_cog(status(bot))
    
    
 
  