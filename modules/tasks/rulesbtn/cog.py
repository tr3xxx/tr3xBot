import discord
from discord.ext import commands,tasks
from dislash import ActionRow, Button, ButtonStyle
from config import BOT_LOG, OWNER_ID,RULES_CHANNEL, RULES_MESSAGE


class rulesbtn(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.rules.start()

    @tasks.loop(hours=1)
    async def rules(self): 
        log = self.bot.get_channel(BOT_LOG)
        channel = self.bot.get_channel(RULES_CHANNEL)
        Rulemessage = await channel.fetch_message(RULES_MESSAGE)
        tr3x = self.bot.get_user(OWNER_ID)
        embed = discord.Embed(title="",description= "",color=0x075FB2)                        
        embed.add_field(name="To get access to the complete server and to use all functions accept the rules but take in mind:\n\n**If you accept you agree with all rules below as well as the general Discord TOS ( https://discord.com/terms )**\n\n",value="\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",inline=False)
        embed.add_field(name=" Languages",value="\n>>> *English and German are the only allowed languages on this server*",inline=False)
        embed.add_field(name=" Rasism/Discrimination",value="\n>>> *Rasism and any sort of Discrimination is of course not allowed and will be punished with a permanent ban*",inline=False)
        embed.add_field(name=" Advertising",value="\n>>> *To promote something on this server it has to be agreed by* {}".format(tr3x.mention),inline=False)
        embed.add_field(name=" Trolling",value="\n>>> *If you annoy or troll someone all the time you can expect a timeout/ban*",inline=False)
        embed.add_field(name=" Bot sabutage",value="\n>>> *If you execute the tr3xBot's commands unnecessarily often or with the intention of provoking an error youll get banned asap (meme/nsfw commands can of course be used as often as you want, this rule means for example spamming play and stop commands unnecessarily)*",inline=True)
        embed.add_field(name=" Be friendly and respectful",value="\n>>> *Treat everyone, not only on this server, in a friendly and respectful way and accept everyone, even if you may have a different view of certain things than this person, as he/she/... is*",inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/695384979495977011/788086281846390804/Rules.png")
        

        button = ActionRow(
            Button(
                style=ButtonStyle.green,
                label="Accept",
                custom_id="green"
            ),
        )
        msg = await Rulemessage.edit(embed=embed,
            components=[button]
        )
        await log.send("Rule-Button Listener active")
        while True:
            inter = await Rulemessage.wait_for_button_click()
            if discord.utils.get(inter.author.roles, name="Member") is None:
                Role = discord.utils.get(Rulemessage.guild.roles, name="Member")
                await inter.author.add_roles(Role,reason=None)
                await inter.reply("{} accepted the Rules".format(inter.author.mention), delete_after= 5.0)   
                await log.send("{} accepted the Rules".format(inter.author))
            else:
                await inter.author.send("You already accepted the Rules.")
                await log.send("{} failed to accept the Rules - Already accepted".format(inter.author))


def setup(bot: commands.Bot):
    bot.add_cog(rulesbtn(bot))