from discord.ext import commands

class Say(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def say(self, ctx: commands.Context ,*, arg: str = None): 
        await ctx.channel.purge(limit=1) 
        if arg is None:
            await ctx.send("What should i say ?")
        else:
            await ctx.send(arg)

def setup(bot: commands.Bot):
    bot.add_cog(Say(bot))