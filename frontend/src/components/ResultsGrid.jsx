import AnimeCard from "./AnimeCard";

/**
 * Shows the actual recommendation results as a grid of cards. This one
 * component handles all three states the results area can be in, still
 * loading, no results yet, or a real list to show.
 */
export default function ResultsGrid({ results, loading }) {
  if (loading) {
    return <p className="status-text">Loading recommendations, please wait.</p>;
  }

  if (!results || results.length === 0) {
    return (
      <p className="status-text">
        No results yet. Search an anime or pick some preferences above.
      </p>
    );
  }

  return (
    <div className="results-grid">
      {results.map((anime) => (
        <AnimeCard key={anime.id} anime={anime} />
      ))}
    </div>
  );
}