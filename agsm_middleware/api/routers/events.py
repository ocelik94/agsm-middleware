# agsm_middleware/api/routers/events.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from agsm_middleware.crud import (
    create_event, get_event, get_events, update_event, delete_event
)
from agsm_middleware.database.connection import SessionLocal
from agsm_middleware.schemas.schemas import Event, EventCreate

router = APIRouter(
    prefix="/events",
    tags=["Events"],
    responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Event)
def create_new_event(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, event)


@router.get("/{event_id}", response_model=Event)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = get_event(db, event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


@router.get("/", response_model=List[Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = get_events(db, skip=skip, limit=limit)
    return events


@router.put("/{event_id}", response_model=Event)
def update_existing_event(event_id: int, event: EventCreate, db: Session = Depends(get_db)):
    db_event = update_event(db, event_id, event)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


@router.delete("/{event_id}")
def delete_existing_event(event_id: int, db: Session = Depends(get_db)):
    success = delete_event(db, event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}
