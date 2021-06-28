
import asyncio
from DiscordUtils.Music import EmptyQueue
import discord
import time
from discord import message
from discord import client
from discord.ext.commands.bot import Bot
from discord.ext.commands.converter import ColourConverter
import requests
import sys
import traceback
import random
from discord.ext import commands
from requests.api import get
from discord.utils import get
from time import sleep
import threading
from discord.ext import commands
import DiscordUtils
import os
from asyncio import sleep
import aiohttp

#from gevent.libev.corecext import async
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="t",help_command=None, intents=intents)
token = "ODMwODQyMjYwNDYyNjMyOTky.YHMkJw.8X6Rtyc5mfEdvJBdAk5JNZ0wijk"
guild = bot.get_guild(718926812033581108)
music = DiscordUtils.Music()
import youtube_dl

youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




@bot.event #login
async def on_ready(): #wird beim start ausgeführt
    
    guild = bot.get_guild(718926812033581108) #guild id des servers
 
    members = bot.guilds[0].members #array mit allen members des servers
    #print(members)
    ip = requests.get('http://api.ipify.org').text #hier her kriegt man die ip
    
    memberings=0
    online=0
    
    for i in members:
        if i.status == discord.Status.offline:                         # brechenung der members ings 
            memberings=memberings+1                                    # und der online members
        elif i.status != discord.Status.offline:                        
            memberings=memberings+1
            online=online+1
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='th for help'),status=discord.Status.do_not_disturb) # ändert den Status des Bots
    
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Online as {0.user}".format(bot),"on:",guild.name)   # reine consolen/terminal ausgabe 
    print(time.strftime('[%H:%M:%S]:', time.localtime()),f"Ping: {int(bot.latency * 1000)} ms / IP:",ip)
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Members: (",online,"/",memberings,")")
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Confirmed Online")
  
    #memchncheck = get(guild.voice_channels, name='⚫ 𝙈𝙚𝙢𝙗𝙚𝙧:')
    #if memchncheck is None:
     #   await guild.create_voice_channel(f"⚫ 𝙈𝙚𝙢𝙗𝙚𝙧: {memberings}", overwrites=None, reason=None)
    #onlchncheck = get(guild.voice_channels, name='🟢 𝙊𝙣𝙡𝙞𝙣𝙚:')
    #if onlchncheck is None:
    #    await guild.create_voice_channel(f"🟢 𝙊𝙣𝙡𝙞𝙣𝙚: {online}", overwrites=None, reason=None)


    


    
#################################################### 

@bot.command() #tdc disconnects the bot
@commands.has_permissions(administrator=True) # nur admins können ihn ausführen
async def dc(ctx): # disconnect bot

    #await ctx.send("Bot shutdown")
    embed = discord.Embed(title="Bot Shutdown",
    description= "The Bot got Shutdowned by an admin/mod",
    color=0xff0000)
    await ctx.send(embed=embed)
    guild = bot.get_guild(718926812033581108)

    #existing_channel = discord.utils.get(guild.channels, name="tr3xBot ONLINE")
    #existing_channel.delete()
    
    if ctx.voice_client.is_connected():                  #soll dafür sorgen, wenn der bot tdced wird auch alle vcs leavt: geht aber akt nicht
     await ctx.voice_client.disconnect()
       

    await bot.change_presence(status=discord.Status.invisible)
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"{0.user}".format(bot)," is Offline now ","on:",guild.name)
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Confirmed Offline")
    await ctx.bot.close() #abmeldung
 
@bot.command()  #bsay "smth with unlimited args"
async def say(ctx,*, arg):  
    await ctx.send(arg)
            
           
@bot.command() #bh help 
async def h(ctx):
    
    embed = discord.Embed(title="tr3xBot Help",
    description= 'Commands:\n\n**broulette BID** -> BID can be: black,red or a number between 0-36\n**bclear x** -> deletes x msgs\n**bsay x** -> says x\n**bkill name** -> kills someone\n**bhug** -> hug urself',
    color=0x22a7f0)
    embed.add_field(name="troulette BID",value="-> BID can be: black,red or a number between 0-36",inline=False)
    embed.add_field(name="tclear x",value="-> deletes x msgs",inline=False)
    embed.add_field(name="tsay x",value="-> says whatever you want",inline=False)
    embed.add_field(name="tkill name",value="-> kill these foes",inline=False)
    embed.add_field(name="thug",value="-> hug urself",inline=False)
    embed.add_field(name="tdm",value="-> sends a nice dm to you",inline=False)
    embed.add_field(name="tdc",value="-> disconnect bot",inline=False)
    embed.set_footer(text="by tr3xGaming")
    await ctx.channel.purge(limit=1)
    await ctx.author.send(embed=embed)


    
