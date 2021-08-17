import discord
from discord.ext import commands,tasks

class status_1(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.status_1.start()

    @tasks.loop(seconds=10.0)
    async def status_1(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="thelp "),status=discord.Status.online)

def setup(bot: commands.Bot):
    bot.add_cog(status_1(bot))