/**
 * API client — wraps all calls to the backend recommendation service.
 * Base URL comes from VITE_API_BASE_URL, set in .env (localhost for dev,
 * http://backend:8000 inside Docker Compose).
 */

const BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

/**
 * Searches anime by name substring, used for autocomplete.
 * @param {string} query - partial anime name
 * @param {number} limit - max results
 * @returns {Promise<Array<{id:number, name:string, genres:string, score:number, image_url:string}>>}
 */
export async function searchAnime(query, limit = 8) {
  const res = await fetch(`${BASE_URL}/animes?q=${encodeURIComponent(query)}&limit=${limit}`);
  if (!res.ok) throw new Error("Failed to search anime");
  return res.json();
}

/**
 * Gets recommendations based on any combination of anime_id, genres, and type.
 * @param {{anime_id?: number, genres?: string[], type?: string, top_n?: number}} params
 * @returns {Promise<Array<Object>>} list of anime with a match_score field
 */
export async function getRecommendations(params) {
  const body = {};
  if (params.anime_id) body.anime_id = params.anime_id;
  if (params.genres && params.genres.length > 0) body.genres = params.genres;
  if (params.type) body.type = params.type;
  body.top_n = params.top_n || 10;

  const res = await fetch(`${BASE_URL}/recommend`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error("Failed to fetch recommendations");
  return res.json();
}