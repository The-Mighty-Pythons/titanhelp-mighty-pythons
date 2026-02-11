@echo off
setlocal

echo ==========================
echo TitanHelp Dev Launcher
echo ==========================

REM --- Backend ---
echo Starting Backend...
start "TitanHelp Backend" cmd /k ^
"cd backend\TitanHelp.Backend && ^
if not exist .venv (py -m venv .venv) && ^
call .venv\Scripts\activate && ^
pip install -r requirements.txt && ^
if not exist .env (copy .env.example .env) && ^
python TitanHelp.Backend.py"

REM --- Frontend (Vite) ---
echo Starting Frontend...
start "TitanHelp Frontend" cmd /k ^
"cd frontend\vite-project && ^
npm install && ^
if not exist .env (copy .env.example .env) && ^
npm run dev"

echo.
echo Open the app:
echo   Frontend: http://localhost:5173
echo   Backend : http://127.0.0.1:5000/api/tickets
echo.
pause
