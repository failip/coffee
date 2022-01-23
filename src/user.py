import json


class User:
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
