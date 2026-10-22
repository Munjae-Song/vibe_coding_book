@echo off
REM ============================================================
REM CSV to SQLite DB Importer - Windows Virtual Env Setup
REM ============================================================

chcp 65001 >nul 2>&1

echo.
echo ========================================
echo  CSV to DB Importer Setup
echo ========================================
echo.

cd /d "%~dp0"

echo [1/5] Checking Python installation...
echo.

python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed.
    echo.
    echo Please install Python 3.8 or higher.
    echo Download: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Installed Python version:
python --version
echo.

if exist "venv\" (
    echo [WARNING] Existing virtual environment found.
    echo Removing and recreating...
    echo.
    rmdir /s /q venv
)

echo [2/5] Creating virtual environment...
python -m venv venv
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to create virtual environment.
    echo.
    pause
    exit /b 1
)
echo [DONE] Virtual environment created
echo.

echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to activate virtual environment.
    echo.
    pause
    exit /b 1
)
echo [DONE] Virtual environment activated
echo.

echo [4/5] Upgrading pip...
python -m pip install --upgrade pip --quiet
echo [DONE] pip upgraded
echo.

echo [5/5] Checking required libraries...
echo.

python -c "import tkinter" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Tkinter is not installed.
    echo Please reinstall Python with tcl/tk option.
    echo.
    pause
    exit /b 1
) else (
    echo - tkinter: OK
)

python -c "import sqlite3" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] sqlite3 is not installed.
    echo.
    pause
    exit /b 1
) else (
    echo - sqlite3: OK
)

python -c "import csv" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] csv module is not available.
    echo.
    pause
    exit /b 1
) else (
    echo - csv: OK
)

echo.
echo Checking program files...
echo.

if exist "003_GUI_CSV_to_DB.py" (
    echo - Main program: OK
) else (
    echo [ERROR] 003_GUI_CSV_to_DB.py not found.
    pause
    exit /b 1
)

if exist "data\" (
    echo - Data folder: OK
) else (
    echo [WARNING] data folder not found.
)

call venv\Scripts\deactivate.bat

echo.
echo ========================================
echo  Setup Complete!
echo ========================================
echo.
echo Virtual environment path: venv\
echo.
echo How to run the program:
echo   1. Run run_windows.bat (Recommended)
echo   2. Or manually:
echo      venv\Scripts\activate
echo      python 003_GUI_CSV_to_DB.py
echo.
echo ========================================
echo.

pause
 