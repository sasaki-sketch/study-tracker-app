"""
イベント統計計算ユーティリティ
"""
from typing import Dict, List, Optional
from services.database import DatabaseService


def calculate_past_exam_stats(db: DatabaseService) -> Dict:
    """過去問演習の統計を計算

    Returns:
        {
            'total_count': 総実施回数,
            'avg_correct_rate': 平均正答率,
            'pass_rate': 合格水準達成率(70%以上の割合),
            'recent_trend': 最近の傾向('improving'/'stable'/'declining')
        }
    """
    events = db.get_events_by_type('past_exam', limit=100)

    if not events:
        return {
            'total_count': 0,
            'avg_correct_rate': 0.0,
            'pass_rate': 0.0,
            'recent_trend': 'stable'
        }

    # 正答率計算
    correct_rates = []
    pass_count = 0

    for event in events:
        details = event['details']
        if details['total_count'] > 0:
            rate = details['correct_count'] / details['total_count'] * 100
            correct_rates.append(rate)
            if rate >= 70:
                pass_count += 1

    avg_correct_rate = round(sum(correct_rates) / len(correct_rates), 1) if correct_rates else 0.0
    pass_rate = round(pass_count / len(events) * 100, 1) if events else 0.0

    # トレンド判定(直近3件 vs その前3件)
    trend = 'stable'
    if len(correct_rates) >= 6:
        recent_avg = sum(correct_rates[:3]) / 3
        prev_avg = sum(correct_rates[3:6]) / 3

        if recent_avg > prev_avg + 5:
            trend = 'improving'
        elif recent_avg < prev_avg - 5:
            trend = 'declining'

    return {
        'total_count': len(events),
        'avg_correct_rate': avg_correct_rate,
        'pass_rate': pass_rate,
        'recent_trend': trend
    }


def calculate_material_progress_stats(db: DatabaseService) -> Dict:
    """教材周回の統計を計算

    Returns:
        {
            'total_materials': 登録教材数,
            'completed_count': 完了教材数,
            'avg_progress': 平均進捗率,
            'total_study_time': 総学習時間,
            'avg_understanding': 平均理解度
        }
    """
    materials = db.get_all_materials()

    if not materials:
        return {
            'total_materials': 0,
            'completed_count': 0,
            'avg_progress': 0.0,
            'total_study_time': 0.0,
            'avg_understanding': 0.0
        }

    completed_count = 0
    total_progress = 0.0
    total_time = 0.0
    total_understanding = 0.0

    for m in materials:
        # 進捗率
        if m['target_laps'] > 0:
            progress = min(m['current_lap'] / m['target_laps'] * 100, 100)
            total_progress += progress
            if progress >= 100:
                completed_count += 1

        # 学習時間
        total_time += m['total_time']

        # 理解度
        if m['avg_understanding'] > 0:
            total_understanding += m['avg_understanding']

    avg_progress = round(total_progress / len(materials), 1) if materials else 0.0
    avg_understanding = round(total_understanding / len(materials), 1) if materials else 0.0

    return {
        'total_materials': len(materials),
        'completed_count': completed_count,
        'avg_progress': avg_progress,
        'total_study_time': total_time,
        'avg_understanding': avg_understanding
    }


def calculate_mock_exam_stats(db: DatabaseService) -> Dict:
    """模試・答練の統計を計算

    Returns:
        {
            'total_count': 総受験回数,
            'first_exam_avg_score': 1次試験平均得点率,
            'second_exam_pass_count': 2次試験合格水準達成回数,
            'recent_performance': 最近のパフォーマンス('excellent'/'good'/'needs_improvement')
        }
    """
    events = db.get_events_by_type('mock_exam', limit=100)

    if not events:
        return {
            'total_count': 0,
            'first_exam_avg_score': 0.0,
            'second_exam_pass_count': 0,
            'recent_performance': 'needs_improvement'
        }

    first_exam_scores = []
    second_exam_pass = 0

    for event in events:
        details = event['details']

        if details['exam_type'] == '1次試験':
            if details['max_score'] > 0:
                score_rate = details['total_score'] / details['max_score'] * 100
                first_exam_scores.append(score_rate)
        else:
            # 2次試験の合格判定
            grade_values = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
            grades = [grade_values[g] for g in details['case_grades'].values()]
            a_count = sum(1 for g in grades if g >= 4)
            has_low = min(grades) < 2

            if a_count >= 2 and not has_low:
                second_exam_pass += 1

    first_avg = round(sum(first_exam_scores) / len(first_exam_scores), 1) if first_exam_scores else 0.0

    # パフォーマンス判定
    performance = 'needs_improvement'
    if first_avg >= 70 or (second_exam_pass > 0 and len(events) > 0):
        performance = 'excellent'
    elif first_avg >= 60:
        performance = 'good'

    return {
        'total_count': len(events),
        'first_exam_avg_score': first_avg,
        'second_exam_pass_count': second_exam_pass,
        'recent_performance': performance
    }


def get_event_timeline(db: DatabaseService, limit: int = 10) -> List[Dict]:
    """イベントタイムラインを取得

    Args:
        limit: 取得件数

    Returns:
        イベントリスト(日付降順)
    """
    return db.get_recent_events(limit=limit)
