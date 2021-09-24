import sqlite3

async def check_nocommands_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM no_commands_channel ")
        result = cursor.fetchall()
        return result