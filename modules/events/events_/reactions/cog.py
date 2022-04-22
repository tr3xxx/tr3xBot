from os import error
from discord.ext import commands
import discord
import numpy as np
from utils.check_reactionRoles import messages_reaction_roles, emoji_reaction_roles, reaction_roles_role


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
                print('21')
                if str(payload.emoji) == (str(emoji_)[2:-3]):
                    print('23')
                    role_name = await reaction_roles_role(int(str(msg_array[i])[2:-2]))
                    print('25')
                    role = discord.utils.get(payload.member.guild.roles, name=str(role_name)[:-1])
                    print(role)
                    if role in payload.member.roles:
                        print("28")
                        pass
                    else:
                        await payload.member.add_roles(role)
                else:
                    print('29')
                    

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