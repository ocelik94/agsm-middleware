from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    valid_to: Optional[datetime] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    valid_to: Optional[datetime] = None


class Category(CategoryBase):
    valid_from: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class GameBase(BaseModel):
    name: str
    image: str
    tag: str
    category: str
    valid_to: Optional[datetime] = None


class GameCreate(GameBase):
    pass


class GameUpdate(BaseModel):
    image: Optional[str] = None
    tag: Optional[str] = None
    category: Optional[str] = None
    valid_to: Optional[datetime] = None


class Game(GameBase):
    valid_from: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ServerBase(BaseModel):
    game: str
    discord_channel_id: int
    valid_to: Optional[datetime] = None


class ServerCreate(ServerBase):
    pass


class ServerUpdate(BaseModel):
    game: Optional[str] = None
    discord_channel_id: Optional[int] = None
    valid_to: Optional[datetime] = None


class Server(ServerBase):
    id: int
    valid_from: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class EventBase(BaseModel):
    event: str
    event_type: Optional[str] = "generic"


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    time: datetime

    class Config:
        orm_mode = True


class ConfigBase(BaseModel):
    key: str
    value: Optional[str] = None
    valid_to: Optional[datetime] = None


class ConfigCreate(ConfigBase):
    pass


class ConfigUpdate(BaseModel):
    value: Optional[str] = None
    valid_to: Optional[datetime] = None


class Config(ConfigBase):
    valid_from: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
