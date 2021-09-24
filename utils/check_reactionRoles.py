import sqlite3 

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

async def messages_reaction_roles():
        db = sqlite3.connect("db.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT message_id FROM reaction_role")
        result = cursor.fetchall()
        return result