import discord
import random
import praw
from discord.ext import commands
reddit = praw.Reddit(client_id='1v8p8QXgpNnQuvs2Zl-8UA',client_secret='-y2Bgh7e0JVA2LD7XnVazi62xffm3Q',user_agent='tr3xBot')


class anime(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def anime(self,ctx):
        async with ctx.typing():
                while True:
                    memes_submissions = reddit.subreddit('Animemes').hot()
                    post_to_pick = random.randint(1, 100)
                    for i in range(0, post_to_pick):
                        submission = next(x for x in memes_submissions if not x.stickied)
                    check_souce =  str(submission.url[8:])
                    if check_souce.startswith('i'):
                        await ctx.send(submission.url)
                        break
                    else:
                        pass


def setup(bot: commands.Bot):
    bot.add_cog(anime(bot))