"""
This file sets up the connection to the database. Everything else in the
backend that needs to talk to Postgres goes through what is defined here.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

# falls back to a local default so the app can still start during quick
# testing even if the env variable is not set, though in practice
# DATABASE_URL always gets set through docker compose or the .env file
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://anime_user:anime_pass@localhost:5432/anime_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """
    FastAPI dependency for getting a database session inside a route.
    Opens a new session, hands it to the route function, then makes sure
    it gets closed afterward even if the route raises an error along the way.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()