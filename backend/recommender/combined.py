"""
This combines content-based and preference-based recommendations.

Logic:
- anime_id only          -> pure content-based similarity
- genres/type only       -> pure preference-based filtering
- both provided          -> get content-based candidates, then boost/filter
                            by whether they also match the given genres/type
"""

from sqlalchemy.orm import Session
from models import Anime
from recommender.preference_based import get_by_preferences


def recommend(
    db: Session,
    content_recommender,
    anime_id: int | None,
    genres: list[str] | None,
    type_: str | None,
    top_n: int = 10,
):
    if anime_id and not genres and not type_:
        similar = content_recommender.get_similar(anime_id, top_n=top_n)
        ids = [int(aid) for aid, _ in similar]
        scores = {aid: score for aid, score in similar}
        animes = db.query(Anime).filter(Anime.id.in_(ids)).all()
        return sorted(
            [(a, scores[a.id]) for a in animes],
            key=lambda pair: pair[1],
            reverse=True,
        )

    if anime_id and (genres or type_):
        # widen candidate pool from content similarity, then filter by preferences
        similar = content_recommender.get_similar(anime_id, top_n=top_n * 5)
        candidate_ids = [int(aid) for aid, _ in similar]
        scores = {aid: score for aid, score in similar}

        query = db.query(Anime).filter(Anime.id.in_(candidate_ids))
        if genres:
            from sqlalchemy import or_
            query = query.filter(or_(*[Anime.genres.ilike(f"%{g}%") for g in genres]))
        if type_:
            query = query.filter(Anime.type.ilike(type_))

        animes = query.all()
        ranked = sorted(
            [(a, scores.get(a.id, 0.0)) for a in animes],
            key=lambda pair: pair[1],
            reverse=True,
        )
        return ranked[:top_n]

    # preference-only path
    animes = get_by_preferences(db, genres, type_, top_n=top_n)
    return [(a, a.score / 10.0) for a in animes]  # normalize score as pseudo match_score