import py_compile
from user.user import User
from database.db import Database
Jan = User("Peter", 72459.0)
database = Database()

database.create_user(Jan)

for user2 in database.users.find({}):
    print(user2)
