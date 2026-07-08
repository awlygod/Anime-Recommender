# API Documentation

The backend is built using FastAPI.

## Base URL

```
http://localhost:8000
```

## Interactive Documentation

Swagger UI

```
http://localhost:8000/docs
```

FastAPI also generates ReDoc automatically at the standard path, though this project primarily uses Swagger during development and testing.

```
http://localhost:8000/redoc
```

## Endpoints

### Search Anime

**GET** `/animes`

Searches anime by name using a partial, case insensitive match. Used by the frontend search bar for autocomplete as the user types.

Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| q | string | no | Partial anime title to search for. If omitted, returns the first rows up to the limit. |
| limit | integer | no | Maximum number of results to return. Defaults to 10. |

Example Request

```
GET /animes?q=naruto&limit=5
```

Example Response

```json
[
  {
    "id": 20,
    "name": "Naruto",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Moments prior to Naruto Uzumaki's birth...",
    "type": "TV",
    "episodes": "220.0",
    "score": 7.99,
    "popularity": 8,
    "image_url": "https://cdn.myanimelist.net/images/anime/13/17405.jpg"
  }
]
```

---

### Get Single Anime

**GET** `/animes/{anime_id}`

Returns full details for a single anime by its id. Used after a user selects a result from search.

Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| anime_id | integer | yes | The unique id of the anime. |

Example Request

```
GET /animes/20
```

Example Response

```json
{
  "id": 20,
  "name": "Naruto",
  "genres": "Action, Adventure, Fantasy",
  "synopsis": "Moments prior to Naruto Uzumaki's birth...",
  "type": "TV",
  "episodes": "220.0",
  "score": 7.99,
  "popularity": 8,
  "image_url": "https://cdn.myanimelist.net/images/anime/13/17405.jpg"
}
```

---

### Generate Recommendations

**POST** `/recommend`

The main endpoint of the application. Accepts any combination of an anime id, genres, and a type, and returns ranked recommendations using whichever strategy fits the input, content based, preference based, or combined.

Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| anime_id | integer | no | Id of an anime to base content based recommendations on. |
| genres | array of strings | no | One or more genres to filter and rank by. |
| type | string | no | Anime type to filter by, for example TV, Movie, OVA. |
| top_n | integer | no | How many results to return. Defaults to 10. |

At least one of anime_id, genres, or type should be provided for a meaningful result. The frontend enforces this before sending the request, but the field is technically optional at the schema level since all three modes share this one endpoint.

Example Request, content based only

```json
{
  "anime_id": 20,
  "top_n": 5
}
```

Example Request, preference based only

```json
{
  "genres": ["Action"],
  "type": "TV",
  "top_n": 5
}
```

Example Request, combined

```json
{
  "anime_id": 20,
  "genres": ["Action"],
  "top_n": 5
}
```
Example Response, content based, anime_id 20

```json
[
  {
    "id": 55453,
    "name": "Naruto (2023)",
    "genres": "Action, Adventure, Comedy, Fantasy",
    "synopsis": "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi ...",
    "type": "TV",
    "episodes": "UNKNOWN",
    "score": 0,
    "popularity": 0,
    "image_url": "https://cdn.myanimelist.net/images/anime/1587/136098.jpg",
    "match_score": 0.999
  },
  {
    "id": 34566,
    "name": "Boruto: Naruto Next Generations",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Following the successful end of the Fourth Shinobi World War, Konohagakure has been ...",
    "type": "TV",
    "episodes": "293.0",
    "score": 6.06,
    "popularity": 193,
    "image_url": "https://cdn.myanimelist.net/images/anime/1091/99847.jpg",
    "match_score": 0.47
  },
  {
    "id": 13667,
    "name": "Naruto: Shippuuden Movie 6 - Road to Ninja",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Returning home to Konohagakure, the young ninja celebrate defeating a group of ...",
    "type": "Movie",
    "episodes": "1.0",
    "score": 7.68,
    "popularity": 659,
    "image_url": "https://cdn.myanimelist.net/images/anime/1620/94336.jpg",
    "match_score": 0.451
  },
  {
    "id": 1735,
    "name": "Naruto: Shippuuden",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "It has been two and a half years since Naruto Uzumaki left Konohagakure, the Hidden ...",
    "type": "TV",
    "episodes": "500.0",
    "score": 8.26,
    "popularity": 15,
    "image_url": "https://cdn.myanimelist.net/images/anime/1565/111305.jpg",
    "match_score": 0.424
  },
  {
    "id": 8246,
    "name": "Naruto: Shippuuden Movie 4 - The Lost Tower",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Led by Yamato, Naruto Uzumaki, Sakura Haruno, and Sai are assigned to capture Mukade, a rogue ...",
    "type": "Movie",
    "episodes": "1.0",
    "score": 7.42,
    "popularity": 916,
    "image_url": "https://cdn.myanimelist.net/images/anime/1479/116734.jpg",
    "match_score": 0.408
  }
]
```

Example Response, preference based, genres Action, type TV

