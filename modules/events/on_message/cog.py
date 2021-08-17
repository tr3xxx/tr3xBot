from discord.ext import commands
from config import BOT_COMMANDS_CHANNEL, BOT_LOG, OWNER_ID, BOT_USER_ID

class on_message(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_message(self,message):

        log = self.bot.get_channel(BOT_LOG)
        if message.channel.id == BOT_COMMANDS_CHANNEL: 
            if str(message.content).startswith(self.bot.command_prefix):
                pass
            else:
                if message.author.id == self.bot.get_user(BOT_USER_ID) or message.author.id == self.bot.get_user(OWNER_ID):
                    pass
                else:
                    await message.channel.purge(limit=1)
                    await message.author.send("You are not allowed to send messages which aren't commands to the '"+str(message.channel)+"' channel")
                    await log.send("Message blocked ({}) in {} from {}".format(message.content,message.channel.mention,message.author))
        if message.channel.id == 803909189990088725:
            if str(message.content).startswith(self.bot.command_prefix):
                await message.channel.purge(limit=1)
                await message.author.send("You are not allowed to send commands to the '"+str(message.channel)+"' channel, Please use the '"+str(message.guild.get_channel(803764491988107334))+"' channel")
                await log.send("Message blocked ({}) in {} from {}".format(message.content,message.channel.mention,message.author))
            else:
                print(31)
                pass
        
       # await self.bot.process_commands(message)
            

def setup(bot: commands.Bot):
    bot.add_cog(on_message(bot))