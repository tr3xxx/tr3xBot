import discord
from discord.ext import commands

class kill(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def kill(self,ctx,member: discord.Member = None):
        if member is None:
            await ctx.channel.purge(limit=1)
            await ctx.send("{}".format(ctx.message.author.mention)+" killed himself")
        else:
            await ctx.send("{} killed {}".format(ctx.message.author.mention,member.mention))

def setup(bot: commands.Bot):
    bot.add_cog(kill(bot))