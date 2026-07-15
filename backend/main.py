"""
Main entry point for the backend application.

This file creates the FastAPI app, registers the API routes, configures
CORS, and prepares the content based recommender when the server starts.
"""

import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal
from models import Anime
from recommender.content_based import ContentRecommender
from routers import anime, recommend, wishlist

load_dotenv()

app = FastAPI(title="Anime Recommendation API")

# Allow requests from the frontend application.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(anime.router)
app.include_router(recommend.router)
app.include_router(wishlist.router)

@app.on_event("startup")
def build_recommender():
    """
    Build the content based recommendation model when the application
    starts.

    The required anime data is loaded from the database and used to
    initialize the recommender only once. This avoids rebuilding the
    TF IDF model for every recommendation request and keeps the API
    responsive.
    """

    db = SessionLocal()

    animes = db.query(Anime).all()

    data = [
        {
            "id": a.id,
            "genres": a.genres,
            "synopsis": a.synopsis,
        }
        for a in animes
    ]

    db.close()

    app.state.content_recommender = ContentRecommender(data)

    print(f"Content recommender built on {len(data)} anime.")


@app.get("/health")
def health():
    """
    Health check endpoint.

    Returns a simple response that can be used to verify that the
    backend is running and able to accept requests.
    """

    return {"status": "ok"}