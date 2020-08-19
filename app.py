import sys
from init_app import conn
from services import Service
from accounts import Account
from persons import Person
from menu import Menu

def load_data() -> None:
    """Load existing records from database into memory."""
    # Load Services
    for row in conn.select_all(Service.table):
        # row: (id, name, url, description)
        Service({"name": row[1], "url": row[2], "description": row[3]}, id_=row[0])
    
    # Load Persons
    for row in conn.select_all(Person.table):
        # row: (id, f_name, s_name, country)
        Person({"f_name": row[1], "s_name": row[2], "country": row[3]}, id_=row[0])

    # Load Accounts
    for row in conn.select_all(Account.table):
        # row: (id, login, password, id_service)
        Account({"login": row[1], "password": row[2], "id_service": row[3]}, id_=row[0])

def main() -> None:
    """Main application entry point and command loop."""
    print("\n" + "*" * 40)
    print("      ACCOUNT MANAGER v1.1 PRO      ")
    print("*" * 40)
    
    # Initialization
    load_data()
    
    # Menu Configuration
    main_menu = Menu("main", {
        "1": "List All Services",
        "2": "List All Persons",
        "3": "List All Accounts",
        "q": "Exit Application"
    })
    
    # Action Mapping
    actions = {
        "1": Service.show_all,
        "2": Person.show_all,
        "3": Account.show_all,
        "q": lambda: sys.exit("Exiting gracefully...")
    }
    
    # Application Loop
    while True:
        main_menu.display()
        choice = input("\nSelect an option: ").strip().lower()
        
        if choice in actions:
            actions[choice]()
        else:
            print(f"Invalid option: '{choice}'. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Goodbye.")
        sys.exit(0)
