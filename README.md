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

Live anime search with autocomplete.

Genre based filtering.

Type based filtering across TV, Movie, OVA, and other formats.

Content based recommendations using TF IDF and cosine similarity.

Preference based recommendations.

A combined recommendation mode that merges both techniques.

Fully containerized application using Docker.

Clean, minimal, dark themed user interface.

## Technology Stack

### Backend

Python

FastAPI

SQLAlchemy

Pandas

Scikit Learn

### Frontend

React

Vite

Nginx

### Database

PostgreSQL

### DevOps

Docker

Docker Compose

### Development Tools

Visual Studio Code

Git

GitHub

## Project Architecture

```
                    User
                      |
                      v
               React Frontend
                      |
             REST API Requests
                      |
                      v
              FastAPI Backend
                      |
            Recommendation Engine
                      |
                      v
              PostgreSQL Database
```

The frontend never communicates with the database directly. Every request goes through the backend first, which keeps the system organized and easier to maintain.

## Project Structure

```
anime-recommender/
├── docker-compose.yml
├── README.md
├── INSTALL.md
├── USAGE.md
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

## How To Install

Full setup instructions, prerequisites, and troubleshooting for getting the project running are in [INSTALL.md](./INSTALL.md).

In short.

```bash
git clone https://github.com/awlygod/anime-recommender.git
cd anime-recommender
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

## Running Without Docker

### Backend

Create a virtual environment.

```bash
python -m venv venv
```

Activate it on Windows.

```bash
venv\Scripts\activate
```

Activate it on Linux or macOS.

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Place the Kaggle dataset inside the data folder, then seed the database.

```bash
python seed.py
```

Run the backend.

```bash
uvicorn main:app --reload
```

### Frontend

Install dependencies.

```bash
npm install
```

Run React.

```bash
npm run dev
```

## Database Setup

The application uses PostgreSQL.

When Docker Compose is executed, the following happens automatically.

The PostgreSQL container starts.

The database and table are created.

The backend checks whether the database already contains data.

If the database is empty, the Kaggle dataset is imported.

If data already exists, seeding is skipped so restarting the application never creates duplicate records.

No manual database setup is required.

## How To Use

A full walkthrough of the interface, what each field does, and a worked example of a recommendation request is in [USAGE.md](./USAGE.md).

In short, search for an anime you like, set genre and type preferences, or do both, then click Get recommendations to see a ranked list of matching anime.

## How the Recommendation Engine Works

The user submits an anime, a set of preferences, or both.

FastAPI receives the request and validates it.

If an anime is provided, the content based engine calculates cosine similarity between that anime and every other anime in the dataset using a TF IDF representation of genres and synopsis.

If preferences are provided, the preference based engine filters and ranks anime by genre, type, and score.

If both are provided, the content based results are filtered further using the given preferences.

The final ranked list is returned as JSON.

React renders the results as a grid of anime cards.

## API Endpoints

| Method | Endpoint | Description |
| ------- | -------- | ----------- |
| GET | /animes?q=\<search\>&limit=\<number\> | Search anime by name |
| GET | /animes/{id} | Get information about one anime |
| POST | /recommend | Generate recommendations |
| GET | /health | Check whether the backend is running |

## Dataset Preparation

This project uses the Anime Dataset 2023 available on Kaggle. The dataset contains approximately twenty five thousand anime entries along with information such as title, genres, synopsis, type, number of episodes, score, and popularity.

Before seeding, missing or invalid values in fields such as score, episodes, and popularity are handled so they do not break the recommendation logic. Text fields used for similarity, namely genres and synopsis, are combined and cleaned before being passed into the TF IDF vectorizer.

The cleaned data is imported into PostgreSQL automatically the first time the backend starts.

## Dataset Source

Dataset used, Anime Dataset 2023.

Source.

https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset

## Installation Files

The entire project can be started without any manual configuration.

The docker-compose.yml file creates and connects all three services on a custom Docker network.

The backend Dockerfile installs the Python environment and required packages.

The frontend Dockerfile builds the React application and serves it through Nginx.

The seed.py file automatically imports the dataset into PostgreSQL whenever the database is empty.

See [INSTALL.md](./INSTALL.md) for the full setup walkthrough.

## Docker Architecture

The project consists of three independent containers connected through a custom Docker network.

Frontend, built with React and served through Nginx.

Backend, built with FastAPI and containing the recommendation engine.

Database, running PostgreSQL.

Docker Compose creates the network automatically and allows the three containers to communicate without any manual setup.

## Screenshots

### User Request Form
![Request Form](User-Form.png)

### Combined Recommendations
![Combined](Combined.png)

### Content Based Recommendations
![Content-Based](conten-based.png)

### Preference Based Recommendations
![Preference Based](Preference-based.png)

## Troubleshooting

### Docker will not start

```bash
docker compose down
docker compose up --build
```

### Port already in use

Change the affected port inside docker-compose.yml, or stop whatever else is using that port.

### Database connection error

Confirm the following.

The PostgreSQL container is running.

The Docker network was created successfully.

The database credentials in docker-compose.yml match what the backend expects.

The backend only starts after PostgreSQL has passed its health check.

More detailed troubleshooting steps are in [INSTALL.md](./INSTALL.md).

## Author

Suraj Tripathi

GitHub:  https://github.com/awlygod

## Acknowledgements

This project was developed as part of a technical recruitment assessment.

Open source technologies used, FastAPI, React, Docker, PostgreSQL, SQLAlchemy, Pydantic, Vite, Scikit Learn.

Thanks to Kaggle and the dataset author for making the Anime Dataset 2023 publicly available.