"""
이 스크립트는 아주 간단한 SQLite 데이터베이스(.db 파일)를 만들고,
그 안에 테이블을 1개 생성하는 예제입니다.

- SQLite는 "파일 1개 = 데이터베이스 1개"인 가벼운 DB입니다.
- 별도의 서버 설치 없이 파이썬 표준 라이브러리 `sqlite3`로 바로 사용할 수 있습니다.
"""

# 파이썬 표준 라이브러리: SQLite DB에 연결/쿼리 실행을 도와주는 모듈
import sqlite3

# 표준 라이브러리: 파일 경로를 문자열보다 안전/편하게 다루게 해주는 클래스(Path)
from pathlib import Path


def create_db_and_table(db_path: Path) -> None:
    """
    지정된 경로(db_path)에 SQLite DB 파일을 만들거나(없으면 생성),
    테이블 `manufacturing_quantity`를 만들거나(없으면 생성) 합니다.

    - db_path: DB 파일의 전체 경로. 예) C:\\...\\vibe_coding.db
    - 반환값: 없음(None). 작업만 수행합니다.
    """

    # DB 파일이 들어갈 "폴더"가 없으면 생성합니다.
    # - db_path.parent: db_path의 "부모 폴더" 경로
    # - parents=True: 중간 폴더가 없어도 함께 생성
    # - exist_ok=True: 이미 폴더가 있어도 에러 내지 않음
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # sqlite3.connect(db_path):
    # - db_path 위치에 DB 파일이 없으면 새로 만듭니다.
    # - 있으면 그 파일에 연결합니다.
    #
    # with ... as conn:
    # - "컨텍스트 매니저" 문법입니다.
    # - 블록이 끝날 때 자동으로 연결을 정리(close)해 주기 때문에 안전합니다.
    with sqlite3.connect(db_path) as conn:
        # conn.execute(...):
        # - SQL 문(문자열)을 실행합니다.
        # - 여기서는 테이블 생성 SQL을 실행합니다.
        conn.execute(
            """
            -- 아래는 SQLite용 SQL 문입니다.
            -- CREATE TABLE: 테이블을 생성합니다.
            -- IF NOT EXISTS: "이미 있으면" 에러 내지 말고 그냥 넘어갑니다.
            CREATE TABLE IF NOT EXISTS manufacturing_quantity (
                -- mnft_id:
                -- - INTEGER: 정수 타입
                -- - PRIMARY KEY: 이 컬럼이 행(row)을 구분하는 대표 키(고유값)
                -- - AUTOINCREMENT: 새 행이 추가될 때마다 1씩 자동 증가
                mnft_id INTEGER PRIMARY KEY AUTOINCREMENT,

                -- mnft_date:
                -- - TEXT: 문자열 타입
                -- - 날짜를 TEXT로 저장(예: "2025-12-16")하는 단순 예제
                --   (더 엄격한 날짜/시간 처리가 필요하면 포맷을 규칙으로 정하는 게 좋아요)
                mnft_date TEXT,

                -- mnft_quantity:
                -- - INTEGER: 수량(정수)
                mnft_quantity INTEGER,

                -- etc:
                -- - TEXT: 기타 메모/비고(설명)
                etc TEXT
            );
            """
        )

        # SQLite는 "변경 사항"이 있을 때 commit()을 해야 파일에 반영됩니다.
        # (CREATE TABLE도 DB 구조를 바꾸는 작업이라 commit이 필요합니다.)
        conn.commit()


def main() -> None:
    """
    이 파일을 직접 실행했을 때 동작하는 진입점(entry point) 함수입니다.
    - DB 파일 경로를 정하고
    - create_db_and_table()을 호출해 DB/테이블을 준비합니다.
    """

    # __file__:
    # - 현재 파이썬 파일(001_create_db_table.py)의 경로를 뜻합니다.
    #
    # Path(__file__).resolve():
    # - 상대경로가 섞여 있어도 "절대경로"로 정리하는데, 파일 이름까지 얻는다.
    #
    # .parent:
    # - 현재 파일이 들어있는 폴더 경로를 얻습니다. 파일 이름은 제외하고 폴더 정보만 얻는다.
    script_dir = Path(__file__).resolve().parent
    

    # DB 파일은 "이 스크립트 파일과 같은 폴더"에 vibe_coding.db 라는 이름으로 둡니다.
    db_path = script_dir / "vibe_coding.db"

    # DB 파일 생성(또는 연결) + 테이블 생성(또는 존재 확인)
    create_db_and_table(db_path)

    # 사용자에게 작업 결과를 출력합니다.
    print(f"DB 생성/확인 완료: {db_path}")
    print("테이블 생성/확인 완료: manufacturing_quantity")


if __name__ == "__main__":
    # 이 파일을 "직접 실행"할 때만 main()을 호출합니다.
    # - 예) python 001_create_db_table.py  -> 실행됨
    # - 다른 파일에서 import 001_create_db_table -> 실행 안 됨
    main()
