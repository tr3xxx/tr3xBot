import discord
import numpy as np
from discord.ext import commands
from utils.check_log import log
from utils.check_voicehub import get_vc

class on_voice_state_update(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
       
        guild = member.guild
        log_channel = self.bot.get_channel(log(member))
        
        result =  get_vc()
        result_array = np.array(result)
        for i in range(0,len(result_array)):
            id = int(str(result_array[i])[2:-2])
            try:
                if after.channel.id == id:
                    global vc 
                    vc = self.bot.get_channel(id)
                    global Talkcategory 
                    Talkcategory = vc.category
                    channel = await guild.create_voice_channel(
                        name="#"+str(len(Talkcategory.channels))+" Talk",
                        reason=None,
                        category=Talkcategory,
                        bitrate= guild.bitrate_limit
                    )
                    await member.move_to(channel)
                    try:
                        await log.send("{} got created by {} via {}".format(channel.name,member,vc))
                    except Exception as err:
                        pass
            except Exception as err:
                pass

        try:
            if not before.channel.members and before.channel.category == Talkcategory and before.channel != vc: 
                try:
                    await log_channel.send("{} got deleted".format(before.channel))
                except Exception as err:
                    pass
                await before.channel.delete()
                    
        except Exception as err:
                pass


            

def setup(bot: commands.Bot):
    bot.add_cog(on_voice_state_update(bot))