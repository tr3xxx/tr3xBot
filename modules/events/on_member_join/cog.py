import discord
from discord.ext import commands
from config import BOT_LOG,WELCOME_CHANNEL

class on_member_join(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self,member):
        log = self.bot.get_channel(BOT_LOG)
        welcomechannel = self.bot.get_channel(WELCOME_CHANNEL)
        await welcomechannel.send(f"Welcome {member.mention} on the tr3xGaming Discord Server !" )

        embed=discord.Embed(title=" Welcome on the tr3xGaming Server, i am the tr3xBot", color=0x00ffcc)
        embed.set_author(name="tr3xBot", url="https://discord.gg/KexhwUVG7p")
        embed.add_field(name="You can find my Commands here:", value="https://tr3xgaming.herokuapp.com/html/tr3xbot/commands.html", inline=False)
        await member.send(embed=embed)
        await log.send("{} joined the Server".format(member))

            

def setup(bot: commands.Bot):
    bot.add_cog(on_member_join(bot))