from typing import Dict, Any, Optional
from init_app import conn

class Person:
    """Core person profile management logic."""
    persons: Dict[int, 'Person'] = {}
    table: str = 'persons'

    def __init__(self, person_obj: Dict[str, Any], id_: Optional[int] = None):
        self.id_ = id_
        self.f_name: str = person_obj["f_name"]
        self.s_name: str = person_obj["s_name"]
        self.country: str = person_obj.get("country", "N/A")
        
        if not self.id_:
            self.id_ = conn.insert(Person.table, person_obj)
        
        if self.id_:
            conn.commit()
            Person.persons.update({self.id_: self})

    @classmethod
    def show_all(cls) -> None:
        """Display all person profiles."""
        for key, person in cls.persons.items():
            print(f"[{person.id_}] {person.f_name} {person.s_name} ({person.country})")
