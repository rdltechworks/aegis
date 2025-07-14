
import sqlite3

def create_db_and_tables():
    conn = sqlite3.connect('data/guardian.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS devices (
        mac_address TEXT PRIMARY KEY,
        device_name TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        log TEXT
    )
    """)
    conn.commit()
    conn.close()
