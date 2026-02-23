"""(Order management ke liye)"""
from fastapi import APIRouter, Depends
from .. import schemas, crud
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=schemas.OrderResponse)
def create_order(user_id: int, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(user_id, db, order)

@router.get("/", response_model=list[schemas.OrderResponse])
def read_order(db: Session = Depends(get_db)):
    return crud.read_order(db)

@router.get("/{order_id}", response_model=schemas.OrderResponse)
def read_order_by_id(order_id: int, db: Session = Depends(get_db)):
    return crud.read_order_by_id(order_id, db)