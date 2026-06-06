"""
データベース初期化スクリプト
"""
import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "study_app" / "study_records.db"

def init_database():
    """データベースとテーブルを初期化"""

    # データベース接続
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 学習記録テーブル
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL UNIQUE,
        phase TEXT,

        -- 診断士
        shindan_time REAL DEFAULT 0,
        shindan_subject TEXT,
        shindan_content TEXT,
        shindan_issue TEXT,

        -- 統計
        toukei_time REAL DEFAULT 0,
        toukei_content TEXT,
        toukei_issue TEXT,

        -- メタデータ
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 科目マスタテーブル
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        abbreviation TEXT,
        category TEXT DEFAULT '1次試験',
        target_hours REAL DEFAULT 90,
        baseline_hours REAL DEFAULT 0,
        completed BOOLEAN DEFAULT 0
    )
    ''')

    # 科目マスタの初期データ (名前, 略称, カテゴリ, 目標時間, 基礎学習時間, 完了)
    # config/subjects.pyと一致させる（中点あり）
    subjects = [
        # 1次試験科目
        ('財務・会計', '財務', '1次試験', 100, 0, 0),
        ('企業経営理論', '企業経営', '1次試験', 90, 0, 0),
        ('運営管理', '運営', '1次試験', 80, 0, 0),
        ('経済学・経済政策', '経済', '1次試験', 90, 0, 0),
        ('経営情報システム', '情報', '1次試験', 70, 0, 0),
        ('経営法務', '法務', '1次試験', 70, 0, 0),
        ('中小企業経営・政策', '中小', '1次試験', 100, 0, 0),
        # 2次試験科目
        ('事例I（組織・人事）', '事例I', '2次試験', 50, 0, 0),
        ('事例II（マーケティング）', '事例II', '2次試験', 50, 0, 0),
        ('事例III（生産・技術）', '事例III', '2次試験', 50, 0, 0),
        ('事例IV（財務）', '事例IV', '2次試験', 50, 0, 0),
    ]

    # INSERT OR IGNORE: 既存レコードは上書きしない（target_hoursを保護）
    for subject in subjects:
        cursor.execute('''
            INSERT INTO subjects (name, abbreviation, category, target_hours, baseline_hours, completed)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET
                abbreviation = excluded.abbreviation
        ''', subject)

    # マイグレーションSQL実行
    migration_file = Path(__file__).parent / "migrations" / "001_add_events.sql"
    if migration_file.exists():
        with open(migration_file, 'r', encoding='utf-8') as f:
            migration_sql = f.read()
            cursor.executescript(migration_sql)
        print(f"✅ マイグレーション実行完了: {migration_file.name}")

    conn.commit()
    conn.close()

    print(f"✅ データベース初期化完了: {DB_PATH}")

if __name__ == "__main__":
    init_database()
