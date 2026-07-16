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
    "synopsis": "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order...",
    "type": "TV",
    "episodes": "220.0",
    "score": 7.99,
    "popularity": 8,
    "image_url": "https://cdn.myanimelist.net/images/anime/13/17405.jpg"
  },
  {
    "id": 442,
    "name": "Naruto Movie 1: Dai Katsugeki!! Yuki Hime Shinobu Houjou Dattebayo!",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Naruto Uzumaki and his squadmates, Sasuke Uchiha and Sakura Haruno, are sent on a mission to escort a movie crew on its way to film in the Land of Snow. They soon find out that they are ...",
    "type": "Movie",
    "episodes": "1.0",
    "score": 7.11,
    "popularity": 786,
    "image_url": "https://cdn.myanimelist.net/images/anime/1231/134484.jpg"
  },
  {
    "id": 594,
    "name": "Naruto: Takigakure no Shitou - Ore ga Eiyuu Dattebayo!",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "After safely escorting the cowardly Takigakure leader Shibuki to his homeland, Naruto Uzumaki, Sasuke Uchiha, and Sakura Haruno are taken aback by the village's sudden invasion of rogue ...",
    "type": "Special",
    "episodes": "1.0",
    "score": 6.76,
    "popularity": 2102,
    "image_url": "https://cdn.myanimelist.net/images/anime/11/20921.jpg"
  },
  {
    "id": 761,
    "name": "Naruto: Akaki Yotsuba no Clover wo Sagase",
    "genres": "Adventure, Comedy",
    "synopsis": "When Konohamaru Sarutobi asks Naruto Uzumaki for help, the latter readily accepts to join his young friend on a special mission—the retrieval of the legendary crimson four-leaf ...",
    "type": "Special",
    "episodes": "1.0",
    "score": 6.56,
    "popularity": 2152,
    "image_url": "https://cdn.myanimelist.net/images/anime/12/11240.jpg"
  },
  {
    "id": 936,
    "name": "Naruto Movie 2: Dai Gekitotsu! Maboroshi no Chiteiiseki Dattebayo!",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "In a tumultuous effort, the Sunagakure ninjas attempt to repel an unforeseen invasion of mysterious armored warriors on the Land of Wind. Shortly afterwards, the same armored ...",
    "type": "Movie",
    "episodes": "1.0",
    "score": 6.87,
    "popularity": 981,
    "image_url": "https://cdn.myanimelist.net/images/anime/1114/134485.jpg"
  },
  {
    "id": 1074,
    "name": "Naruto Narutimate Hero 3: Tsuini Gekitotsu! Jounin vs. Genin!! Musabetsu Dairansen Taikai Kaisai!!",
    "genres": "Action",
    "synopsis": "Konohagakure hosts a special tournament for ninjas of all ranks, stirring up fervor among the rookies who are eager to prove themselves in a competition against their superiors. Additionally, the ...",
    "type": "OVA",
    "episodes": "1.0",
    "score": 6.78,
    "popularity": 2249,
    "image_url": "https://cdn.myanimelist.net/images/anime/10/11244.jpg"
  },
  {
    "id": 1735,
    "name": "Naruto: Shippuuden",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "It has been two and a half years since Naruto Uzumaki left Konohagakure, the Hidden Leaf Village, for intense training following events which fueled his desire to be stronger. Now Akatsuki, the ...",
    "type": "TV",
    "episodes": "500.0",
    "score": 8.26,
    "popularity": 15,
    "image_url": "https://cdn.myanimelist.net/images/anime/1565/111305.jpg"
  },
  {
    "id": 2144,
    "name": "Naruto Movie 3: Dai Koufun! Mikazuki Jima no Animaru Panikku Dattebayo!",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "Led by Kakashi Hatake, Naruto Uzumaki, Sakura Haruno, and Rock Lee are tasked to escort the extravagant Prince Michiru Tsuki and his spoiled son Hikaru to the prosperous Land of Moon when ...",
    "type": "Movie",
    "episodes": "1.0",
    "score": 6.92,
    "popularity": 1108,
    "image_url": "https://cdn.myanimelist.net/images/anime/1918/134487.jpg"
  },
  {
    "id": 2248,
    "name": "Naruto: Dai Katsugeki!! Yuki Hime Shinobu Houjou Dattebayo! - Konoha no Sato no Dai Undoukai",
    "genres": "Action, Comedy, Fantasy",
    "synopsis": "The Konohagakure Grand Sports Festival has begun with all ninja squads vying for the ultimate prize—a whole week of paid leave! Despite his enthusiasm to achieve victory alongside Sasuke Uchiha...",
    "type": "Special",
    "episodes": "1.0",
    "score": 6.86,
    "popularity": 2303,
    "image_url": "https://cdn.myanimelist.net/images/anime/1/2473.jpg"
  },
  {
    "id": 2472,
    "name": "Naruto: Shippuuden Movie 1",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "A group of ninja is planning to revive a powerful demon, and once its spirit is reunited with its body, the world will be destroyed. The only way to prevent this from happening is for ...",
    "type": "Movie",
    "episodes": "1.0",
    "score": 7.29,
    "popularity": 783,
    "image_url": "https://cdn.myanimelist.net/images/anime/1703/134493.jpg"
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
    "synopsis": "Moments prior to Naruto Uzumaki's birth...",
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
    "synopsis": "Following the successful end of the Fourth Shinobi World War...",
    "type": "TV",
    "episodes": "293.0",
    "score": 6.06,
    "popularity": 193,
    "image_url": "https://cdn.myanimelist.net/images/anime/1091/99847.jpg",
    "match_score": 0.47
  }
]
```

The 2023 remake of Naruto comes back as an almost perfect match, 0.999, since its genres and synopsis are nearly identical in wording to the original. Notice its score and popularity both show as 0, this is the UNKNOWN placeholder handling described in the Dataset Preparation section of the main README, not a real rating, so the frontend displays this as N/A rather than a literal zero.

Example Response, preference based, genres Action, type TV

```json
[
  {
    "id": 5114,
    "name": "Fullmetal Alchemist: Brotherhood",
    "genres": "Action, Adventure, Drama, Fantasy",
    "synopsis": "After a horrific alchemy experiment goes wrong in the Elric household...",
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
    "synopsis": "Substitute Soul Reaper Ichigo Kurosaki spends his days fighting against Hollows...",
    "type": "TV",
    "episodes": "13.0",
    "score": 9.07,
    "popularity": 464,
    "image_url": "https://cdn.myanimelist.net/images/anime/1908/135431.jpg",
    "match_score": 0.907
  }
]
```

With no anime selected, this mode simply filters to Action, TV entries and ranks by score, which is why the two highest rated titles in that category come back first. Here match_score is the anime's own score normalized into a 0 to 1 range, not a similarity measurement.

Example Response, combined, anime_id 20 and genres Action

```json

