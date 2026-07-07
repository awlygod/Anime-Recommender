"""
Populate the database with anime data from the Kaggle dataset.

The script checks whether the database already contains data before
importing the CSV, making it safe to run multiple times.
"""

import pandas as pd

from database import Base, SessionLocal, engine
from models import Anime

CSV_PATH = "../data/anime_dataset_2023.csv"

# Maps the dataset column names to the Anime model fields.
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
    """
    Convert a value to a number.

    Some fields in the dataset contain values such as "UNKNOWN" instead
    of numeric data. When conversion fails, the provided default value
    is returned instead.
    """

    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def seed():
    """
    Load the dataset into the database.

    The required columns are renamed, cleaned, and inserted into the
    anime table. If the table already contains data, the import is
    skipped to avoid duplicate records.
    """

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    existing = db.query(Anime).count()

    if existing > 0:
        print(f"Database already seeded ({existing} rows). Skipping.")
        db.close()
        return

    df = pd.read_csv(CSV_PATH)

    df = df.rename(columns=COLUMN_MAP)

    df = df[
        [column for column in COLUMN_MAP.values() if column in df.columns]
    ]

    # Fill missing values and normalize fields before inserting them.
    df["genres"] = df["genres"].fillna("")
    df["synopsis"] = df["synopsis"].fillna("")
    df["score"] = df["score"].apply(lambda value: clean_numeric(value, 0.0))
    df["popularity"] = df["popularity"].apply(
        lambda value: int(clean_numeric(value, 0))
    )
    df["image_url"] = df.get("image_url", "").fillna("")
    df["episodes"] = df["episodes"].astype(str).fillna("")

    records = df.to_dict(orient="records")

    db.bulk_insert_mappings(Anime, records)
    db.commit()
    db.close()

    print(f"Seeded {len(records)} anime records.")


if __name__ == "__main__":
    seed()