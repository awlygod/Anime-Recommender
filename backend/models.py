"""
Database models used by the application.

The project currently uses two tables, one for anime information loaded
from the dataset, and one for tracking which anime have been saved to
the wishlist.
"""

from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text

from database import Base


class Anime(Base):
    """
    Represents an anime stored in the database.

    Each instance of this model corresponds to a single row in the
    anime table and contains the information used throughout the
    recommendation system.
    """

    __tablename__ = "anime"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    genres = Column(String, default="")
    synopsis = Column(Text, default="")
    type = Column(String, default="")

    # Stored as a string because some entries in the dataset use
    # "UNKNOWN" instead of a numeric episode count.
    episodes = Column(String, default="")

    score = Column(Float, default=0.0)
    popularity = Column(Integer, default=0)
    image_url = Column(String, default="")


class Wishlist(Base):
    """
    Represents a single anime saved to the wishlist.

    There is no user login in this project, so this is one shared
    wishlist rather than a separate list per account. The anime_id
    column is unique so the same anime cannot be added twice.
    """

    __tablename__ = "wishlist"

    id = Column(Integer, primary_key=True, index=True)
    anime_id = Column(Integer, ForeignKey("anime.id"), nullable=False, unique=True)
    added_at = Column(DateTime, default=datetime.utcnow)