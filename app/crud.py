"""(DB mein data dalne aur nikalne ke liye)"""
from sqlalchemy.orm import Session
from . import models, schemas, utils 
from fastapi import HTTPException

# --- Products ---
def create_products(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def read_products(db: Session, search: str = None):
    query = db.query(models.Product)
    if search:
        query = query.filter(models.Product.name.contains(search))
    return query.all()

def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return db_product
def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.stock = product.stock
    db.commit()
    db.refresh(db_product)
    return db_product
# --- Users ---
def create_user(db: Session, user: schemas.UserCreate, is_admin: bool = False):
    # Hash the password before saving
    hashed_password = utils.get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_admin=is_admin
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# --- Orders ---
def create_order(user_id: int, db: Session, order: schemas.OrderCreate):
    # 0. User check
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 1. Database se product uthao taake asli price mil sake
    product = db.query(models.Product).filter(models.Product.id == order.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product.stock < order.quantity:
        raise HTTPException(status_code=400, detail="Out of stock")
    
    # Stock update
    product.stock -= order.quantity
    
    # 2. Total price calculation
    calculated_total = product.price * order.quantity
    
    # 3. Order creation
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

def read_order(db: Session):
    return db.query(models.Order).all()

def read_order_by_id(order_id: int, db: Session):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
