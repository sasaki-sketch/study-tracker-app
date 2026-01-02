"""
学習統計ユーティリティ
"""
from datetime import date, datetime, timedelta
from typing import List, Dict, Tuple
from models.record import StudyRecord


def calculate_days_until_exam() -> Tuple[int, int]:
    """試験日までの残り日数を計算

    Returns:
        (統計検定までの日数, 診断士までの日数)
    """
    today = date.today()

    # 統計検定2級: 2月1日
    toukei_exam = date(today.year, 2, 1)
    if today > toukei_exam:
        toukei_exam = date(today.year + 1, 2, 1)

    # 中小企業診断士: 8月上旬（仮に8月5日）
    shindan_exam = date(today.year, 8, 5)
    if today > shindan_exam:
        shindan_exam = date(today.year + 1, 8, 5)

    days_to_toukei = (toukei_exam - today).days
    days_to_shindan = (shindan_exam - today).days

    return days_to_toukei, days_to_shindan


def calculate_required_daily_pace(
    current_total: float,
    goal: float,
    days_remaining: int
) -> float:
    """目標達成に必要な1日あたりの学習時間を計算"""
    if days_remaining <= 0:
        return 0.0

    remaining_hours = goal - current_total
    if remaining_hours <= 0:
        return 0.0

    return round(remaining_hours / days_remaining, 2)


def calculate_streak(records: List[StudyRecord]) -> int:
    """連続学習日数を計算（関連資格を除外）"""
    if not records:
        return 0

    # 日付順にソート（降順）
    sorted_records = sorted(records, key=lambda r: r.date, reverse=True)

    today = date.today()
    streak = 0
    current_date = today

    for record in sorted_records:
        # 関連資格のレコードはカウントしない
        if record.phase == '関連資格':
            continue

        # 学習時間が0の日はカウントしない
        if record.shindan_time == 0 and record.toukei_time == 0:
            continue

        # 期待する日付と一致した場合
        if record.date == current_date:
            streak += 1
            current_date -= timedelta(days=1)
        elif record.date < current_date:
            # 連続が途切れた（早期終了で最適化）
            break

    return streak


def calculate_weekly_stats(records: List[StudyRecord]) -> Dict[str, float]:
    """今週の学習統計を計算（関連資格を除外）

    Returns:
        {'shindan': 総時間, 'toukei': 総時間, 'total': 総時間}
    """
    today = date.today()
    week_start = today - timedelta(days=today.weekday())  # 月曜日
    week_end = week_start + timedelta(days=6)  # 日曜日

    shindan_total = 0.0
    toukei_total = 0.0

    for record in records:
        if week_start <= record.date <= week_end and record.phase != '関連資格':
            shindan_total += record.shindan_time
            toukei_total += record.toukei_time

    return {
        'shindan': shindan_total,
        'toukei': toukei_total,
        'total': shindan_total + toukei_total
    }


def calculate_monthly_stats(records: List[StudyRecord]) -> Dict[str, float]:
    """今月の学習統計を計算（関連資格を除外）

    Returns:
        {'shindan': 総時間, 'toukei': 総時間, 'total': 総時間}
    """
    today = date.today()

    shindan_total = 0.0
    toukei_total = 0.0

    for record in records:
        if record.date.year == today.year and record.date.month == today.month and record.phase != '関連資格':
            shindan_total += record.shindan_time
            toukei_total += record.toukei_time

    return {
        'shindan': shindan_total,
        'toukei': toukei_total,
        'total': shindan_total + toukei_total
    }


def calculate_subject_progress(records: List[StudyRecord]) -> Dict[str, Tuple[float, float]]:
    """科目別の進捗を計算

    Returns:
        {'科目名': (累計時間, 進捗率%), ...}
    """
    subject_hours = {}
    target_per_subject = 90.0  # 各科目の目標時間

    for record in records:
        if record.shindan_subject and record.shindan_time > 0:
            subject = record.shindan_subject
            if subject not in subject_hours:
                subject_hours[subject] = 0.0
            subject_hours[subject] += record.shindan_time

    # 進捗率を計算
    result = {}
    for subject, hours in subject_hours.items():
        progress = round((hours / target_per_subject) * 100, 1)
        result[subject] = (hours, progress)

    return result


def get_week_heatmap_data(records: List[StudyRecord]) -> List[Tuple[date, float]]:
    """週間カレンダー用のヒートマップデータを生成

    Returns:
        [(日付, 合計学習時間), ...]
    """
    today = date.today()
    week_start = today - timedelta(days=today.weekday())  # 月曜日

    # 過去4週間分
    heatmap_data = []
    for i in range(28):  # 4週間 × 7日
        target_date = week_start - timedelta(days=27 - i)

        # その日の学習時間を検索
        total_hours = 0.0
        for record in records:
            if record.date == target_date:
                total_hours = record.shindan_time + record.toukei_time
                break

        heatmap_data.append((target_date, total_hours))

    return heatmap_data


def get_achievement_message(streak: int, total_hours: float, progress: float) -> str:
    """達成状況に応じた称賛メッセージを生成"""
    messages = []

    # ストリーク
    if streak >= 30:
        messages.append("🏆 素晴らしい！30日連続学習達成！")
    elif streak >= 14:
        messages.append("🔥 2週間連続学習継続中！")
    elif streak >= 7:
        messages.append("⭐ 1週間連続学習達成！")
    elif streak >= 3:
        messages.append("💪 3日連続で学習継続中！")

    # 進捗率
    if progress >= 75:
        messages.append("🎯 目標の75%達成！ゴールが見えてきました！")
    elif progress >= 50:
        messages.append("📈 目標の半分到達！順調です！")
    elif progress >= 25:
        messages.append("🌱 目標の1/4達成！この調子で！")

    # 累計時間
    if total_hours >= 500:
        messages.append("🎓 500時間突破！圧倒的な積み上げ！")
    elif total_hours >= 300:
        messages.append("📚 300時間突破！継続は力なり！")
    elif total_hours >= 100:
        messages.append("✨ 100時間突破！")

    if messages:
        return " ".join(messages)
    else:
        return "📝 今日も学習を続けましょう！"
