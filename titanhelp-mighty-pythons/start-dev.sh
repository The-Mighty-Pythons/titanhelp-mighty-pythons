#!/usr/bin/env bash
set -e

echo "=========================="
echo "TitanHelp Dev Launcher"
echo "=========================="

# Backend
(
  cd backend/TitanHelp.Backend
  if [ ! -d ".venv" ]; then python3 -m venv .venv; fi
  source .venv/bin/activate
  pip install -r requirements.txt
  if [ ! -f ".env" ]; then cp .env.example .env; fi
  python TitanHelp.Backend.py
) &

# Frontend (Vite)
(
  cd frontend/vite-project
  npm install
  if [ ! -f ".env" ]; then cp .env.example .env; fi
  npm run dev
) &

echo ""
echo "Open the app:"
echo "  Frontend: http://localhost:5173"
echo "  Backend : http://127.0.0.1:5000/api/tickets"
echo ""

wait
