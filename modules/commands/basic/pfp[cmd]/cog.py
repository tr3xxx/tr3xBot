import discord
from discord.ext import commands


class pfp(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def pfp(self,ctx,*, member: discord.Member = None):
        if member is None:
            embed = discord.Embed(title="{}'s profile picture".format(str(ctx.author)[:-5]), description="")
            embed.set_image(url=ctx.author.avatar)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="{}'s profile picture".format(str(member)[:-5]), description="")
            embed.set_image(url=member.avatar)
            await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(pfp(bot))