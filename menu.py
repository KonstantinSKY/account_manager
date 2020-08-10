# Multi level Menu
from say import Say


class Menu:
    menus = {}

    def __init__(self, menu_obj):
        self.name = list(menu_obj.keys())[0]
        self.title = menu_obj[self.name]['title']
        self.items = menu_obj[self.name]['items']
        Menu.menus.update({self.name: self})

    def start(self):
        items = self.items
        while True:
            keys_list = list(items.keys())
            print('=' * 100 + f'\n{self.title}\n' + '=' * 100)
            for key in items:
                print(key, ":", items[key]['name'])
            print('='*100)
            while True:
                select = input("Select item and press enter: ")
                if select in keys_list:
                    break
                print("Wrong choice! Try again")
            # actions
            if 'action' in items[select]:
                print("Try to Run")
                items[select]['action']()
            # sub menu
            if 'sub' not in items[select]:
                continue
            sub_menu = items[select]["sub"]
            if sub_menu not in Menu.menus:
                print(f"Can't find submenu name {sub_menu} in Menu List")
                print(f" Menu List : {Menu.menus}")
            Menu.menus[sub_menu].start()

    def update_action(self, item_name, action_value):
        if item_name not in self.items:
            print(f"Item  {item_name} not exist in menu: {self.name}")
            print(f"Action  {action_value} not updated")
            return
        self.items[item_name]["action"] = action_value
        print(f"Menu: {self.name}, item: {item_name} updated to {action_value}")

    def add_item(self, item_name, item_obj):
        self.items[item_name] = item_obj
        print(f"Menu: {self.name}, added new item: {item_name}")
