#!/bin/bash
# ============================================================
# CSV to SQLite DB Importer - Linux 환경 확인 스크립트
# ============================================================
# 이 프로그램은 Python 표준 라이브러리만 사용하므로
# 추가 패키지 설치가 필요 없습니다!
# ============================================================

echo ""
echo "========================================"
echo " CSV to DB Importer 환경 확인"
echo "========================================"
echo ""

# 스크립트가 위치한 디렉토리로 이동
cd "$(dirname "$0")"

echo "[1/3] Python 설치 확인 중..."
echo ""

# Python3가 설치되어 있는지 확인
if ! command -v python3 &> /dev/null; then
    echo "[오류] Python3가 설치되어 있지 않습니다."
    echo ""
    echo "Python 3.8 이상 버전을 설치한 후 다시 시도해주세요."
    echo ""
    echo "Ubuntu/Debian: sudo apt-get install python3 python3-tk"
    echo "CentOS/RHEL: sudo yum install python3 python3-tkinter"
    echo "Fedora: sudo dnf install python3 python3-tkinter"
    echo ""
    exit 1
fi

echo "설치된 Python 버전:"
python3 --version
echo ""

echo "[2/3] 필수 라이브러리 확인 중..."
echo ""

# Tkinter 확인
python3 -c "import tkinter" &> /dev/null
if [ $? -ne 0 ]; then
    echo "[경고] Tkinter가 설치되어 있지 않습니다."
    echo ""
    echo "설치 방법:"
    echo "Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "CentOS/RHEL: sudo yum install python3-tkinter"
    echo "Fedora: sudo dnf install python3-tkinter"
    echo ""
    exit 1
else
    echo "- tkinter: OK"
fi

# SQLite3 확인
python3 -c "import sqlite3" &> /dev/null
if [ $? -ne 0 ]; then
    echo "[경고] sqlite3가 설치되어 있지 않습니다."
    echo ""
    exit 1
else
    echo "- sqlite3: OK"
fi

# CSV 모듈 확인
python3 -c "import csv" &> /dev/null
if [ $? -ne 0 ]; then
    echo "[경고] csv 모듈이 없습니다."
    echo ""
    exit 1
else
    echo "- csv: OK"
fi

echo ""
echo "[3/3] 프로그램 파일 확인 중..."
echo ""

if [ -f "003_GUI_CSV_to_DB.py" ]; then
    echo "- 메인 프로그램: OK"
else
    echo "[오류] 003_GUI_CSV_to_DB.py 파일이 없습니다."
    exit 1
fi

if [ -d "data" ]; then
    echo "- 데이터 폴더: OK"
else
    echo "[경고] data 폴더가 없습니다."
fi

echo ""
echo "========================================"
echo " 환경 확인 완료!"
echo "========================================"
echo ""
echo "모든 필수 구성 요소가 준비되었습니다."
echo ""
echo "프로그램 실행 방법:"
echo "  1. ./run_linux.sh (권장)"
echo "  2. python3 003_GUI_CSV_to_DB.py (직접 실행)"
echo ""
echo "실행 권한이 필요한 경우:"
echo "  chmod +x run_linux.sh"
echo ""
echo "========================================"
echo ""

