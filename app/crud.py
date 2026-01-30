"""(DB mein data dalne aur nikalne ke liye)"""
from sqlalchemy.orm import Session
from . import models, schemas 
from fastapi import HTTPException

def create_products (db:Session, product:schemas.productBase):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def read_products(db:Session):
    return db.query(models.Product).all()

def create_user(db:Session, user:schemas.userCreat):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_order( user_id: int,db:Session,order: schemas.orderCreate):
    # 1. Database se product uthao taake asli price mil sake
    product = db.query(models.Product).filter(models.Product.id == order.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.stock < order.quantity:
        raise HTTPException(status_code=400, detail="Out of stock")
    product.stock -= order.quantity
    # 2. Total price backend par calculate karo
    calculated_total = product.price * order.quantity
      # 3. manual object banana
    db_order = models.Order(
        user_id=user_id,
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=calculated_total,
        status="pending"
    )
    
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def read_order(db:Session):
    return db.query(models.Order).all()

def read_order_by_id(order_id:int,db:Session):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if  not db_order:
      raise HTTPException(status_code=404, detail="Order not found")
    return db_order