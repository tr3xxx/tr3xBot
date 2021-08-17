import discord
import random
import praw
from discord.ext import commands
reddit = praw.Reddit(client_id='1v8p8QXgpNnQuvs2Zl-8UA',client_secret='-y2Bgh7e0JVA2LD7XnVazi62xffm3Q',user_agent='tr3xBot')


class gifs(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['gifs'])
    async def gif(self,ctx):
        async with ctx.typing():
            memes_submissions = reddit.subreddit('gifs').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(gifs(bot))