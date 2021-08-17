from discord.ext import commands
import discord
import youtube_dl
import asyncio
queue = []
ytdl_format_options = {'format': 'bestaudio/best','outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s','restrictfilenames': True,'noplaylist': False,'nocheckcertificate': True,'ignoreerrors': False,'logtostderr': False,'quiet': True,'no_warnings': True,'default_search': 'auto','source_address': '0.0.0.0' }
ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

class music(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    class YTDLSource(discord.PCMVolumeTransformer):
            def __init__(self, source, *, data, volume=0.5):
                super().__init__(source, volume)

                self.data = data

                self.title = data.get('title')
                self.url = data.get('url')

            
            @classmethod
            async def from_url(cls, url, *, loop=None, stream=False):
                

                ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

                loop = loop or asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

                if 'entries' in data:
                        # take first item from a playlist
                        data = data['entries'][0]
                
                
                filename = data['url'] if stream else ytdl.prepare_filename(data) 
                return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

    @commands.command()
    async def play(self,ctx, *, arg: str = None):

                if arg is None:
                    embedER = discord.Embed(title="Please tell what i should play (ex. tplay lalala or tplay <yt url>)",color=0x075FB2)
                    await ctx.send(embed=embedER)
                else:
                    url = arg
                    if ctx.author.voice is None:
                        embed = discord.Embed(title="Please connect to an Voice channel first to play Music",color=0x075FB2)
                        await ctx.send(embed=embed)
                    else:
                        if ctx.voice_client == None:
                                await ctx.author.voice.channel.connect()
                        async with ctx.typing():
                                    if ctx.voice_client.is_playing() == True:
                                        global queue
                                        queue.append(url)
                                        player = await self.YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                                        embed = discord.Embed(title="Queued :musical_note:", description=f'[{player.title}]({player.url}) added to queue!',color=0x075FB2)
                                        await ctx.send(embed=embed)
                                    else:
                                        player = await self.YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                                        ctx.voice_client.play(player, after=lambda e: self.play_next(ctx))
                                        embed = discord.Embed(title="Now playing :musical_note:", description=f"[{player.title}]({player.url})",color=0x075FB2)
                                        await ctx.send(embed=embed)

    def play_next(self,ctx):
                asyncio.run_coroutine_threadsafe(self.n(ctx),self.bot.loop)

    async def n(self,ctx):  
                global queue
                if len(queue) > 0:
                    if ctx.voice_client.is_playing() == True:
                        ctx.voice_client.stop()

                    server = ctx.message.guild
                    voice_channel = server.voice_client

                    async with ctx.typing():
                        player = await self.YTDLSource.from_url(queue[0], loop=self.bot.loop, stream=True)
                        voice_channel.play(player, after=lambda e: self.play_next(ctx))

                    embed = discord.Embed(title="Now playing :musical_note:", description=f"[{player.title}]({player.url})",color=0x075FB2)
                    await ctx.send(embed=embed)
                    del(queue[0])
                

    @commands.command()
    async def skip(self,ctx):  
                global queue
                #print("skip ausgeführt")

                if ctx.author.voice is None:
                    embed = discord.Embed(title="Please connect to an Voice channel first to skip",color=0x075FB2)
                    await ctx.send(embed=embed)
                else:
                    if discord.utils.get(self.bot.voice_clients, guild=ctx.guild) != None:
                        if ctx.voice_client.is_playing():
                            if len(queue) > 0:
                                if ctx.voice_client.is_playing() == True:
                                    ctx.voice_client.stop()

                                server = ctx.message.guild
                                voice_channel = server.voice_client

                                async with ctx.typing():
                                    player = await self.YTDLSource.from_url(queue[0], loop=self.bot.loop, stream=True)
                                    voice_channel.play(player, after=lambda e: self.play_next(ctx))

                                embed = discord.Embed(title="Now playing :musical_note:", description=f"[{player.title}]({player.url})",color=0x075FB2)
                                await ctx.send(embed=embed)
                                del(queue[0])
                            else:
                                await ctx.send("No more Songs queued!")
                        else:
                            embed = discord.Embed(title="I am not playing music at the moment",color=0x075FB2)
                            await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title=" I am not connected to any Voice Chat at the moment",color=0x075FB2)
                        await ctx.send(embed=embed)


    @commands.command()
    async def pause(self,ctx):
                if ctx.author.voice is None:
                    embed = discord.Embed(title="Please connect to an Voice channel first to pause me",color=0x075FB2)
                    await ctx.send(embed=embed)
                else:
                    if discord.utils.get(self.bot.voice_clients, guild=ctx.guild) != None:
                        if ctx.voice_client.is_playing():
                            ctx.voice_client.pause()
                            embed = discord.Embed(title="Paused :pause_button:",color=0x075FB2)
                            await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed(title=" I am not playing music at the moment",color=0x075FB2)
                            await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title=" I am not connected to any Voice Chat at the moment",color=0x075FB2)
                        await ctx.send(embed=embed)
                
                
    @commands.command()
    async def resume(self,ctx):
                if ctx.author.voice is None:
                    embed = discord.Embed(title="Please connect to an Voice channel first to resume my audio",color=0x075FB2)
                    await ctx.send(embed=embed)
                else:
                    if discord.utils.get(self.bot.voice_clients, guild=ctx.guild) != None:
                        ctx.voice_client.resume()
                        embed = discord.Embed(title="Resuming :play_pause: ",color=0x075FB2)
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="I am not connected to any Voice Chat at the moment",color=0x075FB2)
                        await ctx.send(embed=embed)

    @commands.command()
    async def stop(self,ctx):
                if ctx.author.voice is None:
                    embed = discord.Embed(title="Please connect to an Voice channel first to stop me",color=0x075FB2)
                    await ctx.send(embed=embed)
                else:
                    if discord.utils.get(self.bot.voice_clients, guild=ctx.guild) != None:
                        if ctx.voice_client.is_playing():
                            try:
                                await ctx.voice_client.stop()
                                embed = discord.Embed(title="Stopped :stop_button:",color=0x075FB2)
                                await ctx.send(embed=embed)
                            except Exception as err:
                                pass
                        else:
                            embed = discord.Embed(title=" I am not playing music at the moment",color=0x075FB2)
                            await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title=" I am not connected to any Voice Chat at the moment",color=0x075FB2)
                        await ctx.send(embed=embed)

    @commands.command()
    async def leave(self,ctx):
                if ctx.author.voice is None:
                    embed = discord.Embed(title="Please connect to an Voice channel first to make me leave the Channel",color=0x075FB2)
                    await ctx.send(embed=embed)
                else:
                    if discord.utils.get(self.bot.voice_clients, guild=ctx.guild) != None:
                        await ctx.voice_client.disconnect()
                    else:
                        embed = discord.Embed(title=" I am not connected to any Voice Chat at the moment",color=0x075FB2)
                        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
        bot.add_cog(music(bot))