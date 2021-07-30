from typing import List
from fastapi import Header, APIRouter, HTTPException

from app import models

fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order once again.',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]

router = APIRouter()

@router.get('/', response_model=List[models.Movie])
async def index():
    return fake_movie_db

@router.post('/', status_code=201)
async def add_movie(payload: models.Movie):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) - 1}

@router.put('/{id}')
async def update_movie(id: int, payload: models.Movie):
    movie = payload.dict()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        fake_movie_db[id] = movie
        return None
    raise HTTPException(status_code=404, detail="Movie with given id not found")

@router.delete('/{id}')
async def delete_movie(id: int):
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        del fake_movie_db[id]
        return None
    raise HTTPException(status_code=404, detail="Movie with given id not found")