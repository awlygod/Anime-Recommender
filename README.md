# AnimeMatch ( Anime Recommendation System)

## Project Overview

Anime Recommender is a full stack web application that helps users discover new anime based on titles they already enjoy and preferences they choose. The application combines content based matching with preference based filtering to generate recommendations that feel more personal than a simple genre list.

The system is built using React for the frontend, FastAPI for the backend, and PostgreSQL for the database. The entire application runs through Docker, with each part of the system running in its own container.

## Why I Chose This Project

Finding a good anime to watch can be difficult because thousands of titles exist across many genres, formats, and eras. Most recommendation systems take one of two approaches. Either they suggest titles similar to something you already like, or they let you filter by genre and type without considering similarity at all.

I wanted to build something that does both at once. A user can pick an anime they already enjoy, set genre and type preferences, or combine the two together. Building this also gave me hands on experience with recommendation logic, REST API design, containerization with Docker, and connecting a real database to a full stack application.

## What Makes This Project Special

Instead of relying on a single matching method, this application supports three modes of recommendation depending on what the user provides.

If a user selects only an anime, the system finds other anime with similar genres and synopsis using text similarity.

If a user selects only preferences such as genre or type, the system filters and ranks anime according to those choices.

If both are provided, the application first finds anime similar to the selected title and then narrows that list down using the chosen preferences, producing results that are both similar and relevant to what the user actually wants.

## Features

* Live anime search with autocomplete.

* Genre based filtering.

* Type based filtering across TV, Movie, OVA, and other formats.

* Content based recommendations using TF IDF and cosine similarity.

* Preference based recommendations.

* A combined recommendation mode that merges both techniques.

* Fully containerized application using Docker.

* Clean, minimal, dark themed user interface.

## Technology Stack

### Backend

* Python

* FastAPI

* SQLAlchemy

* Pandas

* Scikit Learn

### Frontend

* React

* Vite

* Nginx

### Database

* PostgreSQL

### DevOps

* Docker

* Docker Compose

### Development Tools

* Visual Studio Code

* Git

* GitHub

## Project Architecture

```
                    User
                      |
                      |
                      v
               React Frontend
                      |
             REST API Requests
                      |
                      |
                      v
              FastAPI Backend
                      |
            Recommendation Engine
                      |
                      |
                      v
              PostgreSQL Database
```

The frontend never communicates with the database directly. Every request goes through the backend first, which keeps the system organized and easier to maintain.

## Documentation

Detailed documentation has been split into separate files for easier navigation.

[Installation Guide](./INSTALL.md)

[Usage Guide](./USAGE.md)

[API Documentation](./API.md)

## Project Structure

```
Anime-Recommender/
├── docker-compose.yml
├── README.md
├── INSTALL.md
├── USAGE.md
├── API.md
├── data/
│   └── anime_dataset_2023.csv
├── screenshots/
│   └── (screenshot images referenced in the README)
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── seed.py
│   ├── recommender/
│   │   ├── content_based.py
│   │   ├── preference_based.py
│   │   └── combined.py
│   └── routers/
│       ├── anime.py
│       └── recommend.py
└── frontend/
    ├── Dockerfile
    ├── nginx.conf
    ├── package.json
    └── src/
        ├── api/
        │   └── client.js
        ├── components/
        └── pages/
            └── Home.jsx
```

## How To Install

Full setup instructions, prerequisites, and troubleshooting for getting the project running are in [INSTALL.md](./INSTALL.md).

In short.

```bash
git clone https://github.com/awlygod/Anime-Recommender.git
cd Anime-Recommender
docker compose up --build
```

Then open http://localhost:3000.

## Application URLs

Frontend

```
http://localhost:3000
```

Backend API

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

Full manual setup steps for running without Docker are in [INSTALL.md](./INSTALL.md).

## Database Setup

The application uses PostgreSQL.

When Docker Compose is executed, the following happens automatically.

- The PostgreSQL container starts.

- The database and table are created.

- The backend checks whether the database already contains data.

- If the database is empty, the Kaggle dataset is imported.

- If data already exists, seeding is skipped so restarting the application never creates duplicate records.

- No manual database setup is required.

## How To Use

A full walkthrough of the interface, what each field does, and a worked example of a recommendation request is in [USAGE.md](./USAGE.md).

In short, search for an anime you like, set genre and type preferences, or do both, then click Get recommendations to see a ranked list of matching anime.

## Recommendation Engine Architecture

The recommendation engine supports three modes depending on what the user provides, and the backend decides which one to run without the frontend needing to specify a mode explicitly.

![Recommendation Engine Architecture](screenshots/archit.png)

### Content Based Matching

When a user selects a specific anime, the engine converts that anime's combined genres and synopsis text into a TF IDF vector, then computes cosine similarity between that vector and every other anime's vector in the dataset. The anime with the highest similarity scores, excluding itself, are returned as the closest matches.

