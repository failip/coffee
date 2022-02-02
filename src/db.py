from pymongo import MongoClient
from user import User
import json


class Database:
    def __init__(self):
        self.client = MongoClient(
            'localhost', 27017, username="root", password="root")
        self.db = self.client.test_database
        self.users = self.db.users
        self.settings = self.db.settings

    def get_user(self, name):
        data = self.users.find_one({"name": name})
        if (data):
            return User(name=data["name"], balance=data["balance"])
        else:
            return None

    def get_all_users(self):
        pass

    def create_user(self, user):
        if not self.user_exsists(user):
            create_id = self.users.insert_one(user.__dict__).inserted_id
            return create_id
        print("User already exsists")
        return

    def delete_user(self, user):
        if self.user_exsists(user):
            self.users.delete_one({"name": user.name})
            return
        print("User does not exsist")
        return

    def update_balance(self, user):
        self.users.find_one_and_update(
            {"name": user.name}, {"$set": {"balance": user.balance}})

    def increase_balance(self, user, amount):
        user.balance += amount
        self.update_balance(user)

    def decrease_balance(self, user, amount):
        user.balance -= amount
        self.update_balance(user)

    def user_exsists(self, user):
        if list(self.users.find({"name": user.name})):
            return True
        else:
            return False

    def get_settings(self):
        return self.settings.find_one({})

    def update_settings(self, settings):
        items = {}
        for item in settings.items:
            items[item.name] = item.price
        self.settings.find_one_and_update({}, {"$set": items})

    def create_settings(self, settings):
        items = {}
        for item in settings.items:
            items[item.name] = item.price
        self.settings.insert_one(items)
