import asyncio, time, requests, random, discord,youtube_dl, aioconsole,time,praw,coc,urllib
from typing import Text
from os import name
from discord.ext import commands, tasks
from random import choice
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

#py -3 -m pip install -U "package"

print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot is starting...")

bot = commands.Bot(command_prefix="t",help_command=None, intents=discord.Intents().all())
cocclient = coc.login('hapol38642@activesniper.com','U9K!!wO*&RRYUz^WyUHvIVuYw6L') # https://developer.clashofclans.com
reddit = praw.Reddit(client_id='1v8p8QXgpNnQuvs2Zl-8UA',client_secret='-y2Bgh7e0JVA2LD7XnVazi62xffm3Q',user_agent='tr3xBot')
owner = 633412273641095188
botid = 830842260462632992
queue = []
slash = InteractionClient(bot)

@bot.event
async def on_ready():

    
    member_counter.start()
    status_1.start()
    status_2.start()
    boost.start()
    fg.start()
    newsGER.start()
    newsENG.start()
    tr3xGamingWebsiteStatus.start()
    await LoginOutput()
    await tr3xBotStatusOnline()
    await rulesedit()

async def LoginOutput():

    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Online as {0.user}".format(bot))
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Successfully started")
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"«exit» or «tdc» for shutdown, «update» for latest data")

async def tr3xBotStatusOnline():

    statuschannel = bot.get_channel(860642601098280970)
    statusmsg = await statuschannel.fetch_message(871558788388360223)
    tr3x = bot.get_user(633412273641095188)
    botonline = discord.Embed(title="**tr3xBot Status**",
                              description= '`tr3xBot` is currently online ✅ \n \n If you experience problems please get in contact with {} asap'.format(tr3x.mention),
                              color=0x0CFF00)
    botonline.set_footer(text="presents by tr3xBot")
    await statusmsg.edit(embed=botonline)

@tasks.loop(hours=1)
async def tr3xGamingWebsiteStatus():

    statuschannel = bot.get_channel(860642601098280970)
    statusmsg = await statuschannel.fetch_message(873324711650672640)
    tr3x = bot.get_user(633412273641095188)

    if urllib.request.urlopen("https://tr3xgaming.herokuapp.com/").getcode() != 200:
        Websiteoff = discord.Embed(title="**tr3xGaming Website Status**",
                                        description= '`tr3xgaming.herokuapp.com` is currently offline ⛔\n'+urllib.request.urlopen("https://tr3xgaming.herokuapp.com/").getcode()+' \n \n Please get in contact with {} asap'.format(tr3x.mention),
                                        color=0xff0000)
        Websiteoff.set_footer(text="presents by tr3xBot")
        await statusmsg.edit(embed=Websiteoff)
    else:
        Websiteon = discord.Embed(title="**tr3xGaming Website Status**", url='https://tr3xgaming.herokuapp.com/',
                              description= '`tr3xgaming.herokuapp.com` is currently online ✅ \n \n If you experience problems please get in contact with {} asap'.format(tr3x.mention),
                              color=0x0CFF00)
        Websiteon.set_footer(text="presents by tr3xBot")
        await statusmsg.edit(embed=Websiteon)

async def rulesedit(): 
    channel = bot.get_channel(803240539578302524)
    Rulemessage = await channel.fetch_message(860636421047320627)
    tr3x = bot.get_user(633412273641095188)
    embed = discord.Embed(title="",description= "",color=0x075FB2)                        
    embed.add_field(name="To get access to the complete server and to use all functions accept the rules but take in mind:\n\n**If you accept you agree with all rules below as well as the general Discord TOS ( https://discord.com/terms )**\n\n",value="\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",inline=False)
    embed.add_field(name=" Languages",value="\n>>> *English and German are the only allowed languages on this server*",inline=False)
    embed.add_field(name=" Rasism/Discrimination",value="\n>>> *Rasism and any sort of Discrimination is of course not allowed and will be punished with a permanent ban*",inline=False)
    embed.add_field(name=" Advertising",value="\n>>> *To promote something on this server it has to be agreed by* {}".format(tr3x.mention),inline=False)
    embed.add_field(name=" Trolling",value="\n>>> *If you annoy or troll someone all the time you can expect a timeout/ban*",inline=False)
    embed.add_field(name=" Bot sabutage",value="\n>>> *If you execute the tr3xBot's commands unnecessarily often or with the intention of provoking an error youll get banned asap (meme/nsfw commands can of course be used as often as you want, this rule means for example spamming play and stop commands unnecessarily)*",inline=True)
    embed.add_field(name=" Be friendly and respectful",value="\n>>> *Treat everyone, not only on this server, in a friendly and respectful way and accept everyone, even if you may have a different view of certain things than this person, as he/she/... is*",inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/695384979495977011/788086281846390804/Rules.png")
    

    button = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="Accept",
            custom_id="green"
        ),
    )
    msg = await Rulemessage.edit(embed=embed,
        components=[button]
    )
    while True:
        
        inter = await Rulemessage.wait_for_button_click()
        if discord.utils.get(inter.author.roles, name="Member") is None:
            Role = discord.utils.get(Rulemessage.guild.roles, name="Member")
            await inter.author.add_roles(Role,reason=None)
            await inter.reply("{} accepted the Rules".format(inter.author.mention), delete_after= 5.0)   
        else:
            await inter.author.send("You already accepted the Rules.")
    


