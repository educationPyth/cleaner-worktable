import sqlite3
import json


class DatabaseUserSettings:
    def __init__(self, database_name: str):
        self.conn = sqlite3.connect(database=database_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS user_settings(
                                settings_id INTEGER PRIMARY KEY,
                                settings_name_folder TEXT,
                                settings_appropriate_file TEXT
                                )"""
                            )

    def __del__(self):
        self.conn.close()

    def set_data(self, name_folder: str, appropriate_file: list):
        serialized_data = json.dumps(appropriate_file)
        self.cursor.execute("INSERT INTO user_settings"
                            "(settings_name_folder, settings_appropriate_file) VALUES (?, ?)",
                            (name_folder, serialized_data))
        self.conn.commit()

    def get_data(self):
        self.cursor.execute("SELECT * FROM user_settings")
        rows = self.cursor.fetchall()
        return rows

    def clear_table(self):
        self.cursor.execute("DELETE FROM user_settings")
        self.conn.commit()
