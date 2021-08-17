import discord
from discord.ext import commands

class end(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def end(self,ctx):
       log = self.bot.get_channel(875700881360846899)
       if ctx.author.voice is None:
            await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
       else:
            if ctx.author.voice.channel.category == ctx.guild.get_channel(858020017822892092) or ctx.author.id == self.bot.get_user(633412273641095188):
                await ctx.send("Talk '"+str(ctx.author.voice.channel)+"' got deleted by "+str(ctx.author.mention))
                await log.send("Talk '"+str(ctx.author.voice.channel)+"' got deleted by "+str(ctx.author.mention))
                await ctx.author.voice.channel.delete()
                
                
            else:
                await ctx.send('You dont have the permission to edit channels outside the Talks Category')

        

def setup(bot: commands.Bot):
    bot.add_cog(end(bot))