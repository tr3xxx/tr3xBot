import discord
from discord.ext import commands
from config import check_log_channel

class embed(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def embed(self,ctx, *, arg: str = None): 
        log = self.bot.get_channel(await check_log_channel(ctx))
        if arg is None:
            await ctx.send("To create an Embed use the following template (Title,Describtion,Footer)")
        else:            
            args = arg.split(',') 
            if len(args) == 3:
                embed = discord.Embed(title = args[0],
                                        description = args[1],
                                        color=0x075FB2)
                embed.set_footer(text=args[2])
                await ctx.channel.purge(limit=1)
                await ctx.send(embed=embed)
                await log.send("Embed has been created in {} by {}".format(ctx.channel.mention,ctx.author))
        

def setup(bot: commands.Bot):
    bot.add_cog(embed(bot))