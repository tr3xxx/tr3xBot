import discord
import random
import praw
from discord.ext import commands
reddit = praw.Reddit(client_id='1v8p8QXgpNnQuvs2Zl-8UA',client_secret='-y2Bgh7e0JVA2LD7XnVazi62xffm3Q',user_agent='tr3xBot')


class senddick(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True) 
    async def senddick(self,ctx,*,member: discord.Member = None):
        if member is None:
            nsfw = ctx.guild.get_channel(800715988794081281)
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
            nsfw = ctx.guild.get_channel(800715988794081281)
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