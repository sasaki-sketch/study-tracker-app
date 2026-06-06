"""
診断士科目の定義

注意: このファイルは廃止予定です。
科目情報はデータベース（subjects テーブル）から取得してください。

DatabaseService の以下のメソッドを使用:
- get_subject_list(category) : 科目名リスト取得
- get_target_hours_dict(category) : 目標時間辞書取得
- get_subject_settings(category) : 科目設定情報取得
"""

# 【非推奨】以下の定数は使用しないでください
# データベースから動的に取得することを推奨します

# 中小企業診断士 一次試験 7科目
# 非推奨: DatabaseService.get_subject_list('1次試験') を使用してください
SHINDAN_1JI_SUBJECTS = [
    "経済学・経済政策",
    "財務・会計",
    "企業経営理論",
    "運営管理",
    "経営法務",
    "経営情報システム",
    "中小企業経営・政策"
]

# 各科目の推奨学習時間（時間）
# 非推奨: DatabaseService.get_target_hours_dict('1次試験') を使用してください
SUBJECT_RECOMMENDED_HOURS = {
    "経済学・経済政策": 90,
    "財務・会計": 100,
    "企業経営理論": 90,
    "運営管理": 80,
    "経営法務": 70,
    "経営情報システム": 70,
    "中小企業経営・政策": 100
}

# 科目の略称（表示用）
# 非推奨: DatabaseService.get_subject_settings() の abbreviation フィールドを使用してください
SUBJECT_SHORT_NAMES = {
    "経済学・経済政策": "経済学",
    "財務・会計": "財務",
    "企業経営理論": "経営理論",
    "運営管理": "運営",
    "経営法務": "法務",
    "経営情報システム": "情報",
    "中小企業経営・政策": "中小"
}
