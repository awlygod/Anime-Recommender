# Usage Guide

This guide explains how to use AnimeMatch to get anime recommendations based on what you already like, your preferences, or both.

## Getting Started

Before using the application, ensure all services are running. If you have not installed the project yet, follow the [Installation Guide](./INSTALL.md).

Open your browser and navigate to.

```
http://localhost:3000
```

## Getting Recommendations

1. Open the AnimeMatch application.
2. Search for an anime you already enjoy using the search bar, and select it from the dropdown, or skip this if you only want preference based results.
3. Select one or more genres and, optionally, a type such as TV, Movie, or OVA, using the filters below the search bar.
4. Click the **Get recommendations** button.
5. Wait for the recommendation engine to process your request.
6. Browse the returned anime cards.
7. Clear your selected anime at any time and start a new search if you want different results.

## User Inputs

The recommendation engine generates results based on the following information.

| Input | Description |
|-------|-------------|
| Selected Anime | An anime you already like, used to find similar titles |
| Genres | One or more genres to filter and rank results by |
| Type | TV, Movie, OVA, ONA, or Special |
| Result Count | Fixed at 10 results per request in the current UI |

You do not need to provide all of these. Providing just a selected anime, just genres and type, or a combination of both are all valid ways to use the app, and each one triggers a different mode in the recommendation engine.

## How Recommendations Are Generated

After clicking Get recommendations, the application follows the workflow below.

1. The React frontend sends whatever you selected to the FastAPI backend.
2. FastAPI validates the incoming request using Pydantic.
3. The backend checks what was provided, a selected anime, preferences, or both, and picks the matching strategy.
4. If an anime was selected, the content based engine compares it against every other anime in the dataset using TF IDF and cosine similarity.
5. If preferences were set, the preference based engine filters and ranks anime by genre, type, and score.
6. If both were provided, the content based results are narrowed down further by the given preferences.
7. The ranked results are returned to the frontend as JSON.
8. The recommended anime are displayed as a grid of cards for you to browse.

## Recommendation Criteria

The recommendation engine considers different factors depending on the mode being used.

For content based recommendations.

Genre overlap with the selected anime.

Synopsis text similarity with the selected anime.

For preference based recommendations.

Genre match against your selected genres.

Type match against your selected type.

Overall score, used to rank matching results.

By combining these, AnimeMatch generates recommendations tailored to what you actually asked for instead of showing the same popular titles to every user.

## Viewing the Results

Once recommendations are generated, each card in the results grid shows.

The anime's poster image.

Its title and genres.

Its score, or N/A if the original dataset did not have one recorded.

A match percentage, reflecting either similarity to your selected anime or a normalized version of the anime's own score, depending on which mode produced that result.

You can scroll through all returned results without submitting the form again, and you can adjust your search or preferences and click Get recommendations again at any time to get a new set of results.

## Testing the Backend Directly

The backend provides interactive API documentation through Swagger UI.

Open.

```
http://localhost:8000/docs
```

Swagger UI allows you to test every API endpoint, search, recommend, and health, without using the frontend application at all. This is useful for confirming the recommendation logic is working correctly independent of the UI.

Full endpoint details and example requests are documented in [API.md](./API.md).

## Input Validation

All incoming requests to the recommend endpoint are validated using Pydantic.

Examples of validation include.

Incorrect data types, for example sending genres as a plain string instead of a list.

Malformed request bodies.

If validation fails, the API returns a 422 response with details about which field caused the failure, rather than passing invalid data into the recommendation logic.