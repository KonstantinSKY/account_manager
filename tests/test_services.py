import unittest
from unittest.mock import MagicMock
from services import Service
from databases import ConnectDB

class ServicesTestCase(unittest.TestCase):
    """Unit tests for the Service domain model with mocked database."""

    def setUp(self):
        # Reset the static cache before each test
        Service.services = {}
        # Create a mock database connection
        self.mock_db = MagicMock(spec=ConnectDB)
        self.mock_db.insert.return_value = 42  # Simulated new record ID

    def test_service_creation_and_persistence(self):
        """Test that Service correctly interacts with DB on creation."""
        data = {
            "name": "GitHub",
            "url": "https://github.com",
            "description": "Dev Platform"
        }
        
        # Act
        service = Service(data, db=self.mock_db)
        
        # Assert: Persistence call
        self.mock_db.insert.assert_called_once_with(Service.table, data)
        self.mock_db.commit.assert_called_once()
        
        # Assert: State
        self.assertEqual(service.id_, 42)
        self.assertEqual(service.name, "GitHub")
        
        # Assert: Cache update
        self.assertIn(42, Service.services)
        self.assertEqual(Service.services[42], service)

    def test_service_loading_without_db(self):
        """Test creating a Service object from existing ID (no DB calls)."""
        data = {"name": "Local"}
        service = Service(data, id_=10)
        
        self.assertEqual(service.id_, 10)
        self.mock_db.insert.assert_not_called()

if __name__ == '__main__':
    unittest.main()
