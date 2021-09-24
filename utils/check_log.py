import sqlite3

def log(ctx):
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