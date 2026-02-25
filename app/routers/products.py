from fastapi import APIRouter, Depends
from .. import schemas, crud
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[schemas.ProductResponse])
def read_products(search: str = None, db: Session = Depends(get_db)):
    return crud.read_products(db, search=search)

