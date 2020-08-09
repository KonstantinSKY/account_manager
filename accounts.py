class Account:
    accounts = {}
    table = 'accounts'
    def __init__(self, account_obj, id_=None):
        self.id_ = id_
        self.login = account_obj["login"]
        self.password = account_obj["password"]
