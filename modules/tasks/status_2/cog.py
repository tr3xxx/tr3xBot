import discord
from discord.ext import commands,tasks

class status_2(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.status_2.start()

    @tasks.loop(seconds=10.0)
    async def status_2(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=("on {} Servers").format(len(self.bot.guilds))),status=discord.Status.online)

def setup(bot: commands.Bot):
    bot.add_cog(status_2(bot))