from discord.ext import commands
import discord
from config import check_log_channel

class role_Managment(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def createrole(self,ctx,rolename: str = None ): 
            log = self.bot.get_channel(await check_log_channel(ctx))
            if ctx.message.author.guild_permissions.manage_roles:
                if rolename == None:
                    await ctx.send('To create a Role use tcreaterole <rolename>')
                else:
                        role = await ctx.guild.create_role(name=rolename)   
                        await log.send(f"{role.mention}({str(rolename)}) got created by {ctx.author}") 
            else:
                await ctx.author.send('You dont have the permission to create Roles on this Server!')
    
    @commands.command() 
    async def removerole(self,ctx,rolename: str = None ): 
            if ctx.message.author.guild_permissions.administrator:
                    if rolename == None:
                        await ctx.send('Wrong Input, to delete a role type tremoverole <rolename>')
                    else:
                        await ctx.send(f'Are you sure that you want to permanently delete {rolename} ? Type tremoveroleconfirm <@role> <servername>')   
            else:
                await ctx.author.send('You dont have the permission to create Roles on this Server!')
    
    @commands.command()
    async def removeroleconfirm(self,ctx,role: discord.Role = None, servername: str = None):
        log = self.bot.get_channel(await check_log_channel(ctx))
        if ctx.message.author.guild_permissions.administrator:
            if role == None:
                    await ctx.send('Wrong Input, to delete a role type tremoveroleconfirm <@role> <servername>')
            else:
                    if str(servername) == str(ctx.guild.name):
                        rolename = str(role)
                        await log.send(f"{rolename} got delted by {ctx.author}")
                        await ctx.send(f'{rolename} got deleted')
                        await role.delete()
                        
                    else:
                        await ctx.send('Wrong Input, to delete a role type tremoveroleconfirm <@role> <servername>')
        else: 
            await ctx.author.send('You dont have the permission to create Roles on this Server!')
        

def setup(bot: commands.Bot):
    bot.add_cog(role_Managment(bot))