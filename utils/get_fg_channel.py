import sqlite3

async def check_fg_channel():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM fg_channel ")
        result = cursor.fetchall()
        if result is None:
            return
        else:
            return result