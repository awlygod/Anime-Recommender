"""Endpoints for adding, removing, and viewing wishlisted anime."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Anime, Wishlist
from schemas import WishlistAddRequest, WishlistItemOut

router = APIRouter(prefix="/wishlist", tags=["wishlist"])


def _to_wishlist_item(anime: Anime, added_at):
    return WishlistItemOut(
        id=anime.id,
        name=anime.name,
        genres=anime.genres,
        synopsis=anime.synopsis,
        type=anime.type,
        episodes=anime.episodes,
        score=anime.score,
        popularity=anime.popularity,
        image_url=anime.image_url,
        added_at=added_at,
    )


@router.get("", response_model=list[WishlistItemOut])
def get_wishlist(db: Session = Depends(get_db)):
    """
    Retrieve every anime currently on the wishlist.

    Anime are returned most recently added first, joining the wishlist
    table with the anime table so the frontend gets full anime details
    back in a single call instead of fetching each one separately.
    """
    rows = (
        db.query(Anime, Wishlist.added_at)
        .join(Wishlist, Wishlist.anime_id == Anime.id)
        .order_by(Wishlist.added_at.desc())
        .all()
    )

    return [_to_wishlist_item(anime, added_at) for anime, added_at in rows]


@router.post("", response_model=WishlistItemOut)
def add_to_wishlist(payload: WishlistAddRequest, db: Session = Depends(get_db)):
    """
    Add an anime to the wishlist.

    If the anime does not exist, a 404 is returned. If it has already
    been added before, the existing entry is returned instead of creating
    a duplicate, since anime_id is unique on the wishlist table.
    """
    anime = db.query(Anime).filter(Anime.id == payload.anime_id).first()

    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")

    existing = db.query(Wishlist).filter(Wishlist.anime_id == payload.anime_id).first()

    if existing:
        return _to_wishlist_item(anime, existing.added_at)

    entry = Wishlist(anime_id=payload.anime_id)
    db.add(entry)
    db.commit()
    db.refresh(entry)

    return _to_wishlist_item(anime, entry.added_at)


@router.delete("/{anime_id}")
def remove_from_wishlist(anime_id: int, db: Session = Depends(get_db)):
    """
    Remove an anime from the wishlist by its id.

    Safe to call even if the anime was never added, in which case
    nothing happens and a normal response is still returned.
    """
    entry = db.query(Wishlist).filter(Wishlist.anime_id == anime_id).first()

    if entry:
        db.delete(entry)
        db.commit()

    return {"status": "ok"}