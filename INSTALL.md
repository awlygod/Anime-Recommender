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
cd anime-recommender
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

If you prefer to run the backend or frontend outside of Docker for local development, refer to the Running Without Docker section in the main README for the manual setup steps.