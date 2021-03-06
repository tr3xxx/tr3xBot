import numpy as np
from discord.ext import commands
from utils.check_log import log
from utils.check_voicehub import get_vc

class private(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def private(self,ctx):
        result =  await get_vc()
        result_array = np.array(result)
        try:
            for i in range(0,len(result_array)):
                id = int(str(result_array[i])[2:-2])
                global vc
                vc = self.bot.get_channel(id)
                log_channel = self.bot.get_channel(log(ctx))
                if vc is None:
                    continue
                if ctx.author.voice is None:
                    await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
                else:
                    if ctx.author.voice.channel.category.id == int(vc.category.id):
                        await ctx.send("Talk '"+str(ctx.author.voice.channel)+"' was made private by "+str(ctx.author.mention))
                        try:
                            await log_channel.send("Talk '"+str(ctx.author.voice.channel)+"' was made private by "+str(ctx.author))
                        except Exception as err:
                            pass
                        newName = (str(ctx.author.voice.channel.name)+" ["+"private"+"]")
                        await ctx.author.voice.channel.edit(name=newName)
                        await ctx.author.voice.channel.edit(user_limit=len(ctx.author.voice.channel.members))
                        break
                        
                    #else:
                    #    await ctx.send('You dont have the permission to edit channels outside the Talks Category')
        except Exception as err:
                    pass
            

def setup(bot: commands.Bot):
    bot.add_cog(private(bot))