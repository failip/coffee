import py_compile
from user.user import User
from database.db import Database
Jan = User("Jan", 72459.0)
database = Database()

database.create_user(Jan)

for user2 in database.users.find({}):
    print(user2)
database.increase_balance(Jan, 200.0)
for user2 in database.users.find({"name": Jan.name}):
    print(user2)
# database.delete_user(Jan)
