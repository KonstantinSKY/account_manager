# Accounts
from init_app import *


class Account:
    accounts = {}
    table = 'accounts'

    def __init__(self, account_obj, id_=None):
        self.id_ = id_
        self.login = account_obj["login"]
        self.password = account_obj["password"]
        self.id_service = account_obj["id_service"]
        self.id_person = account_obj["id_person"]
        if not self.id_:
            self.id_ = conn.insert(Account.table, account_obj)
        if self.id_:
            conn.commit()
            Account.accounts.update({self.id_: self})

    @classmethod
    def add(cls):
        dialog = Dialog.dialogs['add_account']
        questions = dialog.questions
        dialog.start()
        cls({
            "login": questions[1]['result'],
            "password": questions[2]['result'],
            "id_service": questions[3]['result'],
            "id_person": questions[4]['result']
        })

    @classmethod
    def show_all(cls):
        for key, account in cls.accounts.items():
            print("=" * 100)
            print(account.id_, account.login, account.password, account.description)

    @classmethod
    def get_all_from_db(cls):
        records = conn.select_all(cls.table)
        if not records:
            return
        for record in records:
            cls({
                "login": record[1],
                "password": record[2],
                "id_service": record[3],
                "id_person": record[4]
            },
                record[0]
            )

