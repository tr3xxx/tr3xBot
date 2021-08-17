import discord
import coc
from discord.ext import commands

cocclient = coc.login('hapol38642@activesniper.com','U9K!!wO*&RRYUz^WyUHvIVuYw6L') # https://developer.clashofclans.com

class coc(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def coc(self,ctx, arg: str = None):
        
        if arg is None:
            await ctx.send("Please use the following template to searching a coc account (tcoc #XXXXXXXX)")
        else:
            playerInput = arg
            if playerInput.startswith("#"):
                player = await cocclient.get_player(playerInput)
                clan = await cocclient.get_clan(player.clan.tag)
                if clan.type == "open":
                        joinable = "Yes"
                else:
                        joinable = "No (",clan.type,")"

                if player.town_hall < 9:
                    url = "https://static.wikia.nocookie.net/clashofclans/images/5/52/Town_Hall6.png/revision/latest/scale-to-width-down/100?cb=20170827050220"
                if player.town_hall == 9:
                    url = "https://static.wikia.nocookie.net/clashofclans/images/e/e0/Town_Hall9.png/revision/latest/scale-to-width-down/100?cb=20170827045259"
                if player.town_hall == 10:
                    url = "https://static.wikia.nocookie.net/clashofclans/images/5/5c/Town_Hall10.png/revision/latest/scale-to-width-down/115?cb=20170827040043"
                if player.town_hall == 11:
                    url = "https://static.wikia.nocookie.net/clashofclans/images/9/96/Town_Hall11.png/revision/latest/scale-to-width-down/110?cb=20210410001514"
                if player.town_hall == 12:
                    url = "https://static.wikia.nocookie.net/clashofclans/images/c/c7/Town_Hall12-1.png/revision/latest/scale-to-width-down/120?cb=20180603203226"
                if player.town_hall == 13:
                    url = "https://static.wikia.nocookie.net/clashofclans/images/9/98/Town_Hall13-1.png/revision/latest/scale-to-width-down/120?cb=20200831024426"
                if player.town_hall == 14:
                    url = "https://static.wikia.nocookie.net/clashofclans/images/e/e0/Town_Hall14-1.png/revision/latest/scale-to-width-down/110?cb=20210413000722"
                
                
                embed=discord.Embed(title="Clash of Clans Stats", color=0x075FB2)
                embed.add_field(name="Player", value=player.name, inline=True)
                embed.add_field(name="Level", value=player.exp_level, inline=True)
                embed.add_field(name="Townhall", value=player.town_hall, inline=True)
                embed.add_field(name="Builderhall", value=player.builder_hall, inline=True)
                embed.add_field(name="Multiplayer trophies ", value=player.trophies, inline=True)
                embed.add_field(name="Builderbase trophies ", value=player.versus_trophies, inline=True)
                embed.add_field(name="Clan", value=str(player.clan)+player.clan.tag, inline=True)
                embed.add_field(name="Clan-Level", value=clan.level, inline=True)
                embed.add_field(name="Role", value=player.role, inline=True)
                embed.add_field(name="Clanmember", value=clan.member_count, inline=True)
                embed.add_field(name="Joinable", value=joinable, inline=True)
                embed.add_field(name="Language", value=clan.chat_language, inline=True)
                embed.add_field(name="Discription", value=clan.description, inline=True)
                embed.add_field(name="War-frequency", value=clan.war_frequency, inline=True)
                embed.add_field(name="Rank", value=clan.war_league, inline=True)
                embed.add_field(name="Link", value=clan.share_link, inline=True)
                embed.set_thumbnail(url=url)
                await ctx.send(embed=embed)
            else:
                await ctx.send("Sorry ",playerInput," is not a Valid Playertag, try again")

def setup(bot: commands.Bot):
    bot.add_cog(coc(bot))