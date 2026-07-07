"""Endpoints for searching and retrieving anime."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Anime
from schemas import AnimeOut

router = APIRouter(prefix="/animes", tags=["animes"])


@router.get("", response_model=list[AnimeOut])
def search_animes(q: str = "", limit: int = 10, db: Session = Depends(get_db)):
    """
    Search for anime by title.

    A partial, case insensitive search is used so users can find anime
    without entering the exact name. The number of results returned is
    controlled by the limit parameter.
    """
    query = db.query(Anime)

    if q:
        query = query.filter(Anime.name.ilike(f"%{q}%"))

    return query.limit(limit).all()


@router.get("/{anime_id}", response_model=AnimeOut)
def get_anime(anime_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the details of a single anime.

    The anime is identified using its unique ID and the matching record
    is returned to the frontend.
    """
    return (
        db.query(Anime)
        .filter(Anime.id == anime_id)
        .first()
    )