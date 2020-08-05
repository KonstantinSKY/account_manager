import sqlite3

class ConnectDB(sqlite3.Connection):
    """Basic SQLite connection wrapper."""
    def __init__(self, db_file):
        super().__init__(db_file)
        self.cur = self.cursor()

    def create_table(self, table, fields):
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table} ({fields})")
        return True

    def select_all(self, table):
        self.cur.execute(f"SELECT * FROM {table}")
        return self.cur.fetchall()

    def insert(self, table, data_obj):
        fields = ", ".join(data_obj.keys())
        binds = ", ".join(["?"] * len(data_obj))
        values = list(data_obj.values())
        query = f"INSERT OR IGNORE INTO {table} ({fields}) VALUES ({binds})"
        return self.cur.execute(query, values).lastrowid
