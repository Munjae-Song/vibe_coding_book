"""
CSV to SQLite DB 임포트 프로그램
CSV 파일을 GUI를 통해 선택하고 SQLite 데이터베이스에 저장하는 프로그램
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import csv
import sqlite3
import re
from datetime import datetime
import os


class CSVtoDBApp:
    """CSV 파일을 데이터베이스에 임포트하는 GUI 애플리케이션"""
    
    def __init__(self, root):
        """
        애플리케이션 초기화
        Args:
            root: Tkinter 루트 윈도우
        """
        self.root = root
        self.root.title("CSV to SQLite DB Importer")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        
        # 선택된 CSV 파일 경로를 저장할 변수
        self.csv_file_path = None
        
        # DB 파일 경로 (현재 디렉토리의 vibe_coding.db)
        self.db_path = os.path.join(os.path.dirname(__file__), "vibe_coding.db")
        
        # GUI 요소 생성
        self.create_widgets()
    
    def create_widgets(self):
        """GUI 위젯(버튼, 라벨 등) 생성"""
        
        # 제목 라벨
        title_label = tk.Label(
            self.root,
            text="CSV to SQLite Database Importer",
            font=("Arial", 16, "bold"),
            pady=20
        )
        title_label.pack()
        
        # 파일 선택 프레임
        file_frame = tk.Frame(self.root, pady=10)
        file_frame.pack(fill=tk.X, padx=20)
        
        # 파일 경로 표시 라벨
        self.file_path_label = tk.Label(
            file_frame,
            text="선택된 파일: 없음",
            font=("Arial", 10),
            anchor="w",
            bg="#f0f0f0",
            relief=tk.SUNKEN,
            padx=10,
            pady=5
        )
        self.file_path_label.pack(fill=tk.X, pady=5)
        
        # 파일 선택 버튼
        select_btn = tk.Button(
            file_frame,
            text="📁 CSV 파일 선택",
            font=("Arial", 12),
            command=self.select_csv_file,
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        select_btn.pack(pady=10)
        
        # 구분선
        separator = ttk.Separator(self.root, orient='horizontal')
        separator.pack(fill='x', padx=20, pady=10)
        
        # 테이블 정보 프레임
        info_frame = tk.Frame(self.root, pady=10)
        info_frame.pack(fill=tk.BOTH, padx=20, expand=True)
        
        info_label = tk.Label(
            info_frame,
            text="테이블 정보",
            font=("Arial", 12, "bold")
        )
        info_label.pack(anchor="w")
        
        # 테이블 정보 표시 텍스트박스
        self.info_text = tk.Text(
            info_frame,
            height=10,
            font=("Arial", 10),
            bg="#f9f9f9",
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.info_text.pack(fill=tk.BOTH, expand=True, pady=5)
        self.info_text.config(state=tk.DISABLED)
        
        # 데이터 전송 버튼
        import_btn = tk.Button(
            self.root,
            text="⬆ 데이터베이스로 전송",
            font=("Arial", 12, "bold"),
            command=self.import_to_db,
            bg="#2196F3",
            fg="white",
            padx=20,
            pady=15,
            cursor="hand2"
        )
        import_btn.pack(pady=20)
        
        # 상태 표시줄
        self.status_label = tk.Label(
            self.root,
            text="준비",
            font=("Arial", 9),
            anchor="w",
            bg="#e0e0e0",
            padx=10,
            pady=5
        )
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM)
    
    def select_csv_file(self):
        """CSV 파일 선택 다이얼로그 표시 및 파일 정보 분석"""
        
        # 파일 선택 다이얼로그 열기
        file_path = filedialog.askopenfilename(
            title="CSV 파일 선택",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialdir=os.path.dirname(__file__)
        )
        
        # 파일이 선택되지 않은 경우 (취소 버튼)
        if not file_path:
            return
        
        # 선택된 파일 경로 저장
        self.csv_file_path = file_path
        
        # 파일명만 추출
        file_name = os.path.basename(file_path)
        
        # 파일 경로 라벨 업데이트
        self.file_path_label.config(text=f"선택된 파일: {file_name}")
        
        # 파일명 분석 및 테이블 정보 표시
        self.analyze_filename(file_name)
        
        # 상태 업데이트
        self.status_label.config(text=f"파일 선택됨: {file_name}")
    
    def analyze_filename(self, filename):
        """
        CSV 파일명을 분석하여 테이블 이름과 정보 추출
        
        파일명 형식: DS_PRDT_0220V_805_20.csv
        - DS_PRDT_: 회사명 + 제품명
        - 0220V: 전압 (테이블명에는 V 제외)
        - 805: 용량
        - 20: 년도
        
        Args:
            filename: 분석할 파일명
        """
        
        # 정규식을 사용하여 파일명 파싱
        # 패턴: (접두사)_(전압V)_(용량)_(년도).csv
        pattern = r"^(.+)_(\d+)V_(\d+)_(\d+)\.csv$"
        match = re.match(pattern, filename)
        
        if not match:
            # 파일명 형식이 맞지 않는 경우
            self.update_info_text(
                "오류: 파일명 형식이 올바르지 않습니다.\n"
                "올바른 형식: DS_PRDT_0220V_805_20.csv\n"
                "- 접두사_전압V_용량_년도.csv"
            )
            self.csv_file_path = None  # 파일 선택 취소
            return
        
        # 파일명 구성 요소 추출
        prefix = match.group(1)      # DS_PRDT
        voltage = match.group(2)     # 0220
        capacity = match.group(3)    # 805
        year = match.group(4)        # 20
        
        # 테이블 이름 생성 (V 제외)
        table_name = f"{prefix}_{voltage}_{capacity}_{year}"
        
        # 테이블 정보 표시
        info = f"""
