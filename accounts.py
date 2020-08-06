from databases import ConnectDB


class Account:
    count = 0
    conn = ConnectDB("../DB/accounts.sqlite")

    def __init__(self):
        self.login = None
        self.password = None
        self.url_service = None
        Account.count += 1


print(type(Account.conn))
