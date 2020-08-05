from databases import Connection


class Account:
    count = 0
    conn = Connection("../DB/accounts.sqlite")

    def __init__(self):
        self.login = None
        self.password = None
        self.url_service = None
        Account.count += 1


print(type(Account.conn))
