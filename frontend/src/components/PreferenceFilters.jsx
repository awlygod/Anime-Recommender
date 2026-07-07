import { useState } from "react";

const GENRE_OPTIONS = [
  "Action",
  "Adventure",
  "Comedy",
  "Drama",
  "Fantasy",
  "Horror",
  "Mystery",
  "Romance",
  "Sci-Fi",
  "Slice of Life",
  "Sports",
];

const TYPE_OPTIONS = ["TV", "Movie", "OVA", "ONA", "Special"];

/**
 * The genre chips and type dropdown that drive preference based
 * recommendations. This is the part of the app that does not need any
 * specific anime picked, a user can just tap a few genres and get results.
 *
 * Every time something changes here, onChange gets called with the full
 * current selection, genres and type together, so the parent component
 * always has the latest state without needing to track it separately.
 */
export default function PreferenceFilters({ onChange }) {
  const [selectedGenres, setSelectedGenres] = useState([]);
  const [selectedType, setSelectedType] = useState("");

  function toggleGenre(genre) {
    const alreadySelected = selectedGenres.includes(genre);
    const updatedGenres = alreadySelected
      ? selectedGenres.filter((g) => g !== genre)
      : [...selectedGenres, genre];

    setSelectedGenres(updatedGenres);
    onChange({ genres: updatedGenres, type: selectedType });
  }

  function handleTypeChange(event) {
    const value = event.target.value;
    setSelectedType(value);
    onChange({ genres: selectedGenres, type: value });
  }

  return (
    <div className="preference-filters">
      <div className="genre-chips">
        {GENRE_OPTIONS.map((genre) => (
          <button
            key={genre}
            type="button"
            className={selectedGenres.includes(genre) ? "chip active" : "chip"}
            onClick={() => toggleGenre(genre)}
          >
            {genre}
          </button>
        ))}
      </div>

      <select value={selectedType} onChange={handleTypeChange}>
        <option value="">Any type</option>
        {TYPE_OPTIONS.map((type) => (
          <option key={type} value={type}>
            {type}
          </option>
        ))}
      </select>
    </div>
  );
}