[
  {
    "id": 55453,
    "name": "Naruto (2023)",
    "genres": "Action, Adventure, Comedy, Fantasy",
    "synopsis": "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the village, the ...",
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
    "synopsis": "Following the successful end of the Fourth Shinobi World War, Konohagakure has been enjoying a period of peace, prosperity, and extraordinary technological advancement. This is all due to the efforts of the Allied Shinobi Forces ...",
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
    "synopsis": "Returning home to Konohagakure, the young ninja celebrate defeating a group of supposed Akatsuki members. Naruto Uzumaki and Sakura Haruno, however, feel differently. Naruto is jealous of his comrades' congratulatory families, wishing for the presence of his ...",
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
    "synopsis": "It has been two and a half years since Naruto Uzumaki left Konohagakure, the Hidden Leaf Village, for intense training following events which fueled his desire to be stronger. Now Akatsuki, the mysterious organization of elite rogue ninja, is closing ...",
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
    "synopsis": "Led by Yamato, Naruto Uzumaki, Sakura Haruno, and Sai are assigned to capture Mukade, a rogue ninja who is pursuing the ancient chakra Ryuumyaku located underneath the Rouran ruins. While the Ryuumyaku has been sealed by the Fourth Hokage, the group ...",
    "type": "Movie",
    "episodes": "1.0",
    "score": 7.42,
    "popularity": 916,
    "image_url": "https://cdn.myanimelist.net/images/anime/1479/116734.jpg",
    "match_score": 0.408
  }
]

