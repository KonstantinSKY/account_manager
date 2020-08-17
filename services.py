from typing import Dict, Any, Optional
from databases import ConnectDB

class Service:
    """
    Business logic for web services management.
    Follows Active Record pattern with Dependency Injection support.
    """
    services: Dict[int, 'Service'] = {}
    table: str = 'services'

    def __init__(self, service_obj: Dict[str, Any], id_: Optional[int] = None, db: Optional[ConnectDB] = None):
        """
        Initialize a Service object.
        :param service_obj: Dictionary containing service data (name, url, description).
        :param id_: Optional ID if loading from DB.
        :param db: Database connection instance (required for persistence).
        """
        self.id_ = id_
        self.name: str = service_obj.get("name", "")
        self.url: str = service_obj.get("url", "")
        self.description: str = service_obj.get("description", "")
        
        # Persistence Logic
        if db and not self.id_:
            self.id_ = db.insert(Service.table, service_obj)
            if self.id_:
                db.commit()
        
        # Cache Update
        if self.id_:
            Service.services[self.id_] = self

    def __repr__(self) -> str:
        return f"<Service(id={self.id_}, name='{self.name}')>"

    @classmethod
    def show_all(cls) -> None:
        """Display all services in a clean format."""
        if not cls.services:
            print("No services found.")
            return

        print("\n" + "="*80)
        print(f"{'ID':<5} | {'Name':<20} | {'URL':<40}")
        print("-" * 80)
        for _, service in cls.services.items():
            print(f"{service.id_:<5} | {service.name:<20} | {service.url:<40}")
        print("="*80 + "\n")
