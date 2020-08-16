import sqlite3
from typing import List, Dict, Any, Optional, Tuple, Union
from decorators import try_decor
from say import Say

class ConnectDB(sqlite3.Connection):
    """
    Robust SQLite database wrapper with integrated error handling and typing.
    Provides a high-level API for standard CRUD operations.
    """
    def __init__(self, db_file: str):
        super().__init__(db_file)
        self.cur: sqlite3.Cursor = self.cursor()

    @try_decor
    def create_table(self, table: str, fields: str) -> bool:
        """Creates a table if it doesn't exist."""
        query = f"CREATE TABLE IF NOT EXISTS {table} ({fields})"
        self.cur.execute(query)
        Say(f"Database: Schema verified for table '{table}'").prn_ok()
        return True

    @try_decor
    def select_all(self, table: str) -> List[Tuple[Any, ...]]:
        """Retrieves all records from a specified table."""
        query = f"SELECT * FROM {table}"
        self.cur.execute(query)
        records = self.cur.fetchall()
        # Only log significant record counts to reduce noise
        if records:
            Say(f"Database: Retrieved {len(records)} records from '{table}'").prn_ok()
        return records

    @try_decor
    def insert(self, table: str, data_obj: Dict[str, Any]) -> Optional[int]:
        """
        Inserts a dictionary of data into the table.
        Returns the ID of the new row, or None on failure.
        """
        if not data_obj:
            Say(f"Database Warning: Attempted to insert empty data into '{table}'").prn_err()
            return None

        fields = ", ".join(data_obj.keys())
        # Safe parameter binding using '?'
        placeholders = ", ".join(["?"] * len(data_obj))
        values = list(data_obj.values())
        
        query = f"INSERT OR IGNORE INTO {table} ({fields}) VALUES ({placeholders})"
        self.cur.execute(query, values)
        
        row_id = self.cur.lastrowid
        Say(f"Database: Inserted record ID {row_id} into '{table}'").prn_ok()
        return row_id

    @try_decor
    def update(self, table: str, data: Dict[str, Any], where: str, where_args: Tuple[Any, ...]) -> bool:
        """
        Updates records in the table based on a condition.
        Usage: db.update('users', {'name': 'New'}, 'id = ?', (1,))
        """
        if not data:
            return False

        set_clause = ", ".join([f"{k} = ?" for k in data.keys()])
        values = list(data.values()) + list(where_args)
        
        query = f"UPDATE {table} SET {set_clause} WHERE {where}"
        self.cur.execute(query, values)
        
        Say(f"Database: Updated {self.cur.rowcount} records in '{table}'").prn_ok()
        return self.cur.rowcount > 0

    @try_decor
    def delete(self, table: str, where: str, where_args: Tuple[Any, ...]) -> bool:
        """
        Deletes records from the table based on a condition.
        Usage: db.delete('users', 'id = ?', (1,))
        """
        query = f"DELETE FROM {table} WHERE {where}"
        self.cur.execute(query, where_args)
        
        Say(f"Database: Deleted {self.cur.rowcount} records from '{table}'").prn_ok()
        return self.cur.rowcount > 0
