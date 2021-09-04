import discord
import random
import praw
from discord.ext import commands
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,client_secret=REDDIT_CLIENT_SECRET,user_agent=REDDIT_USER_AGENT)

class hentai(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hentai(self,ctx):
        async with ctx.typing():
            if ctx.channel.is_nsfw():
                while True:
                    memes_submissions = reddit.subreddit('hentai').hot()
                    post_to_pick = random.randint(1, 100)
                    for i in range(0, post_to_pick):
                        submission = next(x for x in memes_submissions if not x.stickied)
                    check_souce =  str(submission.url[8:])
                    if check_souce.startswith('i'):
                        await ctx.send(submission.url)
                        break
                    else:
                        pass
            else:
                await ctx.send("No NSFW Content here, please use an nsfw channel")


def setup(bot: commands.Bot):
    bot.add_cog(hentai(bot))