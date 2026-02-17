import sqlite3
from pathlib import Path

DB_PATH = Path("users.db")

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        full_name TEXT NOT NULL,
        phone TEXT,
        password TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """
)
conn.commit()
