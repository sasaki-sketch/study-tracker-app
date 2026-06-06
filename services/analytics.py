"""
分析データ集計サービス
セッションベースの効率的なデータ集計を提供
"""
from typing import List, Dict, Optional, Tuple
from datetime import date, datetime, timedelta
from dataclasses import dataclass
from collections import defaultdict
import sqlite3


@dataclass
class DailySummary:
    """日次サマリー"""
    date: date
    shindan_hours: float  # 一次+二次の合計（後方互換性のため残す）
    toukei_hours: float
    total_hours: float
    phase: str
    session_count: int
    shindan_1ji_hours: float = 0.0  # 一次試験専用
    shindan_2ji_hours: float = 0.0  # 二次試験専用


@dataclass
class SubjectStats:
    """科目別統計"""
    subject: str
    qualification: str
    total_hours: float
    session_count: int
    avg_hours_per_session: float
    last_studied: Optional[date]


@dataclass
class WeeklyStats:
    """週次統計"""
    week_start: date
    week_end: date
    shindan_hours: float
    toukei_hours: float
    total_hours: float
    study_days: int
    avg_daily_hours: float


@dataclass
class KPIMetrics:
    """KPI指標"""
    total_study_hours: float
    total_study_days: int
    current_streak: int
    longest_streak: int
    avg_daily_hours: float
    this_week_hours: float
    last_week_hours: float
    shindan_total: float
    shindan_goal: float
    shindan_progress_pct: float
    toukei_total: float
    toukei_goal: float
    toukei_progress_pct: float
    # 一次・二次試験別
    shindan_1ji_total: float = 0.0
    shindan_1ji_goal: float = 600.0
    shindan_1ji_progress_pct: float = 0.0
    shindan_2ji_total: float = 0.0
    shindan_2ji_goal: float = 170.0
    shindan_2ji_progress_pct: float = 0.0


