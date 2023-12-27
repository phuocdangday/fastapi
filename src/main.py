from fastapi import FastAPI

from src.database import init_database
from src.users.router import router as users_router

app = FastAPI()

init_database()

app.include_router(users_router)
