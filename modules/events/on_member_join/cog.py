import discord
import sqlite3
from discord.ext import commands
from config import check_log_channel, check_welcome_channel


class on_member_join(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self,member):
        log = self.bot.get_channel(await check_log_channel(member))

        channel = self.bot.get_channel(await check_welcome_channel(member))
        if channel is None:
            return
        else:
            await channel.send(f"Welcome {member.mention} on the {member.guild.name} Discord Server !" )

        embed=discord.Embed(title=" Welcome on the tr3xGaming Server, i am the tr3xBot", color=0x00ffcc)
        embed.set_author(name="tr3xBot", url="https://discord.gg/KexhwUVG7p")
        embed.add_field(name="You can find my Commands here:", value="https://tr3xgaming.herokuapp.com/html/tr3xbot/commands.html", inline=False)
        await member.send(embed=embed)
        await log.send("{} joined the Server".format(member))
            

def setup(bot: commands.Bot):
    bot.add_cog(on_member_join(bot))