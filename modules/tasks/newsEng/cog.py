import discord
import praw
from discord.ext import commands,tasks
reddit = praw.Reddit(client_id='1v8p8QXgpNnQuvs2Zl-8UA',client_secret='-y2Bgh7e0JVA2LD7XnVazi62xffm3Q',user_agent='tr3xBot')

class newsEng(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.newsENG.start()

    @tasks.loop(hours=1)
    async def newsENG(self):
        channel = self.bot.get_channel(874616666921795594)
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


def setup(bot: commands.Bot):
    bot.add_cog(newsEng(bot))