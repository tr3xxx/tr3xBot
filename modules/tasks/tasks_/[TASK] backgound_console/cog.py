
import discord
import time
import aioconsole
from discord.ext import commands

class background_console(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.bot.loop.create_task(background_console.background_task(self))

    async def background_task(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            console_input = await aioconsole.ainput()
            if console_input == "tdc":
                if console_input == "exit" or console_input =="tdc":
                    

                    #voice = discord.utils.get(self.bot.voice_clients, guild=guild)

                    #try:
                     #   if voice.is_connected() == True:
                     #       await voice.disconnect()
                    #except Exception as err:
                    #    pass
                    
                    await self.bot.change_presence(status=discord.Status.invisible)
                    #print(time.strftime('[%H:%M:%S]:', time.localtime()),"{0.user}".format(self.bot)," is Offline now ","on:",guild.name)
                    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Confirmed Offline")
                    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot was shutdowned via console")
                    #await log.send("Bot offline via Console")
                    await self.bot.close()
                
            else: 
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"unexcepted or wrong input")
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"«tdc» for shutdown")


def setup(bot: commands.Bot):
    bot.add_cog(background_console(bot))