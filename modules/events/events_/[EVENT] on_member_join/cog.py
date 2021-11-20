import discord
from discord.ext import commands
from utils.check_log import log
from utils.check_welcome_channel import check_welcome_channel


class on_member_join(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self,member):
        try:
            log_channel = self.bot.get_channel(log(member))
            await log_channel.send("{} joined the Server".format(member))
        except Exception as err:
            pass
        try:
            tr3xbot = self.bot.get_user(830842260462632992)
            embed=discord.Embed(title=f"Welcome on the {member.guild.name} Server",description='If you want to use my Commands, type ´thelp´ to see all my Commands',color=0x075FB2)
            embed.set_author(name="tr3xBot", url="https://github.com/tr3xxx/tr3xBot/",icon_url=tr3xbot.avatar)
            await member.send(embed=embed)
        except Exception as err:
            pass

        try:
            channel = self.bot.get_channel(await check_welcome_channel(member))
            if channel is None:
                return
            else:
                await channel.send(f"Welcome {member.mention} on the {member.guild.name} Discord Server !" )
        except Exception as err:
            pass

        
        
        


        
        
        
        
            

def setup(bot: commands.Bot):
    bot.add_cog(on_member_join(bot))