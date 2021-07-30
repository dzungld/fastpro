from fastapi import APIRouter
from app.api.v1 import movies, users

api_router = APIRouter()
api_router.include_router(movies.router, prefix="/movies", tags=["movies"])
api_router.include_router(users.router, prefix="/users", tags=["users"])