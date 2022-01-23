import yaml

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from db import Database
from user import User

app = FastAPI()
database = Database()


class NewUser(BaseModel):
    name: str
    balance: float


class Order(BaseModel):
    user: str
    item: str


class Deposit(BaseModel):
    user: str
    amount: float


def read_yaml():
    with open("../resources/prices.yaml", "r") as f:
        try:
            prices = yaml.safe_load(f)
            return prices
        except yaml.YAMLError as exc:
            print(exc)


@app.put("/users")
def update_item(new_user: NewUser):
    database.create_user(new_user)


@app.post("/deposit")
def deposit(deposit: Deposit):
    user = database.get_user(deposit.user)
    database.increase_balance(user, deposit.amount)


@app.post("/buy")
def buy(order: Order):
    prices_dict = read_yaml()
    price = prices_dict["prices"][order.item][0]
    user = database.get_user(order.user)
    database.decrease_balance(user, price)
