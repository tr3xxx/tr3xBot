import time,discord,os
from discord.ext import commands
from dislash import InteractionClient
from config import BOT_PREFIX, TOKEN

#py -3 -m pip install -U "package

print(time.strftime('[%H:%M:%S]:', time.localtime()),"Bot is starting...")

bot = commands.Bot(command_prefix=BOT_PREFIX,help_command=None, intents=discord.Intents().all())
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
for folder in os.listdir("modules/commands/setup"):
            if os.path.exists(os.path.join("modules/commands/setup", folder, "cog.py")):
                print(time.strftime('[%H:%M:%S]:', time.localtime()),folder,"loaded")
                bot.load_extension(f"modules.commands.setup.{folder}.cog")

 

@bot.event
async def on_ready():
    for folder in os.listdir("modules/tasks"):
        if os.path.exists(os.path.join("modules/tasks", folder, "cog.py")):
            print(time.strftime('[%H:%M:%S]:', time.localtime()),folder,"loaded")
            bot.load_extension(f"modules.tasks.{folder}.cog")

    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Online as {0.user}".format(bot))
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"Successfully started")
    print(time.strftime('[%H:%M:%S]:', time.localtime()),"«tdc» for shutdown")
    

bot.run(TOKEN)

