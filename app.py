# Account manager  -Main app-

from services import Service
from accounts import Account
from persons import Person
from dialogs import Dialog
from menu import Menu

menu = Menu.menus["main"]
menu.update_action("1", Service.show_all)
menu.update_action("2", Person.show_all)
menu.update_action("3", Account.show_all)
menu.update_action("4", Service.add)
menu.update_action("5", Person.add)
menu.update_action("6", Account.add)
dialog = Dialog.dialogs["add_account"]
dialog.update_select(3, Service.show_all)
dialog.update_select(4, Person.show_all)

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
    "password": "********",
    "id_service": 1,
    "id_person": None
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
