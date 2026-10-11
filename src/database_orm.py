import sqlite3
import os

class SQLiteManager:
    def __init__(self, db_path="data/users.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS audit_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    event_type TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def log_event(self, username, event_type):
        with self.conn:
            self.conn.execute(
                "INSERT INTO audit_logs (username, event_type) VALUES (?, ?)",
                (username, event_type)
            )
