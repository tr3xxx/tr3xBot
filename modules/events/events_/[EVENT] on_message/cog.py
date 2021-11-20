from discord.ext import commands
import numpy as np
import sqlite3
import discord
from utils.check_log import log
from utils.check_cmd_only_channel import check_onlycommands_channel
from utils.check_no_cmd_channel import check_nocommands_channel

class on_message(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_message(self,message):

        if message.channel.type is not discord.ChannelType.private:
            db = sqlite3.connect("db.sqlite")
            cursor = db.cursor() 
            cursor.execute(f"SELECT exp FROM level WHERE guild_id = {message.guild.id} AND user_id = {message.author.id}")
            result = cursor.fetchone()
            
            
            if result is None:
                        exp = 0
                        sql = ("INSERT INTO level(guild_id,user_id,exp) VALUES(?,?,?)")
                        val = (message.guild.id,message.id,exp)
                        cursor.execute(sql,val)
                        db.commit()
                        cursor.close()
                        db.close()
            else:   
                try:
                        exp= int(str(result)[1:-2]) +1
                        sql = (f"UPDATE level SET exp = ? WHERE guild_id = ? AND user_id = ?")
                        val = (exp,message.guild.id,message.author.id,)
                        cursor.execute(sql,val)
                        db.commit()
                        cursor.close()
                        db.close()
                        
                except Exception as err:
                    pass

            try:
                log_channel = self.bot.get_channel(log(message))
            except Exception as err:
                pass

            result =  await check_onlycommands_channel()
            result_array = np.array(result)
            for i in range(0,len(result_array)):
                id = int(str(result_array[i])[2:-2])
                if message.channel.id == id: 
                    if str(message.content).startswith(self.bot.command_prefix):
                        break
                        
                    else:
                        if message.author == self.bot.get_user(830842260462632992):
                            break
                        else:
                            await message.channel.purge(limit=1)
                            await message.author.send("You are not allowed to send messages which aren't commands to the '"+str(message.channel)+"' channel")
                            try:
                                await log_channel.send("Message blocked ({}) in {} from {}".format(message.content,message.channel.mention,message.author))
                            except Exception as err:
                                break
                            break

            result2 =  await check_nocommands_channel()
            result2_array = np.array(result2)
            for i in range(0,len(result2_array)):
                id2 = int(str(result2_array[i])[2:-2])
                if message.channel.id == id2:
                    if str(message.content).startswith(self.bot.command_prefix):
                        #print(message.author.id,self.bot.get_user(BOT_USER_ID))
                        if message.author == self.bot.get_user(830842260462632992):
                            break
                        await message.channel.purge(limit=1)
                        await message.author.send("You are not allowed to send commands to the '"+str(message.channel)+"' channel, Please use the '"+str(message.guild.get_channel(803764491988107334))+"' channel")
                        try:
                            await log_channel.send("Message blocked ({}) in {} from {}".format(message.content,message.channel.mention,message.author))
                        except Exception as err:
                                break
                        break
                        
        
       # await self.bot.process_commands(message)
            

def setup(bot: commands.Bot):
    bot.add_cog(on_message(bot))