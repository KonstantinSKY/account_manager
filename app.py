from services import Service
from accounts import Account
from persons import Person
from menu import Menu
import sys

def main() -> None:
    """Main application entry point."""
    print("Account Manager v1.0 Initializing...")
    
    # Setup Main Menu
    main_menu = Menu("main", {
        "1": "Show Services",
        "2": "Show Persons",
        "3": "Show Accounts",
        "q": "Exit"
    })
    
    # Map Actions
    main_menu.update_action("1", Service.show_all)
    main_menu.update_action("2", Person.show_all)
    main_menu.update_action("3", Account.show_all)
    
    print("Application Ready.")
    # In a real app, we would run a loop here.

if __name__ == "__main__":
    main()
