"""
学習フェーズ判定ユーティリティ
"""
from datetime import date


def get_current_phase() -> str:
    """現在の学習フェーズを取得

    Returns:
        現在の学習フェーズ:
        - 1-3月: 基礎固め期（1次試験基礎学習）
        - 4-5月: 応用力強化期（1次試験応用）
        - 6-7月: 直前追い込み期（1次試験直前）
        - 8-10月: 2次試験対策期（2次試験学習）
        - 11-12月: 基礎固め期（次年度準備）
    """
    today = date.today()
    month = today.month

    # フェーズ定義
    if month in [1, 2, 3]:
        return "基礎固め期"
    elif month in [4, 5]:
        return "応用力強化期"
    elif month in [6, 7]:
        return "直前追い込み期"
    elif month in [8, 9, 10]:
        return "2次試験対策期"
    else:  # 11, 12月
        return "基礎固め期"  # 次年度準備
