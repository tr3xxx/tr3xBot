from discord.ext import commands
from random import choice

class die(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def die(self,ctx):
        responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
        await ctx.send(choice(responses))

def setup(bot: commands.Bot):
    bot.add_cog(die(bot))