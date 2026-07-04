import { useState } from "react";
import SearchBar from "../components/SearchBar";
import PreferenceFilters from "../components/PreferenceFilters";
import ResultsGrid from "../components/ResultsGrid";
import { getRecommendations } from "../api/client";

/**
 * Main page — ties together search (content-based), filters (preference-based),
 * and the combined recommendation call.
 */
export default function Home() {
  const [selectedAnime, setSelectedAnime] = useState(null);
  const [preferences, setPreferences] = useState({ genres: [], type: "" });
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleGetRecommendations = async () => {
    if (!selectedAnime && preferences.genres.length === 0 && !preferences.type) {
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
    } catch (err) {
      console.error(err);
      setError("Something went wrong fetching recommendations.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="home-page">
      <h1>Anime Recommender</h1>
      <p>Pick an anime you like, set preferences, or both — then get recommendations.</p>

      <SearchBar
        onSelect={setSelectedAnime}
        selectedAnime={selectedAnime}
        onClear={() => setSelectedAnime(null)}
      />

      <PreferenceFilters onChange={setPreferences} />

      <button className="recommend-btn" onClick={handleGetRecommendations}>
        Get recommendations
      </button>

      {error && <p className="error-text">{error}</p>}

      <ResultsGrid results={results} loading={loading} />
    </div>
  );
}