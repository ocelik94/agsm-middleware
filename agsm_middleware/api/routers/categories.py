from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from agsm_middleware.crud import (
    create_category, get_category, get_categories, update_category, delete_category
)
from agsm_middleware.database.connection import SessionLocal
from agsm_middleware.schemas.schemas import Category, CategoryCreate, CategoryUpdate

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
    responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Category)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = get_category(db, category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return create_category(db, category)


@router.get("/{name}", response_model=Category)
def read_category(name: str, db: Session = Depends(get_db)):
    db_category = get_category(db, name)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.get("/", response_model=List[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = get_categories(db, skip=skip, limit=limit)
    return categories


@router.put("/{name}", response_model=Category)
def update_existing_category(name: str, category: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = update_category(db, name, category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.delete("/{name}")
def delete_existing_category(name: str, db: Session = Depends(get_db)):
    success = delete_category(db, name)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}
