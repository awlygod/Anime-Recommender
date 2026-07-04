import { useState } from "react";

const GENRE_OPTIONS = [
  "Action", "Adventure", "Comedy", "Drama", "Fantasy",
  "Horror", "Mystery", "Romance", "Sci-Fi", "Slice of Life", "Sports",
];

const TYPE_OPTIONS = ["TV", "Movie", "OVA", "ONA", "Special"];

/**
 * Lets the user pick genres and a type to drive preference-based recommendations.
 * Calls onChange({genres, type}) whenever selections change.
 */
export default function PreferenceFilters({ onChange }) {
  const [selectedGenres, setSelectedGenres] = useState([]);
  const [selectedType, setSelectedType] = useState("");

  const toggleGenre = (genre) => {
    const updated = selectedGenres.includes(genre)
      ? selectedGenres.filter((g) => g !== genre)
      : [...selectedGenres, genre];
    setSelectedGenres(updated);
    onChange({ genres: updated, type: selectedType });
  };

  const handleTypeChange = (e) => {
    const value = e.target.value;
    setSelectedType(value);
    onChange({ genres: selectedGenres, type: value });
  };

  return (
    <div className="preference-filters">
      <div className="genre-chips">
        {GENRE_OPTIONS.map((genre) => (
          <button
            key={genre}
            className={selectedGenres.includes(genre) ? "chip active" : "chip"}
            onClick={() => toggleGenre(genre)}
            type="button"
          >
            {genre}
          </button>
        ))}
      </div>

      <select value={selectedType} onChange={handleTypeChange}>
        <option value="">Any type</option>
        {TYPE_OPTIONS.map((t) => (
          <option key={t} value={t}>{t}</option>
        ))}
      </select>
    </div>
  );
}