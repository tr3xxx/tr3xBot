import discord
import sqlite3
from discord.ext import commands,tasks

class all_member(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.get_all_member.start()
        
    @tasks.loop(minutes=1)
    async def get_all_member(self):
        
        for guild in self.bot.guilds:
            members = guild.members
            for member in members:
                db = sqlite3.connect("db.sqlite")
                cursor = db.cursor() 
                cursor.execute(f"SELECT user_id FROM level WHERE guild_id = {member.guild.id} AND user_id = {member.id}")
                result = cursor.fetchone()
                if result is None:
                    exp = 0
                    sql = ("INSERT INTO level(guild_id,user_id,exp) VALUES(?,?,?)")
                    val = (member.guild.id,member.id,exp)
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()
        
        


        
        
        
        
            

def setup(bot: commands.Bot):
    bot.add_cog(all_member(bot))