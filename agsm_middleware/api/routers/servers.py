# agsm_middleware/api/routers/servers.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from agsm_middleware.crud import (
    create_server, get_server, get_servers, update_server, delete_server
)
from agsm_middleware.database.connection import SessionLocal
from agsm_middleware.schemas.schemas import Server, ServerCreate, ServerUpdate

router = APIRouter(
    prefix="/servers",
    tags=["Servers"],
    responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Server)
def create_new_server(server: ServerCreate, db: Session = Depends(get_db)):
    # Ensure the referenced game exists
    game = db.query(agsm_middleware.models.models.Game).filter(
        agsm_middleware.models.models.Game.name == server.game).first()
    if not game:
        raise HTTPException(status_code=400, detail="Referenced game does not exist")
    return create_server(db, server)


@router.get("/{server_id}", response_model=Server)
def read_server(server_id: int, db: Session = Depends(get_db)):
    db_server = get_server(db, server_id)
    if db_server is None:
        raise HTTPException(status_code=404, detail="Server not found")
    return db_server


@router.get("/", response_model=List[Server])
def read_servers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    servers = get_servers(db, skip=skip, limit=limit)
    return servers


@router.put("/{server_id}", response_model=Server)
def update_existing_server(server_id: int, server: ServerUpdate, db: Session = Depends(get_db)):
    if server.game:
        # Ensure the new game exists
        game = db.query(agsm_middleware.models.models.Game).filter(
            agsm_middleware.models.models.Game.name == server.game).first()
        if not game:
            raise HTTPException(status_code=400, detail="Referenced game does not exist")
    db_server = update_server(db, server_id, server)
    if db_server is None:
        raise HTTPException(status_code=404, detail="Server not found")
    return db_server


@router.delete("/{server_id}")
def delete_existing_server(server_id: int, db: Session = Depends(get_db)):
    success = delete_server(db, server_id)
    if not success:
        raise HTTPException(status_code=404, detail="Server not found")
    return {"message": "Server deleted successfully"}
