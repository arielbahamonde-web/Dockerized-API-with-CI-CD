# Dockerized API with CI/CD

Example project: a simple API built with FastAPI, prepared to run in Docker and orchestrated with `docker-compose`. Includes basic tests and is designed to be integrated into a CI/CD pipeline.

**Features**
- **Language:** Python 3
- **Framework:** FastAPI
- **ASGI server:** Uvicorn
- **Containers:** Docker, Docker Compose
- **Tests:** pytest

**Requirements**
- Docker and Docker Compose installed locally
- Python 3.8+ (for local execution)

**Local installation**
```bash
# create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# start the API for development
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Run with Docker (recommended)**
```bash
# build and start services (service is named 'api' in deploy/docker-compose.yml)
docker compose -f deploy/docker-compose.yml up --build

# or in detached mode
docker compose -f deploy/docker-compose.yml up -d --build

# stop and remove containers
docker compose -f deploy/docker-compose.yml down
```

The application will be available at `http://localhost:8000`.

To build and run the image manually:
```bash
docker build -f build/Dockerfile -t myapi:latest .
docker run --rm -p 8000:8000 myapi:latest
```

**Build / deployment files**
- `build/Dockerfile`: uses `python:3.12-slim`, installs `requirements.txt` and runs `uvicorn` on port `8000`.
- `deploy/docker-compose.yml`: defines the `api` service, maps port `8000` and loads environment variables from `.env`.

**Environment variables**
If you use a `.env` file (referenced by `deploy/docker-compose.yml`) you can add values like:
```
# .env (example)
HOST=0.0.0.0
PORT=8000
```

**Run tests**
```bash
# local
pytest -q

# from Docker (option: run pytest inside the app container)
docker compose -f deploy/docker-compose.yml run --rm api pytest -q
```

This project contains a health test at `tests/test_health.py` which verifies that `GET /health` returns `200` and `{"status": "ok"}`.

**Main endpoints (examples)**
- `GET /` — Basic API status

  Example:
  ```bash
  curl -s http://localhost:8000/
  # => {"message": "API running"}
  ```

- `GET /health` — Health check

  Example:
  ```bash
  curl -s http://localhost:8000/health
  # => {"status": "ok"}
  ```

- `GET /version` — API version

  Example:
  ```bash
  curl -s http://localhost:8000/version
  # => {"version": "1.0.0"}
  ```

- `GET /users/` — Example users list (defined in `app/routes/users.py`)

  Example:
  ```bash
  curl -s http://localhost:8000/users/
  # => [{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]
  ```

**Project structure**
- `build/Dockerfile` : Application image definition
- `deploy/docker-compose.yml` : Services orchestration
- `requirements.txt` : Python dependencies
- `app/` : Application source code
  - `app/main.py` : FastAPI entry point
  - `app/routes/users.py` : Example user routes
- `tests/` : Tests (e.g. `tests/test_health.py`)

**CI / Best practices**
- Add a CI workflow (GitHub Actions, GitLab CI, etc.) that:
  - Builds the Docker image
  - Runs tests with `pytest`
  - Publishes artifacts or deploys when tests pass

**Contributing**
- Open an Issue before implementing significant changes.
- Submit a Pull Request with tests and clear descriptions.

**License**
This repository uses the MIT License (add a `LICENSE` file if not present).
