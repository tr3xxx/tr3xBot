import time,discord,os
from discord.ext import commands
from dislash import InteractionClient

#py -3 -m pip install -U "package

print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot is starting...")

bot = commands.Bot(command_prefix="t",help_command=None, intents=discord.Intents().all())
slash = InteractionClient(bot)
queue = []


for folder in os.listdir("modules/commands/basic"):
            if os.path.exists(os.path.join("modules/commands/basic", folder, "cog.py")):
                bot.load_extension(f"modules.commands.basic.{folder}.cog")
            print(time.strftime('[%H:%M:%S]:', time.localtime()),folder,"loaded")
for folder in os.listdir("modules/commands/nsfw"):
            if os.path.exists(os.path.join("modules/commands/nsfw", folder, "cog.py")):
                print(time.strftime('[%H:%M:%S]:', time.localtime()),folder,"loaded")
                bot.load_extension(f"modules.commands.nsfw.{folder}.cog")
for folder in os.listdir("modules/commands/meme"):
            if os.path.exists(os.path.join("modules/commands/meme", folder, "cog.py")):
                print(time.strftime('[%H:%M:%S]:', time.localtime()),folder,"loaded")
                bot.load_extension(f"modules.commands.meme.{folder}.cog")
for folder in os.listdir("modules/commands/music"):
        if os.path.exists(os.path.join("modules/commands/music", folder, "cog.py")):
            print(time.strftime('[%H:%M:%S]:', time.localtime()),folder,"loaded")
            bot.load_extension(f"modules.commands.music.{folder}.cog")
for folder in os.listdir("modules/events"):
            if os.path.exists(os.path.join("modules/events", folder, "cog.py")):
                print(time.strftime('[%H:%M:%S]:', time.localtime()),folder,"loaded")
                bot.load_extension(f"modules.events.{folder}.cog")

 

@bot.event
async def on_ready():

    for folder in os.listdir("modules/tasks"):
        if os.path.exists(os.path.join("modules/tasks", folder, "cog.py")):
            print(time.strftime('[%H:%M:%S]:', time.localtime()),folder,"loaded")
            bot.load_extension(f"modules.tasks.{folder}.cog")
    
    
    

    log = bot.get_channel(875700881360846899)
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Online as {0.user}".format(bot))
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Successfully started")
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"«exit» or «tdc» for shutdown, «update» for latest data")
    await log.send("Bot started")
    
    statuschannel = bot.get_channel(860642601098280970)
    statusmsg = await statuschannel.fetch_message(871558788388360223)
    tr3x = bot.get_user(633412273641095188)
    botonline = discord.Embed(title="**tr3xBot Status**",
                              description= '`tr3xBot` is currently online ✅ \n \n If you experience problems please get in contact with {} asap'.format(tr3x.mention),
                              color=0x0CFF00)
    botonline.set_footer(text="presents by tr3xBot")
    await statusmsg.edit(embed=botonline)
    await log.send("Changed Bot-Status in {} to Online".format(statuschannel.mention))

bot.run("ODMwODQyMjYwNDYyNjMyOTky.YHMkJw.kfT7gSJUokKHamktiHR8SgvpXrg")

