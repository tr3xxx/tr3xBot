import sqlite3

async def get_vc():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM voicehub_channel ")
        result = cursor.fetchall()
        return result