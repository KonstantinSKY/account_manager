import sqlite3
from typing import List, Dict, Any, Optional
from decorators import try_decor
from say import Say

class ConnectDB(sqlite3.Connection):
    """Senior-level SQLite connection wrapper with full type hints."""
    def __init__(self, db_file: str):
        super().__init__(db_file)
        self.cur = self.cursor()

    @try_decor
    def create_table(self, table: str, fields: str) -> bool:
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table} ({fields})")
        Say(f"Created the table: {table}").prn_ok()
        return True

    @try_decor
    def select_all(self, table: str) -> List[tuple]:
        self.cur.execute(f"SELECT * FROM {table}")
        records = self.cur.fetchall()
        Say(f"Got records: {len(records)}").prn_ok()
        return records

    @try_decor
    def insert(self, table: str, data_obj: Dict[str, Any]) -> Optional[int]:
        fields = ", ".join(data_obj.keys())
        binds = ", ".join(["?"] * len(data_obj))
        values = list(data_obj.values())
        query = f"INSERT OR IGNORE INTO {table} ({fields}) VALUES ({binds})"
        result = self.cur.execute(query, values).lastrowid
        return result
