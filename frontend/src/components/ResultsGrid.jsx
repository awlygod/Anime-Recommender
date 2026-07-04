import AnimeCard from "./AnimeCard";

/**
 * Renders a grid of AnimeCard results, or an empty/loading state.
 */
export default function ResultsGrid({ results, loading }) {
  if (loading) return <p className="status-text">Loading recommendations...</p>;
  if (!results || results.length === 0) {
    return <p className="status-text">No results yet — search an anime or pick preferences above.</p>;
  }

  return (
    <div className="results-grid">
      {results.map((anime) => (
        <AnimeCard key={anime.id} anime={anime} />
      ))}
    </div>
  );
}