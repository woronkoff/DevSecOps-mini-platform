# DevSecOps Mini Platform

A beginner-friendly DevSecOps learning project.

This project starts as a simple Flask API and will grow step by step into a small DevSecOps practice platform.

## Goals

- Practice Linux basics for DevOps
- Practice Git and GitHub workflow
- Build a Flask API
- Learn Docker
- Learn Docker Compose
- Learn CI/CD with GitHub Actions
- Learn environment variables and secrets
- Learn dependency scanning
- Learn static code analysis
- Learn basic vulnerability scanning
- Learn logging and authentication basics
- Later: Nginx, HTTPS, monitoring, and deployment

## Day 1

Created a basic Flask API with:

- `GET /`
- `GET /health`

## How to run locally

Create a virtual environment:

```bash
python3 -m venv venv
```

## Activate it on Linux/macOS:

    source venv/bin/activate

## Activate it on Windows PowerShell:

    .\venv\Scripts\Activate.ps1

## Install dependencies:

    pip install -r requirements.txt

## Run the app:

    python3 run.py

## On Windows, you may need:

    python run.py

## Test the app:

    curl http://127.0.0.1:5000/
    curl http://127.0.0.1:5000/health

## Day 2

Improved the project structure by adding:

- `app/` package
- Flask application factory
- Blueprint-based routes
- `GET /api/info`
- `.env.example` for safe configuration examples

## Project Structure

```text
devsecops-mini-platform/
├── app/
│   ├── __init__.py
│   └── routes.py
├── tests/
│   ├── conftest.py
│   └── test_routes.py
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── pytest.ini
├── run.py
├── README.md
└── requirements.txt
```

## API Endpoints

| Method | Endpoint    | Description             |
| ------ | ----------- | ----------------------- |
| GET    | `/`         | Welcome message         |
| GET    | `/health`   | Health check            |
| GET    | `/api/info` | Application information |

## Day 3

Added automated tests with pytest.

The tests check:

- `GET /`
- `GET /health`
- `GET /api/info`

## Running tests

Activate the virtual environment:

```bash
source venv/bin/activate
```

## On Windows PowerShell:

    .\venv\Scripts\Activate.ps1

## Run tests:

    pytest

## Expected result:

    ============================= test session starts ==============================
    platform linux -- Python 3.13.5, pytest-9.0.3, pluggy-1.6.0
    rootdir: /home/devsecops-mini-platform
    configfile: pytest.ini
    testpaths: tests
    collected 3 items

    tests/test_routes.py ...                                                 [100%]

    ============================== 3 passed in 0.01s ===============================

## Day 4

Added GitHub Actions CI pipeline.

Every push now automatically runs tests using pytest.

If tests fail, the pipeline fails.

## CI

The project uses GitHub Actions to:

- Install dependencies
- Run automated tests

## Day 5

Dockerized the Flask application.

## Run with Docker

## Build image:

```bash
docker build -t devsecops-mini-platform .
```

## Run container:

    docker run -p 5000:5000 devsecops-mini-platform

## Test:

    curl http://127.0.0.1:5000/
    curl http://127.0.0.1:5000/health
    curl http://127.0.0.1:5000/api/info

## Day 6

Added Docker Compose for easier container management.

## Run with Docker Compose

```bash
docker-compose up --build
```

## Stop:

```bash
docker-compose down
```