```

The match_score field means slightly different things depending on the mode. In content based and combined mode, it is the cosine similarity score between the selected anime and the result, ranging from 0 to 1. In pure preference based mode, there is no similarity being measured, so match_score is instead the anime's own score normalized down to a 0 to 1 range, just to keep the response shape consistent across all three modes.

---

### Get Wishlist

**GET** `/wishlist`

Returns every anime currently saved to the wishlist, most recently added first. Joins the wishlist table with the anime table so the frontend gets full anime details back in a single call.

Example Request

```
GET /wishlist
```

Example Response

```json
[
  {
    "id": 28755,
    "name": "Boruto: Naruto the Movie",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "The spirited Boruto Uzumaki, son of Seventh Hokage Naruto, is a skilled ninja who possesses the same brashness and passion his father once had. However, the constant absence of his father, who is busy with his Hokage duties, puts ...",
    "type": "Movie",
    "episodes": "1.0",
    "score": 7.4,
    "popularity": 463,
    "image_url": "https://cdn.myanimelist.net/images/anime/4/78280.jpg",
    "added_at": "2026-07-16T08:01:36.318126"
  },
  {
    "id": 1735,
    "name": "Naruto: Shippuuden",
    "genres": "Action, Adventure, Fantasy",
    "synopsis": "It has been two and a half years since Naruto Uzumaki left Konohagakure, the Hidden Leaf Village, for intense training following events which fueled his desire to be stronger. Now Akatsuki, the mysterious organization of elite rogue ninja, is ...",
    "type": "TV",
    "episodes": "500.0",
    "score": 8.26,
    "popularity": 15,
    "image_url": "https://cdn.myanimelist.net/images/anime/1565/111305.jpg",
    "added_at": "2026-07-16T08:01:27.964457"
  },
  {
    "id": 55453,
    "name": "Naruto (2023)",
    "genres": "Action, Adventure, Comedy, Fantasy",
    "synopsis": "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the ...",
    "type": "TV",
    "episodes": "UNKNOWN",
    "score": 0,
    "popularity": 0,
    "image_url": "https://cdn.myanimelist.net/images/anime/1587/136098.jpg",
    "added_at": "2026-07-16T08:01:23.692423"
  }
]
```

---

### Add To Wishlist

**POST** `/wishlist`

Adds an anime to the wishlist. If it has already been added before, the existing entry is returned instead of creating a duplicate, since anime_id is unique on the wishlist table. Returns a 404 if the given anime_id does not exist.

Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| anime_id | integer | yes | Id of the anime to save to the wishlist. |

Example Request

```json
{
  "anime_id": 41467
}
```

Example Response

```json
{
  "id": 41467,
  "name": "Bleach: Sennen Kessen-hen",
  "genres": "Action, Adventure, Fantasy",
  "synopsis": "Substitute Soul Reaper Ichigo Kurosaki spends his days fighting against Hollows, dangerous ...",
  "type": "TV",
  "episodes": "13.0",
  "score": 9.07,
  "popularity": 464,
  "image_url": "https://cdn.myanimelist.net/images/anime/1908/135431.jpg",
  "added_at": "2026-07-16T08:24:24.307881"
}
```

---

### Remove From Wishlist

**DELETE** `/wishlist/{anime_id}`

Removes an anime from the wishlist by its id. Safe to call even if the anime was never added, in which case nothing happens and a normal response is still returned.

Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| anime_id | integer | yes | Id of the anime to remove from the wishlist. |

Example Request

```
DELETE /wishlist/20
```

Example Response

```json
{
  "status": "ok"
}
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