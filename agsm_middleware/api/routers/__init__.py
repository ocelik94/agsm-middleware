from .categories import router as categories_router
from .configs import router as configs_router
from .events import router as events_router
from .games import router as games_router
from .servers import router as servers_router

__all__ = [
    "categories_router",
    "games_router",
    "servers_router",
    "events_router",
    "configs_router"
]
