import sqlite3

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