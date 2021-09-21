from discord.ext import commands
import numpy as np
from config import check_log_channel, check_voicehub_channel

class talkname(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def talkname(self,ctx,*,arg: str = None):
        result =  await check_voicehub_channel()
        result_array = np.array(result)
        for i in range(0,len(result_array)):
            id = int(str(result_array[i])[2:-2])
            #global vc
            vc = self.bot.get_channel(id)
            try:
                log = self.bot.get_channel(await check_log_channel(ctx))
            except Exception as err:
                pass
            if vc is None:
                continue
            
            if arg is None:
                await ctx.send("To give a channel a custom name use the followning template (ex. ttalkname x x x x x x )")
                break
            else:
                if ctx.author.voice is None:
                    await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
                    break
                else:
                        print(ctx.author.voice.channel.category.id)
                        print(vc.category.id)
                        if ctx.author.voice.channel.category.id == int(vc.category.id):
                            
                            if len(arg) > 7:
                                await ctx.send("Please choose a shorter Talkname")
                               # break
                            else:
                                newName = (str(ctx.author.voice.channel.name)+" ["+str(arg)+"]")
                                await ctx.send("Talkname of '"+str(ctx.author.voice.channel)+"' got changed by "+str(ctx.author.mention)+" to '"+newName+"'")
                                try:
                                    await log.send("Talkname of '"+str(ctx.author.voice.channel)+"' got changed by "+str(ctx.author)+" to '"+newName+"'")
                                except Exception as err:
                                    pass
                                await ctx.author.voice.channel.edit(name=newName)
                               # break
                            
                        #else:
                        #    await ctx.send('You dont have the permission to edit channels outside the Talks Category')
                         #   break

        

def setup(bot: commands.Bot):
    bot.add_cog(talkname(bot))