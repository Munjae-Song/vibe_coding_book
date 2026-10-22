@echo off
REM Quick Test - Check if everything works

echo.
echo ===================================
echo  CSV to DB - Quick Test
echo ===================================
echo.

cd /d "%~dp0"

echo Step 1: Check Python...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not found!
    echo Please install Python 3.8 or higher.
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo Step 2: Check required modules...
python -c "import tkinter" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: tkinter not found!
    echo Please reinstall Python with tcl/tk option.
    pause
    exit /b 1
) else (
    echo - tkinter: OK
)

python -c "import sqlite3" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: sqlite3 not found!
    pause
    exit /b 1
) else (
    echo - sqlite3: OK
)

python -c "import csv" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: csv module not found!
    pause
    exit /b 1
) else (
    echo - csv: OK
)

echo.
echo Step 3: Check main program...
if exist "003_GUI_CSV_to_DB.py" (
    echo - Main program: OK
) else (
    echo ERROR: 003_GUI_CSV_to_DB.py not found!
    pause
    exit /b 1
)

echo.
echo Step 4: Check sample data...
if exist "data\" (
    echo - Data folder: OK
    dir /b data\*.csv 2>nul | find /c /v "" > temp.txt
    set /p count=<temp.txt
    del temp.txt
    echo - CSV files found
) else (
    echo WARNING: data folder not found
    echo You can still run the program with your own CSV files.
)

echo.
echo ===================================
echo  All checks passed!
echo ===================================
echo.
echo Your system is ready to run the program.
echo.
echo To run:
echo   1. simple_setup.bat (first time only)
echo   2. simple_run.bat
echo.
echo Or directly:
echo   python 003_GUI_CSV_to_DB.py
echo.
pause



