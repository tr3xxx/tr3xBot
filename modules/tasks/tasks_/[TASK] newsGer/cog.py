import discord
import asyncpraw
import numpy as np
from discord.ext import commands,tasks
from utils.reddit_login import client_id,client_secret,user_agent
from utils.get_news_channel import check_newsger_channel
reddit = asyncpraw.Reddit(client_id=client_id(),client_secret=client_secret(),user_agent=user_agent())

class newsGer(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.newsGer.start()

    @tasks.loop(hours=1)
    async def newsGer(self):
        result = await check_newsger_channel()
        result_array = np.array(result)
        for i in range (0,len(result_array)):
            try:
                channel = self.bot.get_channel(int(str(result_array[i])[2:-2]))
                messages = await channel.history(limit=200).flatten()
            except Exception as err:
                continue
                
            subreddit = await reddit.subreddit("NachrichtenDE")
            async for submission in subreddit.new(limit=40):
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
                break
            break 



def setup(bot: commands.Bot):
    bot.add_cog(newsGer(bot))