@bot.command() #bembed fach, aufgabe, datum 
async def embed(ctx, *, arg): 
                              
    #print(arg)
    args = arg.split(',') #bembed, fach, aufgabe, datum
    #print(args[0],args[1],args[2])
    #print(len(args))
    if len(args) == 3:
        #print(args[1],args[2],args[3])
        embed = discord.Embed(title = args[0],
                                description = args[1],
                                color=0x22a7f0)
        embed.set_footer(text=args[2])
        await ctx.send(embed=embed)
    
    
            
@bot.command() #bclear 34 
async def clear(ctx,arg):
        
    if ctx.author.permissions_in(ctx.channel).manage_messages:
        #args = arg
        #print(len(args))
        args = arg.split(' ')
        if len(args) == 1:
            if args[0].isdigit():
                count = int(args[0])+1
                deleted = await ctx.channel.purge(limit=count)
                embed = discord.Embed(title = '{} Messages deleted.'.format(len(deleted)-1),
                                color=0x22a7f0)
                await ctx.channel.send(embed=embed)
        
        

@bot.command() #broulette BID 
async def roulette(ctx,arg):
       
    bid = arg
    #print(bid)
    result = random.randint(0,36)
    bid_param = -3
    if bid.lower() == "black":
                bid_param = -1
    elif bid.lower() == "red":
            bid_param = -2
    else: 
        try:
            bid_param = int(bid)
        except:
                bid_param = -3
    if bid_param == -3:
        await ctx.send("unexpected input")
        return
    if bid_param == -1:
        won = result%2 == 0 and not result == 0 
    elif bid_param == -2:
        won = result%2 == 1 
    else:
        won = result == bid_param
                
    if won:
        await ctx.send("Congrats, you won.")
    else:
        await ctx.send("Im sorry, you lost")
        
          
                
@bot.command()  #bhug t hugurself
async def hug(ctx):
    await ctx.send("{} hugs himself :smiling_face_with_tear:".format(ctx.message.author.mention))
        
   
                   
@bot.command()  #bkill name/@name to kill someone 
async def kill(ctx,arg):

    if arg != None:
         await ctx.send("{}".format(ctx.message.author.mention)+" killed "+arg)
         
    else:
         await ctx.send("tell me who... tkill @example")
    #await ctx.channel.purge(limit=1)
    
#@bot.command()   
#async def dm(ctx, user: discord.User, *, message=None):
 #   message = message or ""
  #  await user.send(user, message)

@bot.command()
async def dm(ctx):
    await ctx.author.send("Hello, this is a DM! "+ "{}".format(ctx.message.author.mention))

    #await ctx.channel.purge(limit=1) 


@bot.command()
async def join(ctx):
    voicetrue=ctx.author.voice
    if voicetrue is None:
        return await ctx.send('You are not currently in a voice channel')
    await ctx.author.voice.channel.connect()
    await ctx.send('Joined your voice channel')

#@bot.command()
#async def leave(ctx):
 #   voicetrue=ctx.author.voice
  #  mevoicetrue=ctx.guild.me.voice
  #  if voicetrue is None:
 #       return await ctx.send('You are not currently in a voice channel')
 #   if mevoicetrue is None:
 #       return await ctx.send('I am not currently in a voice channel')
 #   guild = bot.get_guild(718926812033581108)
  #  P = music.get_player(guild_id = guild.id)
 #   await P.stop()
 #   await ctx.voice_client.disconnect()
 #   await ctx.send('Left your voice channel')

@bot.command(description="streams music")
async def play( ctx, *, url):
    voicetrue=ctx.author.voice
    if voicetrue is None:
       return await ctx.send('You are not currently in a voice channel')
    if ctx.voice_client == None:
        await ctx.author.voice.channel.connect()
    async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    embed = discord.Embed(title="Now playing", description=f"[{player.title}]({player.url}) [{ctx.author.mention}]")
    await ctx.send(embed=embed)


