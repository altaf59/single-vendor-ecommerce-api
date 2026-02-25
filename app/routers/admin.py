from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, config
from ..database import get_db

router = APIRouter(prefix="/admin", tags=["admin"])

# --- Admin Registration (with Secret Code) ---

@router.post("/register", response_model=schemas.UserResponse)
def register_admin(admin_data: schemas.AdminCreate, db: Session = Depends(get_db)):
    # 1. Check karo ke secret code sahi hai ya nahi
    if admin_data.secret_code != config.ADMIN_SECRET_CODE:
        raise HTTPException(status_code=403, detail="Wrong Secret Code! You cannot become an admin.")
    
    # 2. Check karo ke email pehle se to nahi hai
    db_user = crud.get_user_by_email(db, email=admin_data.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 3. Admin create karo
    return crud.create_user(db=db, user=admin_data, is_admin=True)

# --- Admin Login ---

@router.post("/login")
def admin_login(credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    # 1. User ko email se dhundo
    user = crud.get_user_by_email(db, email=credentials.email)
    
    # 2. Check karo ke user hai aur wo admin bhi hai
    if not user or not user.is_admin:
        raise HTTPException(status_code=403, detail="Invalid Credentials or Not an Admin")
    
    # 3. Password verify karo
    from ..utils import verify_password
    if not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=403, detail="Invalid Credentials")
    
    return {
        "message": "Admin Login Successful",
        "admin_id": user.id,
        "username": user.username
    }

# --- Product Management (Only for Admin) ---

@router.post("/products", response_model=schemas.ProductResponse)
def admin_create_product(admin_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=admin_id)
    if not user or not user.is_admin:
        raise HTTPException(status_code=403, detail="Access Denied: Only Admin can add products")
    return crud.create_products(db, product)

@router.put("/products/{product_id}", response_model=schemas.ProductResponse)
def admin_update_product(admin_id: int, product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=admin_id)
    if not user or not user.is_admin:
        raise HTTPException(status_code=403, detail="Access Denied")
    return crud.update_product(db, product_id, product)

@router.delete("/products/{product_id}")
def admin_delete_product(admin_id: int, product_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=admin_id)
    if not user or not user.is_admin:
        raise HTTPException(status_code=403, detail="Access Denied")
    crud.delete_product(db, product_id)
    return {"message": "Product deleted successfully"}


# --- Order Management (Viewing all orders) ---

@router.get("/orders", response_model=list[schemas.OrderResponse])
def admin_view_all_orders(admin_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=admin_id)
    if not user or not user.is_admin:
        raise HTTPException(status_code=403, detail="Access Denied: Only Admin can view all orders")
    return crud.read_order(db)
