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
            if 'select' in questions[key]:
                print('CHOICE', questions[key]["select"])
                questions[key]["select"]()
            questions[key]['result'] = input(questions[key]['ask'] + " : ")
            print(questions[key]['result'])

    def update_select(self, item_name, select_value):
        if item_name not in self.questions:
            print(f"Item  {item_name} not exist in menu: {self.name}")
            print(f"Select {select_value} not updated")
            return
        self.questions[item_name]["select"] = select_value
        print(f"Dialog: {self.name}, item: {item_name} updated to {select_value}")
    #
    # def add_item(self, item_name, item_obj):
    #     self.items[item_name] = item_obj
    #     print(f"Menu: {self.name}, added new item: {item_name}")
