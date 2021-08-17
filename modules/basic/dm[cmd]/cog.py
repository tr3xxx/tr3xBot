import discord
from discord.ext import commands

class dm(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def dm(self,ctx,member: discord.Member = None,*, arg):
        await ctx.channel.purge(limit=1)
        if arg is None:
            await ctx.author.send("What should i send? (ex. tdm @tr3xBot I like you)")
        else:
            if member is None:
                await ctx.author.send(arg)
            else:
                await member.send(arg)

def setup(bot: commands.Bot):
    bot.add_cog(dm(bot))