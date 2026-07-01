"""Pydantic request/response schemas."""

from pydantic import BaseModel
from typing import Optional, List


class AnimeOut(BaseModel):
    id: int
    name: str
    genres: str
    synopsis: str
    type: str
    episodes: str
    score: float
    popularity: int
    image_url: str

    class Config:
        from_attributes = True


class RecommendRequest(BaseModel):
    """Input for the /recommend endpoint. All fields optional — combine as needed."""
    anime_id: Optional[int] = None
    genres: Optional[List[str]] = None
    type: Optional[str] = None
    top_n: int = 10


class RecommendResult(AnimeOut):
    match_score: float