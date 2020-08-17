from typing import Dict, Any, Optional
from databases import ConnectDB

class Person:
    """Core person profile management logic."""
    persons: Dict[int, 'Person'] = {}
    table: str = 'persons'

    def __init__(self, person_obj: Dict[str, Any], id_: Optional[int] = None, db: Optional[ConnectDB] = None):
        """
        Initialize a Person object.
        :param person_obj: Data dictionary (f_name, s_name, country).
        :param id_: Optional ID if loading from DB.
        :param db: Database connection for persistence.
        """
        self.id_ = id_
        self.f_name: str = person_obj.get("f_name", "")
        self.s_name: str = person_obj.get("s_name", "")
        self.country: str = person_obj.get("country", "N/A")
        
        # Persistence Logic
        if db and not self.id_:
            self.id_ = db.insert(Person.table, person_obj)
            if self.id_:
                db.commit()
        
        # Cache Update
        if self.id_:
            Person.persons[self.id_] = self

    def __repr__(self) -> str:
        return f"<Person(id={self.id_}, name='{self.f_name} {self.s_name}')>"

    @classmethod
    def show_all(cls) -> None:
        """Display all person profiles in a structured table."""
        if not cls.persons:
            print("No persons found.")
            return

        print("\n" + "="*60)
        print(f"{'ID':<5} | {'Full Name':<30} | {'Country':<20}")
        print("-" * 60)
        for _, person in cls.persons.items():
            full_name = f"{person.f_name} {person.s_name}"
            print(f"{person.id_:<5} | {full_name:<30} | {person.country:<20}")
        print("="*60 + "\n")
