from discord.ext import commands,tasks

class boost_counter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.boost.start()

    @tasks.loop(seconds=5.0)
    async def boost(self):
        log = self.bot.get_channel(875700881360846899)
        guild = self.bot.get_guild(718926812033581108)
        boostchannel = guild.get_channel(861753968890871839)
        beforeboost = boostchannel.name
        boosts = guild.premium_subscription_count
        await boostchannel.edit(name = f"🌐 𝘽𝙤𝙤𝙨𝙩𝙨 : {boosts}")
        
        if beforeboost != boostchannel.name:
            await log.send("Online Counter got updated from {} to {}".format((str(beforeboost)[10:]),(str(boostchannel.name)[10:])))

def setup(bot: commands.Bot):
    bot.add_cog(boost_counter(bot))