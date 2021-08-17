from discord.ext import commands
from config import BOT_LOG, CREATE_TICKET_CHANNEL, GUILD_ID,SUPPORT_CATEGORY

class solved(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def solved(self,ctx):
        log = self.bot.get_channel(BOT_LOG)
        guild = self.bot.get_guild(GUILD_ID)
        if ctx.channel.category == self.bot.get_channel(SUPPORT_CATEGORY):
            if ctx.channel != self.bot.get_channel(CREATE_TICKET_CHANNEL):
                members = ctx.channel.members
                for member in members:
                    if member != guild.me:
                        await member.send(str(ctx.channel.name)+" has been solved and closed by "+str(ctx.author))
                await ctx.channel.delete()
                await log.send("Ticket {} has been solved by {}".format(ctx.channel,ctx.author))
              

def setup(bot: commands.Bot):
    bot.add_cog(solved(bot))