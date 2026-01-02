"""
学習記録データモデル
"""
from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class StudyRecord:
    """学習記録"""
    date: date
    phase: str

    # 診断士
    shindan_time: float = 0.0
    shindan_subject: str = ""
    shindan_content: str = ""
    shindan_issue: str = ""

    # 統計
    toukei_time: float = 0.0
    toukei_content: str = ""
    toukei_issue: str = ""

    # ID（DBから取得時のみ）
    id: Optional[int] = None

    def to_dict(self):
        """辞書形式に変換"""
        return {
            'date': self.date.isoformat(),
            'phase': self.phase,
            'shindan_time': self.shindan_time,
            'shindan_subject': self.shindan_subject,
            'shindan_content': self.shindan_content,
            'shindan_issue': self.shindan_issue,
            'toukei_time': self.toukei_time,
            'toukei_content': self.toukei_content,
            'toukei_issue': self.toukei_issue,
        }


@dataclass
class CumulativeStats:
    """累計統計"""
    shindan_total: float = 0.0
    toukei_total: float = 0.0
    shindan_goal: float = 770.0
    toukei_goal: float = 80.0  # 統計検定2級
    shindan_progress: float = 0.0  # パーセント
    toukei_progress: float = 0.0  # パーセント

    def calculate_progress(self):
        """進捗率を計算"""
        if self.shindan_goal > 0:
            self.shindan_progress = round((self.shindan_total / self.shindan_goal) * 100, 1)
        if self.toukei_goal > 0:
            self.toukei_progress = round((self.toukei_total / self.toukei_goal) * 100, 1)