```json
[
  {
    "id": 5114,
    "name": "Fullmetal Alchemist: Brotherhood",
    "genres": "Action, Adventure, Drama, Fantasy",
    "synopsis": "After a horrific alchemy experiment goes wrong in the Elric household, brothers Edward ...",
    "type": "TV",
    "episodes": "64.0",
    "score": 9.1,
    "popularity": 3,
    "image_url": "https://cdn.myanimelist.net/images/anime/1208/94745.jpg",
    "match_score": 0.91
  },
  {
    "id": 41467,
    "name": "Bleach: Sennen Kessen-hen",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Substitute Soul Reaper Ichigo Kurosaki spends his days fighting against Hollows, dangerous evil ...",
    "type": "TV",
    "episodes": "13.0",
    "score": 9.07,
    "popularity": 464,
    "image_url": "https://cdn.myanimelist.net/images/anime/1908/135431.jpg",
    "match_score": 0.907
  },
  {
    "id": 28977,
    "name": "Gintama°",
    "genres": "Action, Comedy, Sci-Fi",
    "synopsis": "Gintoki, Shinpachi, and Kagura return as the fun-loving but broke members of the Yorozuya team! ...",
    "type": "TV",
    "episodes": "51.0",
    "score": 9.06,
    "popularity": 331,
    "image_url": "https://cdn.myanimelist.net/images/anime/3/72078.jpg",
    "match_score": 0.906
  },
  {
    "id": 38524,
    "name": "Shingeki no Kyojin Season 3 Part 2",
    "genres": "Action, Drama",
    "synopsis": "Seeking to restore humanity's diminishing hope, the Survey Corps embark on a mission to retake Wall ...",
    "type": "TV",
    "episodes": "10.0",
    "score": 9.05,
    "popularity": 24,
    "image_url": "https://cdn.myanimelist.net/images/anime/1517/100633.jpg",
    "match_score": 0.905
  },
  {
    "id": 11061,
    "name": "Hunter x Hunter (2011)",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Hunters devote themselves to accomplishing hazardous tasks, all from traversing the world's ...",
    "type": "TV",
    "episodes": "148.0",
    "score": 9.04,
    "popularity": 10,
    "image_url": "https://cdn.myanimelist.net/images/anime/1337/99013.jpg",
    "match_score": 0.904
  }
]
```

Example Response, combined, anime_id 20 and genres Action

```json
[
  {
    "id": 55453,
    "name": "Naruto (2023)",
    "genres": "Action, Adventure, Comedy, Fantasy",
    "synopsis": "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed ...",
    "type": "TV",
    "episodes": "UNKNOWN",
    "score": 0,
    "popularity": 0,
    "image_url": "https://cdn.myanimelist.net/images/anime/1587/136098.jpg",
    "match_score": 0.999
  },
  {
    "id": 34566,
    "name": "Boruto: Naruto Next Generations",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Following the successful end of the Fourth Shinobi World War, Konohagakure has been enjoying ...",
    "type": "TV",
    "episodes": "293.0",
    "score": 6.06,
    "popularity": 193,
    "image_url": "https://cdn.myanimelist.net/images/anime/1091/99847.jpg",
    "match_score": 0.47
  },
  {
    "id": 13667,
    "name": "Naruto: Shippuuden Movie 6 - Road to Ninja",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Returning home to Konohagakure, the young ninja celebrate defeating a group of supposed ...",
    "type": "Movie",
    "episodes": "1.0",
    "score": 7.68,
    "popularity": 659,
    "image_url": "https://cdn.myanimelist.net/images/anime/1620/94336.jpg",
    "match_score": 0.451
  },
  {
    "id": 1735,
    "name": "Naruto: Shippuuden",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "It has been two and a half years since Naruto Uzumaki left Konohagakure, the Hidden ...",
    "type": "TV",
    "episodes": "500.0",
    "score": 8.26,
    "popularity": 15,
    "image_url": "https://cdn.myanimelist.net/images/anime/1565/111305.jpg",
    "match_score": 0.424
  },
  {
    "id": 8246,
    "name": "Naruto: Shippuuden Movie 4 - The Lost Tower",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Led by Yamato, Naruto Uzumaki, Sakura Haruno, and Sai are assigned to capture Mukade, a rogue ...",
    "type": "Movie",
    "episodes": "1.0",
    "score": 7.42,
    "popularity": 916,
    "image_url": "https://cdn.myanimelist.net/images/anime/1479/116734.jpg",
    "match_score": 0.408
  }
]

```

---

### Health Check

**GET** `/health`

Simple endpoint to confirm the backend is running and able to accept requests.

Example Request

```
GET /health
```

Example Response

```json
{
  "status": "ok"
}
```

## Validation

All incoming requests to `/recommend` are validated using Pydantic through the RecommendRequest schema.

Validation covers.

Correct types for each field, anime_id as an integer, genres as an array of strings, type as a string, top_n as an integer.

Missing fields are allowed since every field in RecommendRequest is optional, but an incorrect type for a provided field, for example sending genres as a single string instead of an array, will be rejected.

If validation fails, FastAPI returns a 422 response with details about which field failed and why, without the request ever reaching the recommendation logic.