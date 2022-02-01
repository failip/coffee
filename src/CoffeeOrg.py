from db import Database
from user import User
import yaml
database = Database()
print("Before change:")
for user2 in database.users.find({}):
    print(user2)
#Jan = database.create_user(["jan", 20.0])
#peter = database.get_user("Jan")
#database.increase_balance(peter, 200.0)
# Jan.buy(Jan, "beer")

print("After changes:")
for user2 in database.users.find({}):
    print(user2)
