import uvicorn
from fastapi import FastAPI

from agsm_middleware.api.routers import (
    categories_router,
    games_router,
    servers_router,
    events_router,
    configs_router
)
from agsm_middleware.config import settings

# Create all tables in the database (if not using Alembic)
# Uncomment the following line if you want SQLAlchemy to create tables automatically
# Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="AGSM Middleware CRUD API",
    description="API for managing categories, games, servers, events, and configs.",
    version="1.0.0"
)

# Include API routers
app.include_router(categories_router)
app.include_router(games_router)
app.include_router(servers_router)
app.include_router(events_router)
app.include_router(configs_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the AGSM Middleware CRUD API"}


if __name__ == "__main__":
    uvicorn.run(
        "agsm_middleware.main:app",
        host=settings.server_host,
        port=settings.server_port,
    )
