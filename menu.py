# Multi level Menu
from say import Say


class Menu:
    menus = {}

    def __init__(self, menu_obj):
        self.name = list(menu_obj.keys())[0]
        self.title = menu_obj[self.name]['title']
        self.items = menu_obj[self.name]['items']
        print(self.title)
        print(self.items)
        Menu.menus.update({self.name: self})

    def start(self):
        print(self.title)
        print("="*100)
        for key in self.items:
            print(key, ":", self.items[key]['name'])
        print(list(self.items.keys()))
        select = None
        while select not in list(self.items.keys()):
            select = input("Select item and press enter")
            if select not in list(self.items.keys()):
                print("Wrong choice! Try again")
        print(select)
        self.items[select]['action']()

    def update_action(self, item_name, action_value):
        self.items[item_name]["action"] = action_value
        Say(f"Menu: {self.name}, item: {item_name} updated to {action_value}").prn_ok()


