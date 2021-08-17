import discord
import random
import praw
from discord.ext import commands
from config import NSFW_CHANNEL, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,client_secret=REDDIT_CLIENT_SECRET,user_agent=REDDIT_USER_AGENT)

class senddick(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True) 
    async def senddick(self,ctx,*,member: discord.Member = None):
        if member is None:
            nsfw = ctx.guild.get_channel(NSFW_CHANNEL)
            if ctx.channel == nsfw:
                memes_submissions = reddit.subreddit('dicks').hot()
                post_to_pick = random.randint(1, 100)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                embed = discord.Embed(title="Oh no an Owngoal", description="")
                embed.set_image(url=submission.url)
                await ctx.author.send(embed=embed)
            else:
                await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))
        else:
            nsfw = ctx.guild.get_channel(NSFW_CHANNEL)
            if ctx.channel == nsfw:
                memes_submissions = reddit.subreddit('dicks').hot()
                post_to_pick = random.randint(1, 100)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                embed = discord.Embed(title="Looks like someone had a gift for you", description="")
                embed.set_image(url=submission.url)
                await member.send(embed=embed)
            else:
                await ctx.send("No NSFW Content here, please use {}".format(nsfw.mention))


def setup(bot: commands.Bot):
    bot.add_cog(senddick(bot))