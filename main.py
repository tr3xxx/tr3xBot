import asyncio, time, requests, random, discord,aiohttp, youtube_dl, aioconsole,re,time
from discord.ext import commands, tasks
from random import choice

#py -3 -m pip install -U aioconsole  @Waldemar

print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot is starting...")
bot = commands.Bot(command_prefix="t",help_command=None, intents=discord.Intents().all())
queue = []

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
    boost.start()

    statuschannel = bot.get_channel(860642601098280970)
    statusmsg = await statuschannel.fetch_message(871558788388360223)
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
                statusmsg = await statuschannel.fetch_message(871558788388360223)
                botoffline = discord.Embed(title="**tr3xBot Status**",
                                        description= 'I am currently offline ⛔',
                                        color=0xff0000)
                botoffline.add_field(name="**What does this mean for you?**",value="All features like commands or the member/online count wont update until i am back online",inline=False)
                botoffline.add_field(name="**Why i am offline?**",value="Most likely i am offline cause an maintenance break or an server crash",inline=False)
                botoffline.set_footer(text="presents by tr3xBot")
                await statusmsg.edit(embed=botoffline)

                #voice = discord.utils.get(bot.voice_clients, guild=guild)
                #if voice.is_connected():
                #   await voice.disconnect()
                

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
            print(time.strftime('[%H:%M:%S]:', time.localtime()),"«exit» or «tdc» for shutdown, «update» for latest data and «restart» for restart")

@tasks.loop(seconds=5.0)
async def status_1():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=' you'),status=discord.Status.online)
@tasks.loop(seconds=5.0)
async def status_2():    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=' with code'),status=discord.Status.online)
    
@tasks.loop(seconds=5.0)
async def boost(seconds= 10.0):
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
    
    embed=discord.Embed(title="Hey, i am the tr3xBot from the tr3xGaming Server :D", color=0x00ffcc)
    embed.set_author(name="tr3xBot", url="https://discord.gg/KexhwUVG7p")
    embed.add_field(name=" â € ", value="My Commands:", inline=False)
    embed.add_field(name="th", value="U should know this already", inline=True)
    embed.add_field(name="troulette", value="Play some roulette ex: troulette black/red/0-36", inline=True)
    embed.add_field(name="tembed", value="Will create an Message in an Embed ex: tembed title,desc,footer", inline=True)
    embed.add_field(name="tclear", value="This will clear X Messages (only available for admins/mods )", inline=True)
    embed.add_field(name="thug", value=" Need a hug after an hard day ? I gotchu", inline=True)
    embed.add_field(name=" â € ", value="Music Commands:", inline=False)
    embed.add_field(name="tjoin", value="Its self-explanatory isnt it?", inline=True)
    embed.add_field(name="tplay ", value="U can play either an url or give the keyword to search for. me an ", inline=True)
    embed.add_field(name="tpause", value="This will create an new universum, nah just kidding its just a pause command", inline=True)
    embed.add_field(name="tresume", value="Will hard to understand what this may do ", inline=True)
    embed.add_field(name="tleave", value="The Bot will leave and stop playing obviously", inline=True)
    embed.add_field(name=" â € ", value="Meme/ NSFW Commands:", inline=False)
    embed.add_field(name="tmemes / tdarkmemes / dankmemes / boobs / ass", value="Just try them out ", inline=True)
    await ctx.channel.purge(limit=1)
    await ctx.author.send(embed=embed)

@bot.command() 
async def help(ctx):
    
    embed=discord.Embed(title="Hey, i am the tr3xBot from the tr3xGaming Server :D", color=0x00ffcc)
    embed.set_author(name="tr3xBot", url="https://discord.gg/KexhwUVG7p")
    embed.add_field(name=" â € ", value="My Commands:", inline=False)
    embed.add_field(name="th", value="U should know this already", inline=True)
    embed.add_field(name="troulette", value="Play some roulette ex: troulette black/red/0-36", inline=True)
    embed.add_field(name="tembed", value="Will create an Message in an Embed ex: tembed title,desc,footer", inline=True)
    embed.add_field(name="tclear", value="This will clear X Messages (only available for admins/mods )", inline=True)
    embed.add_field(name="thug", value=" Need a hug after an hard day ? I gotchu", inline=True)
    embed.add_field(name=" â € ", value="Music Commands:", inline=False)
    embed.add_field(name="tjoin", value="Its self-explanatory isnt it?", inline=True)
    embed.add_field(name="tplay ", value="U can play either an url or give the keyword to search for. me an ", inline=True)
    embed.add_field(name="tpause", value="This will create an new universum, nah just kidding its just a pause command", inline=True)
    embed.add_field(name="tresume", value="Will hard to understand what this may do ", inline=True)
    embed.add_field(name="tleave", value="The Bot will leave and stop playing obviously", inline=True)
    embed.add_field(name=" â € ", value="Meme/ NSFW Commands:", inline=False)
    embed.add_field(name="tmemes / tdarkmemes / dankmemes / boobs / ass", value="Just try them out ", inline=True)
    await ctx.channel.purge(limit=1)
    await ctx.author.send(embed=embed)


