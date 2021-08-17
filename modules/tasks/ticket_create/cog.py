import discord
import random
from discord.ext import commands,tasks
from dislash import InteractionClient, ActionRow, Button, ButtonStyle


class create_ticket(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.createticket.start()

    @tasks.loop(hours=1)
    async def createticket(self): 
        log = self.bot.get_channel(875700881360846899)
        guild = self.bot.get_guild(718926812033581108)
        ticketchannel = self.bot.get_channel(875681346666774578)
        ticketmessage = await ticketchannel.fetch_message(875681774527725588)

        embed = discord.Embed(title="Ticket-Support",description="If you need Help, have an Server certain Question or wanna give Feedback, create an Ticket and an Mod will take care of your business",color=0x075FB2)  
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/premium/png-512-thumb/contact-support-2452176-2029802.png") 

        
        button = ActionRow(
            Button(
                style=ButtonStyle.green,
                label="Create Ticket",
                custom_id="green"
            ),
        )
        msg = await ticketmessage.edit(embed=embed,
            components=[button]
        )
        await log.send("Ticket-Button Listener active")
        while True:
            inter = await ticketmessage.wait_for_button_click()
            category =  self.bot.get_channel(875681228303532032)
            Modrole = discord.utils.get(guild.roles, name="Mods")
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                inter.author: discord.PermissionOverwrite(read_messages=True),
                Modrole: discord.PermissionOverwrite(read_messages=True)
            }
            ticket = await guild.create_text_channel(category=category,name="ticket "+str(random.randint(2000,9999)), overwrites=overwrites)
            await inter.reply("{} your ticket {} has been created!".format(inter.author.mention,ticket.mention), delete_after= 5.0)

            embedTT = discord.Embed(title="Ticket-Support",description="Please describe your problem in detail and precisely, if necessary, indicate reproduction steps \nA moderator will deal with your problem soon\n\nIf your Problem has been solved or you accidentally created an ticket write `tsolved` to delete your ticket",color=0x075FB2)
            await ticket.send(embed=embedTT)
            await log.send("Ticket {} created by {}".format(ticket.mention,inter.author))

       

def setup(bot: commands.Bot):
    bot.add_cog(create_ticket(bot))