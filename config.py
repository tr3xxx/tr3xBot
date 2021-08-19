import os
import discord
import sqlite3

WELCOME_CHANNEL = None
BOT_LOG = 875700881360846899
FREE_GAMES_CHANNEL = 871595543468601404
NEWS_GER_CHANNEL = 872948474264555530
NEWS_ENG_CHANNEL = 874616666921795594

async def check_welcome_channel(member):
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM welcome_channel WHERE guild_id = {member.guild.id}")
        result = cursor.fetchone()
        if result is None:
            return
        else:
            WELCOME_CHANNEL = int(result[0])
            return WELCOME_CHANNEL

async def check_log_channel(ctx):
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM log_channel WHERE guild_id = {ctx.guild.id}")
        result = cursor.fetchone()
        if result is None:
            return
        else:
            BOT_LOG = int(result[0])
            return BOT_LOG

async def check_log_channel_guildonly(guild):
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM log_channel WHERE guild_id = {guild}")
        result = cursor.fetchone()
        if result is None:
            return
        else:
            BOT_LOG = int(result[0])
            return BOT_LOG

async def check_fg_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM fg_channel ")
        result = cursor.fetchall()
        if result is None:
            return
        else:
            return result

async def check_newsger_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM newsger_channel ")
        result = cursor.fetchall()
        if result is None:
            return
        else:
            return result

async def check_newseng_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM newseng_channel ")
        result = cursor.fetchall()
        if result is None:
            return
        else:
            return result

async def check_member_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT member_channel_id FROM stats ")
        result = cursor.fetchall()
        return result

async def check_online_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT online_channel_id FROM stats ")
        result = cursor.fetchall()
        return result

async def check_boost_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT boost_channel_id FROM stats ")
        result = cursor.fetchall()
        return result

async def stats_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT guild_id FROM stats ")
        result = cursor.fetchall()
        return result

TOKEN = os.environ['TOKEN']
OWNER_ID = 633412273641095188
COC_DEV_EMAIL = 'hapol38642@activesniper.com'
COC_DEV_PASS = 'U9K!!wO*&RRYUz^WyUHvIVuYw6L'
TALK_CATEGORY = 858020017822892092
GUILD_ID = 718926812033581108
SUPPORT_CATEGORY = 875681228303532032
CREATE_TICKET_CHANNEL = 875681346666774578
TICKET_MESSAGE = 875681774527725588
NSFW_CHANNEL = 800715988794081281
BOT_PREFIX = 't'
REDDIT_CLIENT_ID = '1v8p8QXgpNnQuvs2Zl-8UA'
REDDIT_CLIENT_SECRET = '-y2Bgh7e0JVA2LD7XnVazi62xffm3Q'
REDDIT_USER_AGENT = 'tr3xBot'
STATUS_CHANNEL = 860642601098280970
BOT_USER_ID = 830842260462632992
VOICEHUB_CHANNEL = 873323443163115560
AFK_CHANNEL = 859718892334350356
MEMBER_CHANNEL = 858711678316052500
ONLINE_CHANNEL = 861365241413107732
STATUS_MESSAGE = 871558788388360223
BOOST_CHANNEL = 861753968890871839
ONLINE_CHANNEL = 861365241413107732
MEMBER_CHANNEL = 858711678316052500
RULES_CHANNEL = 803240539578302524

RULES_MESSAGE = 860636421047320627
BOT_COMMANDS_CHANNEL = 803764491988107334
YTDL_FORMAT_OPTIONS = {'format': 'bestaudio/best', 
                        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
                        'restrictfilenames': True,
                        'noplaylist': False,
                        'nocheckcertificate': True,
                        'ignoreerrors': False,
                        'logtostderr': False,
                        'quiet': True,
                        'no_warnings': True,
                        'default_search': 'auto',
                        'source_address': '0.0.0.0' }
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                  'options': '-vn'}

