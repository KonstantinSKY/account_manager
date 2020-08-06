from databases import ConnectDB

# First program setup, create the tables in db if it not exist

conn = ConnectDB("../DB/accounts.sqlite")

table = 'services'
fields = '''
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    url TEXT UNIQUE NOT NULL,
    description TEXT
    '''
conn.create_table(table, fields)

table = 'accounts'
fields = '''
    id INTEGER PRIMARY KEY, 
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    id_service INTEGER NOT NULL,
    FOREIGN KEY(id_service) REFERENCES services(id)
    '''
conn.create_table(table, fields)

del conn

