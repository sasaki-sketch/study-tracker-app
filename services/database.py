"""
データベース操作サービス
"""
import json
import sqlite3
from contextlib import contextmanager
from datetime import date, datetime
from pathlib import Path
from typing import List, Optional

from models.record import StudyRecord, CumulativeStats, StudySession

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

            # 旧形式の実績時間を取得（後方互換性のため残す）
            cursor.execute('''
                SELECT
                    COALESCE(SUM(shindan_time), 0) as shindan_total,
                    COALESCE(SUM(toukei_time), 0) as toukei_total
                FROM records
                WHERE phase != '関連資格'
            ''')
            row = cursor.fetchone()

            # study_sessionsから1次・2次別の実績時間を取得
            cursor.execute('''
                SELECT
                    COALESCE(SUM(CASE WHEN s.qualification = 'shindan_1ji' THEN s.time_hours ELSE 0 END), 0) as shindan_1ji_total,
                    COALESCE(SUM(CASE WHEN s.qualification = 'shindan_2ji' THEN s.time_hours ELSE 0 END), 0) as shindan_2ji_total,
                    COALESCE(SUM(CASE WHEN s.qualification = 'toukei' THEN s.time_hours ELSE 0 END), 0) as toukei_total
                FROM study_sessions s
                JOIN records r ON s.record_id = r.id
                WHERE r.phase != '関連資格'
            ''')
            session_row = cursor.fetchone()

            # 1次試験の目標時間合計をDBから取得
            cursor.execute('''
                SELECT COALESCE(SUM(target_hours), 0) as goal
                FROM subjects
                WHERE category = '1次試験'
            ''')
            shindan_1ji_goal = cursor.fetchone()['goal'] or 520.0

            # 2次試験の目標時間合計をDBから取得
            cursor.execute('''
                SELECT COALESCE(SUM(target_hours), 0) as goal
                FROM subjects
                WHERE category = '2次試験'
            ''')
            shindan_2ji_goal = cursor.fetchone()['goal'] or 200.0

            # 統計検定の目標時間をDBから取得（なければデフォルト80h）
            cursor.execute('''
                SELECT COALESCE(SUM(target_hours), 0) as goal
                FROM subjects
                WHERE category = '統計検定'
            ''')
            toukei_goal = cursor.fetchone()['goal'] or 80.0

            stats = CumulativeStats(
                # 旧形式（後方互換性のため残す）
                shindan_total=row['shindan_total'],
                shindan_goal=240.0,  # 基礎固め期の目標時間
                toukei_total=row['toukei_total'],
                # 新形式（1次・2次分離）
                shindan_1ji_total=session_row['shindan_1ji_total'],
                shindan_1ji_goal=shindan_1ji_goal,
                shindan_2ji_total=session_row['shindan_2ji_total'],
                shindan_2ji_goal=shindan_2ji_goal,
                toukei_goal=toukei_goal
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

    # ============================================
    # イベント関連メソッド
    # ============================================

    def save_event(self, event) -> int:
        """イベント保存

        Args:
            event: StudyEventオブジェクト(PastExamEvent/MaterialLapEvent/MockExamEvent)

        Returns:
            保存したレコードのID
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # イベントタイプ別の詳細データをJSON化
            details = {}

            if event.event_type == 'past_exam':
                details = {
                    'exam_year': event.exam_year,
                    'question_range': event.question_range,
                    'correct_count': event.correct_count,
                    'total_count': event.total_count,
                    'time_spent': event.time_spent
                }
            elif event.event_type == 'material_lap':
                details = {
                    'material_id': event.material_id,
                    'start_page': event.start_page,
                    'end_page': event.end_page,
                    'time_spent': event.time_spent,
                    'understanding': event.understanding
                }
            elif event.event_type == 'mock_exam':
                details = {
                    'exam_name': event.exam_name,
                    'exam_type': event.exam_type,
                    'total_score': event.total_score,
                    'max_score': event.max_score,
                    'subject_scores': event.subject_scores,
                    'case_grades': event.case_grades
                }

            cursor.execute('''
                INSERT INTO study_events
                (event_type, date, subject, memo, details, created_at)
                VALUES (?, ?, ?, ?, ?, datetime('now'))
            ''', (
                event.event_type,
                event.date.isoformat(),
                event.subject,
                event.memo,
                json.dumps(details, ensure_ascii=False)
            ))

            event_id = cursor.lastrowid

            # n8n Webhook送信（非同期、失敗しても処理は継続）
            try:
                from utils.webhook import send_event_to_n8n
                event_data = {
                    'event_type': event.event_type,
                    'subject': event.subject,
                    'date': event.date.isoformat(),
                    'details': details
                }
                send_event_to_n8n(event_data)
            except Exception as e:
                # Webhook送信失敗してもメイン処理は継続
                print(f"Webhook送信失敗（イベント保存は成功）: {str(e)}")

            return event_id

    def get_events_by_type(self, event_type: str, limit: int = 5) -> List[dict]:
        """イベントタイプ別取得

        Args:
            event_type: 'past_exam' | 'material_lap' | 'mock_exam'
            limit: 取得件数

        Returns:
            イベントリスト(辞書形式)
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM study_events
                WHERE event_type = ?
                ORDER BY date DESC
                LIMIT ?
            ''', (event_type, limit))

            rows = cursor.fetchall()

            events = []
            for row in rows:
                event_data = {
                    'id': row['id'],
                    'event_type': row['event_type'],
                    'date': row['date'],
                    'subject': row['subject'],
                    'memo': row['memo'],
                    'details': json.loads(row['details']) if row['details'] else {}
                }
                events.append(event_data)

            return events

    def get_recent_events(self, limit: int = 10) -> List[dict]:
        """最近のイベント取得(全タイプ混合)

        Args:
            limit: 取得件数

        Returns:
            イベントリスト(辞書形式)
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM study_events
                ORDER BY date DESC, created_at DESC
                LIMIT ?
            ''', (limit,))

            rows = cursor.fetchall()

            events = []
            for row in rows:
                event_data = {
                    'id': row['id'],
                    'event_type': row['event_type'],
                    'date': row['date'],
                    'subject': row['subject'],
                    'memo': row['memo'],
                    'details': json.loads(row['details']) if row['details'] else {}
                }
                events.append(event_data)

            return events

    # ============================================
    # 教材関連メソッド
    # ============================================

    def save_material(self, material) -> int:
        """教材保存

        Args:
            material: Materialオブジェクト

        Returns:
            保存したレコードのID
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            if material.id:
                # 更新
                cursor.execute('''
                    UPDATE materials SET
                        name = ?, subject = ?, material_type = ?,
                        target_laps = ?, updated_at = datetime('now')
                    WHERE id = ?
                ''', (
                    material.name, material.subject, material.material_type,
                    material.target_laps, material.id
                ))
                return material.id
            else:
                # 新規登録
                cursor.execute('''
                    INSERT INTO materials
                    (name, subject, material_type, target_laps, created_at)
                    VALUES (?, ?, ?, ?, datetime('now'))
                ''', (
                    material.name, material.subject, material.material_type,
                    material.target_laps
                ))
                return cursor.lastrowid

    def get_all_materials(self) -> List[dict]:
        """全教材取得

        Returns:
            教材リスト(辞書形式)
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM materials
                ORDER BY last_study_date DESC, name
            ''')

            rows = cursor.fetchall()

            materials = []
            for row in rows:
                material_data = {
                    'id': row['id'],
                    'name': row['name'],
                    'subject': row['subject'],
                    'material_type': row['material_type'],
                    'target_laps': row['target_laps'],
                    'current_lap': row['current_lap'],
                    'total_time': row['total_time'],
                    'avg_understanding': row['avg_understanding'],
                    'last_study_date': row['last_study_date']
                }
                materials.append(material_data)

            return materials

    def get_material_by_id(self, material_id: int) -> Optional[dict]:
        """教材ID検索

        Args:
            material_id: 教材ID

        Returns:
            教材データ(辞書形式) or None
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM materials WHERE id = ?', (material_id,))
            row = cursor.fetchone()

            if row:
                return {
                    'id': row['id'],
                    'name': row['name'],
                    'subject': row['subject'],
                    'material_type': row['material_type'],
                    'target_laps': row['target_laps'],
                    'current_lap': row['current_lap'],
                    'total_time': row['total_time'],
                    'avg_understanding': row['avg_understanding'],
                    'last_study_date': row['last_study_date']
                }
            return None

    def update_material_progress(self, material_id: int):
        """教材進捗更新(イベント記録時に自動実行)

        study_eventsテーブルから該当教材の統計を再計算してmaterialsを更新

        Args:
            material_id: 教材ID
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # 周回数と統計の計算
            cursor.execute('''
                SELECT
                    COUNT(*) as lap_count,
                    SUM(json_extract(details, '$.time_spent')) as total_time,
                    AVG(json_extract(details, '$.understanding')) as avg_understanding,
                    MAX(date) as last_date
                FROM study_events
                WHERE event_type = 'material_lap'
                  AND json_extract(details, '$.material_id') = ?
            ''', (material_id,))

            row = cursor.fetchone()

            if row and row['lap_count'] > 0:
                cursor.execute('''
                    UPDATE materials SET
                        current_lap = ?,
                        total_time = ?,
                        avg_understanding = ?,
                        last_study_date = ?,
                        updated_at = datetime('now')
                    WHERE id = ?
                ''', (
                    row['lap_count'],
                    row['total_time'] or 0.0,
                    round(row['avg_understanding'], 1) if row['avg_understanding'] else 0.0,
                    row['last_date'],
                    material_id
                ))

    # ============================================
    # StudySession（複数科目記録）関連メソッド
    # ============================================

    def save_study_sessions(self, record_id: int, sessions: List[StudySession]) -> None:
        """学習セッションを保存（複数科目対応）

        Args:
            record_id: 親レコードID
            sessions: StudySessionのリスト
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # 新しいセッションの資格タイプを取得
            new_qualifications = set(s.qualification for s in sessions)

            # 新しいセッションに含まれる資格のセッションのみ削除
            # （含まれない資格のセッションは保持）
            if new_qualifications:
                placeholders = ','.join('?' for _ in new_qualifications)
                cursor.execute(
                    f'DELETE FROM study_sessions WHERE record_id = ? AND qualification IN ({placeholders})',
                    (record_id, *new_qualifications)
                )

            # 新規セッションを挿入
            for session in sessions:
                session.validate()  # バリデーション

                cursor.execute('''
                    INSERT INTO study_sessions
                    (record_id, qualification, subject, time_hours, content, issue)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    record_id,
                    session.qualification,
                    session.subject,
                    session.time_hours,
                    session.content,
                    session.issue
                ))

    def get_study_sessions(self, record_id: int) -> List[StudySession]:
        """指定レコードの学習セッションを取得

        Args:
            record_id: 親レコードID

        Returns:
            StudySessionのリスト
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM study_sessions
                WHERE record_id = ?
                ORDER BY qualification, subject
            ''', (record_id,))

            rows = cursor.fetchall()

            sessions = []
            for row in rows:
                sessions.append(StudySession(
                    id=row['id'],
                    record_id=row['record_id'],
                    qualification=row['qualification'],
                    subject=row['subject'],
                    time_hours=row['time_hours'],
                    content=row['content'] or '',
                    issue=row['issue'] or ''
                ))

            return sessions

    def get_sessions_by_subject(self, subject: str) -> List[dict]:
        """科目別の学習セッション一覧を取得（統計用）

        Args:
            subject: 科目名

        Returns:
            セッション情報のリスト（record情報含む）
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT
                    s.*,
                    r.date,
                    r.phase
                FROM study_sessions s
                JOIN records r ON s.record_id = r.id
                WHERE s.subject = ?
                ORDER BY r.date DESC
            ''', (subject,))

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

    def aggregate_sessions_by_subject(self) -> List[dict]:
        """科目別の集計データを取得（N+1問題解消版）

        Returns:
            科目別集計データ [{'subject': str, 'total_hours': float, 'session_count': int}]
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT
                    s.subject,
                    s.qualification,
                    SUM(s.time_hours) as total_hours,
                    COUNT(s.id) as session_count,
                    MAX(r.date) as last_study_date
                FROM study_sessions s
                JOIN records r ON s.record_id = r.id
                WHERE r.phase != '関連資格'
                GROUP BY s.subject, s.qualification
                ORDER BY total_hours DESC
            ''', ())

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

    def get_subject_settings(self, category: str = '1次試験') -> List[dict]:
        """科目設定情報を取得

        Args:
            category: 科目カテゴリ（'1次試験', '2次試験'等）

        Returns:
            科目設定リスト [{'name', 'standard_hours', 'target_hours', 'target_score', 'notes'}]
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT
                    name,
                    abbreviation,
                    category,
                    standard_hours,
                    target_hours,
                    baseline_hours,
                    target_score,
                    notes,
                    completed
                FROM subjects
                WHERE category = ?
                ORDER BY id
            ''', (category,))

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

    def get_subject_list(self, category: str = '1次試験') -> List[str]:
        """科目名のリストを取得

        Args:
            category: 科目カテゴリ（'1次試験', '2次試験'等）

        Returns:
            科目名のリスト
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT name
                FROM subjects
                WHERE category = ?
                ORDER BY id
            ''', (category,))

            rows = cursor.fetchall()
            return [row['name'] for row in rows]

    def get_target_hours_dict(self, category: str = '1次試験') -> dict:
        """科目名をキーとした目標時間の辞書を取得

        Args:
            category: 科目カテゴリ（'1次試験', '2次試験'等）

        Returns:
            {科目名: 目標時間} の辞書
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT name, target_hours
                FROM subjects
                WHERE category = ?
                ORDER BY id
            ''', (category,))

            rows = cursor.fetchall()
            return {row['name']: row['target_hours'] for row in rows}

    def get_all_subjects(self) -> List[dict]:
        """全科目の設定情報を取得

        Returns:
            全科目の設定リスト
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT
                    id,
                    name,
                    abbreviation,
                    category,
                    standard_hours,
                    target_hours,
                    baseline_hours,
                    target_score,
                    notes,
                    completed
                FROM subjects
                ORDER BY
                    CASE category
                        WHEN '1次試験' THEN 1
                        WHEN '2次試験' THEN 2
                        ELSE 3
                    END,
                    id
            ''', ())

            rows = cursor.fetchall()

            return [dict(row) for row in rows]