@bot.command() #tembed titel, desc, footer
async def embed(ctx, *, arg): 
                              
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
async def clear(ctx,arg):
        
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

    await ctx.channel.purge(limit=1)
    if arg != None:
         await ctx.send("{}".format(ctx.message.author.mention)+" killed "+arg)
         
    else:
         await ctx.send("tell me who... tkill @example")

@bot.command()
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(choice(responses))

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
    'options': '-vn'
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

@bot.command()
async def join(ctx):
    voicetrue=ctx.author.voice
    if voicetrue is None:
        return await ctx.send('You are not currently in a voice channel')
    await ctx.author.voice.channel.connect()
    await ctx.send('Joined your voice channel')

@bot.command()
async def remove(ctx, number):
    global queue

    try:
        del(queue[int(number)])
        await ctx.send(f'Your queue is now `{queue}!`')
    
    except:
        await ctx.send('Your queue is either **empty** or the index is **out of range**')

@bot.command()
async def play(ctx, *, arg):
    url = arg
    if ctx.voice_client == None:
            await ctx.author.voice.channel.connect()
    async with ctx.typing():
                if ctx.voice_client.is_playing() == True:
                    global queue
                    queue.append(url)
                    await ctx.send(f'`{url}` added to queue!')
                else:
                    player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
                    ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
                    #ctx.voice_client.play(player, after=lambda e: play_next(ctx))
                    embed = discord.Embed(title="Now playing :musical_note:", description=f"[{player.title}]({player.url})",colour=0x00ffcc)
                    await ctx.send(embed=embed)

#def play_next(ctx):
#    if len(queue) >= 1:
#        del queue[0]
#        player = discord.utils.get(bot.voice_clients, guild=ctx.guild)
#        ctx.voice_client.play(discord.FFmpegPCMAudio(player, after=lambda e: play_next(ctx)))
    
        
@bot.command()
async def next(ctx):
    global queue

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(queue[0], loop=bot.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    embed = discord.Embed(title="Now playing :musical_note:", description=f"[{player.title}]({player.url})",colour=0x00ffcc)
    await ctx.send(embed=embed)
    del(queue[0])


@bot.command()
async def pause( ctx):
    voicetrue=ctx.author.voice
    if voicetrue is None:
        embed = discord.Embed(title="Please connect to an Voice channel first to pause me")
        await ctx.send(embed=embed)
    else:
        ctx.voice_client.pause()
        embed = discord.Embed(title="Paused â¸ï¸")
        await ctx.send(embed=embed)
    
@bot.command()
async def resume( ctx):
    voicetrue=ctx.author.voice
    if voicetrue is None:
        embed = discord.Embed(title="Please connect to an Voice channel first to resume my audio")
        await ctx.send(embed=embed)
    else:
        ctx.voice_client.resume()
        embed = discord.Embed(title="Resuming â¯ï¸")
        await ctx.send(embed=embed)

@bot.command()
async def leave( ctx):
        await ctx.voice_client.disconnect()

@bot.command()
async def stop( ctx):
    voicetrue=ctx.author.voice
    if voicetrue is None:
        embed = discord.Embed(title="Please connect to an Voice channel first to stop me")
        await ctx.send(embed=embed)
    else:
        await ctx.voice_client.stop()

@bot.command()
async def view(ctx):
    await ctx.send(f'Your queue is now `{queue}!`')

@bot.event
async def on_voice_state_update(member, before, after):
    guild = bot.get_guild(718926812033581108)
    username = str(member.name)
    ch = guild.get_channel(862036817363599380)
    schoolch = guild.get_channel(859670479551725578)
    afkch = guild.get_channel(859718892334350356)
    mem = guild.get_channel(858711678316052500)
    onl = guild.get_channel(861365241413107732)
    boost = guild.get_channel(859718892334350356)
    category = guild.get_channel(858020017822892092)
    maxbitrate = guild.bitrate_limit

    if after.channel == ch:
        channel = await guild.create_voice_channel(
            name=username+"`s channel",
            category=category,
            overwrites=None,
            reason=None,
            user_limit=69,
            bitrate=maxbitrate
        )
        await member.move_to(channel)
    if not before.channel.members and before.channel != ch and before.channel != schoolch and before.channel != afkch and before.channel != mem and before.channel != onl and before.channel != boost: 
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
    if payload.message_id !=860636421047320627:
        return
    if payload.emoji.name == "✅":
            Role = discord.utils.get(guild.roles, name="Member")
            print(1)
            await payload.member.add_roles(Role,reason=None)
            print(time.strftime('[%H:%M:%S]:', time.localtime()),payload.member,"accepted the rules and got the member role.") 

@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(718926812033581108)
    if payload.message_id !=860636421047320627:
        return
    else:
        Role = discord.utils.get(guild.roles, name="Member")
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        await member.remove_roles(Role,reason=None)
        print(time.strftime('[%H:%M:%S]:', time.localtime()),member," unaccepted the rules and lost the member role.") 

@bot.event
async def on_member_join(member):
    welcomechannel = bot.get_channel(828410713294372885)
    guild = bot.get_guild(718926812033581108)
    await welcomechannel.send(f"Welcome {member.mention} on the",guild.name,"Discord Server !" )


bot.loop.create_task(background_task())
bot.run("ODMwODQyMjYwNDYyNjMyOTky.YHMkJw.kfT7gSJUokKHamktiHR8SgvpXrg")

