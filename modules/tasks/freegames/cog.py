import discord
import praw
from discord.ext import commands,tasks
from config import FREE_GAMES_CHANNEL, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,client_secret=REDDIT_CLIENT_SECRET,user_agent=REDDIT_USER_AGENT)

class fg(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.fg.start()

    @tasks.loop(hours=1)
    async def fg(self):
        channel = self.bot.get_channel(FREE_GAMES_CHANNEL)
        messages = await channel.history(limit=200).flatten()
            
        memes_submissions = reddit.subreddit('freegames').new()
        post_to_pick = 1
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        embedFG = discord.Embed(title="New Free Game :gift:", description=submission.title)
        embedFG.add_field(name="Get it here:",value=submission.url,inline=True)

        alreadysended = False
        for msg in messages:
                embeds = msg.embeds
                for embed in embeds:
                    if embed.description == submission.title:
                        alreadysended = True
                        break

                if alreadysended == False:
                    await channel.send(embed=embedFG)
                    break
                else:
                    break


def setup(bot: commands.Bot):
    bot.add_cog(fg(bot))