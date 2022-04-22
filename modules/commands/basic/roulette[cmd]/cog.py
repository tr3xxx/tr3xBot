import random
from discord.ext import commands

class roulette(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def roulette(self,ctx,arg: str = None):
        if arg is None:
            await ctx.send("Use the following template to play roulette (troulette [red]/[black]/[0-36])")
        else:
            bid = arg
            result = random.randint(0,36)
            bid_param = -3
            if bid.lower() == "black":
                        bid_param = -1
            elif bid.lower() == "red":
                    bid_param = -2
            else: 
                try:
                    bid_param = int(bid)
                except:
                        bid_param = -3
            if bid_param == -3:
                await ctx.send("unexpected input")
                return
            if bid_param == -1:
                won = result%2 == 0 and not result == 0 
            elif bid_param == -2:
                won = result%2 == 1 
            else:
                won = result == bid_param
                        
            if won:
                await ctx.send("Congrats, you won.")
            else:
                await ctx.send("Im sorry, you lost")

def setup(bot: commands.Bot):
    bot.add_cog(roulette(bot))