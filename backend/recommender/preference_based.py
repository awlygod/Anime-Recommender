"""Preference-based filtering: rank anime by genre/type match and popularity/score."""

from sqlalchemy.orm import Session
from sqlalchemy import or_
from models import Anime


def get_by_preferences(db: Session, genres: list[str] | None, type_: str | None, top_n: int = 10):
    """
    Filters the anime table by genre substring match and/or type,
    then ranks by score descending as a tiebreaker.
    """
    query = db.query(Anime)

    if genres:
        genre_filters = [Anime.genres.ilike(f"%{g}%") for g in genres]
        query = query.filter(or_(*genre_filters))

    if type_:
        query = query.filter(Anime.type.ilike(type_))

    results = query.order_by(Anime.score.desc()).limit(top_n).all()
    return results