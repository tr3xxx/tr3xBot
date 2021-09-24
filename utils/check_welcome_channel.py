import sqlite3

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