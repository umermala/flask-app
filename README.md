# Simple Docker App

A minimal Flask application that runs inside Docker and displays a success message in the browser.

## Run Locally with Docker

```bash
docker build -t simple-docker-app .
docker run -p 5000:5000 simple-docker-app