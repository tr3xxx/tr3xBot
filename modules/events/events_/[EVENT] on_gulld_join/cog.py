import discord
from discord.ext import commands


class on_guild_join(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        
        tr3xbot = self.bot.get_user(830842260462632992)
        setupch = await guild.create_text_channel(name="tr3xBot-Setup", overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False)})
        embed= discord.Embed(title='tr3xBot Setup',description='Thanks for choosing tr3xBot\n\n Please keep in mind that this Bot is developed by only one person\n Thereofore i would appreciate if you could report every bug or wishes on my Discord (https://discord.gg/rVcPPzbQ)\n\n Use `tsetup end` to end the setup after you finished it\n\n\n ',color=0x075FB2)
        embed.add_field(name="Welcome-Messages Channel",value="\n>>> *To set up an Custom Welcome Channel use the following Command: \n `tsetup welcomechannel <#textchannelid>`*",inline=False)
        embed.add_field(name="Log Channel",value="\n>>> *To set up an Custom Log Channel use the following Command: \n `tsetup log <#textchannelid>`*",inline=False)
        embed.add_field(name="Free-Games Channel",value="\n>>> *To set up an Custom Free-Games Channel use the following Command:\n  `tsetup fgchannel <#textchannelid>`*",inline=False)
        embed.add_field(name="German-News Channel",value="\n>>> *To set up an Custom German-News Channel use the following Command: \n `tsetup newschannelger <#textchannelid>`*",inline=False)
        embed.add_field(name="International-News Channel",value="\n>>> *To set up an Custom International-News Channel use the following Command: \n  `tsetup newschanneleng <#textchannelid>`*",inline=False)
        embed.add_field(name="Stats Channel",value="\n>>> *To set up 3 Server specific Channel (Member Counter,Online Counter,Boost Counter) use the following Command:\n `tsetup stats`*",inline=False)
        embed.add_field(name="Voicehub Channel",value="\n>>> *To set up an Voicehub Channel use the following Command:\n `tsetup voicehub <#voicechannelid>`*",inline=False)
        embed.add_field(name="Commands-Only Channel",value="\n>>> *To set up an Custom Commands-Only Channel use the following Command: \n `tsetup commandsonly <#textchannelid>`*",inline=False)
        embed.add_field(name="No-Commands Channel",value="\n>>> *To set up an Custom No-Commands Channel use the following Command: \n `tsetup nocommands <#textchannelid>`*",inline=False)
        embed.set_footer(text="To get an overview of all commands of the bot use `thelp` \nShould something not work as expected please open a ticket on the discord linked above, i will work the problem then.")
        await setupch.send(embed=embed) 
    

def setup(bot: commands.Bot):
    bot.add_cog(on_guild_join(bot))