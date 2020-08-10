# Multi Dialog
from say import Say


class Dialog:
    dialogs = {}

    def __init__(self, dialog_obj):
        self.name = list(dialog_obj.keys())[0]
        self.title = dialog_obj[self.name]['title']
        self.questions = dialog_obj[self.name]['questions']
        Dialog.dialogs.update({self.name: self})

    def start(self):
        questions = self.questions
        print('=' * 100 + f'\n{self.title}\n' + '=' * 100)
        for key in sorted(questions):
            print(key)
            questions[key]['result'] = input(questions[key]['ask'])
            print(questions[key]['result'])



    # def update_action(self, _name, action_value):
    #     if item_name not in self.items:
    #         print(f"Item  {item_name} not exist in menu: {self.name}")
    #         print(f"Action  {action_value} not updated")
    #         return
    #     self.items[item_name]["action"] = action_value
    #     print(f"Menu: {self.name}, item: {item_name} updated to {action_value}")
    #
    # def add_item(self, item_name, item_obj):
    #     self.items[item_name] = item_obj
    #     print(f"Menu: {self.name}, added new item: {item_name}")
