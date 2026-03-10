# TitanHelp — Ticket Management System

A full-stack help desk ticket system built with Flask (Python) and React (Vite).

## First-Time Setup

Run this once after cloning the repo. It creates the Python virtual environment, installs all dependencies for both frontend and backend, and creates the local database.

**In VSCode:** Open the Command Palette (`Ctrl+Shift+P`) → `Tasks: Run Task` → `Setup Everything (First Time)`

**Or manually in a terminal:**

```bash
# Backend — from backend/TitanHelp.Backend/
py -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\flask db upgrade

# Frontend — from frontend/vite-project/
npm install
```

> `flask db upgrade` creates the local SQLite database file at `instance/titanhelp.db`.
> You only need to run this again if a teammate commits a new migration to `migrations/versions/`.

## Running the App

**In VSCode:** Press `F5` and select `Full Stack: Backend + Frontend` to start both servers.

| Server   | URL                    |
|----------|------------------------|
| Backend  | http://127.0.0.1:5000  |
| Frontend | http://localhost:5173  |

**Or via Tasks:** `Ctrl+Shift+P` → `Tasks: Run Task` → `Run Full Stack (Tasks)`

## Running Tests

```bash
# From backend/TitanHelp.Backend/
.venv\Scripts\python -m pytest -v
```

## Project Structure

```
titanhelp-mighty-pythons/
├── backend/TitanHelp.Backend/
│   ├── app/
│   │   ├── api/            # HTTP route handlers (controllers)
│   │   ├── services/       # Business logic
│   │   ├── repositories/   # Database access (SQLAlchemy)
│   │   ├── models/         # ORM models (database schema)
│   │   └── schemas/        # Input validation
│   ├── migrations/         # Database version history (Flask-Migrate)
│   ├── requirements.txt    # Python dependencies
│   └── TitanHelp.Backend.py
└── frontend/vite-project/
    └── src/                # React components
```

## When a Teammate Adds a New Migration

If someone on the team changes the database schema and commits a new file under `migrations/versions/`, you need to apply it:

```bash
# From backend/TitanHelp.Backend/
.venv\Scripts\flask db upgrade
```
