import { useState } from "react";
import { addToWishlist, removeFromWishlist } from "../api/client";

/**
 * Full detail popup for a single anime, shown when Know More is clicked.
 * Includes the full synopsis and a button to add or remove the anime
 * from the wishlist.
 */
export default function AnimeDetailModal({ anime, onClose, isWishlisted, onWishlistChange }) {
  const [saving, setSaving] = useState(false);

  if (!anime) return null;

  async function handleWishlistClick() {
    setSaving(true);
    try {
      if (isWishlisted) {
        await removeFromWishlist(anime.id);
        onWishlistChange(anime.id, false);
      } else {
        await addToWishlist(anime.id);
        onWishlistChange(anime.id, true);
      }
    } catch (error) {
      console.error(error);
    } finally {
      setSaving(false);
    }
  }

  const score = anime.score && anime.score > 0 ? anime.score.toFixed(1) : "N/A";

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(event) => event.stopPropagation()}>
        <button type="button" className="modal-close" onClick={onClose}>
          Close
        </button>

        {anime.image_url && <img src={anime.image_url} alt={anime.name} className="modal-image" />}

        <h2>{anime.name}</h2>
        <p className="genres">{anime.genres}</p>
        <p className="score">Score: {score}</p>
        <p className="type">Type: {anime.type} | Episodes: {anime.episodes}</p>

        <h3>Synopsis</h3>
        <p className="synopsis">{anime.synopsis}</p>

        <button
          type="button"
          className={isWishlisted ? "wishlist-btn active" : "wishlist-btn"}
          onClick={handleWishlistClick}
          disabled={saving}
        >
          {isWishlisted ? "Remove from Wishlist" : "Add to Wishlist"}
        </button>
      </div>
    </div>
  );
}