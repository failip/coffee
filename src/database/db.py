from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient(
            'localhost', 27017, username="root", password="root")
        self.db = self.client.test_database
        self.users = self.db.users

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

    def update_balance(self, user, balance):
        self.users.find_one_and_update(
            {"name": user.name}, {"$inc": {"balance": balance}})

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
