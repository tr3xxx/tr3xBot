import discord
from discord.ext import commands

class hug(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hug(self,ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("{} hugs himself :smiling_face_with_tear:".format(ctx.message.author.mention))
        else:
            await ctx.send("{} hugs {}".format(ctx.message.author.mention,member.mention))
    

def setup(bot: commands.Bot):
    bot.add_cog(hug(bot))