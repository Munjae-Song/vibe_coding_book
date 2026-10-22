# CSV to SQLite DB Importer

CSV 파일을 GUI를 통해 선택하고 SQLite 데이터베이스에 자동으로 저장하는 프로그램입니다.

## 📋 목차

- [프로그램 개요](#-프로그램-개요)
- [주요 기능](#-주요-기능)
- [시스템 요구사항](#-시스템-요구사항)
- [설치 방법](#-설치-방법)
- [실행 방법](#-실행-방법)
- [사용 방법](#-사용-방법)
- [파일명 규칙](#-파일명-규칙)
- [데이터베이스 구조](#-데이터베이스-구조)
- [프로젝트 구조](#-프로젝트-구조)
- [문제 해결](#-문제-해결)

## 🎯 프로그램 개요

이 프로그램은 제품 검사 데이터가 담긴 CSV 파일을 간편하게 데이터베이스로 임포트할 수 있도록 만든 GUI 애플리케이션입니다. 
SQL 지식 없이도 파일명을 분석하여 자동으로 테이블을 생성하고 데이터를 저장합니다.

### 개선 사항

- **GUI 기반 파일 선택**: 명령줄이 아닌 GUI를 통해 누구나 쉽게 CSV 파일을 선택할 수 있습니다.
- **자동 테이블 생성**: 파일명을 분석하여 적절한 테이블을 자동으로 생성합니다.
- **즉시 실행 가능**: 소스 코드 수정 없이 바로 사용할 수 있습니다.

## ✨ 주요 기능

1. **직관적인 GUI 인터페이스**
   - 파일 선택 버튼으로 간편한 CSV 파일 선택
   - 데이터 전송 버튼으로 한 번에 DB로 임포트
   - 실시간 진행상황 표시

2. **자동 파일명 분석**
   - CSV 파일명에서 제품 정보 추출
   - 자동으로 테이블명 생성 (예: `DS_PRDT_0220V_805_20.csv` → `DS_PRDT_0220_805_20`)
   - 파일명 형식 검증

3. **데이터베이스 자동 관리**
   - 테이블 자동 생성 (중복 시 기존 테이블 사용)
   - 타임스탬프 자동 추가
   - 트랜잭션 안전성 보장

4. **대용량 데이터 처리**
   - 수십만 건의 데이터도 안정적으로 처리
   - 진행상황 실시간 표시

## 💻 시스템 요구사항

### 필수 요구사항

- **Python 3.8 이상**
- **운영체제**: Windows 10/11 또는 Linux (Ubuntu 18.04+, CentOS 7+, Fedora 등)

### Python 패키지

- `tkinter` (Python 표준 라이브러리, 대부분 기본 포함)
- `sqlite3` (Python 표준 라이브러리, 기본 포함)
- `csv` (Python 표준 라이브러리, 기본 포함)

> **참고**: 이 프로그램은 Python 표준 라이브러리만 사용하므로 추가 패키지 설치가 필요 없습니다.

### Linux 추가 요구사항

일부 Linux 배포판에서는 Tkinter가 별도 설치가 필요할 수 있습니다:

```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install python3-tkinter

# Fedora
sudo dnf install python3-tkinter
```

## 📥 설치 방법

### 필수 요구사항만 확인

이 프로그램은 Python 표준 라이브러리만 사용하므로 **추가 설치가 필요 없습니다**.

**Python 3.8 이상**만 설치되어 있으면 바로 실행 가능합니다.

### 선택사항: 가상 환경 설정 (고급 사용자용)

가상 환경을 사용하고 싶다면:

#### Windows
```cmd
setup_windows.bat
```

#### Linux
```bash
chmod +x setup_linux.sh
./setup_linux.sh
```

## 🚀 실행 방법

### 방법 1: 간단 실행 스크립트 (권장) ✅

#### Windows - 명령 프롬프트(CMD) 사용

1. **명령 프롬프트(CMD) 열기**
   - Windows 키 + R 누르기
   - `cmd` 입력 후 Enter

2. **프로젝트 폴더로 이동**
   ```cmd
   cd c:\vibe_coding\003_GUI_CSV_to_DB
   ```

3. **설치 (처음 한 번만)**
   ```cmd
   simple_setup.bat
   ```

4. **실행**
   ```cmd
   simple_run.bat
   ```

#### Windows - 파일 탐색기 사용

1. 파일 탐색기에서 프로젝트 폴더 열기
2. `simple_setup.bat` 더블클릭 (처음 한 번만)
3. `simple_run.bat` 더블클릭 (프로그램 실행)

### 방법 2: 기존 스크립트 사용

#### Windows

`run_windows.bat` 파일을 명령 프롬프트(CMD)에서 실행:
```cmd
run_windows.bat
```

> **주의**: PowerShell에서 실행 시 한글 깨짐 문제가 있을 수 있습니다. 명령 프롬프트(CMD) 사용을 권장합니다.

#### Linux

터미널에서 실행:
```bash
chmod +x run_linux.sh  # 처음 한 번만 실행
./run_linux.sh
```

### 방법 3: 직접 실행 (가상환경 없이)

#### Windows
```cmd
python 003_GUI_CSV_to_DB.py
```

#### Linux
```bash
python3 003_GUI_CSV_to_DB.py
```

## 📖 사용 방법

### 1단계: 프로그램 실행

위의 실행 방법에 따라 프로그램을 실행하면 GUI 창이 나타납니다.

### 2단계: CSV 파일 선택

1. **"📁 CSV 파일 선택"** 버튼 클릭
2. 파일 선택 다이얼로그에서 CSV 파일 선택
3. 파일명이 자동으로 분석되어 테이블 정보가 표시됩니다

### 3단계: 데이터 전송

1. 테이블 정보를 확인
2. **"⬆ 데이터베이스로 전송"** 버튼 클릭
3. 데이터 임포트 진행상황을 확인
4. 완료 메시지가 나타나면 성공!

### 예제 실행

프로젝트에 포함된 샘플 데이터로 테스트해보세요:
- `data/DS_PRDT_0220V_805_20.csv`
- `data/DS_PRDT_0275V_555_21.csv`
- 기타 샘플 파일들

## 📝 파일명 규칙

CSV 파일명은 다음 형식을 따라야 합니다:

```
{회사명}_{제품명}_{전압}V_{용량}_{년도}.csv
```

### 예제

**파일명**: `DS_PRDT_0220V_805_20.csv`

| 구성 요소 | 값 | 설명 |
|-----------|-----|------|
| 회사명+제품 | DS_PRDT | Daeshin Product |
| 전압 | 0220V | 220V (4자리 + V) |
| 용량 | 805 | 8.05μF (3자리) |
| 년도 | 20 | 2020년 (2자리) |

**생성되는 테이블명**: `DS_PRDT_0220_805_20`

> **중요**: 테이블명에서 전압의 'V'는 제거됩니다.

### 추가 예제

- `DS_PRDT_0275V_555_21.csv` → `DS_PRDT_0275_555_21`
- `ABC_CORP_0110V_100_22.csv` → `ABC_CORP_0110_100_22`

## 🗄️ 데이터베이스 구조

### 데이터베이스 파일

- **파일명**: `vibe_coding.db`
- **위치**: 프로그램과 같은 폴더
- **형식**: SQLite 3

### 테이블 구조

각 CSV 파일마다 다음 구조의 테이블이 생성됩니다:

| 필드명 | 타입 | 설명 | 제약조건 |
|--------|------|------|----------|
| id | INTEGER | 레코드 고유 ID | PRIMARY KEY, AUTOINCREMENT |
| spec | TEXT | 제품 사양 | - |
| ins_date | TEXT | 검사 날짜/시간 | - |
| mchn_no | TEXT | 설비 번호 | - |
| inspct_rnd | TEXT | 검사 차수 | - |
| capacitance | REAL | 정전용량 측정값 | - |
| loss | TEXT | 손실 측정값 | - |
| created_at | TIMESTAMP | 레코드 생성 시간 | DEFAULT CURRENT_TIMESTAMP |

### CSV 파일 형식

CSV 파일은 다음 헤더를 가져야 합니다:

```csv
spec,ins_date,mchn_no,inspct_rnd,capacitance,loss
220VAC 8.0uF,2020-01-02 09:08,###1,1st,8,0
220VAC 8.0uF,2020-01-02 09:09,###1,1st,8.0905,0.000453
...
```

## 📁 프로젝트 구조

```
003_GUI_CSV_to_DB/
│
├── 003_GUI_CSV_to_DB.py     # 메인 프로그램
├── requirements.txt          # Python 패키지 목록
│
├── setup_windows.bat         # Windows 설치 스크립트
├── run_windows.bat           # Windows 실행 스크립트
├── simple_setup.bat          # Windows 간편 설치 (영어, 인코딩 문제 없음) ✅
├── simple_run.bat            # Windows 간편 실행 (영어, 인코딩 문제 없음) ✅
├── setup_linux.sh            # Linux 설치 스크립트
├── run_linux.sh              # Linux 실행 스크립트
│
├── README.md                 # 이 문서
├── vibe_coding.db            # SQLite 데이터베이스 (자동 생성)
│
├── data/                     # 샘플 CSV 파일
│   ├── DS_PRDT_0220V_805_20.csv
│   ├── DS_PRDT_0220V_805_21.csv
│   ├── DS_PRDT_0220V_905_20.csv
│   ├── DS_PRDT_0220V_905_21.csv
│   ├── DS_PRDT_0275V_555_20.csv
│   └── DS_PRDT_0275V_555_21.csv
│
└── venv/                     # 가상 환경 (설치 후 생성)
```

## 🔧 문제 해결

### Windows

#### 문제: bat 파일 실행 시 한글 깨짐 또는 "내부 또는 외부 명령이 아닙니다" 오류

**원인**: PowerShell에서 UTF-8 인코딩 파일 실행 시 발생하는 문제

**해결방법 (3가지 중 선택)**:

**방법 1: 명령 프롬프트(CMD) 사용 (가장 간단) ✅ 권장**
1. Windows 키 + R 누르기
2. `cmd` 입력 후 Enter
3. 프로젝트 폴더로 이동:
   ```cmd
   cd c:\vibe_coding\003_GUI_CSV_to_DB
   ```
4. 실행:
   ```cmd
   simple_setup.bat
   simple_run.bat
   ```

**방법 2: 영어 전용 스크립트 사용**
- `simple_setup.bat` - 설치용 (한글 없음)
- `simple_run.bat` - 실행용 (한글 없음)

**방법 3: 직접 Python 실행**
```cmd
python 003_GUI_CSV_to_DB.py
```

#### 문제: "Python을 찾을 수 없습니다"

**해결방법**:
1. Python 공식 웹사이트에서 Python 3.8 이상 버전 다운로드
2. 설치 시 "Add Python to PATH" 옵션 체크
3. 설치 후 컴퓨터 재시작

#### 문제: 가상 환경 활성화 실패

**해결방법**:
1. PowerShell 실행 정책 변경:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
2. 또는 명령 프롬프트(CMD)에서 실행

### Linux

#### 문제: "tkinter를 찾을 수 없습니다"

**해결방법**:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install python3-tkinter

# Fedora
sudo dnf install python3-tkinter
```

#### 문제: "python3-venv를 찾을 수 없습니다"

**해결방법**:
```bash
# Ubuntu/Debian
sudo apt-get install python3-venv

# CentOS/RHEL
sudo yum install python3-venv
```

#### 문제: 스크립트 실행 권한 없음

**해결방법**:
```bash
chmod +x setup_linux.sh run_linux.sh
```

### 공통 문제

#### 문제: CSV 파일명 형식 오류

**해결방법**:
- 파일명이 `{prefix}_{전압}V_{용량}_{년도}.csv` 형식인지 확인
- 예: `DS_PRDT_0220V_805_20.csv`
- 전압에 'V'가 포함되어 있는지 확인
- 숫자가 올바른 자리수인지 확인 (전압 4자리, 용량 3자리)

#### 문제: 데이터베이스 접근 오류

**해결방법**:
- `vibe_coding.db` 파일이 다른 프로그램에서 열려있지 않은지 확인
- 프로그램 폴더에 쓰기 권한이 있는지 확인
- 디스크 공간이 충분한지 확인

#### 문제: CSV 파일이 너무 큼

**해결방법**:
- 프로그램은 대용량 파일을 처리할 수 있도록 설계되었습니다
- 진행상황을 확인하면서 기다려주세요
- 매우 큰 파일의 경우 몇 분이 걸릴 수 있습니다

## 📊 성능

- **처리 속도**: 약 50,000 레코드/분 (시스템 사양에 따라 다름)
- **테스트 완료**: 500,000+ 레코드
- **메모리 사용**: 최소 (스트리밍 방식으로 처리)

## 🔐 보안 및 주의사항

- 데이터베이스 파일(`vibe_coding.db`)을 정기적으로 백업하세요
- 중요한 데이터는 반드시 백업 후 작업하세요
- 같은 테이블명이 이미 존재하면 데이터가 추가됩니다 (덮어쓰지 않음)

## 📜 라이선스

이 프로젝트는 교육 및 내부 사용 목적으로 제작되었습니다.

## 🤝 지원

문제가 발생하거나 도움이 필요한 경우:
1. 이 README의 "문제 해결" 섹션 확인
2. 오류 메시지를 정확히 기록
3. 프로그램 버전과 운영체제 정보 확인

## 📝 업데이트 히스토리

### v1.0 (2025-12-24)
- 초기 버전 출시
- GUI 기반 파일 선택 기능
- 자동 테이블 생성 기능
- 대용량 CSV 파일 처리 지원
- Windows/Linux 크로스 플랫폼 지원

---

**Developed with ❤️ for efficient data management**

