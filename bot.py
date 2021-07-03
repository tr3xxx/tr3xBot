import asyncio, time, requests, random, discord, DiscordUtils, aiohttp, youtube_dl, aioconsole 
from discord.ext import commands, tasks

#py -3 -m pip install -U aioconsole

print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot is starting...")
bot = commands.Bot(command_prefix="t",help_command=None, intents=discord.Intents().all())

@bot.event
async def on_ready():
    guild = bot.get_guild(718926812033581108) 
    members = bot.guilds[0].members 
    memberings=0
    online =0
    for i in members:
        if i.status == discord.Status.offline:                        
            memberings=memberings+1                                    
        elif i.status != discord.Status.offline:

            memberings=memberings+1
            online=online+1

    member_counter.start()
    status_1.start()
    status_2.start()

    ruleschannel = bot.get_channel(803240539578302524)
    rulemsg = await ruleschannel.fetch_message(860636421047320627)
    await rulemsg.add_reaction("✅")

    statuschannel = bot.get_channel(860642601098280970)
    statusmsg = await statuschannel.fetch_message(860645008168058880)
    botonline = discord.Embed(title="**tr3xBot Status**",
                              description= 'I am currently online ✅',
                              color=0x0CFF00)
    botonline.set_footer(text="presents by tr3xBot")
    await statusmsg.edit(embed=botonline)
    
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Online as {0.user}".format(bot),"on:",guild.name) 
    print(time.strftime('[%H:%M:%S]:', time.localtime()),f"Ping: {int(bot.latency * 1000)} ms")
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"IP:",requests.get('http://api.ipify.org').text)
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Members: (",online,"/",memberings,")")
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Confirmed Online")
    print(" ")
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"«exit» or «tdc» for shutdown, «update» for latest data")

async def background_task():
    await bot.wait_until_ready()
    while not bot.is_closed():
        console_input = await aioconsole.ainput()
        if console_input == "exit" or console_input == "tdc" or console_input == "update":
            if console_input == "exit" or console_input =="tdc":
                guild = bot.get_guild(718926812033581108)

                statuschannel = bot.get_channel(860642601098280970)
                statusmsg = await statuschannel.fetch_message(860645008168058880)
                botoffline = discord.Embed(title="**tr3xBot Status**",
                                        description= 'I am currently offline :no_entry:',
                                        color=0xff0000)
                botoffline.add_field(name="**What does this mean for you?**",value="All features like commands or the member/online count wont update until i am back online",inline=False)
                botoffline.add_field(name="**Why i am offline?**",value="Most likely i am offline cause an maintenance break or an server crash",inline=False)
                botoffline.set_footer(text="presents by tr3xBot")
                await statusmsg.edit(embed=botoffline)

                await bot.change_presence(status=discord.Status.invisible)
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"{0.user}".format(bot)," is Offline now ","on:",guild.name)
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"Confirmed Offline")
                print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot was shutdowned via console")
                await bot.logout()
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
            print(time.strftime('[%H:%M:%S]:', time.localtime()),"«exit» or «tdc» for shutdown, «update» for latest data")

@tasks.loop(seconds=10.0)
async def status_1():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='BETA'),status=discord.Status.do_not_disturb)
@tasks.loop(seconds=5.0)
async def status_2():    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=' with code'),status=discord.Status.do_not_disturb) 
@tasks.loop(seconds=10.0)
async def member_counter():
    guild = bot.get_guild(718926812033581108)
    channelmember = guild.get_channel(858711678316052500)
    channelonline = guild.get_channel(858711812736548884)
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
    
@bot.command() 
async def say(ctx,*, arg): 
    await ctx.channel.purge(limit=1) 
    await ctx.send(arg)

#@bot.event
#async def on_message(message):
#
#    if message.channel.id == 803764491988107334:
#        if message.content.startswith("t"):
#            return
#        else:
#            await message.channel.purge(limit=1)
#            embed = discord.Embed(title="**Your Message got deleted**",
#                                description= "Your message got deleted cause you havent used an command of me.\nIf you wanna know my commands, use th.",
#                                color=0xff0000)
#            await message.author.send(embed=embed)
#    else:
#        return
#
# Funktioniert zwar aber, warum auch immer crashed das den kompletten Bot also es funktioniert kein command mehr, da ehr scheinbar nur noch den channel "bewacht" lol

           
@bot.command() 
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


