from discord.ext import commands
import discord

class github(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def github(self,ctx):

        embed=discord.Embed(title='tr3xBot GitHub Page', description='https://github.com/tr3xxx/tr3xBot',color=0x075FB2)
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(github(bot))