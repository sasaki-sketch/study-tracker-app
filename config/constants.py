"""
アプリケーション全体で使用する定数定義
"""
from datetime import date

# ==================== 試験日程 ====================
TOUKEI_EXAM_DATE = date(2026, 2, 1)           # 統計検定2級試験日
SHINDAN_1ST_EXAM_DATE = date(2026, 8, 5)      # 中小企業診断士1次試験日
SHINDAN_2ND_EXAM_DATE = date(2026, 10, 25)    # 中小企業診断士2次試験日

# ==================== 目標学習時間 ====================
SHINDAN_GOAL_HOURS = 770.0    # 中小企業診断士目標時間（業界標準: 700-1000h）
SHINDAN_1ST_GOAL_HOURS = 600.0  # 1次試験対策時間
SHINDAN_2ND_GOAL_HOURS = 170.0  # 2次試験対策時間
TOUKEI_GOAL_HOURS = 80.0      # 統計検定2級目標時間

# ==================== 学習開始日 ====================
STUDY_START_DATE = date(2025, 10, 12)  # Day番号計算の基準日

# ==================== X投稿設定 ====================
TWEET_CHAR_LIMIT = 140  # X投稿の文字数制限（日本語短文）

# ==================== 学習フェーズ ====================
PHASE_FOUNDATION = "基礎固め期"        # 1月-3月
PHASE_APPLICATION = "応用力強化期"     # 4月-5月
PHASE_INTENSIVE = "直前追い込み期"     # 6月-7月
PHASE_2ND_EXAM = "2次試験対策期"       # 8月-10月

# ==================== 科目別目標時間 ====================
SUBJECT_TARGET_HOURS = 90.0  # 各科目の標準学習時間
