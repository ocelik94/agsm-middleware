# agsm_middleware/api/routers/configs.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from agsm_middleware.crud import (
    create_config, get_config, get_configs, update_config, delete_config
)
from agsm_middleware.database.connection import SessionLocal
from agsm_middleware.schemas.schemas import Config, ConfigCreate, ConfigUpdate

router = APIRouter(
    prefix="/configs",
    tags=["Configs"],
    responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Config)
def create_new_config(config: ConfigCreate, db: Session = Depends(get_db)):
    db_config = get_config(db, config.key)
    if db_config:
        raise HTTPException(status_code=400, detail="Config key already exists")
    return create_config(db, config)


@router.get("/{key}", response_model=Config)
def read_config(key: str, db: Session = Depends(get_db)):
    db_config = get_config(db, key)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Config not found")
    return db_config


@router.get("/", response_model=List[Config])
def read_configs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    configs = get_configs(db, skip=skip, limit=limit)
    return configs


@router.put("/{key}", response_model=Config)
def update_existing_config(key: str, config: ConfigUpdate, db: Session = Depends(get_db)):
    db_config = update_config(db, key, config)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Config not found")
    return db_config


@router.delete("/{key}")
def delete_existing_config(key: str, db: Session = Depends(get_db)):
    success = delete_config(db, key)
    if not success:
        raise HTTPException(status_code=404, detail="Config not found")
    return {"message": "Config deleted successfully"}
