"""
X投稿文生成サービス
"""
import random
from models.record import StudyRecord, CumulativeStats
from datetime import datetime, date
from utils.subjects import SUBJECT_EMOJI_MAP

# 学習開始日（Day番号計算用）
STUDY_START_DATE = date(2025, 10, 12)  # 最初の記録日

# 論語の引用リスト
RONGO_QUOTES = [
    "学びて時に之を習う、亦た説ばしからずや",
    "温故知新",
    "吾れ十有五にして学に志す",
    "之を知る者は之を好む者に如かず、之を好む者は之を楽しむ者に如かず",
    "学びて思わざれば則ち罔し、思いて学ばざれば則ち殆し",
    "過ぎたるは猶及ばざるが如し",
    "君子は和して同ぜず、小人は同じて和せず",
    "これを知るをこれを知ると為し、知らざるを知らずと為す、是れ知るなり",
]


class TweetService:
    """X投稿文生成クラス"""

    @staticmethod
    def _calculate_day_number(target_date: date) -> int:
        """学習開始日からの経過日数を計算"""
        delta = target_date - STUDY_START_DATE
        return delta.days + 1

    @staticmethod
    def _get_insight(record: StudyRecord) -> str:
        """気づき文を生成（issueまたはcontentから）"""
        # issueがあればそれを優先
        if record.shindan_issue and record.shindan_issue.strip():
            insight = record.shindan_issue.strip()
            # 改行を除去して1行に
            insight = insight.replace('\n', ' ')
            # 長すぎる場合は切り詰め（50文字まで）
            if len(insight) > 50:
                insight = insight[:47] + "..."
            return insight

        # contentから抽出
        if record.shindan_content and record.shindan_content.strip():
            content = record.shindan_content.strip()
            content = content.replace('\n', ' ')
            if len(content) > 50:
                content = content[:47] + "..."
            return content

        # どちらもない場合のデフォルト
        return "着実に知識を積み上げ中"

    @staticmethod
    def _get_subject_emoji(subject: str) -> str:
        """科目に対応する絵文字を取得"""
        return SUBJECT_EMOJI_MAP.get(subject, "📚")

    @staticmethod
    def generate_daily_tweet(record: StudyRecord, stats: CumulativeStats) -> str:
        """日次投稿文を生成（140文字制限対応）"""
        lines = []

        # Day番号を計算
        day_num = TweetService._calculate_day_number(record.date)

        # 日付フォーマット（例: 1月3日）
        date_str = f"{record.date.month}月{record.date.day}日"

        # タイトル（【】なし、：使用）
        lines.append(f"{date_str} / Day {day_num}：中小企業診断士への積み上げ")
        lines.append("")

        # 両方学習した場合
        if record.shindan_time > 0 and record.toukei_time > 0:
            # 診断士
            emoji = TweetService._get_subject_emoji(record.shindan_subject)
            lines.append(f"{emoji} {record.shindan_subject} {record.shindan_time}h")

            # 統計検定
            lines.append(f"📊 統計検定 {record.toukei_time}h")

            # 気づき（簡潔に）
            if record.shindan_issue and record.shindan_issue.strip():
                issue = record.shindan_issue.strip().replace('\n', '、')
                # 20文字以内に収める
                if len(issue) > 20:
                    issue = issue[:17] + "..."
                lines.append(f"💡{issue}")

            lines.append("")
            lines.append(f"累計 {stats.shindan_total}h/{stats.shindan_goal}h")

        # 診断士のみ
        elif record.shindan_time > 0:
            emoji = TweetService._get_subject_emoji(record.shindan_subject)
            subject_text = record.shindan_subject if record.shindan_subject else "診断士学習"
            lines.append(f"{emoji} {subject_text} {record.shindan_time}h")

            # 学習内容を簡潔に表示（contentから、長すぎる場合は省略）
            if record.shindan_content and record.shindan_content.strip():
                content = record.shindan_content.strip().replace('\n', '、')
                # 30文字以内に収める
                if len(content) > 30:
                    content = content[:27] + "..."
                lines.append(f"└ {content}")

            # 気づき（issueがある場合）
            if record.shindan_issue and record.shindan_issue.strip():
                issue = record.shindan_issue.strip().replace('\n', '、')
                # 20文字以内に収める
                if len(issue) > 20:
                    issue = issue[:17] + "..."
                lines.append(f"💡{issue}")

            lines.append("")
            lines.append(f"累計 {stats.shindan_total}h/{stats.shindan_goal}h")

        # 統計検定のみ
        elif record.toukei_time > 0:
            lines.append(f"📊 統計検定2級 {record.toukei_time}h")

            # 学習内容（簡潔に）
            if record.toukei_content and record.toukei_content.strip():
                content = record.toukei_content.strip().replace('\n', '、')
                # 30文字以内に収める
                if len(content) > 30:
                    content = content[:27] + "..."
                lines.append(f"└ {content}")

            # 気づき（issueがある場合）
            if record.toukei_issue and record.toukei_issue.strip():
                issue = record.toukei_issue.strip().replace('\n', '、')
                # 20文字以内に収める
                if len(issue) > 20:
                    issue = issue[:17] + "..."
                lines.append(f"💡{issue}")

            lines.append("")
            lines.append(f"累計 {stats.toukei_total}h/{stats.toukei_goal}h")

        lines.append("")

        # ハッシュタグ（2-3個に抑える）
        hashtags = []
        if record.shindan_time > 0:
            hashtags.append("#中小企業診断士")
        if record.toukei_time > 0:
            hashtags.append("#統計検定")

        # 共通ハッシュタグ
        hashtags.append("#勉強垢")

        lines.append(" ".join(hashtags))

        return "\n".join(lines)

    @staticmethod
    def generate_weekly_tweet(
        weekly_stats: dict,
        total_shindan: float,
        total_toukei: float,
        phase: str
    ) -> str:
        """週次投稿文を生成

        Args:
            weekly_stats: 科目別集計 {"財務会計": 12.0, "企業経営理論": 6.5, ...}
            total_shindan: 診断士合計時間
            total_toukei: 統計合計時間
            phase: 学習フェーズ
        """
        lines = []

        # タイトル
        lines.append(f"今週の積み上げ({phase})")
        lines.append("")

        # 中小企業診断士セクション
        if total_shindan > 0:
            lines.append(f"★中小企業診断士:{total_shindan}h")

            # 科目別表示（上位3つまで）
            sorted_subjects = sorted(
                weekly_stats.items(),
                key=lambda x: x[1],
                reverse=True
            )
            for subject, hours in sorted_subjects[:3]:
                lines.append(f"  {subject}:{hours}h")

            lines.append("")

        # 統計検定2級セクション
        if total_toukei > 0:
            lines.append(f"★統計検定2級:{total_toukei}h")
            lines.append("")

        # コメント
        lines.append("来週:継続して積み上げ")
        lines.append("")

        # 論語引用
        rongo = random.choice(RONGO_QUOTES)
        lines.append(rongo)
        lines.append("")

        # 試験日情報
        lines.append("試験日:中小企業診断士8月")

        # ハッシュタグ
        lines.append("#中小企業診断士")

        return "\n".join(lines)

    @staticmethod
    def generate_monthly_tweet(
        monthly_stats: dict,
        total_shindan: float,
        total_toukei: float,
        cumulative_shindan: float,
        shindan_goal: float,
        progress: float,
        phase: str
    ) -> str:
        """月次投稿文を生成

        Args:
            monthly_stats: 科目別集計 {"財務会計": 30.0, ...}
            total_shindan: 診断士月間合計時間
            total_toukei: 統計月間合計時間
            cumulative_shindan: 診断士累計時間
            shindan_goal: 診断士目標時間
            progress: 進捗率
            phase: 学習フェーズ
        """
        lines = []

        # 月名を取得（例: "1月"）
        from datetime import date
        month_name = f"{date.today().month}月"

        # タイトル
        lines.append(f"{month_name}の積み上げ({phase})")
        lines.append("")

        # 中小企業診断士セクション
        if total_shindan > 0:
            lines.append(f"★中小企業診断士:{total_shindan}h(累計{cumulative_shindan}h)")
            lines.append(f"進捗:{cumulative_shindan}/{shindan_goal:.0f}h({progress}%)")
            lines.append("")

            # 科目別表示
            lines.append("科目別:")
            sorted_subjects = sorted(
                monthly_stats.items(),
                key=lambda x: x[1],
                reverse=True
            )
            for subject, hours in sorted_subjects:
                lines.append(f"  {subject}:{hours}h")

            lines.append("")

        # 統計検定2級セクション
        if total_toukei > 0:
            lines.append(f"★統計検定2級:{total_toukei}h")
            lines.append("")

        # 達成・課題
        lines.append("達成:")
        lines.append("今月の目標時間達成")
        lines.append("")

        lines.append("来月重点:")
        lines.append("次フェーズに向けた準備")
        lines.append("")

        # 論語引用
        rongo = random.choice(RONGO_QUOTES)
        lines.append(rongo)
        lines.append("")

        # ハッシュタグ
        lines.append("#中小企業診断士")

        return "\n".join(lines)