async def background_task():
    await bot.wait_until_ready()
    while not bot.is_closed():
        console_input = await aioconsole.ainput()
        if console_input == "exit" or console_input == "tdc" or console_input == "update":
            if console_input == "exit" or console_input =="tdc":
                guild = bot.get_guild(718926812033581108)

                statuschannel = bot.get_channel(860642601098280970)
                statusmsg = await statuschannel.fetch_message(871558788388360223)
                botoffline = discord.Embed(title="**tr3xBot Status**",
                                        description= '`tr3xBot` is currently offline ⛔',
                                        color=0xff0000)
                botoffline.add_field(name="**What does this mean for you?**",value="All features like commands or the member/online count wont update until i am back online",inline=False)
                botoffline.add_field(name="**Why i am offline?**",value="Most likely i am offline cause an maintenance break or an server crash",inline=False)
                botoffline.set_footer(text="presents by tr3xBot")
                await statusmsg.edit(embed=botoffline)

                voice = discord.utils.get(bot.voice_clients, guild=guild)

                try:
                    if voice.is_connected() == True:
                        await voice.disconnect()
                except Exception as err:
                    pass
                
                await bot.change_presence(status=discord.Status.invisible)
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"{0.user}".format(bot)," is Offline now ","on:",guild.name)
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"Confirmed Offline")
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot was shutdowned via console")
                await bot.close()
            if console_input == "update":
                guild = bot.get_guild(718926812033581108) 
                memberings=0
                online=0
                members = bot.guilds[0].members 
                for i in members:
                    if i.status == discord.Status.offline:                         
                        memberings=memberings+1                                    
                    elif i.status != discord.Status.offline:                        
                        memberings=memberings+1
                        online=online+1
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"The latest data is being loaded...")
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"Online as {0.user}".format(bot),"on:",guild.name) 
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"IP:",requests.get('http://api.ipify.org').text)
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"Members: (",online,"/",memberings,")")
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"Confirmed Online")  
        else: 
            print(time.strftime('[%H:%M:%S]:', time.localtime()),"unexcepted or wrong input")
            print(time.strftime('[%H:%M:%S]:', time.localtime()),"«exit» or «tdc» for shutdown, «update» for latest data and «restart» for restart")

@tasks.loop(seconds=10.0)
async def status_1():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="th for Help"),status=discord.Status.online)
@tasks.loop(seconds=5.0)
async def status_2():    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with code"),status=discord.Status.online)
    
@tasks.loop(seconds=5.0)
async def boost():
    guild = bot.get_guild(718926812033581108)
    boostschannel = guild.get_channel(861753968890871839)
    boosts = guild.premium_subscription_count
    await boostschannel.edit(name = f"🌐 𝘽𝙤𝙤𝙨𝙩𝙨 : {boosts}")
@tasks.loop(seconds=10.0)
async def member_counter():
    guild = bot.get_guild(718926812033581108)
    channelmember = guild.get_channel(858711678316052500)
    channelonline = guild.get_channel(861365241413107732)
    memberings=0
    online=0
    members = bot.guilds[0].members 
    for i in members:
        if i.status == discord.Status.offline:                         
            memberings=memberings+1                                   
        elif i.status != discord.Status.offline:                        
            memberings=memberings+1
            online=online+1
    await channelmember.edit(name = f'⚫ 𝙈𝙚𝙢𝙗𝙚𝙧 : {guild.member_count}')
    await channelonline.edit(name = f'🟢 𝙊𝙣𝙡𝙞𝙣𝙚 : {online}')

