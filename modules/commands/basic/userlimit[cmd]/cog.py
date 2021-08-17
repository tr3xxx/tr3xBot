from discord.ext import commands

class userlimit(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def userlimit(self,ctx,*,arg: str = None):
        log = self.bot.get_channel(875700881360846899)
        if arg is None:
            await ctx.send("To give a channel a userlimit use the followning template (ex. tuserlimit x )")
        else:
            if ctx.author.voice is None:
                await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
            else:
                if ctx.author.voice.channel.category == ctx.guild.get_channel(858020017822892092) or ctx.author.id == self.bot.get_user(633412273641095188):
                    if int(arg) >= 99:
                        await ctx.send("Value should be less than or equal to 99")
                    else:
                        await ctx.send("Userlimit of '"+str(ctx.author.voice.channel)+"' got changed by "+str(ctx.author)+" from "+str(ctx.author.voice.channel.user_limit)+" to "+arg)
                        await log.send("Userlimit of "+str(ctx.author.voice.channel)+" was changed by "+str(ctx.author)+" from "+str(ctx.author.voice.channel.user_limit)+" to "+arg)
                        await ctx.author.voice.channel.edit(user_limit=int(arg))
                        
                        
                else:
                    await ctx.send("You dont have the permission to edit channels outside the Talks Category")

        

def setup(bot: commands.Bot):
    bot.add_cog(userlimit(bot))