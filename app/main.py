from fastapi import FastAPI
from app.config.database import Base, engine
from app.routes import item_route

# automatically genrate table if database not created it
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD Basic")

# add router
app.include_router(item_route.router)