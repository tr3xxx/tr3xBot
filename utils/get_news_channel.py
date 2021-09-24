import sqlite3

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