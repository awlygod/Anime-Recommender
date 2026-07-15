"""Endpoint powering the combined recommendation flow."""

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from database import get_db
from recommender.combined import recommend
from schemas import RecommendRequest, RecommendResult

router = APIRouter(prefix="/recommend", tags=["recommend"])


def _to_recommend_result(anime, score: float) -> RecommendResult:
    return RecommendResult(
        id=anime.id,
        name=anime.name,
        genres=anime.genres,
        synopsis=anime.synopsis,
        type=anime.type,
        episodes=anime.episodes,
        score=anime.score,
        popularity=anime.popularity,
        image_url=anime.image_url,
        match_score=round(score, 3),
    )


@router.post("", response_model=list[RecommendResult])
def get_recommendations(payload: RecommendRequest, request: Request, db: Session = Depends(get_db)):
    """
    Returns ranked anime recommendations based on whichever inputs are provided:
    anime_id (content-based), genres/type (preference-based), or both.
    """
    content_recommender = request.app.state.content_recommender

    results = recommend(
        db=db,
        content_recommender=content_recommender,
        anime_id=payload.anime_id,
        genres=payload.genres,
        type_=payload.type,
        top_n=payload.top_n,
    )

    return [_to_recommend_result(anime, score) for anime, score in results]