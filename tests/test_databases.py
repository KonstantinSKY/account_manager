import unittest
from databases import ConnectDB

class TestDatabases(unittest.TestCase):
    def test_connection_init(self):
        # We use memory for tests
        conn = ConnectDB(":memory:")
        self.assertIsNotNone(conn)
        conn.close()

if __name__ == "__main__":
    unittest.main()
