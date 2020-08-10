# Web services
from init_app import *


class Service:
    services = {}
    table = 'services'

    def __init__(self, service_obj, id_=None):
        self.id_ = id_
        self.name = service_obj["name"]
        self.url = service_obj["url"]
        self.description = service_obj["description"]
        if not self.id_:
            self.id_ = conn.insert(Service.table, service_obj)
        if self.id_:
            conn.commit()
            Service.services.update({self.id_: self})

    @classmethod
    def add(cls):
        dialog = Dialog.dialogs['add_service']
        questions = dialog.questions
        dialog.start()
        cls({
            "name": questions[1]['result'],
            "url": questions[2]['result'],
            "description": questions[3]['result']
        })

    @classmethod
    def show_all(cls):
        for key, service in cls.services.items():
            print("="*100)
            print(service.id_, service.name, service.url, service.description)

    @classmethod
    def get_all_from_db(cls):
        records = conn.select_all(cls.table)
        if not records:
            return
        for record in records:
            cls({
                "name": record[1],
                "url": record[2],
                "description": record[3]
            },
                record[0]
            )

