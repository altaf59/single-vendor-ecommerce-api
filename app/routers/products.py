"""(Saman/Products ke liye)"""
from fastapi import APIRouter, Depends
from .. import schemas, crud
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_products(db, product)

@router.get("/", response_model=list[schemas.ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return crud.read_products(db)