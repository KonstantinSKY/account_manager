# Account manager  -Main app-

from services import Service
from accounts import Account
from persons import Person
from menu import Menu

Menu.menus["main"].update_action("1", Service.show_all)
Menu.menus["main"].update_action("2", Person.show_all)
Menu.menus["main"].update_action("3", Account.show_all)

Service.get_all_from_db()
print(Service.services)

Service({
    "name": "LinkedIn",
    "url": "https://www.linkedin.com",
    "description": "test_description LinkedIn"
})

print(Menu.menus)
Person.get_all_from_db()
print(Person.persons)

Person({
    "f_name": "John",
    "s_name": "Smith",
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
# menu
print(Account.accounts)


def new_function():
    print("New test function!")


print(Menu.menus['main'].start())

Menu.menus["main"].update_action("8", new_function)

Menu.menus["main"].add_item("3", {
    "name": "Show  all accounts",
    "action": new_function,
    "sub": "fourth_level"
    })

print(Menu.menus['main'].start())
