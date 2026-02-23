"""(API ko chalane wali file)"""
from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routers import products, orders, user

# Database tables create karna
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mart Ecommerce API", version="1.0.0")

# Routers include karna
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(user.router)
