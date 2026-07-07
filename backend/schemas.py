"""
Pydantic models used for request validation and API responses.

These schemas define the data exchanged between the frontend and backend.
"""

from typing import List, Optional

from pydantic import BaseModel


class AnimeOut(BaseModel):
    """
    Represents an anime returned by the API.

    This schema contains all the information the frontend needs to display
    an anime, including its details, rating, popularity, and image.
    """

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
        # Allows SQLAlchemy model instances to be returned directly.
        from_attributes = True


class RecommendRequest(BaseModel):
    """
    Request body for the recommendation endpoint.

    The user can provide an anime ID, preferred genres, a type, or any
    combination of these values. The recommendation system decides which
    strategy to use based on the information included in the request.
    """

    anime_id: Optional[int] = None
    genres: Optional[List[str]] = None
    type: Optional[str] = None
    top_n: int = 10


class RecommendResult(AnimeOut):
    """
    Response returned for each recommended anime.

    In addition to the anime details, this schema includes a match score
    that indicates how closely the recommendation matches the user's
    request.
    """

    match_score: float