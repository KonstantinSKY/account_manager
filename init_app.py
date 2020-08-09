# Initialization data for the app
from databases import ConnectDB
from menu import Menu

# databases
conn = ConnectDB('../DB/accounts.sqlite')


# # menu
def func():
    print("This is temporary function for action, use .update_action() for change ")


Menu({
    "main": {
        "title": "Main menu",
        "items": {
            "1": {
                "name": "Show all services",
                "action": None,
            },
            "2": {
                "name": "Show all persons",
                "action": None,
            },
            "3": {
                "name": "Show all accounts",
                "action": None,
            },
            "4": {
                "name": "Add services",
                "action": None,
            },
            "5": {
                "name": "Add person",
                "action": None,
            },
            "6": {
                "name": "Add person",
                "action": None,
            }

        }
    }
})
Menu({
    "Second_level": {
        "title": "Second_level menu",
        "items": {
            "1": {
                "name": "Show Second_level all services",
                "action": "ghjghj",
                "sub": "Second_level"
            },
            "2": {
                "name": "Show all Second_level persons",
                # "action": func,
                "sub": "Third_level"
            }
        }
    }
})

print(Menu.menus)
#Menu.menus["main"].start()
