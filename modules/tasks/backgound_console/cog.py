
import discord
import time
import aioconsole
import requests

from discord.ext import commands,tasks

class background_console(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.bot.loop.create_task(background_console.background_task(self))

    async def background_task(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            console_input = await aioconsole.ainput()
            if console_input == "exit" or console_input == "tdc" or console_input == "update":
                if console_input == "exit" or console_input =="tdc":
                    guild = self.bot.get_guild(718926812033581108)
                    log = self.bot.get_channel(875700881360846899)
                    statuschannel = self.bot.get_channel(860642601098280970)
                    statusmsg = await statuschannel.fetch_message(871558788388360223)
                    botoffline = discord.Embed(title="**tr3xBot Status**",
                                            description= '`tr3xBot` is currently offline ⛔',
                                            color=0xff0000)
                    botoffline.add_field(name="**What does this mean for you?**",value="All features like commands or the member/online count wont update until i am back online",inline=False)
                    botoffline.add_field(name="**Why i am offline?**",value="Most likely i am offline cause an maintenance break or an server crash",inline=False)
                    botoffline.set_footer(text="presents by tr3xBot")
                    await statusmsg.edit(embed=botoffline)

                    voice = discord.utils.get(self.bot.voice_clients, guild=guild)

                    try:
                        if voice.is_connected() == True:
                            await voice.disconnect()
                    except Exception as err:
                        pass
                    
                    await self.bot.change_presence(status=discord.Status.invisible)
                    print(time.strftime('[%H:%M:%S]:', time.localtime()),"{0.user}".format(self.bot)," is Offline now ","on:",guild.name)
                    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Confirmed Offline")
                    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot was shutdowned via console")
                    await log.send("Bot offline via Console")
                    await self.bot.close()
                if console_input == "update":
                    guild = self.bot.get_guild(718926812033581108) 
                    memberings=0
                    online=0
                    members = self.bot.guilds[0].members 
                    for i in members:
                        if i.status == discord.Status.offline:                         
                            memberings=memberings+1                                    
                        elif i.status != discord.Status.offline:                        
                            memberings=memberings+1
                            online=online+1
                    print(time.strftime('[%H:%M:%S]:', time.localtime()),"The latest data is being loaded...")
                    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Online as {0.user}".format(self.bot),"on:",guild.name) 
                    print(time.strftime('[%H:%M:%S]:', time.localtime()),"IP:",requests.get('http://api.ipify.org').text)
                    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Members: (",online,"/",memberings,")")
                    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Confirmed Online")  
            else: 
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"unexcepted or wrong input")
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"«exit» or «tdc» for shutdown, «update» for latest data and «restart» for restart")


def setup(bot: commands.Bot):
    bot.add_cog(background_console(bot))