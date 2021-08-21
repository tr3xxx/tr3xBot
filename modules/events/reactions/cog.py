from discord import guild, reaction, utils
from discord.ext import commands
import discord
from config import messages_reaction_roles, emoji_reaction_roles, reaction_roles_role
import numpy as np


class reactions(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        messages = await messages_reaction_roles()
        msg_array = np.array(messages)
        for i in range(0,len(msg_array)):
            if payload.message_id == int(str(msg_array[i])[2:-2]):
                emoji_ = await emoji_reaction_roles(int(str(msg_array[i])[2:-2]))
                if str(payload.emoji) == (str(emoji_)[2:-3]):
                    role_name = await reaction_roles_role(int(str(msg_array[i])[2:-2]))
                    role = discord.utils.get(payload.member.guild.roles, name=str(role_name)[:-1])
                    if role in payload.member.roles:
                        pass
                    else:
                        await payload.member.add_roles(role)
                    

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        messages = await messages_reaction_roles()
        msg_array = np.array(messages)
        for i in range(0,len(msg_array)):
            if payload.message_id == int(str(msg_array[i])[2:-2]):
                emoji_ = await emoji_reaction_roles(int(str(msg_array[i])[2:-2]))
                if str(payload.emoji) == (str(emoji_)[2:-3]):
                    role_name = await reaction_roles_role(int(str(msg_array[i])[2:-2]))
                    guild = self.bot.get_guild(payload.guild_id)
                    member = discord.utils.get(guild.members, id=payload.user_id)
                    role = discord.utils.get(member.guild.roles, name=str(role_name)[:-1])
                    if role in member.roles:
                        await member.remove_roles(role)
                    else:
                        pass


def setup(bot: commands.Bot):
    bot.add_cog(reactions(bot))