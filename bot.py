import discord
import time
import requests
import sys
import traceback
import random
from discord.ext import commands
from requests.api import get
from discord.utils import get



#from gevent.libev.corecext import async
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="t", intents=intents)
token = "ODMwODQyMjYwNDYyNjMyOTky.YHMkJw.8X6Rtyc5mfEdvJBdAk5JNZ0wijk"





@bot.event #login
async def on_ready():
    
    guild = bot.get_guild(718926812033581108)
 
    members = bot.guilds[0].members
    #print(members)
    ip = requests.get('http://api.ipify.org').text
    
    memberings=0
    online=0
    
    for i in members:
        if i.status == discord.Status.offline:
            memberings=memberings+1
        elif i.status != discord.Status.offline:
            memberings=memberings+1
            online=online+1
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name='tr3xBotBETA'),status=discord.Status.dnd)
    
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Online as {0.user}".format(bot),"on:",guild.name)
    print(time.strftime('[%H:%M:%S]:', time.localtime()),f"Ping: {int(bot.latency * 1000)} ms / IP:",ip)
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Members: (",online,"/",memberings,")")
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Confirmed Online")
    
    memchncheck = get(guild.voice_channels, name='⚫ 𝙈𝙚𝙢𝙗𝙚𝙧:')
    if memchncheck is None:
        await guild.create_voice_channel(f"⚫ 𝙈𝙚𝙢𝙗𝙚𝙧: {memberings}", overwrites=None, reason=None)
    onlchncheck = get(guild.voice_channels, name='🟢 𝙊𝙣𝙡𝙞𝙣𝙚:')
    if onlchncheck is None:
        await guild.create_voice_channel(f"🟢 𝙊𝙣𝙡𝙞𝙣𝙚: {online}", overwrites=None, reason=None)
    
  
    #channel  = await guild.create_text_channel as message.guild.create_text_channel ("⚫ 𝙈𝙚𝙢𝙗𝙚𝙧: ",memberings)
    #channel2 = await guild.create_text_channel as message.guild.create_text_channel ("🟢 𝙊𝙣𝙡𝙞𝙣𝙚: ",online)
    

    
#################################################### 
 
@bot.command()  #bsay "smth with unlimited args"
async def say(ctx,*, arg):  
    await ctx.send(arg)
            
           
@bot.command() #th
async def hp(ctx):
    
    embed = discord.Embed(title="tr3xBot Help",
    description= 'Commands:\n\n**broulette BID** -> BID can be: black,red or a number between 0-36\n**bclear x** -> deletes x msgs\n**bsay x** -> says x\n**bkill name** -> kills someone\n**bhug** -> hug urself',
    color=0x22a7f0)
    embed.add_field(name="broulette BID",value="-> BID can be: black,red or a number between 0-36",inline=False)
    embed.add_field(name="bclear x",value="-> deletes x msgs",inline=False)
    embed.add_field(name="say x",value="-> says x",inline=False)
    embed.add_field(name="bkill name",value="-> kills someone",inline=False)
    embed.add_field(name="bhug",value="-> hug urself",inline=False)
    embed.set_footer(text="by tr3xGaming")
    await ctx.send(embed=embed)
    
    
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
    
       
    
bot.run(token)