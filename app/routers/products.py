"""(Saman/Products ke liye)"""
from fastapi import APIRouter, Depends
from .. import schemas, crud
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(prefix="/products",tags=["products"])


@router.post("/", response_model=schemas.productBase)
def create_product(product:schemas.productBase, db:Session = Depends(get_db)):
    return crud.create_products(db, product)