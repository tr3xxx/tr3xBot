import discord
from discord.ext import commands
import pyshorteners

class link_shorter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def shortlink(self,ctx,arg: str = None):

        if arg is None:
            await ctx.send('To short a link type tshortlink <long-link>')
        else:
            try:
                s = pyshorteners.Shortener()
                url = s.tinyurl.short(str(arg))
                await ctx.send(f'Your short link is ready: {url}')
            except Exception as err:
                await ctx.send(err)
        
    
        

def setup(bot: commands.Bot):
    bot.add_cog(link_shorter(bot))