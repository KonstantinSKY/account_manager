from typing import Dict, Any, Optional
from init_app import conn

class Service:
    """Business logic for web services management."""
    services: Dict[int, 'Service'] = {}
    table: str = 'services'

    def __init__(self, service_obj: Dict[str, Any], id_: Optional[int] = None):
        self.id_ = id_
        self.name: str = service_obj["name"]
        self.url: str = service_obj["url"]
        self.description: str = service_obj["description"]
        
        if not self.id_:
            self.id_ = conn.insert(Service.table, service_obj)
        
        if self.id_:
            conn.commit()
            Service.services.update({self.id_: self})

    @classmethod
    def show_all(cls) -> None:
        """Display all services in a clean format."""
        for key, service in cls.services.items():
            print("="*80)
            print(f"[{service.id_}] {service.name} | {service.url}")
