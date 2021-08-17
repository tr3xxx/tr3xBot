import discord
from discord.ext import commands

class private(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def private(self,ctx):
        log = self.bot.get_channel(875700881360846899)
        if ctx.author.voice is None:
            await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
        else:
            if ctx.author.voice.channel.category == ctx.guild.get_channel(858020017822892092) or ctx.author.id == self.bot.get_user(633412273641095188):
                await ctx.send("Talk '"+str(ctx.author.voice.channel)+"' was made private by "+str(ctx.author.mention))
                await log.send("Talk '"+str(ctx.author.voice.channel)+"' was made private by "+str(ctx.author.mention))
                newName = (str(ctx.author.voice.channel.name)+" ["+"private"+"]")
                await ctx.author.voice.channel.edit(name=newName)
                await ctx.author.voice.channel.edit(user_limit=len(ctx.author.voice.channel.members))
                
            else:
                await ctx.send('You dont have the permission to edit channels outside the Talks Category')

        

def setup(bot: commands.Bot):
    bot.add_cog(private(bot))