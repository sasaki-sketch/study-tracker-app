"""
データベース操作サービス
"""
import sqlite3
from contextlib import contextmanager
from datetime import date, datetime
from pathlib import Path
from typing import List, Optional

from models.record import StudyRecord, CumulativeStats

DB_PATH = Path.home() / "study_app" / "study_records.db"


class DatabaseService:
    """データベース操作クラス"""

    def __init__(self):
        self.db_path = DB_PATH

    @contextmanager
    def get_connection(self):
        """DB接続を取得（コンテキストマネージャー）

        Usage:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                # ... database operations
        """
        conn = sqlite3.connect(self.db_path, check_same_thread=False, timeout=30.0)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def save_record(self, record: StudyRecord) -> int:
        """学習記録を保存"""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                INSERT OR REPLACE INTO records
                (date, phase, shindan_time, shindan_subject, shindan_content, shindan_issue,
                 toukei_time, toukei_content, toukei_issue, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                record.date.isoformat(),
                record.phase,
                record.shindan_time,
                record.shindan_subject,
                record.shindan_content,
                record.shindan_issue,
                record.toukei_time,
                record.toukei_content,
                record.toukei_issue,
                datetime.now().isoformat()
            ))

            return cursor.lastrowid

    def get_record_by_date(self, target_date: date) -> Optional[StudyRecord]:
        """指定日の記録を取得"""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM records WHERE date = ?
            ''', (target_date.isoformat(),))

            row = cursor.fetchone()

            if row:
                return StudyRecord(
                    id=row['id'],
                    date=date.fromisoformat(row['date']),
                    phase=row['phase'],
                    shindan_time=row['shindan_time'],
                    shindan_subject=row['shindan_subject'] or '',
                    shindan_content=row['shindan_content'] or '',
                    shindan_issue=row['shindan_issue'] or '',
                    toukei_time=row['toukei_time'],
                    toukei_content=row['toukei_content'] or '',
                    toukei_issue=row['toukei_issue'] or '',
                )
            return None

    def get_cumulative_stats(self) -> CumulativeStats:
        """累計統計を取得（関連資格の学習記録を除外）"""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT
                    COALESCE(SUM(shindan_time), 0) as shindan_total,
                    COALESCE(SUM(toukei_time), 0) as toukei_total
                FROM records
                WHERE phase != '関連資格'
            ''')

            row = cursor.fetchone()

            stats = CumulativeStats(
                shindan_total=row['shindan_total'],
                toukei_total=row['toukei_total'],
                shindan_goal=770.0
            )
            stats.calculate_progress()

            return stats

    def get_all_records(self) -> List[StudyRecord]:
        """全記録を取得"""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM records ORDER BY date DESC
            ''')

            rows = cursor.fetchall()

            records = []
            for row in rows:
                records.append(StudyRecord(
                    id=row['id'],
                    date=date.fromisoformat(row['date']),
                    phase=row['phase'],
                    shindan_time=row['shindan_time'],
                    shindan_subject=row['shindan_subject'] or '',
                    shindan_content=row['shindan_content'] or '',
                    shindan_issue=row['shindan_issue'] or '',
                    toukei_time=row['toukei_time'],
                    toukei_content=row['toukei_content'] or '',
                    toukei_issue=row['toukei_issue'] or '',
                ))

            return records

    def get_recent_records(self, limit: int = 5) -> List[StudyRecord]:
        """最近の記録を取得（関連資格を除く）"""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM records
                WHERE phase != '関連資格'
                ORDER BY date DESC
                LIMIT ?
            ''', (limit,))

            rows = cursor.fetchall()

            records = []
            for row in rows:
                records.append(StudyRecord(
                    id=row['id'],
                    date=date.fromisoformat(row['date']),
                    phase=row['phase'],
                    shindan_time=row['shindan_time'],
                    shindan_subject=row['shindan_subject'] or '',
                    shindan_content=row['shindan_content'] or '',
                    shindan_issue=row['shindan_issue'] or '',
                    toukei_time=row['toukei_time'],
                    toukei_content=row['toukei_content'] or '',
                    toukei_issue=row['toukei_issue'] or '',
                ))

            return records

    def get_subjects(self) -> List[tuple]:
        """科目リストを取得"""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT name, abbreviation FROM subjects ORDER BY id')
            subjects = cursor.fetchall()

            return [(s['name'], s['abbreviation']) for s in subjects]
