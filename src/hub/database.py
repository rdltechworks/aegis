import sqlite3
import threading
from typing import List, Optional

# Thread-local storage for database connections
local = threading.local()

def get_db_connection():
    """Establishes a thread-safe SQLite connection."""
    if not hasattr(local, "connection"):
        local.connection = sqlite3.connect("data/guardian.db", check_same_thread=False)
        local.connection.row_factory = sqlite3.Row
    return local.connection

def close_db_connection(exception):
    """Closes the thread-local database connection."""
    if hasattr(local, "connection"):
        local.connection.close()
        delattr(local, "connection")

def init_db():
    """Initializes the database schema."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create devices table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            status TEXT DEFAULT 'online'
        )
    """)

    # Create network_logs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS network_logs (
            timestamp TEXT NOT NULL,
            source_ip TEXT NOT NULL,
            destination_ip TEXT NOT NULL,
            protocol TEXT NOT NULL,
            port INTEGER NOT NULL
        )
    """)

    # Create system_events table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS system_events (
            timestamp TEXT NOT NULL,
            service TEXT NOT NULL,
            event_type TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    conn.commit()

# Example functions to interact with the database

def get_all_devices() -> List[dict]:
    """Retrieves all devices from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devices")
    return [dict(row) for row in cursor.fetchall()]

def get_network_logs(limit: int = 100) -> List[dict]:
    """Retrieves the latest network logs."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM network_logs ORDER BY timestamp DESC LIMIT ?", (limit,))
    return [dict(row) for row in cursor.fetchall()]
