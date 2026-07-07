"""
Database models used by the application.

The project currently uses a single table to store anime information
loaded from the dataset.
"""

from sqlalchemy import Column, Float, Integer, String, Text

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