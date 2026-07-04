import { useState, useEffect, useRef } from "react";
import { searchAnime } from "../api/client";

/**
 * Autocomplete search for picking a base anime (content-based input).
 * Calls onSelect(anime) when the user picks a result.
 */
export default function SearchBar({ onSelect, selectedAnime, onClear }) {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const debounceRef = useRef(null);

  useEffect(() => {
    if (!query || query.length < 2) {
      setResults([]);
      return;
    }

    if (debounceRef.current) clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(async () => {
      setLoading(true);
      try {
        const data = await searchAnime(query);
        setResults(data);
      } catch (err) {
        console.error(err);
        setResults([]);
      } finally {
        setLoading(false);
      }
    }, 300);

    return () => clearTimeout(debounceRef.current);
  }, [query]);

  if (selectedAnime) {
    return (
      <div className="search-bar selected">
        <span>Selected: <strong>{selectedAnime.name}</strong></span>
        <button onClick={onClear}>Clear</button>
      </div>
    );
  }

  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Search an anime (e.g. Naruto)"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      {loading && <p>Searching...</p>}
      {results.length > 0 && (
        <ul className="search-results">
          {results.map((anime) => (
            <li
              key={anime.id}
              onClick={() => {
                onSelect(anime);
                setQuery("");
                setResults([]);
              }}
            >
              {anime.name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}