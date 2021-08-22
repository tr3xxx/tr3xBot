import discord
import sqlite3
from discord.ext import commands
from config import check_log_channel, check_welcome_channel, BOT_USER_ID


class on_member_join(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self,member):
        try:
            log = self.bot.get_channel(await check_log_channel(member))
            await log.send("{} joined the Server".format(member))
        except Exception as err:
            pass
        try:
            tr3xbot = self.bot.get_user(BOT_USER_ID)
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