class AnalyticsService:
    """分析データ集計サービス"""

    def __init__(self, db_service):
        """
        Args:
            db_service: DatabaseServiceインスタンス
        """
        self.db = db_service

    def get_daily_summary(
        self,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        qualification_filter: Optional[List[str]] = None
    ) -> List[DailySummary]:
        """日次サマリーを取得（1回のクエリで全データ取得）

        Args:
            start_date: 開始日（Noneの場合は全期間）
            end_date: 終了日（Noneの場合は全期間）
            qualification_filter: 資格フィルタ（Noneの場合は全資格）

        Returns:
            日次サマリーのリスト
        """
        query = """
            SELECT
                r.date,
                r.phase,
                COALESCE(SUM(CASE WHEN s.qualification IN ('shindan_1ji', 'shindan_2ji') THEN s.time_hours ELSE 0 END), 0) as shindan_hours,
                COALESCE(SUM(CASE WHEN s.qualification = 'toukei' THEN s.time_hours ELSE 0 END), 0) as toukei_hours,
                COALESCE(SUM(s.time_hours), 0) as total_hours,
                COUNT(s.id) as session_count,
                COALESCE(SUM(CASE WHEN s.qualification = 'shindan_1ji' THEN s.time_hours ELSE 0 END), 0) as shindan_1ji_hours,
                COALESCE(SUM(CASE WHEN s.qualification = 'shindan_2ji' THEN s.time_hours ELSE 0 END), 0) as shindan_2ji_hours
            FROM records r
            LEFT JOIN study_sessions s ON r.id = s.record_id
            WHERE 1=1
        """

        params = []
        if start_date:
            query += " AND r.date >= ?"
            params.append(start_date.isoformat())
        if end_date:
            query += " AND r.date <= ?"
            params.append(end_date.isoformat())
        if qualification_filter:
            placeholders = ','.join(['?' for _ in qualification_filter])
            query += f" AND s.qualification IN ({placeholders})"
            params.extend(qualification_filter)

        query += """
            GROUP BY r.id, r.date, r.phase
            ORDER BY r.date ASC
        """

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()

        summaries = []
        for row in rows:
            summaries.append(DailySummary(
                date=datetime.strptime(row[0], '%Y-%m-%d').date(),
                phase=row[1],
                shindan_hours=round(row[2], 1),
                toukei_hours=round(row[3], 1),
                total_hours=round(row[4], 1),
                session_count=row[5],
                shindan_1ji_hours=round(row[6], 1),
                shindan_2ji_hours=round(row[7], 1)
            ))

        return summaries

    def get_subject_breakdown(self, qualification_filter: Optional[List[str]] = None) -> Dict[str, SubjectStats]:
        """科目別統計を取得（1回のJOINクエリ）

        Args:
            qualification_filter: 資格フィルタ（Noneの場合は全資格）

        Returns:
            科目名をキーとした統計辞書
        """
        query = """
            SELECT
                s.subject,
                s.qualification,
                SUM(s.time_hours) as total_hours,
                COUNT(s.id) as session_count,
                AVG(s.time_hours) as avg_hours,
                MAX(r.date) as last_studied
            FROM study_sessions s
            JOIN records r ON s.record_id = r.id
            WHERE 1=1
        """

        params = []
        if qualification_filter:
            placeholders = ','.join(['?' for _ in qualification_filter])
            query += f" AND s.qualification IN ({placeholders})"
            params.extend(qualification_filter)

        query += """
            GROUP BY s.subject, s.qualification
            ORDER BY total_hours DESC
        """

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()

        stats = {}
        for row in rows:
            subject = row[0]
            stats[subject] = SubjectStats(
                subject=subject,
                qualification=row[1],
                total_hours=round(row[2], 1),
                session_count=row[3],
                avg_hours_per_session=round(row[4], 2),
                last_studied=datetime.strptime(row[5], '%Y-%m-%d').date() if row[5] else None
            )

        return stats

    def get_weekly_stats(self, weeks: int = 4, qualification_filter: Optional[List[str]] = None) -> List[WeeklyStats]:
        """週次統計を取得

        Args:
            weeks: 取得する週数（デフォルト4週間）
            qualification_filter: 資格フィルタ（Noneの場合は全資格）

        Returns:
            週次統計のリスト
        """
        # 今日の日付から週の開始日（月曜）を計算
        today = date.today()
        current_week_start = today - timedelta(days=today.weekday())

        weekly_stats = []

        for i in range(weeks):
            week_start = current_week_start - timedelta(weeks=i)
            week_end = week_start + timedelta(days=6)

            # その週のデータを取得
            summaries = self.get_daily_summary(week_start, week_end, qualification_filter=qualification_filter)

            if summaries:
                shindan_total = sum(s.shindan_hours for s in summaries)
                toukei_total = sum(s.toukei_hours for s in summaries)
                total_hours = sum(s.total_hours for s in summaries)
                study_days = len([s for s in summaries if s.total_hours > 0])
                avg_daily = total_hours / 7 if total_hours > 0 else 0

                weekly_stats.append(WeeklyStats(
                    week_start=week_start,
                    week_end=week_end,
                    shindan_hours=round(shindan_total, 1),
                    toukei_hours=round(toukei_total, 1),
                    total_hours=round(total_hours, 1),
                    study_days=study_days,
                    avg_daily_hours=round(avg_daily, 1)
                ))

        return weekly_stats

    def get_study_streak(self, qualification_filter: Optional[List[str]] = None) -> Tuple[int, int]:
        """連続学習日数を取得

        Args:
            qualification_filter: 資格フィルタ（Noneの場合は全資格）

        Returns:
            (現在の連続日数, 最長連続日数)
        """
        summaries = self.get_daily_summary(qualification_filter=qualification_filter)

        if not summaries:
            return (0, 0)

        # 日付順にソート（念のため）
        summaries.sort(key=lambda x: x.date)

        # 学習した日のみ抽出
        study_dates = [s.date for s in summaries if s.total_hours > 0]

        if not study_dates:
            return (0, 0)

        # 現在の連続日数を計算
        current_streak = 0
        today = date.today()
        check_date = today

        # 今日または昨日から連続しているか確認
        if study_dates[-1] == today:
            check_date = today
        elif study_dates[-1] == today - timedelta(days=1):
            check_date = today - timedelta(days=1)
        else:
            # 連続していない
            current_streak = 0

        if check_date in study_dates:
            current_streak = 1
            for i in range(1, len(study_dates)):
                prev_date = check_date - timedelta(days=i)
                if prev_date in study_dates:
                    current_streak += 1
                else:
                    break

        # 最長連続日数を計算
        longest_streak = 0
        temp_streak = 1

        for i in range(1, len(study_dates)):
            if (study_dates[i] - study_dates[i-1]).days == 1:
                temp_streak += 1
                longest_streak = max(longest_streak, temp_streak)
            else:
                temp_streak = 1

        longest_streak = max(longest_streak, temp_streak, current_streak)

        return (current_streak, longest_streak)

    def get_kpi_metrics(self, current_phase: Optional[str] = None, qualification_filter: Optional[List[str]] = None) -> KPIMetrics:
        """KPI指標を一括取得

        Args:
            current_phase: 現在のフェーズ（指定すると、そのフェーズのみで平均計算）
            qualification_filter: 資格フィルタ（Noneの場合は全資格）

        Returns:
            KPI指標
        """
        # 累計統計
        stats = self.db.get_cumulative_stats()

        # 全日次サマリー（資格フィルタ適用）
        summaries = self.get_daily_summary(qualification_filter=qualification_filter)

        # 平均計算用のサマリー（フェーズ指定時はフィルタ）
        if current_phase:
            phase_summaries = [s for s in summaries if s.phase == current_phase]
        else:
            phase_summaries = summaries

        # 基本指標（フェーズ別）
        total_hours = sum(s.total_hours for s in phase_summaries)
        study_days = len([s for s in phase_summaries if s.total_hours > 0])
        avg_daily = total_hours / study_days if study_days > 0 else 0

        # 連続日数（資格フィルタ適用）
        current_streak, longest_streak = self.get_study_streak(qualification_filter=qualification_filter)

        # 今週と先週の学習時間（資格フィルタ適用）
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        last_week_start = week_start - timedelta(days=7)

        this_week_summaries = self.get_daily_summary(week_start, today, qualification_filter=qualification_filter)
        last_week_summaries = self.get_daily_summary(last_week_start, week_start - timedelta(days=1), qualification_filter=qualification_filter)

        this_week_hours = sum(s.total_hours for s in this_week_summaries)
        last_week_hours = sum(s.total_hours for s in last_week_summaries)

        # 進捗率計算
        shindan_progress = (stats.shindan_total / stats.shindan_goal * 100) if stats.shindan_goal > 0 else 0
        toukei_progress = 100.0  # 統計検定は「達成」扱い

        # 一次・二次試験別の集計
        shindan_1ji_total = sum(s.shindan_1ji_hours for s in summaries)
        shindan_2ji_total = sum(s.shindan_2ji_hours for s in summaries)

        shindan_1ji_goal = 600.0
        shindan_2ji_goal = 170.0

        shindan_1ji_progress = (shindan_1ji_total / shindan_1ji_goal * 100) if shindan_1ji_goal > 0 else 0
        shindan_2ji_progress = (shindan_2ji_total / shindan_2ji_goal * 100) if shindan_2ji_goal > 0 else 0

        return KPIMetrics(
            total_study_hours=round(total_hours, 1),
            total_study_days=study_days,
            current_streak=current_streak,
            longest_streak=longest_streak,
            avg_daily_hours=round(avg_daily, 1),
            this_week_hours=round(this_week_hours, 1),
            last_week_hours=round(last_week_hours, 1),
            shindan_total=round(stats.shindan_total, 1),
            shindan_goal=round(stats.shindan_goal, 1),
            shindan_progress_pct=round(shindan_progress, 1),
            toukei_total=round(stats.toukei_total, 1),
            toukei_goal=round(stats.toukei_goal, 1),
            toukei_progress_pct=round(toukei_progress, 1),
            shindan_1ji_total=round(shindan_1ji_total, 1),
            shindan_1ji_goal=shindan_1ji_goal,
            shindan_1ji_progress_pct=round(shindan_1ji_progress, 1),
            shindan_2ji_total=round(shindan_2ji_total, 1),
            shindan_2ji_goal=shindan_2ji_goal,
            shindan_2ji_progress_pct=round(shindan_2ji_progress, 1)
        )
