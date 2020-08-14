from typing import Dict, Any, Callable

class Menu:
    """Professional CLI Menu system."""
    menus: Dict[str, 'Menu'] = {}

    def __init__(self, name: str, items: Dict[str, str]):
        self.name = name
        self.items = items
        self.actions: Dict[str, Callable] = {}
        Menu.menus[name] = self

    def update_action(self, key: str, action: Callable) -> None:
        self.actions[key] = action

    def display(self) -> None:
        print(f"\n--- {self.name.upper()} ---")
        for key, value in self.items.items():
            print(f"{key}. {value}")
