import sqlite3


class DatabaseUserSettings:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database=database_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user_settings(
                                path TEXT,
                                name_folder TEXT,
                                appropriate_file TEXT
                                """
                            )

    def __del__(self):
        self.conn.close()

    def set_data(self, name_folder, appropriate_file):
        self.cursor.execute("INSERT INTO user_settings (path, name_folder, appropriate_file) VALUES (?, ?, ?)",
                            (name_folder, appropriate_file))
        self.conn.commit()

    def get_data(self):
        self.cursor.execute("SELECT * FROM user_settings")
        self.conn.commit()

    def clear_table(self):
        self.cursor.execute("DELETE FROM user_settings")
        self.conn.commit()
