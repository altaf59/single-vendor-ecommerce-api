from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routers import products, orders, user, admin


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mart Ecommerce API", version="1.0.0")


app.include_router(products.router)
app.include_router(orders.router)
app.include_router(user.router)
app.include_router(admin.router)

