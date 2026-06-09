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
├── .env.example
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## API Endpoints

| Method | Endpoint    | Description             |
| ------ | ----------- | ----------------------- |
| GET    | `/`         | Welcome message         |
| GET    | `/health`   | Health check            |
| GET    | `/api/info` | Application information |

