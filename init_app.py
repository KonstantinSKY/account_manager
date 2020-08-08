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
                "action": func,
                "sub": "Second_level"
            },
            "2": {
                "name": "Show all persons",
                "action": func,
                "sub": "Third_level"
            }
        }
    }
})

diction = {
    "main": {
        "title": "Main menu",
        "items": {
            "1": {
                "name": "Show all services",
                "action": func,
                "sub": "Second_level"
            }
        }
    }
}

print(Menu.menus)
#Menu.menus["main"].start()