@bot.command(description="pauses music")
async def pause( ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused ⏸️")
    
@bot.command(description="resumes music")
async def resume( ctx):
        ctx.voice_client.resume()
        await ctx.send("Resuming ⏯️")

@bot.command(description="stops and disconnects the bot from voice")
async def leave( ctx):
        await ctx.voice_client.disconnect()

@bot.command(description="skipped music")
async def skip( ctx):
        ctx.voice_client.skip()
        await ctx.send("Skipped :track_next:")


#@bot.command()
#async def play(ctx, *, url):
  #  voicetrue=ctx.author.voice
  #  if voicetrue is None:
  #      return await ctx.send('You are not currently in a voice channel')
  #  if ctx.voice_client == None:
  #   await ctx.author.voice.channel.connect()
  #  await ctx.send('Joined your voice channel')
  #  guild = bot.get_guild(718926812033581108)
  #  P = music.get_player(guild_id = guild.id)
  #  if not P:
  #              P = music.create_player(ctx)
  #  if not ctx.voice_client.is_playing():
  #              await P.queue(url, search=True)
 #               song = await P.play()
 #               await ctx.send(f'I have started playing `{song.name}`')

    

                #
                #while ctx.voice_client.is_playing():            # Das soll eig den bot, wenn er nichts mehr spielt
                #    await sleep(1)                              # kicken aber er kickt ihn einfach random zwischendurch
                #await ctx.voice_client.disconnect()             
                
 #   else:
#                song = await P.queue(url, search=True)
#                await ctx.send(f'`{song.name}` has been added to queue')
    

#@bot.command()
#async def skip(ctx):
 #   guild = bot.get_guild(718926812033581108)
 #   P = music.get_player(guild_id = guild.id)
 #   await P.skip()
 #   if P.queue is EmptyQueue:                                              # funktioniert noch nicht, ka wie man checkt ob die queue leer ist 
 #       await ctx.send("There are no new Songs in the queue")              # also ob sie dann 0 oder None oder EmptyQueue ist.

#@bot.command()
#async def pause(ctx):
 #   guild = bot.get_guild(718926812033581108)
 #   P = music.get_player(guild_id = guild.id)
 #   await P.pause()

#@bot.command()
#async def resume(ctx):
 #   guild = bot.get_guild(718926812033581108)
 #   P = music.get_player(guild_id = guild.id)
 #   await P.resume()

#@bot.command()
#async def stop(ctx):
 #   guild = bot.get_guild(718926812033581108)
  #  P = music.get_player(guild_id = guild.id)
 #   await P.stop()
      
@bot.event
async def on_voice_state_update(member, before, after):
    guild = bot.get_guild(718926812033581108)
    username = str(member.name)
    ch = guild.get_channel(858272905108258816)
    category = guild.get_channel(858020017822892092)

    if after.channel == ch:
        channel = await guild.create_voice_channel(
            name=username+"`s channel",
            category=category,
            overwrites=None,
            reason=None,
            user_limit=10,
            bitrate=256000
        )
        await member.move_to(channel)
    if not before.channel.members and before.channel != ch and before.channel != None and before != None:
        await before.channel.delete()

@bot.event
async def on_member_join(member):
    print(member+" joined the server")
@bot.event
async def on_member_remove(member):
    print(member+" left the server")
@bot.event
async def on_member_ban(guild, user):
    print(user+" got banned")
@bot.event
async def on_member_unban(guild, user):
    print(user+" got unbanned")
@bot.event
async def on_invite_create(invite):
    print("an invite was created "+(invite))


@bot.command(pass_context=True)
async def memes(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def darkmemes(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/darkmemers/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def dankmemes(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def boobs(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/boobs/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def ass(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/ass/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def lesbian(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/Lesbian_gifs/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def pussy(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/pussy/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def jofleak(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/OFLeaksNSFW/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def hentai(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/hentai/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def ofleak(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
     async with cs.get('https://www.reddit.com/r/OFLeaksNSFW/new.json?sort=hot') as r:
        res = await r.json()
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url_overridden_by_dest'])
        await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def gif(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/milf/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
bot.run(token)