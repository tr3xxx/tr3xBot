import discord
from discord.ext import commands

class talkname(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def talkname(self,ctx,*,arg: str = None):
        log = self.bot.get_channel(875700881360846899)
        if arg is None:
            await ctx.send("To give a channel a custom name use the followning template (ex. ttalkname x x x x x x )")
        else:
            if ctx.author.voice is None:
                await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
            else:
                if ctx.author.voice.channel.category == ctx.guild.get_channel(858020017822892092) or ctx.author.id == self.bot.get_user(633412273641095188):
                    if len(arg) > 7:
                        await ctx.send("Please choose a shorter Talkname")
                    else:
                        newName = (str(ctx.author.voice.channel.name)+" ["+str(arg)+"]")
                        await ctx.send("Talkname of '"+str(ctx.author.voice.channel)+"' got changed by "+str(ctx.author.mention)+" to '"+newName+"'")
                        await log.send("Talkname of '"+str(ctx.author.voice.channel)+"' got changed by "+str(ctx.author.mention)+" to '"+newName+"'")
                        await ctx.author.voice.channel.edit(name=newName)
                    
                else:
                    await ctx.send('You dont have the permission to edit channels outside the Talks Category')

        

def setup(bot: commands.Bot):
    bot.add_cog(talkname(bot))