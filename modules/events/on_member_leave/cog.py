from discord.ext import commands
from config import check_log_channel, check_welcome_channel


class on_member_leave(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        log = self.bot.get_channel(await check_log_channel(member))

        channel = self.bot.get_channel(await check_welcome_channel(member))

        if channel is None:
            return
        else:
            await channel.send(f"{member} left {member.guild.name}!" )
            await log.send("{} left the Server".format(member))
            

def setup(bot: commands.Bot):
    bot.add_cog(on_member_leave(bot))