This is computed on demand per request rather than precomputed for every possible pair of anime ahead of time, since storing a full similarity matrix for roughly twenty five thousand anime would use a large amount of memory for something only a fraction of which ever actually gets used in a given session.

### Preference Based Matching

When a user selects genres and or a type without picking a specific anime, the engine filters the anime table down to rows matching those criteria using a case insensitive genre match and an exact type match, then ranks the results by score, highest first.

### Combined Matching

When a user provides both an anime and preferences, the engine first pulls a wider pool of content based candidates than it normally would, since narrowing that pool down by genre and type afterward will reduce it further. It then filters that pool by the given genres and type, and ranks whatever remains by similarity score. This produces results that are both textually similar to the chosen anime and aligned with the user's stated preferences.

The user submits an anime, a set of preferences, or both. FastAPI receives the request and validates it. Depending on which fields were provided, one of the three strategies above runs, and the final ranked list is returned as JSON. React renders the results as a grid of anime cards.

Full request and response examples for every endpoint are in [API.md](./API.md).

## Data Flow

The full request flow, end to end, looks like this.

![Data Flow Diagram](screenshots/flow.png)



## API Endpoints

| Method | Endpoint | Description |
| ------- | -------- | ----------- |
| GET | /animes?q=\<search\>&limit=\<number\> | Search anime by name |
| GET | /animes/{id} | Get information about one anime |
| POST | /recommend | Generate recommendations |
| GET | /health | Check whether the backend is running |

Full request and response examples for every endpoint are in [API.md](./API.md).

## Dataset Preparation

This project uses the Anime Dataset 2023 from Kaggle, containing around twenty five thousand anime entries with details such as title, genres, synopsis, type, episodes, score, and popularity.

Before inserting the data, `seed.py` performs several preprocessing steps.

Missing genres and synopsis values are replaced with empty strings since they are required for the TF IDF vectorizer and cannot be null.

The score and popularity columns sometimes contain the text `UNKNOWN` instead of numbers. A helper function safely converts these values and falls back to `0` when conversion fails, which is why some anime appear with a score of `N/A` in the application.

The episodes field is stored as a string because it can also contain `UNKNOWN`, avoiding unnecessary conversion issues.

After cleaning, the dataset is inserted into a PostgreSQL table using SQLAlchemy bulk inserts for better performance. Before importing, the script checks whether data already exists and skips the process if the table is already populated, preventing duplicate records.

The cleaned dataset is imported automatically the first time the backend starts.


## Dataset Source

Dataset used, Anime Dataset 2023.

Source.

https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset

## Installation Files

The entire project can be started without any manual configuration.

* The docker-compose.yml file creates and connects all three services on a custom Docker network.

* The backend Dockerfile installs the Python environment and required packages.

* The frontend Dockerfile builds the React application and serves it through Nginx.

* The seed.py file automatically imports the dataset into PostgreSQL whenever the database is empty.

See [INSTALL.md](./INSTALL.md) for the full setup walkthrough.

## Docker Architecture

The project consists of three independent containers connected through a custom Docker network.

Frontend : built with React and served through Nginx.

Backend  : built with FastAPI and containing the recommendation engine.

Database : running PostgreSQL.

Docker Compose creates the network automatically and allows the three containers to communicate without any manual setup.

## Screenshots

### User Request Form
![Request Form](screenshots/User-Form.png)

### Combined Recommendations
![Combined](screenshots/Combined.png)

### Content Based Recommendations
![Content-Based](screenshots/conten-based.png)

### Preference Based Recommendations
![Preference Based](screenshots/Preference-based.png)

Running into an issue? Troubleshooting steps for common Docker and database problems are in [INSTALL.md](./INSTALL.md).

## Author

Suraj Tripathi

GitHub:  https://github.com/awlygod

## Acknowledgements

This project was developed as part of a technical recruitment assessment.

Open source technologies used, FastAPI, React, Docker, PostgreSQL, SQLAlchemy, Pydantic, Vite, Scikit Learn.

Thanks to Kaggle and the dataset author for making the Anime Dataset 2023 publicly available.

## Declaration

To be fully transparent, I used Claude/AI to help speed up parts of this project.

Debugging environment issues: diagnosing a `.gitignore` encoding problem on Windows that was silently preventing `.env` from being ignored, and working through a CORS mismatch caused by Vite's default dev port differing from the Docker port.

Data preprocessing: writing the fallback logic in `seed.py` that handles the literal `UNKNOWN` values present in the Kaggle dataset's score, episodes, and popularity fields, so they don't break the seeding process or the recommendation engine.

Proofreading: Checking grammar and formatting structure of the technical docs and comments.

Aside from that, the recommendation logic itself, content based matching using TF IDF and cosine similarity, preference based filtering, and the combined mode that merges both, the database schema, the React components, and the Docker network structure were built and understood by me.