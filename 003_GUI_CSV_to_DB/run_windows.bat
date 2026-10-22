@echo off
REM ============================================================
REM CSV to SQLite DB Importer - Windows Run Script
REM ============================================================

chcp 65001 >nul 2>&1

echo.
echo ========================================
echo  CSV to DB Importer
echo ========================================
echo.

cd /d "%~dp0"

if not exist "venv\" (
    echo [ERROR] Virtual environment not found.
    echo.
    echo Please run setup_windows.bat first.
    echo.
    pause
    exit /b 1
)

echo [1/2] Activating virtual environment...
call venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to activate virtual environment.
    echo.
    pause
    exit /b 1
)

echo [DONE] Virtual environment activated
echo.
echo Python version:
python --version
echo.
echo [2/2] Starting program...
echo.

python 003_GUI_CSV_to_DB.py

call venv\Scripts\deactivate.bat

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] An error occurred during execution.
    echo.
    pause
    exit /b 1
)

echo.
echo Program finished.
pause
