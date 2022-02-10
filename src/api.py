from lib2to3.pytree import Base
import yaml

from typing import Optional, List, TypedDict

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from bson.json_util import dumps

from db import Database

app = FastAPI()
database = Database()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    name: str
    balance: float


class Order(BaseModel):
    user: str
    item: str


class Deposit(BaseModel):
    user: str
    amount: float


class Item(BaseModel):
    name: str
    price: float


class Settings(BaseModel):
    items: List[Item]


def read_yaml():
    with open("../resources/prices.yaml", "r") as f:
        try:
            prices = yaml.safe_load(f)
            return prices
        except yaml.YAMLError as exc:
            print(exc)


@app.put("/users")
def update_item(new_user: User):
    database.create_user(new_user)


@app.post("/deposit")
def deposit(deposit: Deposit):
    user = database.get_user(deposit.user)
    database.increase_balance(user, deposit.amount)


@app.post("/buy")
def buy(order: Order):
    prices_dict = database.get_settings()
    price = prices_dict[order.item]
    user = database.get_user(order.user)
    database.decrease_balance(user, price)


@app.get("/user")
def get_user_by_name(name: str):
    user = database.users.find_one({"name": name})
    if user is not None:
        return JSONResponse(content=dumps(user))
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/users")
def get_all_users():
    users = database.users.find({})
    if users is not None:
        return JSONResponse(content=dumps(users))


@app.get("/settings")
def get_settings():
    settings = database.get_settings()
    print(settings)
    if settings is not None:
        return JSONResponse(content=dumps(settings))


@app.post("/settings")
def update_settings(settings: Settings):
    database.update_settings(settings)


@app.put("/settings")
def create_settings(settings: Settings):
    database.create_settings(settings)
