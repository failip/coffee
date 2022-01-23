from db import Database
from user import User

database = Database()
print("Before change:")
for user2 in database.users.find({}):
    print(user2)


peter = database.get_user("Peter")
database.increase_balance(peter, 200.0)

print("After changes:")
for user2 in database.users.find({}):
    print(user2)
