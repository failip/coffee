from pymongo import MongoClient
import datetime
client = MongoClient('localhost', 27017, username="root", password="root")

db = client.test_database
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts  # get posts

post_id = posts.insert_one(post).inserted_id
# collection = db.test_collection


class Database:
    def __init__(self):
        self.client = MongoClient(
            'localhost', 27017, username="root", password="root")
        self.db = client.test_database
        self.users = db.users

    def get_all_users(self):
        pass
        # self.all_users=

    def create_user(self, user):
        if not self.user_exsists(user):
            create_id = self.users.insert_one(user.__dict__).inserted_id
            return create_id
        print("User already exsists")
        return

    def delete_user(self, user):
        if self.users.find({"name": user.name}):
            self.users.delete_one({"name": user.name})
            return
        print("User does not exsist")
        return

    def change_balance(self, user, balance):
        pass

    def increase_balance(self, user, amount):
        updated_balance = self.users.find_one_and_update(
            {"name": user.name}, {"$inc": {"balance": amount}})
        print("Updated Balance: ")
        return

    def decrease_balance(self, user, amount):
        pass

    def user_exsists(self, user):
        if list(self.users.find({"name": user.name})):
            return True
        else:
            return False
