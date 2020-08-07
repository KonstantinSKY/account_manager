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

table = 'persons'
fields = '''
    id INTEGER PRIMARY KEY,
    f_name TEXT NOT NULL,
    s_name TEXT,
    zip INTEGER,
    country TEXT,
    industry TEXT,
    description TEXT
    '''
conn.create_table(table, fields)

table = 'accounts'
fields = '''
    id INTEGER PRIMARY KEY, 
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    id_service INTEGER NOT NULL,
    id_person INTEGER,
    FOREIGN KEY(id_service) REFERENCES services(id)
    FOREIGN KEY(id_person) REFERENCES persons(id)
    '''
conn.create_table(table, fields)

del conn

