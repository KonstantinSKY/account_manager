# Persons
from init_app import *


class Person:
    persons = {}
    table = 'persons'

    def __init__(self, person_obj, id_=None):
        self.id_ = id_
        self.f_name = person_obj["f_name"]
        self.s_name = person_obj["s_name"]
        self.zip = person_obj["zip"]
        self.country = person_obj["country"]
        self.industry = person_obj["industry"]
        self.description = person_obj["description"]
        if not self.id_:
            self.id_ = conn.insert(Person.table, person_obj)
        if self.id_:
            conn.commit()
            Person.persons.update({self.id_: self})

    @classmethod
    def get_all_from_db(cls):
        records = conn.select_all(cls.table)
        if not records:
            return
        for record in records:
            cls({
                "f_name": record[1],
                "s_name": record[2],
                "zip": record[3],
                "country": record[4],
                "industry": record[5],
                "description": record[6]
            },
                record[0]
            )