파일명 분석 결과:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
원본 파일명: {filename}
생성될 테이블명: {table_name}

파일명 구성:
  • 회사명+제품: {prefix}
  • 전압: {voltage} (원본: {voltage}V)
  • 용량: {capacity}
  • 년도: {year}

테이블 필드 (8개):
  1. id           : INTEGER (자동 증가 기본키)
  2. spec         : TEXT (제품 사양)
  3. ins_date     : TEXT (검사 날짜/시간)
  4. mchn_no      : TEXT (설비 번호)
  5. inspct_rnd   : TEXT (검사 차수)
  6. capacitance  : REAL (정전용량 측정값)
  7. loss         : TEXT (손실 측정값)
  8. created_at   : TIMESTAMP (레코드 생성 시간)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        
        self.update_info_text(info)
    
    def update_info_text(self, text):
        """정보 텍스트박스 내용 업데이트"""
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(1.0, text)
        self.info_text.config(state=tk.DISABLED)
    
    def parse_table_name(self, filename):
        """
        파일명에서 테이블 이름 추출
        
        Args:
            filename: CSV 파일명
            
        Returns:
            str: 테이블 이름 (형식이 맞지 않으면 None)
        """
        pattern = r"^(.+)_(\d+)V_(\d+)_(\d+)\.csv$"
        match = re.match(pattern, filename)
        
        if not match:
            return None
        
        prefix = match.group(1)
        voltage = match.group(2)
        capacity = match.group(3)
        year = match.group(4)
        
        return f"{prefix}_{voltage}_{capacity}_{year}"
    
    def import_to_db(self):
        """CSV 데이터를 데이터베이스로 임포트"""
        
        # 파일이 선택되지 않은 경우
        if not self.csv_file_path:
            messagebox.showwarning("경고", "먼저 CSV 파일을 선택해주세요.")
            return
        
        # 파일이 존재하는지 확인
        if not os.path.exists(self.csv_file_path):
            messagebox.showerror("오류", "선택한 파일이 존재하지 않습니다.")
            return
        
        # 파일명에서 테이블 이름 추출
        filename = os.path.basename(self.csv_file_path)
        table_name = self.parse_table_name(filename)
        
        if not table_name:
            messagebox.showerror(
                "오류",
                "파일명 형식이 올바르지 않습니다.\n"
                "올바른 형식: DS_PRDT_0220V_805_20.csv"
            )
            return
        
        try:
            # 상태 업데이트
            self.status_label.config(text="데이터베이스 연결 중...")
            self.root.update()
            
            # SQLite 데이터베이스 연결
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 테이블 생성 (이미 존재하면 생성하지 않음)
            self.status_label.config(text=f"테이블 '{table_name}' 확인 중...")
            self.root.update()
            
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                spec TEXT,
                ins_date TEXT,
                mchn_no TEXT,
                inspct_rnd TEXT,
                capacitance REAL,
                loss REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(create_table_query)
            
            # 테이블이 새로 생성되었는지 확인
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (table_name,)
            )
            table_exists = cursor.fetchone()
            
            if table_exists:
                self.status_label.config(text=f"테이블 '{table_name}' 준비 완료")
            else:
                self.status_label.config(text=f"테이블 '{table_name}' 생성 완료")
            
            self.root.update()
            
            # CSV 파일 읽기 및 데이터 삽입
            self.status_label.config(text="CSV 파일 읽는 중...")
            self.root.update()
            
            # 삽입된 레코드 수 카운트
            inserted_count = 0
            
            with open(self.csv_file_path, 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                
                # CSV의 각 행을 데이터베이스에 삽입
                for row in csv_reader:
                    insert_query = f"""
                    INSERT INTO {table_name} 
                    (spec, ins_date, mchn_no, inspct_rnd, capacitance, loss)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """
                    
                    # capacitance 값을 REAL 타입으로 변환
                    try:
                        capacitance_value = float(row['capacitance'])
                    except (ValueError, KeyError):
                        capacitance_value = 0.0
                    
                    cursor.execute(insert_query, (
                        row.get('spec', ''),
                        row.get('ins_date', ''),
                        row.get('mchn_no', ''),
                        row.get('inspct_rnd', ''),
                        capacitance_value,
                        row.get('loss', '')
                    ))
                    
                    inserted_count += 1
                    
                    # 1000개마다 진행상황 업데이트
                    if inserted_count % 1000 == 0:
                        self.status_label.config(
                            text=f"데이터 삽입 중... ({inserted_count:,}개)"
                        )
                        self.root.update()
            
            # 변경사항 커밋
            conn.commit()
            
            # 데이터베이스 연결 종료
            cursor.close()
            conn.close()
            
            # 성공 메시지
            self.status_label.config(text="완료!")
            messagebox.showinfo(
                "성공",
                f"CSV 데이터를 데이터베이스에 성공적으로 저장했습니다.\n\n"
                f"테이블명: {table_name}\n"
                f"삽입된 레코드 수: {inserted_count:,}개\n"
                f"데이터베이스: {os.path.basename(self.db_path)}"
            )
            
            self.status_label.config(
                text=f"완료: {inserted_count:,}개 레코드가 '{table_name}' 테이블에 저장됨"
            )
            
        except sqlite3.Error as e:
            # 데이터베이스 오류 처리
            messagebox.showerror(
                "데이터베이스 오류",
                f"데이터베이스 작업 중 오류가 발생했습니다:\n{str(e)}"
            )
            self.status_label.config(text="오류 발생")
            
        except Exception as e:
            # 기타 오류 처리
            messagebox.showerror(
                "오류",
                f"예상치 못한 오류가 발생했습니다:\n{str(e)}"
            )
            self.status_label.config(text="오류 발생")
        
        finally:
            # 연결이 열려있다면 닫기
            try:
                if 'conn' in locals() and conn:
                    conn.close()
            except:
                pass


def main():
    """메인 함수: 애플리케이션 실행"""
    
    # Tkinter 루트 윈도우 생성
    root = tk.Tk()
    
    # 애플리케이션 인스턴스 생성
    app = CSVtoDBApp(root)
    
    # 이벤트 루프 시작
    root.mainloop()


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수 호출
    main()









