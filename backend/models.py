"""SQLAlchemy ORM models."""

from sqlalchemy import Column, Integer, String, Float, Text
from database import Base


class Anime(Base):
    """Represents a single anime entry sourced from the Kaggle dataset."""

    __tablename__ = "anime"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    genres = Column(String, default="")
    synopsis = Column(Text, default="")
    type = Column(String, default="")
    episodes = Column(String, default="")
    score = Column(Float, default=0.0)
    popularity = Column(Integer, default=0)
    image_url = Column(String, default="")