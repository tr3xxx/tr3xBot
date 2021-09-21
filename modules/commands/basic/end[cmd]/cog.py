from discord.ext import commands
import numpy as np
from config import check_voicehub_channel, check_log_channel

class end(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def end(self,ctx):
    
        result =  await check_voicehub_channel()
        result_array = np.array(result)
        for i in range(0,len(result_array)):
            id = int(str(result_array[i])[2:-2])
            global vc
            vc = self.bot.get_channel(id)
            log = self.bot.get_channel(await check_log_channel(ctx))
            if vc is None:
                continue
            if ctx.author.voice is None:
                    await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
            else:
                    print(vc.category.id)
                    print(ctx.author.voice.channel.category.id)
                    if ctx.author.voice.channel.category.id == int(vc.category.id):
                        
                        await ctx.send("Talk '"+str(ctx.author.voice.channel)+"' got deleted by "+str(ctx.author.mention))
                        try:
                            await log.send("Talk '"+str(ctx.author.voice.channel)+"' got deleted by "+str(ctx.author))
                        except Exception as err:
                            pass
                        await ctx.author.voice.channel.delete()
                        break
                        
                   # else:
                   #     await ctx.send("You dont have the permission to edit channels outside the Talks Category")

            

def setup(bot: commands.Bot):
    bot.add_cog(end(bot))