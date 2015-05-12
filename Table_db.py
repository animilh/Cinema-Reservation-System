from settings import SQL_FILE, DB_NAME
import sqlite3

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

with open(SQL_FILE, "r") as f:
    cursor.executescript(f.read())
    conn.commit()
