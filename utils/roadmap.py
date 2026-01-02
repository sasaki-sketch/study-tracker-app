"""
学習ロードマップ生成ユーティリティ
"""
from datetime import date, timedelta
from typing import List, Dict, Tuple
import pandas as pd


def generate_roadmap_data() -> pd.DataFrame:
    """学習ロードマップデータを生成

    Returns:
        DataFrame with columns: date, phase, phase_name, days_from_start
    """
    # 基準日: 2026年1月1日
    start_date = date(2026, 1, 1)

    # 試験日
    toukei_exam = date(2026, 2, 1)  # 統計検定
    shindan_exam = date(2026, 8, 5)  # 診断士

    # フェーズ定義
    phases = [
        {
            'name': '基礎固め期',
            'start': start_date,
            'end': date(2026, 3, 31),
            'color': '#4ecdc4',
            'phase_num': 1
        },
        {
            'name': '応用力強化期',
            'start': date(2026, 4, 1),
            'end': date(2026, 5, 31),
            'color': '#ff6b6b',
            'phase_num': 2
        },
        {
            'name': '直前追い込み期',
            'start': date(2026, 6, 1),
            'end': shindan_exam,
            'color': '#ffd93d',
            'phase_num': 3
        }
    ]

    # DataFrameを作成
    rows = []

    for phase in phases:
        current = phase['start']
        while current <= phase['end']:
            days_from_start = (current - start_date).days

            rows.append({
                'date': current,
                'phase': phase['phase_num'],
                'phase_name': phase['name'],
                'color': phase['color'],
                'days_from_start': days_from_start
            })

            current += timedelta(days=1)

    df = pd.DataFrame(rows)

    # マイルストーン追加
    df['milestone'] = ''
    df.loc[df['date'] == toukei_exam, 'milestone'] = '統計検定'
    df.loc[df['date'] == shindan_exam, 'milestone'] = '診断士試験'

    return df


def get_phase_boundaries() -> List[Dict]:
    """フェーズの境界情報を取得"""
    return [
        {
            'name': '基礎固め期',
            'start': date(2026, 1, 1),
            'end': date(2026, 3, 31),
            'color': '#4ecdc4',
            'description': 'インプット中心、基礎知識の定着'
        },
        {
            'name': '応用力強化期',
            'start': date(2026, 4, 1),
            'end': date(2026, 5, 31),
            'color': '#ff6b6b',
            'description': '過去問演習、弱点補強'
        },
        {
            'name': '直前追い込み期',
            'start': date(2026, 6, 1),
            'end': date(2026, 8, 5),
            'color': '#ffd93d',
            'description': '総仕上げ、模試、最終調整'
        }
    ]


def get_current_phase_info() -> Dict:
    """現在のフェーズ情報を取得"""
    today = date.today()
    phases = get_phase_boundaries()

    for phase in phases:
        if phase['start'] <= today <= phase['end']:
            return {
                **phase,
                'days_in_phase': (today - phase['start']).days + 1,
                'days_remaining': (phase['end'] - today).days,
                'total_days': (phase['end'] - phase['start']).days + 1
            }

    # デフォルト（基礎固め期）
    return {
        **phases[0],
        'days_in_phase': 1,
        'days_remaining': 0,
        'total_days': 90
    }
