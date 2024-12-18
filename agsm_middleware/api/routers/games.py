from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from agsm_middleware.crud import (
    create_game, get_game, get_games, update_game, delete_game
)
from agsm_middleware.database.connection import SessionLocal
from agsm_middleware.schemas.schemas import Game, GameCreate, GameUpdate

router = APIRouter(
    prefix="/games",
    tags=["Games"],
    responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Game)
def create_new_game(game: GameCreate, db: Session = Depends(get_db)):
    db_game = get_game(db, game.name)
    if db_game:
        raise HTTPException(status_code=400, detail="Game already exists")
    # Ensure the category exists
    category = db.query(agsm_middleware.models.models.Category).filter(
        agsm_middleware.models.models.Category.name == game.category).first()
    if not category:
        raise HTTPException(status_code=400, detail="Referenced category does not exist")
    return create_game(db, game)


@router.get("/{name}", response_model=Game)
def read_game(name: str, db: Session = Depends(get_db)):
    db_game = get_game(db, name)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game


@router.get("/", response_model=List[Game])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = get_games(db, skip=skip, limit=limit)
    return games


@router.put("/{name}", response_model=Game)
def update_existing_game(name: str, game: GameUpdate, db: Session = Depends(get_db)):
    if game.category:
        # Ensure the new category exists
        category = db.query(agsm_middleware.models.models.Category).filter(
            agsm_middleware.models.models.Category.name == game.category).first()
        if not category:
            raise HTTPException(status_code=400, detail="Referenced category does not exist")
    db_game = update_game(db, name, game)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game


@router.delete("/{name}")
def delete_existing_game(name: str, db: Session = Depends(get_db)):
    success = delete_game(db, name)
    if not success:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"message": "Game deleted successfully"}
