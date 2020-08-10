import sqlite3
from decorators import try_decor
from say import Say

class ConnectDB(sqlite3.Connection):
    """Extended SQLite connection wrapper with logging and decorators."""
    def __init__(self, db_file):
        super().__init__(db_file)
        self.cur = self.cursor()

    @try_decor
    def create_table(self, table, fields):
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table} ({fields})")
        Say(f"Created the table: {table}").prn_ok()
        return True

    @try_decor
    def select_all(self, table):
        self.cur.execute(f"SELECT * FROM {table}")
        records = self.cur.fetchall()
        Say(f"Got records: {len(records)}").prn_ok()
        return records

    @try_decor
    def insert(self, table, data_obj):
        fields = ", ".join(data_obj.keys())
        binds = ", ".join(["?"] * len(data_obj))
        values = list(data_obj.values())
        query = f"INSERT OR IGNORE INTO {table} ({fields}) VALUES ({binds})"
        return self.cur.execute(query, values).lastrowid
