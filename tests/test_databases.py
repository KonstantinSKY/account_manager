import unittest
from databases import ConnectDB

import sqlite3

# from init_app import *

db_file = "../../DB/accounts.sqlite"
conn = ConnectDB(db_file)


class DatabasesTestCase(unittest.TestCase):

    def test_insert(self):
        conn.insert("services", {
                        "name": "mail.ru",
                        "url": "https://www.mail.ru",
                        "description": "Email service, Russia"
                    })


unittest.main()

conn = ConnectDB(db_file)
curs = conn.cursor()
print(type(conn.cursor))
print(type(conn.cur))

conn2 = sqlite3.connect(db_file)
curs2 = conn2.cursor()
print(type(curs))
print(dir(curs2))

print(type(curs2))
print(dir(curs2))

print(type(conn))
print(dir(conn))

print(type(conn2))
print(dir(conn2))