@bot.event
async def on_message(message):
    if message.channel.id == 803764491988107334:
        if str(message.content).startswith(bot.command_prefix):
            pass
        else:
            if message.author.id == botid or owner:
                pass
            else:
                await message.channel.purge(limit=1)
                await message.author.send("You are not allowed to send messages which aren't commands to the '"+str(message.channel)+"' channel")
    if message.channel.id == 803909189990088725:
        if str(message.content).startswith(bot.command_prefix):
            await message.channel.purge(limit=1)
            await message.author.send("You are not allowed to send commands to the '"+str(message.channel)+"' channel, Please use the '"+str(message.guild.get_channel(803764491988107334))+"' channel")
        else:
            pass

    await bot.process_commands(message)
    
@bot.command() 
async def say(ctx,*, arg: str = None): 
    await ctx.channel.purge(limit=1) 
    if arg is None:
        await ctx.send("What should i say ?")
    else:
        await ctx.send(arg)

@bot.command(aliases=["h"]) 
async def help(ctx):
    
    embed=discord.Embed(title="Hey, i am the tr3xBot from the tr3xGaming Server :D", color=0x00ffcc)
    embed.set_author(name="tr3xBot", url="https://discord.gg/KexhwUVG7p")
    embed.add_field(name="You can find my Commands here:", value="https://tr3xgaming.herokuapp.com/html/tr3xbot/commands.html", inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    
    await ctx.channel.purge(limit=1)
    await ctx.author.send(embed=embed)


@bot.command()
async def embed(ctx, *, arg: str = None): 
    if arg is None:
        await ctx.send("To create an Embed use the following template (Title,Describtion,Footer)")
    else:            
        args = arg.split(',') 
        if len(args) == 3:
            embed = discord.Embed(title = args[0],
                                    description = args[1],
                                    color=0x00ffcc)
            embed.set_footer(text=args[2])
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)
        
         
@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx,arg: str = None):

    if arg is None:
        await ctx.channel.purge(limit=1)
        await ctx.author.send("How many Messaages should i delete? (tclear x)")
    else:
        if ctx.author.permissions_in(ctx.channel).manage_messages:
            args = arg.split(' ')
            if len(args) == 1:
                if args[0].isdigit():
                    count = int(args[0])+1
                    deleted = await ctx.channel.purge(limit=count)
                    embed = discord.Embed(title = '{} Messages deleted.'.format(len(deleted)-1),
                                    color=0x00ffcc)
                    await ctx.channel.purge(limit=1)
                    await ctx.send(embed=embed, delete_after= 10.0)
        
@bot.command()
async def roulette(ctx,arg: str = None):
    if arg is None:
        await ctx.send("Use the following template to play roulette (troulette [red]/[black]/[0-36])")
    else:
        bid = arg
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
                
@bot.command()
async def hug(ctx):
    await ctx.send("{} hugs himself :smiling_face_with_tear:".format(ctx.message.author.mention))

