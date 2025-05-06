import sqlite3
import os

def connect_to_sqlite(db_name):
    try:
        os.makedirs("sqlite_db", exist_ok=True)
        conn = sqlite3.connect("sqlite_db/" + db_name)
        return conn
    except Exception as e:
        print("Error connecting to SQLite:", e)
        return None