import sqlite3
from decorators import try_decor
from say import Say


class ConnectDB:        # The class expands the possibilities of working with the database
    count = 0

    def __init__(self, db_file):
        super().__init__()
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.password = None
        self.url_service = None
        ConnectDB.count += 1

    @try_decor
    def create_table(self, table, fields):
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table} ({fields})")
        Say(f"Created the table: {table}").prn_ok()
        return True
