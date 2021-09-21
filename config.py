import sqlite3
import os

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
        cursor.execute(f"SELECT channel_id FROM log_channel WHERE guild_id = {guild.id}")
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

async def check_voicehub_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM voicehub_channel ")
        result = cursor.fetchall()
        return result

async def check_onlycommands_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM command_only_channel ")
        result = cursor.fetchall()
        return result

async def check_nocommands_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM no_commands_channel ")
        result = cursor.fetchall()
        return result

async def check_ticketsystem_guild_id():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT guild_id FROM ticketsystem ")
        result = cursor.fetchall()
        return result
        

async def check_ticketsystem_ticket_channel(guild):
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT ticketcreate_channel_id FROM ticketsystem WHERE guild_id = {guild.id}")
        result = cursor.fetchone()
        return int(str(result)[2:-3])

async def check_ticketsystem_ticket_msg(guild):
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT ticketcreate_msg_id FROM ticketsystem WHERE guild_id = {guild.id}")
        result = cursor.fetchone()
        return int(str(result)[2:-3])

async def check_ticketsystem_ticket_category(guild):
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT category_id FROM ticketsystem WHERE guild_id = {guild.id}")
        result = cursor.fetchone()
        return int(str(result)[2:-3])

async def check_ticketsystem_ticket_role(guild):
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT role_id FROM ticketsystem WHERE guild_id = {guild.id}")
        result = cursor.fetchone()
        return int(str(result)[2:-3])

async def check_ticketsystem_ticket_solve():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT ticket_channel_id FROM tickets")
        result = cursor.fetchall()
        return result

async def messages_reaction_roles():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT message_id FROM reaction_role")
        result = cursor.fetchall()
        return result

async def emoji_reaction_roles(msgid):
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT emoji FROM reaction_role WHERE message_id = {msgid}")
        result = cursor.fetchone()
        return result

async def reaction_roles_role(msgid):
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT role FROM reaction_role WHERE message_id = {msgid}")
        result = cursor.fetchone()
        return (str(result)[2:-2])

async def get_rank(exp):
        if exp <100:
            return int(1)
        if exp <400:
            return int(2)
        if exp <1000:
            return int(3)
        if exp <3000:
            return int(4)
        if exp <5000:
            return int(5)
        if exp <7500:
            return int(6)
        if exp <12000:
            return int(7)
        if exp <20000:
            return int(8)
        if exp <40000:
            return int(9)
        if exp <100000:
            return int(10)
        else:
            return int(11)

TOKEN = 'TOKEN'
COC_DEV_EMAIL = 'hapol38642@activesniper.com'
COC_DEV_PASS = 'U9K!!wO*&RRYUz^WyUHvIVuYw6L'
SUPPORT_CATEGORY = 875681228303532032
CREATE_TICKET_CHANNEL = 875681346666774578
TICKET_MESSAGE = 875681774527725588
BOT_PREFIX = 't'
REDDIT_CLIENT_ID = '1v8p8QXgpNnQuvs2Zl-8UA'
REDDIT_CLIENT_SECRET = '-y2Bgh7e0JVA2LD7XnVazi62xffm3Q'
REDDIT_USER_AGENT = 'tr3xBot'
STATUS_CHANNEL = 860642601098280970
STATUS_MESSAGE = 871558788388360223
BOT_USER_ID = 830842260462632992
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

