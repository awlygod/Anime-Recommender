# Installation and Setup Guide

This project is fully containerized with Docker, meaning you do not need to install Python, Node.js, or PostgreSQL on your local machine to run it.

## Prerequisites

* Git, to clone the repository
* Docker Desktop, must be installed and running on your machine

You can confirm both are installed by running.

```bash
git --version
docker --version
docker compose version
```

## How to Run

Clone the repository.

```bash
git clone https://github.com/awlygod/Anime-Recommender.git
cd Anime-Recommender
```

Start the containers. Run the following command in the root directory. This will download the necessary base images, install all dependencies, seed the database from the Kaggle dataset, and start all three services on a shared network.

```bash
docker compose up --build
```

The first run takes a little longer than usual since the database has to be seeded with the full anime dataset. Once the terminal shows the backend printing a message like Content recommender built on 24905 anime, the application is ready.

## Access the Application

Once the terminal shows that the database, backend, and frontend are all running, open your web browser.

* Frontend UI, http://localhost:3000
* Backend API, http://localhost:8000
* Swagger Docs, http://localhost:8000/docs

## Stopping and Resetting

To gracefully stop the application, press Ctrl + C in the terminal where Docker is running, or run.

```bash
docker compose down
```

To perform a full reset, if you want to completely wipe the database and start from a clean slate, for example to re-run the seeding process, use the -v flag to destroy the stored volumes before rebuilding.

```bash
docker compose down -v
docker compose up --build
```

## Environment Variables

You do not need to manually create any .env files to run the project with Docker. All necessary environment variables, such as database credentials, the frontend origin used for CORS, and service ports, are already handled and injected directly through the docker-compose.yml file.

## Running Without Docker

This is only needed if you want to work on the backend or frontend directly during development. Docker is still the recommended way to run the full project.

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

Place the Kaggle dataset inside the data folder, then seed the database. This step requires a PostgreSQL instance already running and reachable, either through a standalone container or a local install.

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

Vite's dev server runs on port 5173 by default, not 3000. If you are also running the backend locally through uvicorn rather than Docker, update `FRONTEND_ORIGIN` in `backend/.env` to `http://localhost:5173` before starting the backend, otherwise the browser will block requests from the frontend due to CORS, since the backend only allows one configured origin at a time.

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