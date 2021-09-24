import os
import time

async def load(bot):
    for folder1 in os.listdir("modules"):
            if os.path.exists(os.path.join("modules", folder1)):
                for folder2 in os.listdir(f"modules/{folder1}"):
                    for folder3 in os.listdir(f"modules/{folder1}/{folder2}"):
                            if os.path.exists(os.path.join("modules",folder1,folder2,folder3,"cog.py")):
                                if folder3 == '__pycache__':
                                        pass
                                else:
                                    bot.load_extension(f"modules.{folder1}.{folder2}.{folder3}.cog")
                                    print(time.strftime('[%H:%M:%S]:', time.localtime()),folder3+': '+f'modules.{folder1}.{folder2}.{folder3}.cog'+ ': successfully loaded')