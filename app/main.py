"""(API ko chalane wali file)"""

from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routers import products,orders


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(products.router)
app.include_router(orders.router)
