import unittest
from services import Service
from databases import ConnectDB
from init_app import *

# db_file = "../../DB/accounts.sqlite"
# conn = ConnectDB(db_file)


class ServicesTestCase(unittest.TestCase):

    def test_create_service(self):
        ser = Service({
                "name": "test_name",
                "url": "test_url",
                "description": "test_description"
        })
        print(ser)



if __name__ == '__main__':
    unittest.main()
