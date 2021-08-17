import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, arg: str = None):
        await ctx.author.create_dm()
        if ctx.channel.id == ctx.author.dm_channel.id:
            if arg is None:
                embed=discord.Embed(title="tr3xBot - Help", description= "Use the following Commands for the Specific help commands here in the direct Messages",color=0x075FB2)
                embed.add_field(name="Basic Commands",value="\n>>> *thelp basic*",inline=False)
                embed.add_field(name="Music Commands",value="\n>>> *thelp music*",inline=False)
                embed.add_field(name="VoiceChannel Commands",value="\n>>> *thelp vc*",inline=False)
                embed.add_field(name="Meme Commands",value="\n>>> *thelp meme*",inline=False)
                embed.add_field(name="NSFW Commands",value="\n>>> *thelp nsfw*",inline=False)
                await ctx.author.send(embed=embed)
            if arg == "basic":
                embed=discord.Embed(title="tr3xBot - Basic Commands", color=0x075FB2)
                embed.add_field(name="thelp",value="\n>>> *Need some Help with the Commands? thelp gotcha you*",inline=False)
                embed.add_field(name="tclear",value="\n>>> *Oh so you want to blur tracks? - Only aviable for Admins/Mods*",inline=False)
                embed.add_field(name="tembed",value="\n>>> *Normal Messages? Boriiing get some Style in it*",inline=False)
                embed.add_field(name="tsay",value="\n>>> *I dont want to say anything you want, but i have to... - sadly noises*",inline=False)
                embed.add_field(name="tkill",value="\n>>> *Yea kill this mother fuc... funtioner , yea, mother functioner - dont ask what it is*",inline=False)
                embed.add_field(name="tdie",value="\n>>> *No no noooo*",inline=False)
                embed.add_field(name="tdm",value="\n>>> *write someone a nice dm via me*",inline=False)
                embed.add_field(name="tpfp",value="\n>>> *Why would you like to have someones pfp ? I doont know but go on*",inline=False)
                embed.add_field(name="troulette",value="\n>>> *Wanna gamble a little bit ?*",inline=False)
                embed.add_field(name="tcoc",value="\n>>> *Wanna flex with your clash of clans village? here we go*",inline=False)
                embed.add_field(name="thug",value="\n>>> *Oh you had a hard day? come over here*",inline=False)
                await ctx.author.send(embed=embed)
            if arg == "music":
                embed=discord.Embed(title="tr3xBot - Music Commands", color=0x075FB2)
                embed.add_field(name="tplay",value="\n>>> *rap,pop or maybe rock ? what do you want to hear today, i got it*",inline=False)
                embed.add_field(name="tstop",value="\n>>> *oh the party is over already?*",inline=False)
                embed.add_field(name="tpause",value="\n>>> *little pause, we'll be right back*",inline=False)
                embed.add_field(name="tresume",value="\n>>> *I dont want to say anything you want, but i have to... - sadly noises*",inline=False)
                embed.add_field(name="tleave",value="\n>>> *tr3xbot is out*",inline=False)
                await ctx.author.send(embed=embed)
            if arg == "vc":
                embed=discord.Embed(title="tr3xBot - VoiceChannel Commands", color=0x075FB2)
                embed.add_field(name="ttalkname",value="\n>>> *Customize the Name of your VoiceChannel*",inline=False)
                embed.add_field(name="tuserlimit",value="\n>>> *Customize the User-Limit of your VoiceChannel*",inline=False)
                embed.add_field(name="tprivate",value="\n>>> *Wanna be alone? Make your VoiceChannel Private*",inline=False)
                embed.add_field(name="tend",value="\n>>> *The end is near - use this carefully*",inline=False)
                await ctx.author.send(embed=embed)
            if arg == "meme":
                embed=discord.Embed(title="tr3xBot - Meme Commands", color=0x075FB2)
                embed.add_field(name="tmeme",value="\n>>> *Some classic memes are still the best, isnt it?*",inline=False)
                embed.add_field(name="tcats",value="\n>>> *Miau*",inline=False)
                embed.add_field(name="tgif",value="\n>>> *Oh yea gifs are also here*",inline=False)
                embed.add_field(name="twaifu",value="\n>>> *You want it - You got it*",inline=False)
                embed.add_field(name="tanime",value="\n>>> *Anime Memes - isnt anime a meme itself?*",inline=False)
                embed.add_field(name="tdankmemes",value="\n>>> *thing about it*",inline=False)
                await ctx.author.send(embed=embed)
            if arg == "nsfw":
                embed=discord.Embed(title="tr3xBot - Meme Commands", color=0x075FB2)
                embed.add_field(name="tass",value="\n>>> *Classic - always good*",inline=False)
                embed.add_field(name="tpussy",value="\n>>> *Classic and always good aswell*",inline=False)
                embed.add_field(name="tteen",value="\n>>> *are we young & hungry ?*",inline=False)
                embed.add_field(name="tmilf",value="\n>>> *Oh you like it old*",inline=False)
                embed.add_field(name="tcum",value="\n>>> *Why would you like to see this?*",inline=False)
                embed.add_field(name="tdick",value="\n>>> *she sayed 'he's not that small' have to check the competitor*",inline=False)
                embed.add_field(name="tsenddick",value="\n>>>*you friends will love it, trust me*",inline=False)
                embed.add_field(name="tlesbian",value="\n>>> *Two are always twice as much as one - double fun*",inline=False)
                embed.add_field(name="thentai",value="\n>>> *If you like it - take it*",inline=False)
                await ctx.author.send(embed=embed)
        else:
            if arg is None:
                embed=discord.Embed(title="tr3xBot - Help", description= "Use the following Commands for the Specific help commands here in the direct Messages",color=0x075FB2)
                embed.add_field(name="Basic Commands",value="\n>>> *thelp basic*",inline=False)
                embed.add_field(name="Music Commands",value="\n>>> *thelp music*",inline=False)
                embed.add_field(name="VoiceChannel Commands",value="\n>>> *thelp vc*",inline=False)
                embed.add_field(name="Meme Commands",value="\n>>> *thelp meme*",inline=False)
                embed.add_field(name="NSFW Commands",value="\n>>> *thelp nsfw*",inline=False)
                await ctx.channel.purge(limit=1)
                await ctx.author.send(embed=embed)
            else:
                await ctx.send("Specific help commands are only available in private chats, use `thelp` first")


def setup(bot: commands.Bot):
    bot.add_cog(help(bot))