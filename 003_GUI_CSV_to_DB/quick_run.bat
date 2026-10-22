@echo off
REM 빠른 실행 스크립트 - 에러 메시지 없이 바로 실행
chcp 65001 >nul 2>&1
cd /d "%~dp0"
python 003_GUI_CSV_to_DB.py

