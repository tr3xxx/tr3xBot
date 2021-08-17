from discord.ext import commands

class on_message(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_message(self,message):

        log = self.bot.get_channel(875700881360846899)
        if message.channel.id == 803764491988107334: 
            if str(message.content).startswith(self.bot.command_prefix):
                pass
            else:
                if message.author.id == self.bot.get_user(830842260462632992) or message.author.id == self.bot.get_user(633412273641095188):
                    print(message.author.id)
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