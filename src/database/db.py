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
        if self.users.find({"name": user.name}):
            print("User already exsists")
            return
        create_id = self.users.insert_one(user.__dict__).inserted_id
        return create_id

    def delete_user(self, user):
        pass

    def change_balance(self, user, balance):
        pass

    def increase_balance(self, user, amount):
        pass

    def decrease_balance(self, user, amount):
        pass
