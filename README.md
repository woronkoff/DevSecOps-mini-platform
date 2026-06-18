# DevSecOps Mini Platform

A hands-on DevSecOps learning project built step by step.

This project starts as a simple Flask API and evolves into a small platform covering core DevOps and DevSecOps practices such as testing, CI/CD, containerization, and secure configuration.

---

## Quick Start

### Run locally

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python3 run.py
```

Test:

```bash
curl http://127.0.0.1:5000/
```

---

### Run with Docker

```bash
docker build -t devsecops-mini-platform .
docker run -p 5000:5000 devsecops-mini-platform
```

---

### Run with Docker Compose

```bash
docker compose up --build
# or (older systems)
docker-compose up --build
```

---

## Project Goals

* Practice Linux basics for DevOps
* Improve Git and GitHub workflows
* Build and structure a Flask API
* Learn Docker and containerization
* Use Docker Compose for service orchestration
* Implement CI with GitHub Actions
* Manage configuration with environment variables
* Introduce DevSecOps practices (security, scanning, etc.)

---

## Project Structure

```
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

---

## API Endpoints

| Method | Endpoint    | Description             |
| ------ | ----------- | ----------------------- |
| GET    | `/`         | Welcome message         |
| GET    | `/health`   | Health check            |
| GET    | `/api/info` | Application information |

---

## Testing

Run tests:

```bash
pytest
```

The test suite validates API endpoints and ensures stability.

---

## CI (GitHub Actions)

This project uses GitHub Actions to:

* Install dependencies
* Run automated tests on every push

This ensures that broken code is detected early.

---

## Docker

The application is containerized using Docker.

Why this matters:

* Consistent environments
* Easier deployment
* Isolation of dependencies

---

## Docker Compose

Docker Compose is used to manage services.

Why this matters:

* Prepares for multi-service architecture
* Simplifies running the application
* Standard in real-world DevOps setups

---

## Configuration (Environment Variables)

The application uses environment variables instead of hardcoded values.

Example:

```
APP_NAME=DevSecOps Mini Platform
APP_VERSION=0.1.0
APP_ENV=development
```

Why this matters:

* Improves security (no secrets in code)
* Makes deployments flexible
* Required for CI/CD pipelines

`.env` is not committed to Git for security reasons.

## Security

- `.env` is not committed to Git
- CI uses GitHub Secrets for configuration
- Default values are used as fallback

This prevents leaking sensitive information.

---

## Progress (Learning Log)

### Day 1

* Created Flask API
* Added `/` and `/health` endpoints

### Day 2

* Introduced application factory pattern
* Added `/api/info`
* Improved project structure

### Day 3

* Added pytest tests
* Validated API endpoints

### Day 4

* Implemented GitHub Actions CI pipeline

### Day 5

* Dockerized the application

### Day 6

* Added Docker Compose

### Day 7

* Introduced environment variables and configuration management

## Day 8

* Added secure handling of environment variables using GitHub Secrets.


---

## Next Steps

* Secrets management in CI/CD
* Security scanning (dependencies, code)
* Reverse proxy (Nginx)
* HTTPS setup
* Logging and monitoring
* Deployment strategies