@bot.command()
async def coc(ctx, arg: str = None):
    if arg is None:
        await ctx.send("Please use the following template to searching a coc account (tcoc #XXXXXXXX)")
    else:
        playerInput = arg
        if playerInput.startswith("#"):
            player = await cocclient.get_player(playerInput)
            clan = await cocclient.get_clan(player.clan.tag)
            if clan.type == "open":
                    joinable = "Yes"
            else:
                    joinable = "No (",clan.type,")"

            if player.town_hall < 9:
                url = "https://static.wikia.nocookie.net/clashofclans/images/5/52/Town_Hall6.png/revision/latest/scale-to-width-down/100?cb=20170827050220"
            if player.town_hall == 9:
                url = "https://static.wikia.nocookie.net/clashofclans/images/e/e0/Town_Hall9.png/revision/latest/scale-to-width-down/100?cb=20170827045259"
            if player.town_hall == 10:
                url = "https://static.wikia.nocookie.net/clashofclans/images/5/5c/Town_Hall10.png/revision/latest/scale-to-width-down/115?cb=20170827040043"
            if player.town_hall == 11:
                url = "https://static.wikia.nocookie.net/clashofclans/images/9/96/Town_Hall11.png/revision/latest/scale-to-width-down/110?cb=20210410001514"
            if player.town_hall == 12:
                url = "https://static.wikia.nocookie.net/clashofclans/images/c/c7/Town_Hall12-1.png/revision/latest/scale-to-width-down/120?cb=20180603203226"
            if player.town_hall == 13:
                url = "https://static.wikia.nocookie.net/clashofclans/images/9/98/Town_Hall13-1.png/revision/latest/scale-to-width-down/120?cb=20200831024426"
            if player.town_hall == 14:
                url = "https://static.wikia.nocookie.net/clashofclans/images/e/e0/Town_Hall14-1.png/revision/latest/scale-to-width-down/110?cb=20210413000722"
            
            
            embed=discord.Embed(title="Clash of Clans Stats", color=0xf0d005)
            embed.add_field(name="Player", value=player.name, inline=True)
            embed.add_field(name="Level", value=player.exp_level, inline=True)
            embed.add_field(name="Townhall", value=player.town_hall, inline=True)
            embed.add_field(name="Builderhall", value=player.builder_hall, inline=True)
            embed.add_field(name="Multiplayer trophies ", value=player.trophies, inline=True)
            embed.add_field(name="Builderbase trophies ", value=player.versus_trophies, inline=True)
            embed.add_field(name="Clan", value=str(player.clan)+player.clan.tag, inline=True)
            embed.add_field(name="Clan-Level", value=clan.level, inline=True)
            embed.add_field(name="Role", value=player.role, inline=True)
            embed.add_field(name="Clanmember", value=clan.member_count, inline=True)
            embed.add_field(name="Joinable", value=joinable, inline=True)
            embed.add_field(name="Language", value=clan.chat_language, inline=True)
            embed.add_field(name="Discription", value=clan.description, inline=True)
            embed.add_field(name="War-frequency", value=clan.war_frequency, inline=True)
            embed.add_field(name="Rank", value=clan.war_league, inline=True)
            embed.add_field(name="Link", value=clan.share_link, inline=True)
            embed.set_thumbnail(url=url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Sorry ",playerInput," is not a Valid Playertag, try again")
        
api_key = "abbc964449ba2ad5a22facf4dd51fcaf"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@bot.command()
async def kill(ctx,arg: str = None):
    if arg is None:
        await ctx.channel.purge(limit=1)
        await ctx.send("{}".format(ctx.message.author.mention)+" killed himself")
    else:
        if arg != None:
            await ctx.send("{}".format(ctx.message.author.mention)+" killed "+arg)
            
        else:
            await ctx.send("tell me who... tkill @example")

@bot.command()
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(choice(responses))

ytdl_format_options = {'format': 'bestaudio/best','outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s','restrictfilenames': True,'noplaylist': False,'nocheckcertificate': True,'ignoreerrors': False,'logtostderr': False,'quiet': True,'no_warnings': True,'default_search': 'auto','source_address': '0.0.0.0' }
ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

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

@bot.command()
async def play(ctx, *, arg: str = None):

    if arg is None:
        embedER = discord.Embed(title="Please tell what i should play (ex. tplay lalala or tplay <yt url>)",color=0x00ffcc)
        await ctx.send(embed=embedER)
    else:
        url = arg
        if ctx.author.voice is None:
            embed = discord.Embed(title="Please connect to an Voice channel first to play Music",colour=0x00ffcc)
            await ctx.send(embed=embed)
        else:
            if ctx.voice_client == None:
                    await ctx.author.voice.channel.connect()
            async with ctx.typing():
                        if ctx.voice_client.is_playing() == True:
                            global queue
                            queue.append(url)
                            player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
                            embed = discord.Embed(title="Queued :musical_note:", description=f'[{player.title}]({player.url}) added to queue!',colour=0x00ffcc)
                            await ctx.send(embed=embed)
                        else:
                            player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
                            ctx.voice_client.play(player, after=lambda e: play_next(ctx))
                            embed = discord.Embed(title="Now playing :musical_note:", description=f"[{player.title}]({player.url})",colour=0x00ffcc)
                            await ctx.send(embed=embed)

def play_next(ctx):
    asyncio.run_coroutine_threadsafe(n(ctx), bot.loop)

async def n(ctx):  
    global queue
    if len(queue) > 0:
        if ctx.voice_client.is_playing() == True:
            ctx.voice_client.stop()

        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            player = await YTDLSource.from_url(queue[0], loop=bot.loop, stream=True)
            voice_channel.play(player, after=lambda e: play_next(ctx))

        embed = discord.Embed(title="Now playing :musical_note:", description=f"[{player.title}]({player.url})",colour=0x00ffcc)
        await ctx.send(embed=embed)
        del(queue[0])
    

@bot.command()
async def skip(ctx):  
    global queue

    if ctx.author.voice is None:
        embed = discord.Embed(title="Please connect to an Voice channel first to skip",colour=0x00ffcc)
        await ctx.send(embed=embed)
    else:
        if discord.utils.get(bot.voice_clients, guild=ctx.guild) != None:
            if ctx.voice_client.is_playing():
                if len(queue) > 0:
                    if ctx.voice_client.is_playing() == True:
                        ctx.voice_client.stop()

                    server = ctx.message.guild
                    voice_channel = server.voice_client

                    async with ctx.typing():
                        player = await YTDLSource.from_url(queue[0], loop=bot.loop, stream=True)
                        voice_channel.play(player, after=lambda e: play_next(ctx))

                    embed = discord.Embed(title="Now playing :musical_note:", description=f"[{player.title}]({player.url})",colour=0x00ffcc)
                    await ctx.send(embed=embed)
                    del(queue[0])
                else:
                    await ctx.send("No more Songs queued!")
            else:
                embed = discord.Embed(title="I am not playing music at the moment",colour=0x00ffcc)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=" I am not connected to any Voice Chat at the moment",colour=0x00ffcc)
            await ctx.send(embed=embed)


