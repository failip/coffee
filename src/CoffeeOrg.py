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


def read_yaml():
    with open("../resources/prices.yaml", "r") as f:
        try:
            prices = yaml.safe_load(f)
            return prices
        except yaml.YAMLError as exc:
            print(exc)


def buy(user, something):
    prices_dict = read_yaml()
    price_of_something = prices_dict["prices"][something][0]
    database.decrease_balance(user, price_of_something)


buy(database.get_user("Jan"), "beer")
