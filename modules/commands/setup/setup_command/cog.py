import discord
from discord.ext import commands
import sqlite3

class setupCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def setup(self,ctx):
        await ctx.author.send("///Setup///\n tsetup welcomechannel \n tsetup log \n tsetup fgchannel \n tsetup newschannelger \n tsetup newschanneleng")

    @setup.command()
    async def welcomechannel(self,ctx, channel: discord.TextChannel):
        if channel is None:
            await ctx.send("Please tag the Channel where Welcome Messages should be send in (ex. tsetup welcomechannel #<id>)")
        else:
            if ctx.message.author.guild_permissions.manage_messages:
                db = sqlite3.connect("db.sqlite")
                cursor = db.cursor() 
                cursor.execute(f"SELECT channel_id FROM welcome_channel WHERE guild_id = {ctx.guild.id}")
                result = cursor.fetchone()
                if result is None:
                    sql = ("INSERT INTO welcome_channel(guild_id,channel_id) VALUES(?,?)")
                    val = (ctx.guild.id, channel.id)
                    await ctx.send(f"channel has been set to {channel.mention}")
                elif result is not None:
                    sql = ("UPDATE welcome_channel SET channel_id = ? WHERE guild_id = ?")
                    val = (channel.id, ctx.guild.id )
                    await ctx.send(f"channel has been updated to {channel.mention}")
                cursor.execute(sql,val)
                db.commit()
                cursor.close()
                db.close()
    
    @setup.command()
    async def log(self,ctx, channel: discord.TextChannel):
            if channel is None:
                await ctx.send("Please tag the Channel where log Messages should be send in (ex. tsetup log #<id>)")
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM log_channel WHERE guild_id = {ctx.guild.id}")
                    result = cursor.fetchone()
                    if result is None:
                        sql = ("INSERT INTO log_channel(guild_id,channel_id) VALUES(?,?)")
                        val = (ctx.guild.id, channel.id)
                        await ctx.send(f"log channel has been set to {channel.mention}")
                    elif result is not None:
                        sql = ("UPDATE log_channel SET channel_id = ? WHERE guild_id = ?")
                        val = (channel.id, ctx.guild.id )
                        await ctx.send(f"log channel has been updated to {channel.mention}")
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()
    
    @setup.command()
    async def fgchannel(self,ctx, channel: discord.TextChannel):
            if channel is None:
                await ctx.send("Please tag the Channel where fg Messages should be send in (ex. tsetup fgchannel #<id>)")
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM fg_channel WHERE guild_id = {ctx.guild.id}")
                    result = cursor.fetchone()
                    if result is None:
                        sql = ("INSERT INTO fg_channel(guild_id,channel_id) VALUES(?,?)")
                        val = (ctx.guild.id, channel.id)
                        await ctx.send(f"fg channel has been set to {channel.mention}")
                    elif result is not None:
                        sql = ("UPDATE fg_channel SET channel_id = ? WHERE guild_id = ?")
                        val = (channel.id, ctx.guild.id )
                        await ctx.send(f"fg channel has been updated to {channel.mention}")
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()
            embed = discord.Embed(title="FreeGames Channel",description="In this Channel the latest free games from all platforms are now regularly posted.")
            await channel.send(embed=embed)
    
    @setup.command()
    async def newschannelger(self,ctx, channel: discord.TextChannel):
            if channel is None:
                await ctx.send("Please tag the Channel where news ger Messages should be send in (ex. tsetup newschannelger #<id>)")
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM newsger_channel WHERE guild_id = {ctx.guild.id}")
                    result = cursor.fetchone()
                    if result is None:
                        sql = ("INSERT INTO newsger_channel(guild_id,channel_id) VALUES(?,?)")
                        val = (ctx.guild.id, channel.id)
                        await ctx.send(f"news ger channel has been set to {channel.mention}")
                    elif result is not None:
                        sql = ("UPDATE newsger_channel SET channel_id = ? WHERE guild_id = ?")
                        val = (channel.id, ctx.guild.id )
                        await ctx.send(f"news ger channel has been updated to {channel.mention}")
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()
            embed = discord.Embed(title="Deutsche Nachrichten",description=" In diesem Channel werden fortan relevante Deutsche Nachrichten geposted.")
            await channel.send(embed=embed)
    
    @setup.command()
    async def newschanneleng(self,ctx, channel: discord.TextChannel):
            if channel is None:
                await ctx.send("Please tag the Channel where news eng Messages should be send in (ex. tsetup newschannelger #<id>)")
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM newseng_channel WHERE guild_id = {ctx.guild.id}")
                    result = cursor.fetchone()
                    if result is None:
                        sql = ("INSERT INTO newseng_channel(guild_id,channel_id) VALUES(?,?)")
                        val = (ctx.guild.id, channel.id)
                        await ctx.send(f"news eng channel has been set to {channel.mention}")
                    elif result is not None:
                        sql = ("UPDATE newseng_channel SET channel_id = ? WHERE guild_id = ?")
                        val = (channel.id, ctx.guild.id )
                        await ctx.send(f"news eng channel has been updated to {channel.mention}")
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()
            embed = discord.Embed(title="International News",description="In this Channel the latest International News are now regularly posted.")
            await channel.send(embed=embed)
    
    @setup.command()
    async def stats(self,ctx):

                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT member_channel_id FROM stats WHERE guild_id = {ctx.guild.id}")
                    result_member = cursor.fetchall()
                    cursor.execute(f"SELECT online_channel_id FROM stats WHERE guild_id = {ctx.guild.id}")
                    result_online = cursor.fetchall()
                    cursor.execute(f"SELECT boost_channel_id FROM stats WHERE guild_id = {ctx.guild.id}")
                    result_boost = cursor.fetchall()
                    [] == False
                    if result_member == [] and result_online == [] and result_boost == []:
                            member_channel = await ctx.guild.create_voice_channel(name="Member Counter:")
                            online_channel = await ctx.guild.create_voice_channel(name="Online Counter:")
                            boost_channel = await ctx.guild.create_voice_channel(name="Boost Counter:")


                            sql = ("INSERT INTO stats(guild_id,member_channel_id,online_channel_id,boost_channel_id) VALUES(?,?,?,?)")
                            val = (ctx.guild.id, member_channel.id, online_channel.id, boost_channel.id)
                            await ctx.send("stats channel are created")
                            cursor.execute(sql,val)
                            db.commit()
                            cursor.close()
                            db.close()
                    if result_member != [] and result_online != [] and result_boost != []:
                            await ctx.send("stats channel are already created on this server, sorry")
                    
                
                        
                    
            
    

def setup(bot: commands.Bot):
    bot.add_cog(setupCommand(bot))