@bot.command()
async def pause( ctx):
    if ctx.author.voice is None:
        embed = discord.Embed(title="Please connect to an Voice channel first to pause me",colour=0x00ffcc)
        await ctx.send(embed=embed)
    else:
        if discord.utils.get(bot.voice_clients, guild=ctx.guild) != None:
            if ctx.voice_client.is_playing():
                ctx.voice_client.pause()
                embed = discord.Embed(title="Paused :pause_button:",colour=0x00ffcc)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title=" I am not playing music at the moment",colour=0x00ffcc)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=" I am not connected to any Voice Chat at the moment",colour=0x00ffcc)
            await ctx.send(embed=embed)
    
@bot.command()
async def resume( ctx):
    if ctx.author.voice is None:
        embed = discord.Embed(title="Please connect to an Voice channel first to resume my audio",colour=0x00ffcc)
        await ctx.send(embed=embed)
    else:
        if discord.utils.get(bot.voice_clients, guild=ctx.guild) != None:
            ctx.voice_client.resume()
            embed = discord.Embed(title="Resuming :play_pause: ",colour=0x00ffcc)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="I am not connected to any Voice Chat at the moment",colour=0x00ffcc)
            await ctx.send(embed=embed)

@bot.command()
async def stop( ctx):
    if ctx.author.voice is None:
        embed = discord.Embed(title="Please connect to an Voice channel first to stop me",colour=0x00ffcc)
        await ctx.send(embed=embed)
    else:
        if discord.utils.get(bot.voice_clients, guild=ctx.guild) != None:
            if ctx.voice_client.is_playing():
                try:
                    await ctx.voice_client.stop()
                    embed = discord.Embed(title="Stopped :stop_button:",colour=0x00ffcc)
                    await ctx.send(embed=embed)
                except Exception as err:
                    pass
            else:
                embed = discord.Embed(title=" I am not playing music at the moment",colour=0x00ffcc)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=" I am not connected to any Voice Chat at the moment",colour=0x00ffcc)
            await ctx.send(embed=embed)

@bot.command()
async def leave(ctx):
    if ctx.author.voice is None:
        embed = discord.Embed(title="Please connect to an Voice channel first to make me leave the Channel",colour=0x00ffcc)
        await ctx.send(embed=embed)
    else:
        if discord.utils.get(bot.voice_clients, guild=ctx.guild) != None:
            await ctx.voice_client.disconnect()
        else:
            embed = discord.Embed(title=" I am not connected to any Voice Chat at the moment",colour=0x00ffcc)
            await ctx.send(embed=embed)

