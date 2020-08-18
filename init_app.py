"""
Centralized application initialization.
Provides shared resources like database connections and global configurations.
"""
from databases import ConnectDB
import os

# Ensure DB directory exists
DB_PATH = 'accounts.sqlite'

# Global database connection instance
conn = ConnectDB(DB_PATH)

# Initialize schema
conn.create_table('services', 'id INTEGER PRIMARY KEY, name TEXT, url TEXT, description TEXT')
conn.create_table('persons', 'id INTEGER PRIMARY KEY, f_name TEXT, s_name TEXT, country TEXT')
conn.create_table('accounts', 'id INTEGER PRIMARY KEY, login TEXT, password TEXT, id_service INTEGER')
