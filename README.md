# Anime Recommender

Anime Recommender is a full stack web application that helps users discover new anime based on what they already enjoy and the preferences they choose. The application combines content similarity with user preferences to generate recommendations that feel more accurate and relevant.

The project is built using React for the frontend, FastAPI for the backend, PostgreSQL for storing the data, and Docker to run the complete application in separate containers.

# Why I Built This Project

Finding a good anime to watch can be difficult because thousands of titles are available across many different genres and formats. Most recommendation systems either suggest anime that are similar to one title or simply filter anime based on genres.

I wanted to build a system that combines both approaches. A user can choose an anime they already like, select genres or formats they prefer, or use both together. This creates recommendations that are much more personalized while also giving me practical experience working with recommendation systems, REST APIs, Docker, databases, and full stack development.

# System Architecture

The application is divided into three separate services that communicate with each other through a Docker network.

### Frontend

The frontend is developed using React and Vite. Once built, it is served using Nginx on port 3000. Users interact with the application through this interface.

### Backend

The backend is built with FastAPI and runs on port 8000. It receives requests from the frontend, searches the database, generates recommendations, and returns the results.

### Database

The application stores all anime information inside a PostgreSQL database running on port 5432.

The frontend never communicates directly with the database. Every request first goes to the backend, making the application more secure and easier to maintain.

When the application starts for the first time, the backend automatically loads the dataset into PostgreSQL and builds the recommendation model in memory.

# Design Decisions

## Combining Two Recommendation Methods

The application supports both content based recommendations and preference based recommendations.

If a user selects only an anime, the system finds other anime with similar descriptions and content.

If a user selects only preferences such as genres or type, the system recommends anime that satisfy those filters.

If both are provided, the application combines the two approaches and produces recommendations that are similar while also matching the user's preferences.

## TF IDF and Cosine Similarity

The recommendation engine uses TF IDF to convert anime descriptions into numerical values. Cosine similarity is then used to measure how closely two anime are related.

Instead of storing similarity values for every possible pair of anime, similarities are calculated only when needed. This keeps memory usage low while still providing fast recommendations.

## Automatic Database Seeding

The backend checks whether the database already contains data before importing the dataset.

This allows the application to restart safely without inserting duplicate records.

## Separate Frontend and Backend

The frontend only communicates with the backend through REST APIs.

Because of this separation, each service can be developed, tested, and deployed independently.

## PostgreSQL Database

The dataset is imported into PostgreSQL instead of reading directly from the CSV file for every request.

Using a database provides much faster searching and makes the application behave like a real production system.

# Technology Stack

| Component | Technology |
| ---------- | ---------- |
| Frontend | React, JavaScript, Vite, Nginx |
| Backend | FastAPI, SQLAlchemy, Pandas, Scikit Learn |
| Database | PostgreSQL |
| Containerization | Docker, Docker Compose |

# Project Structure

```text
anime-recommender/

├── docker-compose.yml
├── README.md
├── data/
│   └── anime_dataset_2023.csv
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

# Dataset

This project uses the Anime Dataset 2023 available on Kaggle.

The dataset contains approximately twenty five thousand anime entries along with information such as title, genres, synopsis, type, number of episodes, score, and popularity.

The CSV file is placed inside the data folder. During the first startup, the backend automatically imports the data into PostgreSQL.

# Installation Files

The entire project can be started without any manual configuration.

The `docker-compose.yml` file creates and connects all services.

The backend Dockerfile installs the Python environment and required packages.

The frontend Dockerfile builds the React application and serves it through Nginx.

The `seed.py` file automatically imports the dataset into PostgreSQL whenever the database is empty.

# Installation

Before starting, make sure Docker Desktop is installed and running.

```bash
git clone https://github.com/<your-username>/anime-recommender.git

cd anime-recommender

docker compose up --build
```

During the first startup, Docker performs the following steps.

1. Starts the PostgreSQL database.

2. Builds the FastAPI backend.

3. Imports the Kaggle dataset into PostgreSQL.

4. Creates the recommendation model.

5. Builds the React frontend.

6. Serves the frontend using Nginx.

Once everything is running, open the application by visiting:

http://localhost:3000

# Using the Application

Open the application in your browser.

Search for an anime that you already enjoy and choose it from the search results if you want recommendations based on similar content.

You can also select one or more genres together with an anime type such as TV, Movie, or OVA if you want recommendations based on your preferences.

You may also combine both options. The application will first find anime that are similar to your selected title and then rank them according to your chosen preferences.

After clicking the recommendation button, the application displays a ranked list of anime together with posters, genres, scores, and similarity percentages.

# API Endpoints

| Method | Endpoint | Description |
| ------- | -------- | ----------- |
| GET | `/animes?q=<search>&limit=<number>` | Search anime by name |
| GET | `/animes/{id}` | Get information about one anime |
| POST | `/recommend` | Generate recommendations |
| GET | `/health` | Check whether the backend is running |

# Features

1. Live anime search with autocomplete.

2. Genre based filtering.

3. Type based filtering.

4. Content based recommendations using TF IDF and cosine similarity.

5. Preference based recommendations.

6. Combined recommendation system that merges both techniques.

7. Fully containerized application using Docker.

8. Clean and responsive user interface.