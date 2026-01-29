"""(API ko chalane wali file)"""
from fastapi import FastAPI
from .database import engine, Base
from .import models

Base.metadata.create_all(engine)
app=FastAPI()

