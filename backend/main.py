"""FastAPI application entrypoint — wires routers, CORS, and builds the recommender at startup."""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from database import SessionLocal
from models import Anime
from recommender.content_based import ContentRecommender
from routers import anime, recommend

load_dotenv()

app = FastAPI(title="Anime Recommendation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(anime.router)
app.include_router(recommend.router)


@app.on_event("startup")
def build_recommender():
    """Loads all anime into memory once and builds the TF-IDF similarity model."""
    db = SessionLocal()
    animes = db.query(Anime).all()
    data = [
        {"id": a.id, "genres": a.genres, "synopsis": a.synopsis}
        for a in animes
    ]
    db.close()
    app.state.content_recommender = ContentRecommender(data)
    print(f"Content recommender built on {len(data)} anime.")


@app.get("/health")
def health():
    return {"status": "ok"}