"""
科目名関連のユーティリティ関数
"""
from typing import Optional

# 科目の別名・略称マッピング
SUBJECT_ALIASES = {
    # 1次試験科目
    "財務": "財務会計",
    "財務会計論": "財務会計",
    "企業経営": "企業経営理論",
    "企業経営論": "企業経営理論",
    "経営理論": "企業経営理論",
    "運管": "運営管理",
    "オペレーション": "運営管理",
    "経済": "経済学",
    "情報": "経営情報システム",
    "システム": "経営情報システム",
    "経営情報": "経営情報システム",
    "法務": "経営法務",
    "中小": "中小企業経営政策",
    "政策": "中小企業経営政策",
    "中小企業": "中小企業経営政策",

    # 2次試験科目
    "事例1": "事例I",
    "事例Ⅰ": "事例I",
    "組織": "事例I",
    "事例2": "事例II",
    "事例Ⅱ": "事例II",
    "マーケ": "事例II",
    "マーケティング": "事例II",
    "事例3": "事例III",
    "事例Ⅲ": "事例III",
    "生産": "事例III",
    "オペ": "事例III",
    "事例4": "事例IV",
    "事例Ⅳ": "事例IV",
    "財務会計": "事例IV",  # 2次試験の財務

    # その他
    "統計": "統計検定2級",
    "統計検定": "統計検定2級",
}

# 科目絵文字マッピング
SUBJECT_EMOJI_MAP = {
    # 1次試験科目（正式名称）
    "財務・会計": "💰",
    "財務会計": "💰",  # 旧名（後方互換性）
    "企業経営理論": "📊",
    "運営管理": "🏭",
    "経済学・経済政策": "📈",
    "経済学": "📈",  # 旧名（後方互換性）
    "経営情報システム": "💻",
    "経営法務": "⚖️",
    "中小企業経営・政策": "🏢",
    "中小企業経営政策": "🏢",  # 旧名（後方互換性）
    # 2次試験科目
    "事例I": "👥",
    "事例II": "📢",
    "事例III": "⚙️",
    "事例IV": "💹",
    # その他
    "統計検定2級": "📊",
}


def normalize_subject_name(subject: str) -> Optional[str]:
    """
    科目名を正規化する

    Args:
        subject: 入力された科目名（略称や別名の可能性あり）

    Returns:
        正規化された科目名。マッチしない場合はNone

    Examples:
        >>> normalize_subject_name("財務")
        '財務会計'
        >>> normalize_subject_name("事例1")
        '事例I'
        >>> normalize_subject_name("マーケ")
        '事例II'
    """
    if not subject:
        return None

    # 前後の空白を削除
    subject = subject.strip()

    # 完全一致する正式名称の場合
    if subject in SUBJECT_EMOJI_MAP:
        return subject

    # 別名・略称からマッピング
    if subject in SUBJECT_ALIASES:
        return SUBJECT_ALIASES[subject]

    # 大文字小文字を無視してマッチング
    subject_lower = subject.lower()
    for alias, canonical in SUBJECT_ALIASES.items():
        if alias.lower() == subject_lower:
            return canonical

    # マッチしない場合はNone
    return None


def get_subject_emoji(subject: str) -> str:
    """
    科目に対応する絵文字を取得

    Args:
        subject: 科目名

    Returns:
        絵文字（見つからない場合は📚）
    """
    return SUBJECT_EMOJI_MAP.get(subject, "📚")


def format_subject_with_emoji(subject: str) -> str:
    """
    科目名を絵文字付きでフォーマット

    Args:
        subject: 科目名

    Returns:
        絵文字 + 科目名の形式（例: "💰 財務会計"）
    """
    emoji = get_subject_emoji(subject)
    return f"{emoji} {subject}"
