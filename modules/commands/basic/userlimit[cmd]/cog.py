from discord.ext import commands
import numpy as np
from config import check_voicehub_channel, check_log_channel

class userlimit(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def userlimit(self,ctx,*,arg: str = None):
        result =  await check_voicehub_channel()
        result_array = np.array(result)
        for i in range(0,len(result_array)):
            id = int(str(result_array[i])[2:-2])
            global vc
            vc = self.bot.get_channel(id)
            log = self.bot.get_channel(await check_log_channel(ctx))
            
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
                                await log.send("Userlimit of "+str(ctx.author.voice.channel)+" was changed by "+str(ctx.author)+" from "+str(ctx.author.voice.channel.user_limit)+" to "+arg)
                            except Exception as err:
                                pass
                            await ctx.author.voice.channel.edit(user_limit=int(arg))
                            break

                    else:
                        await ctx.send('You dont have the permission to edit channels outside the Talks Category')

        

def setup(bot: commands.Bot):
    bot.add_cog(userlimit(bot))