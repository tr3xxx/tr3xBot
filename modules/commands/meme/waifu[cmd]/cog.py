import discord
import random
import praw
from discord.ext import commands
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,client_secret=REDDIT_CLIENT_SECRET,user_agent=REDDIT_USER_AGENT)


class waifu(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def waifu(self,ctx):
        async with ctx.typing():
            memes_submissions = reddit.subreddit('waifusfortr3x').hot()
            post_to_pick = random.randint(1, 52)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="", description="")
            embed.set_image(url=submission.url)

            alreadysended = False
            messages = await ctx.history(limit=200).flatten()
            for msg in messages:
                embeds = msg.embeds
                for embed in embeds:
                    if embed.image_url == submission.url:
                        alreadysended = True
                        break
                if alreadysended == False:
                    await ctx.send(embed=embed)
                    break
                else:
                    break
            #await ctx.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(waifu(bot))
