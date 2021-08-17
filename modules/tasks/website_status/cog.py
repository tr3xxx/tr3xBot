from config import BOT_LOG, OWNER_ID, STATUS_CHANNEL, STATUS_MESSAGE
import discord
import urllib
from discord.ext import commands,tasks
from config import BOT_LOG

class website_status(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.tr3xGamingWebsiteStatus.start()

    @tasks.loop(hours=1)
    async def tr3xGamingWebsiteStatus(self):
        log = self.bot.get_channel(BOT_LOG)
        statuschannel = self.bot.get_channel(STATUS_CHANNEL)
        statusmsg = await statuschannel.fetch_message(STATUS_MESSAGE)
        tr3x = self.bot.get_user(OWNER_ID)

        if urllib.request.urlopen("https://tr3xgaming.herokuapp.com/").getcode() != 200:
            Websiteoff = discord.Embed(title="**tr3xGaming Website Status**",
                                            description= '`tr3xgaming.herokuapp.com` is currently offline ⛔\n'+urllib.request.urlopen("https://tr3xgaming.herokuapp.com/").getcode()+' \n \n Please get in contact with {} asap'.format(tr3x.mention),
                                            color=0xff0000)
            Websiteoff.set_footer(text="presents by tr3xBot")
            await statusmsg.edit(embed=Websiteoff)
            await log.send("Changed Website-Status in {} to Offline".format(statuschannel.mention))
        else:
            Websiteon = discord.Embed(title="**tr3xGaming Website Status**", url='https://tr3xgaming.herokuapp.com/',
                                description= '`tr3xgaming.herokuapp.com` is currently online ✅ \n \n If you experience problems please get in contact with {} asap'.format(tr3x.mention),
                                color=0x0CFF00)
            Websiteon.set_footer(text="presents by tr3xBot")
            await statusmsg.edit(embed=Websiteon)
            await log.send("Changed Website-Status in {} to Online".format(statuschannel.mention))




def setup(bot: commands.Bot):
    bot.add_cog(website_status(bot))