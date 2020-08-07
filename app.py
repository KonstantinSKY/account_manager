# Account manager  -Main app-

from services import Service
from accounts import Account

Service.get_all_from_db()
print(Service.services)

Service({
    "name": "LinkedIn",
    "url": "https://www.linkedin.com",
    "description": "test_description LinkedIn"
})

print(Service.services)
#print(serv)

Account.get_all_from_db()
print(Account.accounts)

Account({
    "login": "test_login",
    "password": "test_passwd",
    "id_service": 1
})

print(Account.accounts)
