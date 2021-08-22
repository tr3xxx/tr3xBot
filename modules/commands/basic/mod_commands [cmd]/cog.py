from discord.ext import commands
import discord
from config import check_log_channel

class moderation_commands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command() 
    async def ban(self,ctx,user: discord.Member = None): 
       
            if ctx.message.author.guild_permissions.manage_roles:
                if user == None:
                    await ctx.author.send('To ban a user type tban @user ')
                else:
                    try:
                        log = self.bot.get_channel(await check_log_channel(ctx))
                        await ctx.send(f'{user} got permanently banned by {ctx.author}')
                        await log.send(f'{user} got permanently banned by {ctx.author}')
                        await user.send(f'You got permantly bannend from {str(ctx.guild.name)} by {str(ctx.author)}')
                        await user.ban()
                    except Exception as err:
                        pass
                    
            else:
                await ctx.author.send('You dont have the permission to ban users on this Server!')
    
    @commands.command() 
    async def kick(self,ctx,user: discord.Member = None): 
       
            if ctx.message.author.guild_permissions.manage_roles:
                if user == None:
                    await ctx.author.send('To kick a user type tkick @user ')
                else:
                    try:
                        log = self.bot.get_channel(await check_log_channel(ctx))
                        await ctx.send(f'{user} got kicked by {ctx.author}')
                        await log.send(f'{user} got kicked by {ctx.author}')
                        await user.send(f'You got kicked from {str(ctx.guild.name)} by {str(ctx.author)}')
                        await user.kick()
                    except Exception as err:
                        pass
                    
            else:
                await ctx.author.send('You dont have the permission to kick users on this Server!')
    
    @commands.command() 
    async def mute(self,ctx,user: discord.Member = None): 
       
            if ctx.message.author.guild_permissions.manage_roles:
                if user == None:
                    await ctx.author.send('To mute a user type tmute @user ')
                else:
                    try:
                        log = self.bot.get_channel(await check_log_channel(ctx))
                        await ctx.send(f'{user} got muted by {ctx.author}')
                        await log.send(f'{user} got muted by {ctx.author}')
                        await user.send(f'You got mute on {str(ctx.guild.name)} by {str(ctx.author)}')
                        await user.edit(mute = True)
                    except Exception as err:
                        pass
                    
            else:
                await ctx.author.send('You dont have the permission to mute users on this Server!')
    
    @commands.command() 
    async def unmute(self,ctx,user: discord.Member = None): 
       
            if ctx.message.author.guild_permissions.manage_roles:
                if user == None:
                    await ctx.author.send('To unmute a user type tunmute @user ')
                else:
                    try:
                        log = self.bot.get_channel(await check_log_channel(ctx))
                        await log.send(f'{user} got unmuted by {ctx.author}')
                        await user.edit(mute = False)
                    except Exception as err:
                        pass
                    
            else:
                await ctx.author.send('You dont have the permission to unmute users on this Server!')
    
        

def setup(bot: commands.Bot):
    bot.add_cog(moderation_commands(bot))