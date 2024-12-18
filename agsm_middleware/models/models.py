from sqlalchemy import Column, String, Integer, BigInteger, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship

from agsm_middleware.database.connection import Base


class Category(Base):
    __tablename__ = "categories"

    name = Column(String, primary_key=True, index=True)
    valid_to = Column(TIMESTAMP, nullable=True)
    valid_from = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

    games = relationship("Game", back_populates="category_obj")


class Game(Base):
    __tablename__ = "games"

    name = Column(String, primary_key=True, index=True)
    image = Column(String, nullable=False)
    tag = Column(String, nullable=False)
    category = Column(String, ForeignKey("categories.name"), nullable=False)
    valid_to = Column(TIMESTAMP, nullable=True)
    valid_from = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

    category_obj = relationship("Category", back_populates="games")
    servers = relationship("Server", back_populates="game_obj")


class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)
    game = Column(String, ForeignKey("games.name"), nullable=False)
    discord_channel_id = Column(BigInteger, nullable=False)
    valid_to = Column(TIMESTAMP, nullable=True)
    valid_from = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

    game_obj = relationship("Game", back_populates="servers")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event = Column(String, nullable=False)
    event_type = Column(String, default="generic")
    time = Column(TIMESTAMP, server_default=func.now(), nullable=False)


class Config(Base):
    __tablename__ = "configs"

    key = Column(String, primary_key=True, index=True)
    value = Column(String, nullable=True)
    valid_to = Column(TIMESTAMP, nullable=True)
    valid_from = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
