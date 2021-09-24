import sqlite3

async def check_onlycommands_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM command_only_channel ")
        result = cursor.fetchall()
        return result