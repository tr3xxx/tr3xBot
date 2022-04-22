import asyncpraw
from discord.ext import commands
from utils.reddit_login import client_id,client_secret,user_agent
reddit = asyncpraw.Reddit(client_id=client_id(),client_secret=client_secret(),user_agent=user_agent())
class dankmemes(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def dankmemes(self,ctx):
       async with ctx.typing():
            while True:
                    subreddit = await reddit.subreddit("dankmemes")
                    async for submission in subreddit.new(limit=40):
                        check_souce =  str(submission.url[8:])
                        alreadysended = False
                        messages = await ctx.channel.history(limit=40).flatten()
                        for msg in messages:
                            if msg.content == submission.url:
                                alreadysended = True
                                break

                        if alreadysended == False:
                            if check_souce.startswith('i'):
                                await ctx.send(submission.url)
                                break
                        continue   
                    break 
              
        


def setup(bot: commands.Bot):
    bot.add_cog(dankmemes(bot))