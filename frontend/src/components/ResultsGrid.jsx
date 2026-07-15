import AnimeCard from "./AnimeCard";

/**
 * Shows the actual recommendation results as a grid of cards. Passes the
 * onKnowMore handler down to each card so clicking it opens that anime's
 * detail modal.
 */
export default function ResultsGrid({ results, loading, onKnowMore }) {
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
        <AnimeCard key={anime.id} anime={anime} onKnowMore={onKnowMore} />
      ))}
    </div>
  );
}