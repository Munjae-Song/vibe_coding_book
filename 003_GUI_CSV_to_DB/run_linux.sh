#!/bin/bash
# ============================================================
# CSV to SQLite DB Importer - Linux 실행 스크립트
# ============================================================
# 이 스크립트는 Python 프로그램을 직접 실행합니다.
# ============================================================

echo ""
echo "========================================"
echo " CSV to DB Importer 실행"
echo "========================================"
echo ""

# 스크립트가 위치한 디렉토리로 이동
cd "$(dirname "$0")"

# Python3가 설치되어 있는지 확인
if ! command -v python3 &> /dev/null; then
    echo "[오류] Python3가 설치되어 있지 않습니다."
    echo "Python 3.8 이상 버전을 설치한 후 다시 시도해주세요."
    echo ""
    echo "Ubuntu/Debian: sudo apt-get install python3 python3-tk"
    echo "CentOS/RHEL: sudo yum install python3 python3-tkinter"
    echo "Fedora: sudo dnf install python3 python3-tkinter"
    echo ""
    exit 1
fi

echo "Python 버전 확인:"
python3 --version
echo ""
echo "프로그램을 시작합니다..."
echo ""

# Python 프로그램 실행
python3 003_GUI_CSV_to_DB.py

# 실행 오류 확인
if [ $? -ne 0 ]; then
    echo ""
    echo "[오류] 프로그램 실행 중 오류가 발생했습니다."
    echo "Tkinter가 설치되어 있는지 확인해주세요."
    echo ""
    echo "Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "CentOS/RHEL: sudo yum install python3-tkinter"
    echo "Fedora: sudo dnf install python3-tkinter"
    echo ""
    exit 1
fi

echo ""
echo "프로그램이 종료되었습니다."

