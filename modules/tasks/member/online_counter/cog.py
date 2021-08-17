import discord
from discord.ext import commands,tasks

class boost_counter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.member_counter.start()

    
    @tasks.loop(seconds=10.0)
    async def member_counter(self):
        log = self.bot.get_channel(875700881360846899)
        guild = self.bot.get_guild(718926812033581108)
        channelmember = guild.get_channel(858711678316052500)
        channelonline = guild.get_channel(861365241413107732)
        beforeonline = channelonline.name
        beforemember = channelmember.name
        memberings=0
        online=0
        members = self.bot.guilds[0].members 
        for i in members:
            if i.status == discord.Status.offline:                         
                memberings=memberings+1                                   
            elif i.status != discord.Status.offline:                        
                memberings=memberings+1
                online=online+1
        await channelmember.edit(name = f'⚫ 𝙈𝙚𝙢𝙗𝙚𝙧 : {guild.member_count}')
        await channelonline.edit(name = f'🟢 𝙊𝙣𝙡𝙞𝙣𝙚 : {online}')

        if beforeonline != channelonline.name:
            await log.send("Online Counter got updated from {} to {}".format((str(beforeonline)[10:]),(str(channelonline.name)[10:])))
        if beforemember != channelmember.name:
            await log.send("Member Counter got updated from {} to {}".format((str(beforemember)[10:]),(str(channelmember.name)[10:])))

def setup(bot: commands.Bot):
    bot.add_cog(boost_counter(bot))