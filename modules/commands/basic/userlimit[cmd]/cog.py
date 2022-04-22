from discord.ext import commands
import numpy as np
from utils.check_log import log
from utils.check_voicehub import get_vc

class userlimit(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def userlimit(self,ctx,*,arg: str = None):
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
                if arg is None:
                    await ctx.send("To give a channel a userlimit use the followning template (ex. tuserlimit x )")
                else:
                    if ctx.author.voice is None:
                        await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
                    else:
                        if ctx.author.voice.channel.category.id == int(vc.category.id):
                            if int(arg) >= 99:
                                await ctx.send("Value should be less than or equal to 99")
                            else:
                                await ctx.send("Userlimit of '"+str(ctx.author.voice.channel)+"' got changed by "+str(ctx.author)+" from "+str(ctx.author.voice.channel.user_limit)+" to "+arg)
                                try:
                                    await log_channel.send("Userlimit of "+str(ctx.author.voice.channel)+" was changed by "+str(ctx.author)+" from "+str(ctx.author.voice.channel.user_limit)+" to "+arg)
                                except Exception as err:
                                    pass
                                await ctx.author.voice.channel.edit(user_limit=int(arg))
                                break

                        #else:
                    #     await ctx.send('You dont have the permission to edit channels outside the Talks Category')
        except Exception as err:
                    pass
        

def setup(bot: commands.Bot):
    bot.add_cog(userlimit(bot))