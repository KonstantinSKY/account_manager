# Initialization data for the app
from databases import ConnectDB
from menu import Menu
from dialogs import Dialog
# databases
conn = ConnectDB('../DB/accounts.sqlite')


Menu({
    "main": {
        "title": "Main menu",
        "items": {
            "1": {
                "name": "Show all services",
            },
            "2": {
                "name": "Show all persons",
            },
            "3": {
                "name": "Show all accounts",
            },
            "4": {
                "name": "Add WEB Service",
            },
            "5": {
                "name": "Add Person",
            },
            "6": {
                "name": "Add Account",
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

Dialog({
    'add_service': {
        'title': "Adding Web Service dialog",
        'questions': {
            1: {
                'ask': "Input Service name and press Enter",
                'condition': "Second_level"
            },
            2: {
                'ask': "Input Service URL and press Enter"
            },
            3: {
                'ask': "Input Service description and press Enter"
            }
        }
    }
})
Dialog({
    'add_person': {
        'title': "Adding Person dialog",
        'questions': {
            1: {
                'ask': "Input First Name and press Enter",
                'condition': "Second_level"
            },
            2: {
                'ask': "Input Second Name and press Enter"
            },
            3: {
                'ask': "Input ZIP Code and press Enter"
            },
            4: {
                'ask': "Input Country and press Enter"
            },
            5: {
                'ask': "Input Industry Code and press Enter"
            },
            6: {
                'ask': "Input Description and press Enter"
            }

        }
    }
})
Dialog({
    'add_account': {
        'title': "Adding Account -  dialog",
        'questions': {
            1: {
                'ask': "Input Login and press Enter",
                'condition': "Second_level"
            },
            2: {
                'ask': "Input Password and press Enter"
            },
            3: {
                'ask': "Select number of Web Service for The Account",
                'select': None
            },
            4: {
                'ask': "Select number of Person from the list for The Account",
                'select': None
            },
        }
    }
})






























