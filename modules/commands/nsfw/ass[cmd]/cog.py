import discord
import random
import praw
from discord.ext import commands
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,client_secret=REDDIT_CLIENT_SECRET,user_agent=REDDIT_USER_AGENT)


class ass(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ass(self,ctx):
        async with ctx.typing():
            
            if ctx.channel.is_nsfw():
                memes_submissions = reddit.subreddit('ass').hot()
                post_to_pick = random.randint(1, 100)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                embed = discord.Embed(title="", description="")
                embed.set_image(url=submission.url)
                await ctx.send(embed=embed)
            else:
                await ctx.send("No NSFW Content here, please use an nsfw channel")


def setup(bot: commands.Bot):
    bot.add_cog(ass(bot))