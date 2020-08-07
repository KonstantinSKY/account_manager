# Account manager  -Main app-

from services import Service
from accounts import Account
from persons import Person

Service.get_all_from_db()
print(Service.services)

Service({
    "name": "LinkedIn",
    "url": "https://www.linkedin.com",
    "description": "test_description LinkedIn"
})

print(Service.services)

Person.get_all_from_db()
print(Person.persons)

Person({
    "f_name": "LinkedIn",
    "s_name": "LinkedIn",
    "zip": 99999,
    "country": "United States",
    "industry": "Computers",
    "description": "test_description LinkedIn"
})
print(Person.persons)

Account.get_all_from_db()
print(Account.accounts)

Account({
    "login": "test_login",
    "password": "test_passwd",
    "id_service": 1
})

print(Account.accounts)
