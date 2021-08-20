import discord
import praw
import numpy as np
from discord.ext import commands,tasks
from config import  REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, check_newseng_channel
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,client_secret=REDDIT_CLIENT_SECRET,user_agent=REDDIT_USER_AGENT)

class newsEng(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.newsENG.start()

    @tasks.loop(hours=1)
    async def newsENG(self):
        result = await check_newseng_channel()
        result_array = np.array(result)
        for i in range (0,len(result_array)):
            try:
                channel = self.bot.get_channel(int(str(result_array[i])[2:-2]))
                messages = await channel.history(limit=200).flatten()
            except Exception as err:
                continue
                
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


def setup(bot: commands.Bot):
    bot.add_cog(newsEng(bot))