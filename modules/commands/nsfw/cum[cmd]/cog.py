import discord
import random
import praw
from discord.ext import commands
from config import NSFW_CHANNEL, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,client_secret=REDDIT_CLIENT_SECRET,user_agent=REDDIT_USER_AGENT)


class cum(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def cum(self,ctx):
        async with ctx.typing():
            nsfw = ctx.guild.get_channel(NSFW_CHANNEL)
            if ctx.channel == nsfw:
                memes_submissions = reddit.subreddit('cum').hot()
                post_to_pick = random.randint(1, 100)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                embed = discord.Embed(title="", description="")
                embed.set_image(url=submission.url)
                await ctx.send(embed=embed)
            else:
                await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))



def setup(bot: commands.Bot):
    bot.add_cog(cum(bot))