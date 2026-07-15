import { useState } from "react";
import SearchBar from "../components/SearchBar";
import PreferenceFilters from "../components/PreferenceFilters";
import ResultsGrid from "../components/ResultsGrid";
import AnimeDetailModal from "../components/AnimeDetailModal";
import { getRecommendations } from "../api/client";

/**
 * Main page of the application.
 *
 * It manages the user's selections, requests recommendations from the
 * backend, displays the returned results, and handles opening the detail
 * modal for any result.
 */
export default function Home({ onOpenWishlist }) {
  const [selectedAnime, setSelectedAnime] = useState(null);
  const [preferences, setPreferences] = useState({ genres: [], type: "" });
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const [modalAnime, setModalAnime] = useState(null);
  const [wishlistedIds, setWishlistedIds] = useState(new Set());

  async function handleGetRecommendations() {
    const hasNoInput =
      !selectedAnime &&
      preferences.genres.length === 0 &&
      !preferences.type;

    if (hasNoInput) {
      setError("Pick an anime or select at least one preference first.");
      return;
    }

    setError(null);
    setLoading(true);

    try {
      const data = await getRecommendations({
        anime_id: selectedAnime?.id,
        genres: preferences.genres,
        type: preferences.type,
        top_n: 10,
      });

      setResults(data);
    } catch (error) {
      console.error(error);
      setError("Something went wrong fetching recommendations.");
    } finally {
      setLoading(false);
    }
  }

  function handleWishlistChange(animeId, isNowWishlisted) {
    setWishlistedIds((current) => {
      const updated = new Set(current);
      if (isNowWishlisted) {
        updated.add(animeId);
      } else {
        updated.delete(animeId);
      }
      return updated;
    });
  }

  return (
    <div className="home-page">
      <div className="top-bar">
        <h1>AnimeMatch</h1>
        <button type="button" className="btn btn-dark" onClick={onOpenWishlist}>
          Wishlist
        </button>
      </div>

      <div className="content">
        <div className="page-header">
          <div>
            <h2>Find your next anime</h2>
            <p className="subtitle">
              Search a title, set preferences, or both
            </p>
          </div>
        </div>

        <SearchBar
          onSelect={setSelectedAnime}
          selectedAnime={selectedAnime}
          onClear={() => setSelectedAnime(null)}
        />

        <PreferenceFilters onChange={setPreferences} />

        <div className="btn-row">
          <button
            className="recommend-btn"
            onClick={handleGetRecommendations}
          >
            Get recommendations
          </button>
        </div>

        {error && <p className="error-text">{error}</p>}

        {results.length === 0 && !loading ? (
          <div className="empty-state">
            <p className="main">No recommendations yet</p>
            <p className="sub">
              Search an anime or select preferences above
            </p>
          </div>
        ) : (
          <ResultsGrid
            results={results}
            loading={loading}
            onKnowMore={setModalAnime}
          />
        )}
      </div>

      <AnimeDetailModal
        anime={modalAnime}
        onClose={() => setModalAnime(null)}
        isWishlisted={modalAnime ? wishlistedIds.has(modalAnime.id) : false}
        onWishlistChange={handleWishlistChange}
      />
    </div>
  );
}