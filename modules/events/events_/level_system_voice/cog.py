import sqlite3
from discord.ext import commands,tasks


class voice_leveling(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_leveling_check.start()

    @tasks.loop(minutes=10.0)
    async def voice_leveling_check(self):
         for guild in self.bot.guilds:
            members = guild.members
            for member in members:
                voice_state = member.voice
                afk = guild.afk_channel
                if voice_state is None:
                    continue
                else:
                    if afk is None:
                            db = sqlite3.connect("db.sqlite")
                            cursor = db.cursor() 
                            cursor.execute(f"SELECT exp FROM level WHERE guild_id = {guild.id} AND user_id = {member.id}")
                            result = cursor.fetchone()
                            if result is None:
                                        exp = 0
                                        sql = ("INSERT INTO level(guild_id,user_id,exp) VALUES(?,?,?)")
                                        val = (guild.id,member.id,exp)
                                        cursor.execute(sql,val)
                                        db.commit()
                                        cursor.close()
                                        db.close()

                            beforeexp = int(str(result)[1:-2])
                            exp = 3
                            afterexp = int(beforeexp) + int(exp)
                            sql = (f"UPDATE level SET exp = ? WHERE guild_id = ? AND user_id = ?")
                            val = (afterexp,guild.id,member.id,)
                            cursor.execute(sql,val)
                            db.commit()
                            cursor.close()
                            db.close()
                    else:
                        if member.channel != afk: 
                            db = sqlite3.connect("db.sqlite")
                            cursor = db.cursor() 
                            cursor.execute(f"SELECT exp FROM level WHERE guild_id = {guild.id} AND user_id = {member.id}")
                            result = cursor.fetchone()

                            if result is None:
                                        exp = 0
                                        sql = ("INSERT INTO level(guild_id,user_id,exp) VALUES(?,?,?)")
                                        val = (guild.id,member.id,exp)
                                        cursor.execute(sql,val)
                                        db.commit()
                                        cursor.close()
                                        db.close()

                            beforeexp = int(str(result)[1:-2])
                            exp = 3
                            afterexp = int(beforeexp) + int(exp)
                            sql = (f"UPDATE level SET exp = ? WHERE guild_id = ? AND user_id = ?")
                            val = (afterexp,guild.id,member.id,)
                            cursor.execute(sql,val)
                            db.commit()
                            cursor.close()
                            db.close()
                

def setup(bot: commands.Bot):
    bot.add_cog(voice_leveling(bot))