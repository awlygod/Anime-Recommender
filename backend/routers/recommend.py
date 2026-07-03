"""Endpoint powering the combined recommendation flow."""

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database import get_db
from schemas import RecommendRequest, RecommendResult
from recommender.combined import recommend

router = APIRouter(prefix="/recommend", tags=["recommend"])


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

    return [
        RecommendResult(**anime.__dict__, match_score=round(score, 3))
        for anime, score in results
    ]