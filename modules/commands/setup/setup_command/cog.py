import discord
from discord.ext import commands
import sqlite3

class setupCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def setup(self,ctx):
        await ctx.author.send("///Setup///")

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
    
    

def setup(bot: commands.Bot):
    bot.add_cog(setupCommand(bot))