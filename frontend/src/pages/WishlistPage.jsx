import { useEffect, useState } from "react";
import { getWishlist, removeFromWishlist } from "../api/client";

/**
 * Shows every anime currently saved to the wishlist. Fetches fresh from
 * the backend each time this page opens, rather than relying on state
 * carried over from the Home page.
 */
export default function WishlistPage({ onBack }) {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadWishlist();
  }, []);

  async function loadWishlist() {
    setLoading(true);
    try {
      const data = await getWishlist();
      setItems(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  async function handleRemove(animeId) {
    try {
      await removeFromWishlist(animeId);
      setItems((current) => current.filter((item) => item.id !== animeId));
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className="home-page">
      <div className="top-bar">
        <h1>AnimeMatch</h1>
        <button type="button" className="btn btn-dark" onClick={onBack}>
          Back to Search
        </button>
      </div>

      <div className="content">
        <div className="page-header">
          <div>
            <h2>Your Wishlist</h2>
            <p className="subtitle">Anime you have saved to watch later</p>
          </div>
        </div>

        {loading ? (
          <p className="status-text">Loading your wishlist...</p>
        ) : items.length === 0 ? (
          <div className="empty-state">
            <p className="main">Your wishlist is empty</p>
            <p className="sub">Open any anime's details and add it to your wishlist</p>
          </div>
        ) : (
          <div className="results-grid">
            {items.map((anime) => (
              <div key={anime.id} className="anime-card">
                {anime.image_url && <img src={anime.image_url} alt={anime.name} />}
                <div className="anime-card-body">
                  <h3>{anime.name}</h3>
                  <p className="genres">{anime.genres}</p>
                  <button type="button" className="know-more-btn" onClick={() => handleRemove(anime.id)}>
                    Remove
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}