"""(Pydantic validation ke liye)"""
from pydantic import BaseModel

class productBase(BaseModel):
    name:str
    price:float
    stock:int

class userCreat(BaseModel):
    username:str
    email:str
    password:str
