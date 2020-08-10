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
    def add(cls):
        dialog = Dialog.dialogs['add_person']
        questions = dialog.questions
        dialog.start()
        cls({
            "f_name": questions[1]['result'],
            "s_name": questions[2]['result'],
            "zip": questions[3]['result'],
            "country": questions[4]['result'],
            "industry": questions[5]['result'],
            "description": questions[5]['result'],
        })
        print("Added new Person :")

    @classmethod
    def show_all(cls):
        for key, person in cls.persons.items():
            print("=" * 100)
            print(person.id_, person.f_name, person.s_name, person.zip,
                  person.country, person.industry, person.description)

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
