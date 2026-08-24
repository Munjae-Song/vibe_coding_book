# ======================================================================
# CSV 파일의 데이터를 SQLite 데이터베이스로 업로드하는 프로그램
# ======================================================================
# 이 프로그램은 CSV 파일의 생산 데이터를 읽어서 SQLite DB에
# 저장합니다.
#
# 작동 순서:
# 1. CSV 파일을 열어서 모든 데이터를 메모리에 저장
# 2. SQLite 데이터베이스에 연결
# 3. 메모리에 저장된 데이터를 DB 테이블에 순차적으로 입력
# 4. 입력된 데이터의 정확성 검증
# 5. 데이터베이스 연결 종료
# ======================================================================

import csv  # CSV 파일을 읽고 쓰기 위한 파이썬 표준 라이브러리
import sqlite3  # SQLite DB를 사용하기 위한 파이썬 표준 라이브러리


def main():
    """메인 함수: 프로그램의 전체 흐름을 제어합니다."""
    # ==================================================================
    # 설정 부분: 파일 경로와 테이블 이름을 지정합니다
    # ==================================================================
    csv_file = 'manu_quantity.csv'  # 읽을 CSV 파일의 이름
    db_file = 'vibe_coding.db'  # SQLite 데이터베이스 파일 이름
    table_name = 'manufacturing_quantity'  # 데이터를 저장할 테이블 이름

    # ==================================================================
    # 1단계: CSV 파일을 열어서 모든 데이터를 메모리에 저장
    # ==================================================================
    print(f"CSV 파일 '{csv_file}'을 읽는 중...")

    # 데이터를 저장할 빈 리스트를 생성합니다
    # 리스트는 여러 개의 데이터를 순서대로 저장하는 자료구조입니다
    data_list = []

    # with 문: 파일을 열고 작업이 끝나면 자동으로 닫아줍니다
    # 'r': 읽기 모드(read)로 파일을 엽니다
    # encoding='utf-8-sig': 한글이 포함된 CSV 파일을 올바르게
    #                       읽기 위한 설정
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        # csv.DictReader: CSV 파일을 딕셔너리 형태로 읽어줍니다
        # 각 행이 {헤더이름: 값} 형태의 딕셔너리로 변환됩니다
        csv_reader = csv.DictReader(file)

        # CSV 파일의 헤더(첫 번째 줄)를 출력하여 확인합니다
        print(f"CSV 헤더: {csv_reader.fieldnames}")

        # for 반복문: CSV 파일의 각 행(row)을 하나씩 읽어서
        # 처리합니다
        for row in csv_reader:
            # CSV 파일의 헤더 이름을 자동으로 감지합니다
            # 'date_time' 컬럼이 있으면 사용하고, 없으면 첫 번째
            # 컬럼을 사용
            if 'date_time' in row:
                date_col = 'date_time'
            else:
                date_col = list(row.keys())[0]

            # 'mnft_quantity' 컬럼이 있으면 사용하고, 없으면
            # 두 번째 컬럼을 사용
            if 'mnft_quantity' in row:
                qty_col = 'mnft_quantity'
            else:
                qty_col = list(row.keys())[1]

            # 읽어온 데이터를 딕셔너리 형태로 리스트에 추가합니다
            # strip(): 문자열 양 끝의 공백을 제거합니다
            # int(): 문자열을 정수로 변환합니다
            data_list.append({
                'mnft_date': row[date_col].strip(),  # 생산 날짜
                'mnft_quantity': int(row[qty_col].strip())  # 생산량
            })

    # len(): 리스트의 길이(항목 개수)를 반환합니다
    csv_record_count = len(data_list)
    print(f"CSV 파일에서 {csv_record_count}개의 레코드를 읽었습니다.")
    

    # ==================================================================
    # 2단계: SQLite 데이터베이스에 연결
    # ==================================================================
    print(f"\nDB 파일 '{db_file}'에 접속 중...")

    # sqlite3.connect(): SQLite 데이터베이스 파일에 연결합니다
    # 파일이 없으면 새로 생성되지만, 여기서는 기존 파일을 사용합니다
    conn = sqlite3.connect(db_file)

    # cursor(): SQL 명령을 실행하기 위한 커서 객체를 생성합니다
    # 커서는 데이터베이스와 상호작용하기 위한 도구입니다
    cursor = conn.cursor()

    # ==================================================================
    # 3단계: 데이터를 데이터베이스 테이블에 순차적으로 입력
    # ==================================================================
    print(f"테이블 '{table_name}'에 데이터를 입력 중...")

    # 실제로 입력된 레코드 개수를 세기 위한 변수
    insert_count = 0

    # for 반복문: 메모리에 저장된 데이터를 하나씩 꺼내서 DB에
    # 입력합니다
    for data in data_list:
        # cursor.execute(): SQL 명령을 실행합니다
        # INSERT INTO: 새로운 데이터를 테이블에 추가하는 SQL 명령
        # (?, ?): SQL 인젝션 공격을 방지하기 위한 안전한 방식
        #         (placeholder)
        # mnft_id는 자동 증가(AUTOINCREMENT)되므로 입력하지 않습니다
        sql = (
            f"INSERT INTO {table_name} "
            f"(mnft_date, mnft_quantity) VALUES (?, ?)"
        )
        cursor.execute(
            sql,
            (data['mnft_date'], data['mnft_quantity'])
        )
        insert_count += 1  # 입력된 레코드 개수 증가

    # commit(): 데이터베이스에 변경사항을 실제로 저장(확정)합니다
    # commit()을 하지 않으면 데이터가 저장되지 않습니다!
    conn.commit()
    print(f"{insert_count}개의 레코드를 DB에 입력했습니다.")
    

    # ==================================================================
    # 4단계: 데이터가 정확하게 입력되었는지 검증
    # ==================================================================

    # SELECT COUNT(*): 테이블의 전체 레코드 개수를 세는 SQL 명령
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")

    # fetchone(): SQL 쿼리 결과의 첫 번째 행을 가져옵니다
    # [0]: 튜플의 첫 번째 값(레코드 개수)을 추출합니다
    db_record_count = cursor.fetchone()[0]

    # 검증 결과를 화면에 출력합니다
    print(f"\n=== 검증 결과 ===")
    print(f"CSV 파일 레코드 수: {csv_record_count}")
    print(f"DB 테이블 레코드 수: {db_record_count}")

    # if-else 조건문: 세 가지 값이 모두 같은지 확인합니다
    if csv_record_count == insert_count == db_record_count:
        print("[성공] 모든 데이터가 정상적으로 입력되었습니다.")
    else:
        print("[오류] 레코드 수가 일치하지 않습니다. 확인이 필요합니다.")

    # 실제로 저장된 데이터의 샘플을 확인합니다
    print("\n=== 입력된 데이터 샘플 (처음 5개) ===")

    # SELECT: 데이터를 조회하는 SQL 명령
    # LIMIT 5: 처음 5개의 레코드만 가져옵니다
    sql = (
        f"SELECT mnft_id, mnft_date, mnft_quantity "
        f"FROM {table_name} LIMIT 5"
    )
    cursor.execute(sql)

    # fetchall(): 쿼리 결과의 모든 행을 리스트로 가져옵니다
    rows = cursor.fetchall()

    # 가져온 각 행을 화면에 출력합니다
    for row in rows:
        # row[0]: mnft_id (자동 생성된 ID)
        # row[1]: mnft_date (생산 날짜)
        # row[2]: mnft_quantity (생산량)
        print(f"ID: {row[0]}, 날짜: {row[1]}, 생산량: {row[2]}")

    # ==================================================================
    # 5단계: 데이터베이스 연결 종료
    # ==================================================================

    # close(): 데이터베이스 연결을 닫습니다
    # 항상 작업이 끝나면 연결을 닫아야 리소스가 해제됩니다
    conn.close()
    print("\nDB 연결을 종료했습니다.")
    print("프로그램을 종료합니다.")


# ======================================================================
# 프로그램 실행 부분
# ======================================================================
# __name__ == "__main__": 이 파일이 직접 실행될 때만 main()
# 함수를 호출합니다
# 다른 파일에서 import 되었을 때는 실행되지 않습니다
if __name__ == "__main__":
    main()

