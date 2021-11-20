from discord.ext import commands
import discord
import sqlite3

class reaction_role(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def test(self,ctx,emoji: discord.Emoji = None): 
        await ctx.send(emoji)
    
    @commands.command() 
    async def reactionrole(self,ctx,msgid: int = None,emoji: str = None , role: discord.Role = None ): 

    
        if msgid is None:
            await ctx.send('Use the following template to create reactionroles (ex. treactionrole <#messageid> <emoji> <@role>)')
        elif emoji is None:
            await ctx.send('Use the following template to create reactionroles (ex. treactionrole <#messageid> <emoji> <@role>)')
        elif role is None:
            await ctx.send('Use the following template to create reactionroles (ex. treactionrole <#messageid> <emoji> <@role>)')
        else:
            if ctx.message.author.guild_permissions.manage_roles:
                        db = sqlite3.connect("db.sqlite")
                        cursor = db.cursor() 
                        sql = ("INSERT INTO reaction_role(message_id,emoji,role) VALUES(?,?,?)")
                        #print(emoji.url)
                        val = (msgid,emoji,str(role))
                        msg = await ctx.channel.fetch_message(int(msgid))
                        await msg.add_reaction(emoji)
                        cursor.execute(sql,val)
                        db.commit()
                        cursor.close()
                        db.close()
            else:
                await ctx.author.send('You dont have the permission to use reactionroles on this Server!')
        
        

def setup(bot: commands.Bot):
    bot.add_cog(reaction_role(bot))