@bot.command()
async def userlimit(ctx,arg: str = None):
    if arg is None:
        await ctx.send("To give a channel a userlimit use the followning template (ex. tuserlimit x )")
    else:
        if ctx.author.voice is None:
            await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
        else:
            if ctx.author.voice.channel.category == ctx.guild.get_channel(858020017822892092) or ctx.author.id == owner:
                if int(arg) >= 99:
                    await ctx.send("Value should be less than or equal to 99")
                else:
                    await ctx.send("Userlimit of '"+str(ctx.author.voice.channel)+"' got changed by "+str(ctx.author)+" from "+str(ctx.author.voice.channel.user_limit)+" to "+arg)
                    await ctx.author.voice.channel.edit(user_limit=int(arg))
                    
            else:
                await ctx.send("You dont have the permission to edit channels outside the Talks Category")

@bot.command()
async def talkname(ctx,*,arg: str = None):
    if arg is None:
        await ctx.send("To give a channel a custom name use the followning template (ex. ttalkname x x x x x x )")
    else:
        if ctx.author.voice is None:
            await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
        else:
            if ctx.author.voice.channel.category == ctx.guild.get_channel(858020017822892092) or ctx.author.id == owner:
                if len(arg) > 15:
                    await ctx.send("Please choose a shorter Talkname")
                else:
                    await ctx.send("Talkname of '"+str(ctx.author.voice.channel)+"' got changed by "+str(ctx.author)+" to '"+arg+"'")
                    await ctx.author.voice.channel.edit(name=str(arg))
                
            else:
                await ctx.send('You dont have the permission to edit channels outside the Talks Category')

@bot.command()
async def end(ctx):
    if ctx.author.voice is None:
        await ctx.send("Connect to a Voice Channel in Talks first to edit it ")
    else:
        if ctx.author.voice.channel.category == ctx.guild.get_channel(858020017822892092) or ctx.author.id == owner:
            await ctx.send("Talk '"+str(ctx.author.voice.channel)+"' got deleted by "+str(ctx.author))
            await ctx.author.voice.channel.delete()
            
            
        else:
            await ctx.send('You dont have the permission to edit channels outside the Talks Category')




@bot.event
async def on_voice_state_update(member, before, after):
    guild = member.guild
    voicehub = guild.get_channel(873323443163115560)
    Talkcategory = guild.get_channel(858020017822892092)

    if after.channel == voicehub:
        channel = await guild.create_voice_channel(
            name=str(member.name)+"`s channel",
            category=Talkcategory,
            reason=None,
            bitrate= guild.bitrate_limit
        )
        await member.move_to(channel)
    try:
        if not before.channel.members and before.channel.category == Talkcategory and before.channel != voicehub:
            await before.channel.delete()
    except Exception as err:
        pass


@bot.command()
async def meme(ctx):
    async with ctx.typing():
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title="", description="")
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def dankmemes(ctx):
    async with ctx.typing():
        memes_submissions = reddit.subreddit('dankmemes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title="", description="")
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def cats(ctx):
    async with ctx.typing():
        memes_submissions = reddit.subreddit('cats').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title="", description="")
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def boobs(ctx):
    async with ctx.typing():
        nsfw = ctx.guild.get_channel(800715988794081281)
        if ctx.channel == nsfw:
            memes_submissions = reddit.subreddit('boobs').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))

@bot.command(pass_context=True)
async def ass(ctx):
    async with ctx.typing():
        nsfw = ctx.guild.get_channel(800715988794081281)
        if ctx.channel == nsfw:
            memes_submissions = reddit.subreddit('ass').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))

@bot.command(pass_context=True)
async def teen(ctx):
    async with ctx.typing():
        nsfw = ctx.guild.get_channel(800715988794081281)
        if ctx.channel == nsfw:
            memes_submissions = reddit.subreddit('LegalTeens').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))

@bot.command(pass_context=True)
async def pussy(ctx):
    async with ctx.typing():
        nsfw = ctx.guild.get_channel(800715988794081281)
        if ctx.channel == nsfw:
            memes_submissions = reddit.subreddit('pussy').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))

@bot.command(pass_context=True)
async def dick(ctx):
    async with ctx.typing():
        nsfw = ctx.guild.get_channel(800715988794081281)
        if ctx.channel == nsfw:
            memes_submissions = reddit.subreddit('dicks').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))

@bot.command(pass_context=True)
async def cum(ctx):
    async with ctx.typing():
        nsfw = ctx.guild.get_channel(800715988794081281)
        if ctx.channel == nsfw:
            memes_submissions = reddit.subreddit('cum').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))

