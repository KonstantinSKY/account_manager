class Say(str):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def prn(self):
        print(self.text)

    def prn_ok(self):
        print(f"OK: {self.text}")
