import discord
from discord.ext import commands
from config import AFK_CHANNEL, BOT_LOG, TALK_CATEGORY, VOICEHUB_CHANNEL

class on_voice_state_update(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guild = member.guild
        log = self.bot.get_channel(BOT_LOG)
        voicehub = guild.get_channel(VOICEHUB_CHANNEL)
        Talkcategory = guild.get_channel(TALK_CATEGORY)
        afk = guild.get_channel(AFK_CHANNEL)
        MemberRole = discord.utils.get(guild.roles, name="Member")

        if after.channel == voicehub:
            channel = await guild.create_voice_channel(
                name="#"+str(len(Talkcategory.channels))+" Talk",
                category=Talkcategory,
                reason=None,
                bitrate= guild.bitrate_limit,
                overwrites = {
                    MemberRole: discord.PermissionOverwrite(view_channel=True),
                    guild.default_role: discord.PermissionOverwrite(view_channel=False)
                }
            )
            await member.move_to(channel)
            await log.send("{} got created by {} via {}".format(channel.name,member,after.channel))

        if after.channel == afk:
            await member.send("You seem to be afk for a while, you got moved to the afk channel")
            await log.send(str(member)+" is afk")

        try:
            if not before.channel.members and before.channel.category == Talkcategory and before.channel != voicehub:
                await log.send("{} got deleted".format(before.channel))
                await before.channel.delete()
                
        except Exception as err:
            pass


            

def setup(bot: commands.Bot):
    bot.add_cog(on_voice_state_update(bot))