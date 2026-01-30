"""(DB mein data dalne aur nikalne ke liye)"""
from sqlalchemy.orm import Session
from . import models, schemas 

def create_products (db:Session, product:schemas.productBase):
    db_prouduct = models.Product(**product.model_dump())
    db.add(db_prouduct)
    db.commit()
    db.refresh(db_prouduct)
    return db_prouduct

def get_products(db:Session):
    return db.query(models.Product).all()

def create_user(db:Session, user:schemas.userCreat):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

