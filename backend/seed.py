"""
Seeds the database from the Kaggle anime CSV.
Idempotent — skips if the table already has data.
Run once: python seed.py
"""

import pandas as pd
from database import engine, SessionLocal, Base
from models import Anime

CSV_PATH = "../data/anime_dataset_2023.csv"

# Map Kaggle column names -> our model fields.
# Adjust left-hand keys if your CSV's actual headers differ slightly.
COLUMN_MAP = {
    "anime_id": "id",
    "Name": "name",
    "Genres": "genres",
    "Synopsis": "synopsis",
    "Type": "type",
    "Episodes": "episodes",
    "Score": "score",
    "Popularity": "popularity",
    "Image URL": "image_url",
}


def clean_numeric(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    existing = db.query(Anime).count()
    if existing > 0:
        print(f"Database already seeded ({existing} rows). Skipping.")
        db.close()
        return

    df = pd.read_csv(CSV_PATH)
    df = df.rename(columns=COLUMN_MAP)
    df = df[[c for c in COLUMN_MAP.values() if c in df.columns]]

    df["genres"] = df["genres"].fillna("")
    df["synopsis"] = df["synopsis"].fillna("")
    df["score"] = df["score"].apply(lambda v: clean_numeric(v, 0.0))
    df["popularity"] = df["popularity"].apply(lambda v: int(clean_numeric(v, 0)))
    df["image_url"] = df.get("image_url", "").fillna("")
    df["episodes"] = df["episodes"].astype(str).fillna("")

    records = df.to_dict(orient="records")
    db.bulk_insert_mappings(Anime, records)
    db.commit()
    db.close()
    print(f"Seeded {len(records)} anime records.")


if __name__ == "__main__":
    seed()