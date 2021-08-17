import discord
from discord.ext import commands

class clear(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self,ctx,arg: str = None):
        log = self.bot.get_channel(875700881360846899)
        if arg is None:
            await ctx.channel.purge(limit=1)
            await ctx.author.send("How many Messaages should i delete? (tclear x)")
        else:
            args = arg.split(' ')
            if len(args) == 1:
                if args[0].isdigit():
                        count = int(args[0])+1
                        deleted = await ctx.channel.purge(limit=count)
                        embed = discord.Embed(title = '{} Messages deleted.'.format(len(deleted)-1),
                                        color=0x075FB2)
                        await ctx.channel.purge(limit=1)
                        await ctx.send(embed=embed, delete_after= 10.0)
                        await log.send("{} Messages got deleted in {} by {}".format(count,ctx.channel.mention,ctx.author))
        

def setup(bot: commands.Bot):
    bot.add_cog(clear(bot))