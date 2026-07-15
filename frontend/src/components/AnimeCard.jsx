/**
 * Displays a single anime result, poster, title, genres, score, match
 * percentage, and a button to open the full detail modal.
 */
export default function AnimeCard({ anime, onKnowMore }) {
  const score = anime.score && anime.score > 0 ? anime.score.toFixed(1) : "N/A";
  const matchPercent = anime.match_score ? Math.round(anime.match_score * 100) : null;

  return (
    <div className="anime-card">
      {anime.image_url && <img src={anime.image_url} alt={anime.name} />}
      <div className="anime-card-body">
        <h3>{anime.name}</h3>
        <p className="genres">{anime.genres}</p>
        <p className="score">Score: {score}</p>
        {matchPercent !== null && <p className="match">Match: {matchPercent}%</p>}
        <button type="button" className="know-more-btn" onClick={() => onKnowMore(anime)}>
          Know More
        </button>
      </div>
    </div>
  );
}