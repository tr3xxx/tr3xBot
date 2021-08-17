from discord.ext import commands

class solved(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def solved(self,ctx):
        log = self.bot.get_channel(875700881360846899)
        guild = self.bot.get_guild(718926812033581108)
        if ctx.channel.category == self.bot.get_channel(875681228303532032):
            if ctx.channel != self.bot.get_channel(875681346666774578):
                members = ctx.channel.members
                for member in members:
                    if member != guild.me:
                        await member.send(str(ctx.channel.name)+" has been solved and closed by "+str(ctx.author))
                await ctx.channel.delete()
                await log.send("Ticket {} has been solved by {}".format(ctx.channel,ctx.author))
              

def setup(bot: commands.Bot):
    bot.add_cog(solved(bot))