import discord
import numpy as np
from discord.ext import commands,tasks
from config import check_member_channel, check_online_channel, stats_channel, check_boost_channel

class stats_counter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.member_counter.start()

    @tasks.loop(minutes=1)
    async def member_counter(self):
        stats_channel_list = await stats_channel()
        result_member = await check_member_channel()
        result_online = await check_online_channel()
        result_boost =  await check_boost_channel()
        stats_channel_array = np.array(stats_channel_list)
        result_member_array = np.array(result_member)
        result_online_array = np.array(result_online)
        result_boosy_array = np.array(result_boost)
        channelmember = None
        channelonline = None

       
        for i in range(0,len(stats_channel_array)):
            
            guild = self.bot.get_guild(int(str(stats_channel_array[i])[2:-2]))

            channelboost  = self.bot.get_channel(int(str(result_boosy_array[i])[2:-2]))                   
            channelmember = self.bot.get_channel(int(str(result_member_array[i])[2:-2]))
            channelonline = self.bot.get_channel(int(str(result_online_array[i])[2:-2]))

            if channelboost or channelmember or channelonline is None:
                print(channelboost,channelmember,channelonline)
            else:
                online=0
                members = guild.members
                
                for i in members:
                    if i.status != discord.Status.offline: 
                        online=online+1

                
                ono = (channelonline.name).split(":")
                onm = (channelmember.name).split(":")
                boo = (channelboost.name).split(":")

                oldnamemember = np.array(onm)
                oldnameonline = np.array(ono)
                oldboostch = np.array(boo)

                namemem = str(oldnamemember[0])+": "+str(guild.member_count)
                nameon = str(oldnameonline[0])+": "+str(online)
                nameboost = str(oldboostch[0])+": "+str(guild.premium_subscription_count)

                await channelmember.edit(name = namemem)
                await channelonline.edit(name = nameon)
                await channelboost.edit(name = nameboost)

            

def setup(bot: commands.Bot):
    bot.add_cog(stats_counter(bot))