@bot.command(pass_context=True)
async def hentai(ctx):
    async with ctx.typing():
        nsfw = ctx.guild.get_channel(800715988794081281)
        if ctx.channel == nsfw:
            memes_submissions = reddit.subreddit('hentai').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))

@bot.command(pass_context=True)
async def milf(ctx):
    async with ctx.typing():
        nsfw = ctx.guild.get_channel(800715988794081281)
        if ctx.channel == nsfw:
            memes_submissions = reddit.subreddit('MILFs').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))

@bot.command(pass_context=True)
async def lesbian(ctx):
    async with ctx.typing():
        nsfw = ctx.guild.get_channel(800715988794081281)
        if ctx.channel == nsfw:
            memes_submissions = reddit.subreddit('lesbians').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))


@bot.command(pass_context=True)
async def gif(ctx):
    async with ctx.typing():
        memes_submissions = reddit.subreddit('gifs').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title="", description="")
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def waifu(ctx):
    async with ctx.typing():
        memes_submissions = reddit.subreddit('waifusfortr3x').hot()
        post_to_pick = random.randint(1, 40)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title="", description="")
        embed.set_image(url=submission.url)

        alreadysended = False
        messages = await ctx.history(limit=200).flatten()
        for msg in messages:
            embeds = msg.embeds
            for embed in embeds:
                if embed.image_url == submission.url:
                    alreadysended = True
                    break
            if alreadysended == False:
                await ctx.send(embed=embed)
                break
            else:
                break
        #await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def anime(ctx):
    async with ctx.typing():
        memes_submissions = reddit.subreddit('Animemes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title="", description="")
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)


@bot.event
async def on_member_join(member):
    welcomechannel = bot.get_channel(828410713294372885)
    guild = bot.get_guild(718926812033581108)
    await welcomechannel.send(f"Welcome {member.mention} on the tr3xGaming Discord Server !" )

    embed=discord.Embed(title=" Welcome on the tr3xGaming Server, i am the tr3xBot", color=0x00ffcc)
    embed.set_author(name="tr3xBot", url="https://discord.gg/KexhwUVG7p")
    embed.add_field(name="You can find my Commands here:", value="https://tr3xgaming.herokuapp.com/html/tr3xbot/commands.html", inline=False)
    await member.send(embed=embed)

@tasks.loop(hours=1)
async def fg():
    channel = bot.get_channel(871595543468601404)
    messages = await channel.history(limit=200).flatten()
        
    memes_submissions = reddit.subreddit('freegames').new()
    post_to_pick = 1
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embedFG = discord.Embed(title="New Free Game :gift:", description=submission.title)
    embedFG.add_field(name="Get it here:",value=submission.url,inline=True)

    alreadysended = False
    for msg in messages:
            embeds = msg.embeds
            for embed in embeds:
                if embed.description == submission.title:
                    alreadysended = True
                    break

            if alreadysended == False:
                await channel.send(embed=embedFG)
                break
            else:
                break

@tasks.loop(hours=1)
async def newsGER():
    channel = bot.get_channel(872948474264555530)
    messages = await channel.history(limit=200).flatten()
        
    memes_submissions = reddit.subreddit('NachrichtenDE').new()
    post_to_pick = 1
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embedN = discord.Embed(title="News :newspaper:", description=submission.title)
    embedN.add_field(name="Source: ",value=submission.url,inline=True)

    alreadysended = False
    for msg in messages:
            embeds = msg.embeds
            for embed in embeds:
                if embed.description == submission.title:
                    alreadysended = True
                    break

            if alreadysended == False:
                await channel.send(embed=embedN)
                break
            else:
                break

@tasks.loop(hours=1)
async def newsENG():
    channel = bot.get_channel(874616666921795594)
    messages = await channel.history(limit=200).flatten()
        
    memes_submissions = reddit.subreddit('news').new()
    post_to_pick = 1
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embedN = discord.Embed(title="News :newspaper:", description=submission.title)
    embedN.add_field(name="Source: ",value=submission.url,inline=True)

    alreadysended = False
    for msg in messages:
            embeds = msg.embeds
            for embed in embeds:
                if embed.description == submission.title:
                    alreadysended = True
                    break

            if alreadysended == False:
                await channel.send(embed=embedN)
                break
            else:
                break


bot.loop.create_task(background_task())
bot.run("ODMwODQyMjYwNDYyNjMyOTky.YHMkJw.kfT7gSJUokKHamktiHR8SgvpXrg")

