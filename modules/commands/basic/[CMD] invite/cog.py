from discord.ext import commands
import discord

class invite(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def invite(self,ctx):
        embed=discord.Embed(title='tr3xBot Invite', description='You can invite me to any Sever with this link: \n https://discord.com/api/oauth2/authorize?client_id=830842260462632992&permissions=8&scope=bot',color=0x075FB2)
        await ctx.send(embed=embed)
def setup(bot: commands.Bot):
    bot.add_cog(invite(bot))