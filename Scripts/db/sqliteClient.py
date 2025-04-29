import sqlite3

def connect_to_sqlite(db_name):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Exception as e:
        print("Error connecting to SQLite:", e)
        return None