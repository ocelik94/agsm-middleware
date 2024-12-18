from typing import List, Optional

from sqlalchemy.orm import Session

from agsm_middleware.models.models import Category, Game, Server, Event, Config
from agsm_middleware.schemas.schemas import (
    CategoryCreate,
    CategoryUpdate,
    GameCreate,
    GameUpdate,
    ServerCreate,
    ServerUpdate,
    EventCreate,
    ConfigCreate,
    ConfigUpdate,
)


# Category CRUD
def create_category(db: Session, category: CategoryCreate) -> Category:
    db_category = Category(
        name=category.name,
        valid_to=category.valid_to
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db: Session, name: str) -> Optional[Category]:
    return db.query(Category).filter(Category.name == name).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100) -> List[Category]:
    return db.query(Category).offset(skip).limit(limit).all()


def update_category(db: Session, name: str, category: CategoryUpdate) -> Optional[Category]:
    db_category = get_category(db, name)
    if db_category:
        if category.valid_to is not None:
            db_category.valid_to = category.valid_to
        db.commit()
        db.refresh(db_category)
    return db_category


def delete_category(db: Session, name: str) -> bool:
    db_category = get_category(db, name)
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False


# Game CRUD
def create_game(db: Session, game: GameCreate) -> Game:
    db_game = Game(
        name=game.name,
        image=game.image,
        tag=game.tag,
        category=game.category,
        valid_to=game.valid_to
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_game(db: Session, name: str) -> Optional[Game]:
    return db.query(Game).filter(Game.name == name).first()


def get_games(db: Session, skip: int = 0, limit: int = 100) -> List[Game]:
    return db.query(Game).offset(skip).limit(limit).all()


def update_game(db: Session, name: str, game: GameUpdate) -> Optional[Game]:
    db_game = get_game(db, name)
    if db_game:
        if game.image is not None:
            db_game.image = game.image
        if game.tag is not None:
            db_game.tag = game.tag
        if game.category is not None:
            db_game.category = game.category
        if game.valid_to is not None:
            db_game.valid_to = game.valid_to
        db.commit()
        db.refresh(db_game)
    return db_game


def delete_game(db: Session, name: str) -> bool:
    db_game = get_game(db, name)
    if db_game:
        db.delete(db_game)
        db.commit()
        return True
    return False


# Server CRUD
def create_server(db: Session, server: ServerCreate) -> Server:
    db_server = Server(
        game=server.game,
        discord_channel_id=server.discord_channel_id,
        valid_to=server.valid_to
    )
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server


def get_server(db: Session, server_id: int) -> Optional[Server]:
    return db.query(Server).filter(Server.id == server_id).first()


def get_servers(db: Session, skip: int = 0, limit: int = 100) -> List[Server]:
    return db.query(Server).offset(skip).limit(limit).all()


def update_server(db: Session, server_id: int, server: ServerUpdate) -> Optional[Server]:
    db_server = get_server(db, server_id)
    if db_server:
        if server.game is not None:
            db_server.game = server.game
        if server.discord_channel_id is not None:
            db_server.discord_channel_id = server.discord_channel_id
        if server.valid_to is not None:
            db_server.valid_to = server.valid_to
        db.commit()
        db.refresh(db_server)
    return db_server


def delete_server(db: Session, server_id: int) -> bool:
    db_server = get_server(db, server_id)
    if db_server:
        db.delete(db_server)
        db.commit()
        return True
    return False


# Event CRUD
def create_event(db: Session, event: EventCreate) -> Event:
    db_event = Event(
        event=event.event,
        event_type=event.event_type
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_event(db: Session, event_id: int) -> Optional[Event]:
    return db.query(Event).filter(Event.id == event_id).first()


def get_events(db: Session, skip: int = 0, limit: int = 100) -> List[Event]:
    return db.query(Event).offset(skip).limit(limit).all()


def update_event(db: Session, event_id: int, event: EventCreate) -> Optional[Event]:
    db_event = get_event(db, event_id)
    if db_event:
        db_event.event = event.event
        db_event.event_type = event.event_type
        db.commit()
        db.refresh(db_event)
    return db_event


def delete_event(db: Session, event_id: int) -> bool:
    db_event = get_event(db, event_id)
    if db_event:
        db.delete(db_event)
        db.commit()
        return True
    return False


# Config CRUD
def create_config(db: Session, config: ConfigCreate) -> Config:
    db_config = Config(
        key=config.key,
        value=config.value,
        valid_to=config.valid_to
    )
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config


def get_config(db: Session, key: str) -> Optional[Config]:
    return db.query(Config).filter(Config.key == key).first()


def get_configs(db: Session, skip: int = 0, limit: int = 100) -> List[Config]:
    return db.query(Config).offset(skip).limit(limit).all()


def update_config(db: Session, key: str, config: ConfigUpdate) -> Optional[Config]:
    db_config = get_config(db, key)
    if db_config:
        if config.value is not None:
            db_config.value = config.value
        if config.valid_to is not None:
            db_config.valid_to = config.valid_to
        db.commit()
        db.refresh(db_config)
    return db_config


def delete_config(db: Session, key: str) -> bool:
    db_config = get_config(db, key)
    if db_config:
        db.delete(db_config)
        db.commit()
        return True
    return False
