import discord
from discord.ext import commands

owner = 633412273641095188
botid = 830842260462632992

class on_member_join(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self,member):
        log = self.bot.get_channel(875700881360846899)
        welcomechannel = self.bot.get_channel(828410713294372885)
        guild = self.bot.get_guild(718926812033581108)
        await welcomechannel.send(f"Welcome {member.mention} on the tr3xGaming Discord Server !" )

        embed=discord.Embed(title=" Welcome on the tr3xGaming Server, i am the tr3xBot", color=0x00ffcc)
        embed.set_author(name="tr3xBot", url="https://discord.gg/KexhwUVG7p")
        embed.add_field(name="You can find my Commands here:", value="https://tr3xgaming.herokuapp.com/html/tr3xbot/commands.html", inline=False)
        await member.send(embed=embed)
        await log.send("{} joined the Server".format(member))

            

def setup(bot: commands.Bot):
    bot.add_cog(on_member_join(bot))