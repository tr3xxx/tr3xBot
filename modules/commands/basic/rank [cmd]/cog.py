import discord
from discord.ext import commands
from config import check_log_channel, get_rank
import sqlite3

class rank(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    async def rank(self,ctx,member: discord.Member = None):   
        
        if member is None:
            db = sqlite3.connect("db.sqlite")
            cursor = db.cursor() 
            cursor.execute(f"SELECT exp FROM level WHERE guild_id = {ctx.guild.id} AND user_id = {ctx.author.id}")
            result = cursor.fetchone()
            
            if result is None:
                        exp = 0
                        sql = ("INSERT INTO level(guild_id,user_id,exp) VALUES(?,?,?)")
                        val = (ctx.guild.id,ctx.author.id,exp)
                        cursor.execute(sql,val)
                        db.commit()
                        cursor.close()
                        db.close()

                        await ctx.send(f'You are currently Level 1 on the {ctx.guild.name} Discord, you have {exp} Experience points (Levelsystem: 1 point per message, 3 for being in a voicechannel for every 10 minutes)')
            else:
                exp= int(str(result)[1:-2])
                level = await get_rank(exp)
                await ctx.send(f'You are currently Level {int(level)} on the {ctx.guild.name} Discord, you have {exp} Experience points (Levelsystem: 1 point per message, 3 for being in a voicechannel for every 10 minutes)')
        else:
            db = sqlite3.connect("db.sqlite")
            cursor = db.cursor() 
            cursor.execute(f"SELECT exp FROM level WHERE guild_id = {ctx.guild.id} AND user_id = {member.id}")
            result = cursor.fetchone()
            
            if result is None:
                        exp = 0
                        sql = ("INSERT INTO level(guild_id,user_id,exp) VALUES(?,?,?)")
                        val = (ctx.guild.id,member.id,exp)
                        cursor.execute(sql,val)
                        db.commit()
                        cursor.close()
                        db.close()

                        await ctx.send(f'{member.nick} is currently Level 1 on the {ctx.guild.name} Discord, {member.nick} has {exp} Experience points (Levelsystem: 1 point per message, 3 for being in a voicechannel for every 10 minutes)')
            else:
                exp= int(str(result)[1:-2])
                level = await get_rank(exp)
                await ctx.send(f'{member} is currently Level {int(level)} on the {ctx.guild.name} Discord, {member} has {exp} Experience points (Levelsystem: 1 point per message, 3 for being in a voicechannel for every 10 minutes)')
        

                    

                    

    @commands.command()
    async def give_exp(self,ctx,member: discord.Member = None, exp: int = 0): 

        if ctx.message.author.guild_permissions.administrator:
            if member is None:
                await ctx.send('To give someone exp, use tgive_exp @Member ExpPoints')
            else:
                db = sqlite3.connect("db.sqlite")
                cursor = db.cursor() 
                cursor.execute(f"SELECT exp FROM level WHERE guild_id = {ctx.guild.id} AND user_id = {ctx.author.id}")
                result = cursor.fetchone()

                if result is None:
                            exp = 0
                            sql = ("INSERT INTO level(guild_id,user_id,exp) VALUES(?,?,?)")
                            val = (ctx.guild.id,ctx.id,exp)
                            cursor.execute(sql,val)
                            db.commit()
                            cursor.close()
                            db.close()

                beforeexp = int(str(result)[1:-2])
                afterexp = int(beforeexp) + int(exp)
                sql = (f"UPDATE level SET exp = ? WHERE guild_id = ? AND user_id = ?")
                val = (afterexp,ctx.guild.id,ctx.author.id,)
                cursor.execute(sql,val)
                db.commit()
                cursor.close()
                db.close()

                await ctx.send(f'{member.mention} got {afterexp} exp points')
        
        else:
            await ctx.send("You dont have the permission to give exp to someone on this server")

    @commands.command()
    async def remove_exp(self,ctx,member: discord.Member = None, exp: int = 0): 

        if ctx.message.author.guild_permissions.administrator:
            if member is None:
                await ctx.send('To remove someones exp, use tremove_exp @Member ExpPoints')
            else:
                db = sqlite3.connect("db.sqlite")
                cursor = db.cursor() 
                cursor.execute(f"SELECT exp FROM level WHERE guild_id = {ctx.guild.id} AND user_id = {ctx.author.id}")
                result = cursor.fetchone()

                if result is None:
                            exp = 0
                            sql = ("INSERT INTO level(guild_id,user_id,exp) VALUES(?,?,?)")
                            val = (ctx.guild.id,ctx.id,exp)
                            cursor.execute(sql,val)
                            db.commit()
                            cursor.close()
                            db.close()

                beforeexp = int(str(result)[1:-2])
                afterexp = int(beforeexp) - int(exp)
                sql = (f"UPDATE level SET exp = ? WHERE guild_id = ? AND user_id = ?")
                val = (afterexp,ctx.guild.id,ctx.author.id,)
                cursor.execute(sql,val)
                db.commit()
                cursor.close()
                db.close()
                
                await ctx.send(f'{afterexp} exp points were removed from {member.mention}')
        else:
            await ctx.send("You dont have the permission to give exp to someone on this server")
                    
        

def setup(bot: commands.Bot):
    bot.add_cog(rank(bot))