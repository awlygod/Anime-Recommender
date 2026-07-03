"""Endpoints for browsing/searching anime directly."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Anime
from schemas import AnimeOut

router = APIRouter(prefix="/animes", tags=["animes"])


@router.get("", response_model=list[AnimeOut])
def search_animes(q: str = "", limit: int = 10, db: Session = Depends(get_db)):
    """Search anime by name substring — used for frontend autocomplete."""
    query = db.query(Anime)
    if q:
        query = query.filter(Anime.name.ilike(f"%{q}%"))
    return query.limit(limit).all()


@router.get("/{anime_id}", response_model=AnimeOut)
def get_anime(anime_id: int, db: Session = Depends(get_db)):
    """Fetch a single anime by ID."""
    return db.query(Anime).filter(Anime.id == anime_id).first()