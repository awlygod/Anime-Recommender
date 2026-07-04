import { useState } from "react";
import SearchBar from "../components/SearchBar";
import PreferenceFilters from "../components/PreferenceFilters";
import ResultsGrid from "../components/ResultsGrid";
import { getRecommendations } from "../api/client";

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
      <div className="top-bar">
        <h1>AnimeMatch</h1>
      </div>

      <div className="content">
        <div className="page-header">
          <div>
            <h2>Find your next anime</h2>
            <p className="subtitle">Search a title, set preferences, or both</p>
          </div>
        </div>

        <SearchBar
          onSelect={setSelectedAnime}
          selectedAnime={selectedAnime}
          onClear={() => setSelectedAnime(null)}
        />

        <PreferenceFilters onChange={setPreferences} />

        <div className="btn-row">
          <button className="recommend-btn" onClick={handleGetRecommendations}>
            Get recommendations
          </button>
        </div>

        {error && <p className="error-text">{error}</p>}

        {results.length === 0 && !loading ? (
          <div className="empty-state">
            <p className="main">No recommendations yet</p>
            <p className="sub">Search an anime or select preferences above</p>
          </div>
        ) : (
          <ResultsGrid results={results} loading={loading} />
        )}
      </div>
    </div>
  );
}