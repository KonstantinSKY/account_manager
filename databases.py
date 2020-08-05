import sqlite3
import sys


class ConnectDB:        # The class expands the possibilities of working with the database
    count = 0

    def __init__(self, db_file):
        super().__init__()
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.password = None
        self.url_service = None
        ConnectDB.count += 1

    def create_table(self, table, fields):
        try:
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table} ({fields})")
            print("Created the table:", table)
            return True
        except Exception as e:
            print('Filed to Create table:', table)
            print(repr(e))
            print("Error:", sys.exc_info()[0])
            return
