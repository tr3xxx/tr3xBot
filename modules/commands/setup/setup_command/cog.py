
import discord
from discord.ext import commands
import sqlite3
class setupCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def setup(self,ctx):
        if ctx.message.author.guild_permissions.manage_messages:
            embed=discord.Embed(title='tr3xBot Setup',description='Thanks for choosing tr3xBot\n\n Please keep in mind that this Bot is developed by only one person\n Thereofore i would appreciate if you could report every bug or wishes on my Discord (https://discord.gg/rVcPPzbQ)\n\n\n\n ',color=0x075FB2)
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/830842260462632992/6f5341620fb3a4238741b50d2eef417b.png?size=1024")
            embed.add_field(name="Welcome-Messages Channel",value="\n>>> *To set up an Custom Welcome Channel use the following Command: \n `tsetup welcomechannel <#textchannelid>`*",inline=False)
            embed.add_field(name="Log Channel",value="\n>>> *To set up an Custom Log Channel use the following Command: \n `tsetup log <#textchannelid>`*",inline=False)
            embed.add_field(name="Free-Games Channel",value="\n>>> *To set up an Custom Free-Games Channel use the following Command:\n  `tsetup fgchannel <#textchannelid>`*",inline=False)
            embed.add_field(name="German-News Channel",value="\n>>> *To set up an Custom German-News Channel use the following Command: \n `tsetup newschannelger <#textchannelid>`*",inline=False)
            embed.add_field(name="International-News Channel",value="\n>>> *To set up an Custom International-News Channel use the following Command: \n  `tsetup newschanneleng <#textchannelid>`*",inline=False)
            embed.add_field(name="Stats Channel",value="\n>>> *To set up 3 Server specific Channel (Member Counter,Online Counter,Boost Counter) use the following Command:\n `tsetup stats`*",inline=False)
            embed.add_field(name="Voicehub Channel",value="\n>>> *To set up an Voicehub Channel use the following Command:\n `tsetup voicehub <#voicechannelid>`*",inline=False)
            embed.add_field(name="Commands-Only Channel",value="\n>>> *To set up an Custom Commands-Only Channel use the following Command: \n `tsetup commandsonly <#textchannelid>`*",inline=False)
            embed.add_field(name="No-Commands Channel",value="\n>>> *To set up an Custom No-Commands Channel use the following Command: \n `tsetup nocommands <#textchannelid>`*",inline=False)
            embed.set_footer(text="To get an overview of all commands of the bot use `thelp` \nShould something not work as expected please open a ticket on the discord linked above, i will work the problem then.")
            
            await ctx.send(embed=embed) 
        else:
            await ctx.author.send('You dont have the permission to use setup Commands on this Server!')

    @setup.command()
    async def welcomechannel(self,ctx, channel: discord.TextChannel):
        if channel is None:
            await ctx.send("Wrong Input, please use following Command (<#id> id has to be from your server/ or tag the channel without the <>) `tsetup welcomechannel <#textchannelid>` ")
        else:
            if ctx.message.author.guild_permissions.manage_messages:
                db = sqlite3.connect("db.sqlite")
                cursor = db.cursor() 
                cursor.execute(f"SELECT channel_id FROM welcome_channel WHERE guild_id = {ctx.guild.id}")
                result = cursor.fetchone()
                if result is None:
                    sql = ("INSERT INTO welcome_channel(guild_id,channel_id) VALUES(?,?)")
                    val = (ctx.guild.id, channel.id)
                    await ctx.send(f"Welcome-Messages will be send to {channel.mention}")
                elif result is not None:
                    sql = ("UPDATE welcome_channel SET channel_id = ? WHERE guild_id = ?")
                    val = (channel.id, ctx.guild.id )
                    await ctx.send(f"Welcome-Messages will be send to {channel.mention}")
                cursor.execute(sql,val)
                db.commit()
                cursor.close()
                db.close()
            else:
                await ctx.author.send('You dont have the permission to use setup Commands on this Server!')
    
    @setup.command()
    async def log(self,ctx, channel: discord.TextChannel):
            if channel is None:
                await ctx.send("Wrong Input, please use following Command (<#id> id has to be from your server/ or tag the channel without the <>) `tsetup log <#textchannelid>` ")            
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM log_channel WHERE guild_id = {ctx.guild.id}")
                    result = cursor.fetchone()
                    if result is None:
                        sql = ("INSERT INTO log_channel(guild_id,channel_id) VALUES(?,?)")
                        val = (ctx.guild.id, channel.id)
                        await ctx.send(f"Log-Messages will be send to {channel.mention}")
                    elif result is not None:
                        sql = ("UPDATE log_channel SET channel_id = ? WHERE guild_id = ?")
                        val = (channel.id, ctx.guild.id )
                        await ctx.send(f"Log-Messages will be send to {channel.mention}")
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()
                else:
                    await ctx.author.send('You dont have the permission to use setup Commands on this Server!')
    @setup.command()
    async def fgchannel(self,ctx, channel: discord.TextChannel):
            if channel is None:
                await ctx.send("Wrong Input, please use following Command (<#id> id has to be from your server/ or tag the channel without the <>) `tsetup fgchannel <#textchannelid>` ")            
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM fg_channel WHERE guild_id = {ctx.guild.id}")
                    result = cursor.fetchone()
                    sql = ("INSERT INTO fg_channel(guild_id,channel_id) VALUES(?,?)")
                    val = (ctx.guild.id, channel.id)
                    await ctx.send(f"Free-Games will be send to {channel.mention}")
                    embed = discord.Embed(title="FreeGames Channel",description="In this Channel the latest free games from all platforms are now regularly posted.")
                    await channel.send(embed=embed)
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()
                else:
                    await ctx.author.send('You dont have the permission to use setup Commands on this Server!')
            
    
    @setup.command()
    async def newschannelger(self,ctx, channel: discord.TextChannel):
            if channel is None:
                await ctx.send("Wrong Input, please use following Command (<#id> id has to be from your server/ or tag the channel without the <>) `tsetup newschannelger <#textchannelid>` ")            
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM newsger_channel WHERE guild_id = {ctx.guild.id}")
                    result = cursor.fetchone()
                    sql = ("INSERT INTO newsger_channel(guild_id,channel_id) VALUES(?,?)")
                    val = (ctx.guild.id, channel.id)
                    await ctx.send(f"German-News will be send to {channel.mention}")
                    embed = discord.Embed(title="Deutsche Nachrichten",description=" In diesem Channel werden fortan relevante Deutsche Nachrichten geposted.")
                    await channel.send(embed=embed)
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()
                else:
                    await ctx.author.send('You dont have the permission to use setup Commands on this Server!')
    
    @setup.command()
    async def newschanneleng(self,ctx, channel: discord.TextChannel):
            if channel is None:
                await ctx.send("Wrong Input, please use following Command (<#id> id has to be from your server/ or tag the channel without the <>) `tsetup newschanneleng <#textchannelid>` ")            
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM newseng_channel WHERE guild_id = {ctx.guild.id}")
                    result = cursor.fetchone()
                    sql = ("INSERT INTO newseng_channel(guild_id,channel_id) VALUES(?,?)")
                    val = (ctx.guild.id, channel.id)
                    await ctx.send(f"International-News will be send to {channel.mention}")
                    embed = discord.Embed(title="International News",description="In this Channel the latest International News are now regularly posted.")
                    await channel.send(embed=embed)
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()
                else:
                    await ctx.author.send('You dont have the permission to use setup Commands on this Server!')
           
    
    @setup.command()
    async def stats(self,ctx):

                online=0
                members = ctx.guild.members
                
                for i in members:
                    if i.status != discord.Status.offline: 
                        online=online+1

                if ctx.message.author.guild_permissions.manage_messages:
                            db = sqlite3.connect("db.sqlite")
                            cursor = db.cursor() 
                    #cursor.execute(f"SELECT member_channel_id FROM stats WHERE guild_id = {ctx.guild.id}")
                    #result_member = cursor.fetchall()
                    #cursor.execute(f"SELECT online_channel_id FROM stats WHERE guild_id = {ctx.guild.id}")
                    #result_online = cursor.fetchall()
                    #cursor.execute(f"SELECT boost_channel_id FROM stats WHERE guild_id = {ctx.guild.id}")
                    #result_boost = cursor.fetchall()
                    #[] == False
                    #if result_member == [] and result_online == [] and result_boost == []:
                            member_channel = await ctx.guild.create_voice_channel(name=("Member Counter: "+str(ctx.guild.member_count)))
                            online_channel = await ctx.guild.create_voice_channel(name=("Online Counter: "+str(online)))
                            boost_channel = await ctx.guild.create_voice_channel(name="Boost Counter: "+str(ctx.guild.premium_subscription_count))


                            sql = ("INSERT INTO stats(guild_id,member_channel_id,online_channel_id,boost_channel_id) VALUES(?,?,?,?)")
                            val = (ctx.guild.id, member_channel.id, online_channel.id, boost_channel.id)
                            await ctx.send("stats channel are created")
                            cursor.execute(sql,val)
                            db.commit()
                            cursor.close()
                            db.close()
                    #if result_member != [] and result_online != [] and result_boost != []:
                           # await ctx.send("stats channel are already created on this server, sorry")
                else:
                    await ctx.author.send('You dont have the permission to use setup Commands on this Server!')



    @setup.command()
    async def voicehub(self,ctx, channel: discord.VoiceChannel):
            if channel is None:
                await ctx.send("Wrong Input, please use following Command (<#id> id has to be from your server/ or tag the channel without the <>) `tsetup voicehub <#textchannelid>` ")            
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM voicehub_channel WHERE guild_id = {ctx.guild.id}")
                    result = cursor.fetchone()
                    sql = ("INSERT INTO voicehub_channel(guild_id,channel_id) VALUES(?,?)")
                    val = (ctx.guild.id, channel.id)
                    await ctx.send(f"{channel.mention} will now work as a Voicehub")
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()      
                else:
                    await ctx.author.send('You dont have the permission to use setup Commands on this Server!')     
                        
    @setup.command()
    async def commandsonly(self,ctx, channel: discord.TextChannel):
            if channel is None:
                await ctx.send("Wrong Input, please use following Command (<#id> id has to be from your server/ or tag the channel without the <>) `tsetup commandsonly <#textchannelid>` ")            
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM command_only_channel WHERE guild_id = {ctx.guild.id}")
                    sql = ("INSERT INTO command_only_channel(guild_id,channel_id) VALUES(?,?)")
                    val = (ctx.guild.id, channel.id)
                    await ctx.send(f"{channel.mention} is now a Command-Only Channel")
                    
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()  
                else:
                    await ctx.author.send('You dont have the permission to use setup Commands on this Server!')  

    @setup.command()
    async def nocommands(self,ctx, channel: discord.TextChannel):
            if channel is None:
                await ctx.send("Wrong Input, please use following Command (<#id> id has to be from your server/ or tag the channel without the <>) `tsetup nocommands <#textchannelid>` ")            
            else:
                if ctx.message.author.guild_permissions.manage_messages:
                    db = sqlite3.connect("db.sqlite")
                    cursor = db.cursor() 
                    cursor.execute(f"SELECT channel_id FROM no_commands_channel WHERE guild_id = {ctx.guild.id}")
                    sql = ("INSERT INTO no_commands_channel(guild_id,channel_id) VALUES(?,?)")
                    val = (ctx.guild.id, channel.id)
                    await ctx.send(f"{channel.mention} is now a No-Commands Channel")
                    
                    cursor.execute(sql,val)
                    db.commit()
                    cursor.close()
                    db.close()   
                else:
                    await ctx.author.send('You dont have the permission to use setup Commands on this Server!')        
    
    @setup.command()
    async def end(self,ctx):
        setupch = discord.utils.get(ctx.guild.channels, name='tr3xbot-setup')
        if ctx.message.author.guild_permissions.manage_messages:
            if ctx.channel.id is setupch.id:
                await ctx.send('Setup completed!')
                await ctx.channel.delete()
            else:
                await ctx.send('Setup could not be terminated because this is not the setup channel, please use {} to terminate the setup if one is in progress'.format(setupch.mention))
        else:
             await ctx.author.send('You dont have the permission to use setup Commands on this Server!')
    

        
  

def setup(bot: commands.Bot):
    bot.add_cog(setupCommand(bot))