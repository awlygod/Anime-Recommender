"""
Content-based recommendation using TF-IDF + cosine similarity.

We vectorize each anime's genres + synopsis into a TF-IDF representation,
then for a given anime, compute cosine similarity between its vector and
every other anime's vector on demand. This avoids storing a full NxN
similarity matrix in memory (which becomes huge on large datasets).
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentRecommender:
    def __init__(self, animes: list[dict]):
        """
        animes: list of dicts with at least 'id', 'genres', 'synopsis'.
        Builds the TF-IDF matrix once at startup.
        """
        self.df = pd.DataFrame(animes)
        self.df["text"] = (self.df["genres"].fillna("") + " " + self.df["synopsis"].fillna(""))
        self.vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["text"])
        self.id_to_index = {row.id: idx for idx, row in self.df.iterrows()}

    def get_similar(self, anime_id: int, top_n: int = 10) -> list[tuple[int, float]]:
        """Returns [(anime_id, similarity_score), ...] sorted by similarity, excluding itself."""
        if anime_id not in self.id_to_index:
            return []

        idx = self.id_to_index[anime_id]
        query_vector = self.tfidf_matrix[idx]
        scores = cosine_similarity(query_vector, self.tfidf_matrix).flatten()

        ranked = sorted(
            ((int(self.df.iloc[i].id), float(score)) for i, score in enumerate(scores) if i != idx),
            key=lambda pair: pair[1],
            reverse=True,
        )
        return ranked[:top_n]