@bot.command() #tembed titel, desc, footer
async def embed(ctx, *, arg): 
                              
    args = arg.split(',') 
    if len(args) == 3:
        embed = discord.Embed(title = args[0],
                                description = args[1],
                                color=0x22a7f0)
        embed.set_footer(text=args[2])
        await ctx.send(embed=embed)
         
@bot.command()
async def clear(ctx,arg):
        
    if ctx.author.permissions_in(ctx.channel).manage_messages:
        args = arg.split(' ')
        if len(args) == 1:
            if args[0].isdigit():
                count = int(args[0])+1
                deleted = await ctx.channel.purge(limit=count)
                embed = discord.Embed(title = '{} Messages deleted.'.format(len(deleted)-1),
                                color=0x22a7f0)
                await ctx.channel.send(embed=embed)
        
@bot.command()
async def roulette(ctx,arg):
       
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
async def kill(ctx,arg):

    if arg != None:
         await ctx.send("{}".format(ctx.message.author.mention)+" killed "+arg)
         
    else:
         await ctx.send("tell me who... tkill @example")

@bot.command()
async def dm(ctx):
    await ctx.author.send("Hello, this is a DM! "+ "{}".format(ctx.message.author.mention))

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
    'source_address': '0.0.0.0'
}

music = DiscordUtils.Music()
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

ffmpeg_options = {
    'options': '-vn',
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
}

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
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@bot.command()
async def join(ctx):
    voicetrue=ctx.author.voice
    if voicetrue is None:
        return await ctx.send('You are not currently in a voice channel')
    await ctx.author.voice.channel.connect()
    await ctx.send('Joined your voice channel')

@bot.command()
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
    print(player.queue)


@bot.command()
async def pause( ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused ⏸️")
    
@bot.command()
async def resume( ctx):
        ctx.voice_client.resume()
        await ctx.send("Resuming ⏯️")

@bot.command()
async def leave( ctx):
        await ctx.voice_client.disconnect()

@bot.command()
async def skip( ctx):
        ctx.voice_client.skip()
        await ctx.send("Skipped :track_next:")

@bot.event
async def on_voice_state_update(member, before, after):
    guild = bot.get_guild(718926812033581108)
    username = str(member.name)
    ch = guild.get_channel(858272905108258816)
    schoolch = guild.get_channel(859670479551725578)
    afkch = guild.get_channel(859718892334350356)
    category = guild.get_channel(858020017822892092)

    if after.channel == ch:
        channel = await guild.create_voice_channel(
            name=username+"`s channel",
            category=category,
            overwrites=None,
            reason=None,
            user_limit=69,
            bitrate=256000
        )
        await member.move_to(channel)
    if not before.channel.members and before.channel != ch and before.channel != None and before != None and before.channel != schoolch and before.channel != afkch:
        await before.channel.delete()

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
        async with cs.get('https://www.reddit.com/r/gifs/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(718926812033581108)
    if payload.message_id != 860636421047320627:
        return
    if payload.emoji.name == "✅":
            Role = discord.utils.get(guild.roles, name="Member")
            await payload.member.add_roles(Role,reason=None)
            print(time.strftime('[%H:%M:%S]:', time.localtime()),payload.member,"accepted the rules and got the member role.") 

@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(718926812033581108)
    if payload.message_id != 860636421047320627:
        return
    else:
            Role = discord.utils.get(guild.roles, name="Member")
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(Role,reason=None)
            print(time.strftime('[%H:%M:%S]:', time.localtime()),payload.member," unaccepted the rules and lost the member role.") 

bot.loop.create_task(background_task())
bot.run("ODMwODQyMjYwNDYyNjMyOTky.YHMkJw.dpS5uYAO3xLRW3JHQue4yDzp75g")
