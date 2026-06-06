"""
X投稿プロンプト生成ユーティリティ
複数科目対応の統一プロンプトテンプレート（ストーリー＋数字型）
"""
from datetime import date as dt_date
from typing import List
from models.record import StudyRecord, CumulativeStats, StudySession


# 統一プロンプトテンプレート（ストーリー＋数字型）
TWEET_PROMPT_TEMPLATE = """以下のテキストをそのままコピー＆ペーストして出力してください。一切の変更・加工・追加を禁止します：

📅 Day {day_number}｜中小企業診断士

{hook_text}

▶ 今日やったこと
{sessions_block}

▶ 積み上げ
累計 {shindan_total}h / {shindan_goal}h（{phase} {progress_pct}%）

#中小企業診断士 #勉強垢

【厳格な指示】
- 上記のテキストを一字一句そのままコピーして出力すること
- 改行、スペース、句読点を含め、全く変更しないこと
- 要約、言い換え、補足説明は一切禁止
- この指示文は出力に含めないこと
"""


def _extract_hook_text(sessions: List[StudySession]) -> str:
    """セッションのissue（課題・気づき）から冒頭フック文を抽出

    1. 全セッションのissueを収集
    2. 最初の非空issueの1行目を抽出
    3. 末尾に「。」がなければ追加
    4. issue が全て空の場合: フォールバック
    """
    for session in sessions:
        if session.issue and session.issue.strip():
            first_line = session.issue.strip().split('\n')[0].strip()
            if first_line:
                if not first_line.endswith('。'):
                    first_line += '。'
                return first_line
    return "今日も積み上げ。"


def _build_sessions_block(sessions: List[StudySession]) -> str:
    """科目ごとのセッションブロックを生成

    例:
    💰 財務・会計 2.5h
    　まとめシート＋過去問（証券投資論、ポートフォリオ理論、CAPM）
    """
    from utils.subjects import SUBJECT_EMOJI_MAP

    lines = []
    for session in sessions:
        emoji = SUBJECT_EMOJI_MAP.get(session.subject, "📚")
        lines.append(f"{emoji} {session.subject} {session.time_hours}h")
        if session.content and session.content.strip():
            # 全角スペースでインデント
            lines.append(f"\u3000{session.content.strip()}")
    return '\n'.join(lines)


def generate_tweet_prompt_from_sessions(
    record: StudyRecord,
    stats: CumulativeStats,
    sessions: List[StudySession]
) -> str:
    """学習セッションから投稿プロンプトを生成（複数科目対応）

    Args:
        record: 学習記録
        stats: 累計統計
        sessions: 学習セッションリスト

    Returns:
        プロンプト文字列
    """
    # Day番号計算（2026年1月1日起点）
    start_date = dt_date(2026, 1, 1)
    day_number = (record.date - start_date).days + 1

    # セッションを資格別に分類
    shindan_sessions = [s for s in sessions if s.qualification in ('shindan', 'shindan_1ji', 'shindan_2ji')]

    # フック文生成
    hook_text = _extract_hook_text(shindan_sessions if shindan_sessions else sessions)

    # セッションブロック生成
    sessions_block = _build_sessions_block(shindan_sessions if shindan_sessions else sessions)

    # 進捗率計算
    if stats.shindan_goal > 0:
        progress_pct = round(stats.shindan_total / stats.shindan_goal * 100)
    else:
        progress_pct = 0

    # プロンプト生成
    prompt = TWEET_PROMPT_TEMPLATE.format(
        day_number=day_number,
        hook_text=hook_text,
        sessions_block=sessions_block,
        phase=record.phase,
        shindan_total=round(stats.shindan_total, 1),
        shindan_goal=round(stats.shindan_goal, 1),
        progress_pct=progress_pct
    )

    return prompt


def generate_tweet_text_from_prompt(prompt: str) -> str:
    """プロンプトから投稿文を抽出

    Args:
        prompt: プロンプト文字列

    Returns:
        投稿文（指示部分を除いた本文のみ）
    """
    # 【厳格な指示】以降を除去
    if "【厳格な指示】" in prompt:
        prompt = prompt.split("【厳格な指示】")[0]

    # 冒頭のプロンプト指示（「以下のテキストを...」の行）を除去
    lines = prompt.strip().split('\n')

    result_lines = []
    skip_header = True

    for line in lines:
        if skip_header:
            # 冒頭の指示文をスキップ（📅まで）
            if line.strip().startswith('📅'):
                skip_header = False
                result_lines.append(line)
        else:
            result_lines.append(line)

    return '\n'.join(result_lines).strip()


def generate_tweet_prompt_legacy(record: StudyRecord, stats: CumulativeStats) -> str:
    """レガシー記録から投稿プロンプトを生成（後方互換性）

    Args:
        record: 学習記録（レガシー形式）
        stats: 累計統計

    Returns:
        プロンプト文字列
    """
    # レガシーデータをセッション形式に変換
    sessions = []

    if record.shindan_time > 0:
        sessions.append(StudySession(
            record_id=record.id or 0,
            qualification='shindan_1ji',
            subject=record.shindan_subject or '未分類',
            time_hours=record.shindan_time,
            content=record.shindan_content,
            issue=record.shindan_issue
        ))

    if record.toukei_time > 0:
        sessions.append(StudySession(
            record_id=record.id or 0,
            qualification='toukei',
            subject='統計検定2級',
            time_hours=record.toukei_time,
            content=record.toukei_content,
            issue=record.toukei_issue
        ))

    return generate_tweet_prompt_from_sessions(record, stats, sessions)
