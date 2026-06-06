"""
学習記録データモデル
"""
from dataclasses import dataclass
from datetime import date
from typing import Optional, List

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
    # 診断士（全体）
    shindan_total: float = 0.0
    shindan_goal: float = 240.0
    shindan_progress: float = 0.0

    # 診断士1次試験
    shindan_1ji_total: float = 0.0
    shindan_1ji_goal: float = 520.0
    shindan_1ji_progress: float = 0.0

    # 診断士2次試験
    shindan_2ji_total: float = 0.0
    shindan_2ji_goal: float = 200.0
    shindan_2ji_progress: float = 0.0

    # 統計検定
    toukei_total: float = 0.0
    toukei_goal: float = 80.0
    toukei_progress: float = 0.0

    def calculate_progress(self):
        """進捗率を計算"""
        if self.shindan_goal > 0:
            self.shindan_progress = round((self.shindan_total / self.shindan_goal) * 100, 1)
        if self.shindan_1ji_goal > 0:
            self.shindan_1ji_progress = round((self.shindan_1ji_total / self.shindan_1ji_goal) * 100, 1)
        if self.shindan_2ji_goal > 0:
            self.shindan_2ji_progress = round((self.shindan_2ji_total / self.shindan_2ji_goal) * 100, 1)
        if self.toukei_goal > 0:
            self.toukei_progress = round((self.toukei_total / self.toukei_goal) * 100, 1)


@dataclass
class StudySession:
    """学習セッション（科目別の学習記録）"""
    record_id: int
    qualification: str  # 'shindan' or 'toukei'
    subject: str
    time_hours: float
    content: str = ""
    issue: str = ""
    id: Optional[int] = None

    def to_dict(self):
        """辞書形式に変換"""
        return {
            'id': self.id,
            'record_id': self.record_id,
            'qualification': self.qualification,
            'subject': self.subject,
            'time_hours': self.time_hours,
            'content': self.content,
            'issue': self.issue
        }

    def validate(self):
        """バリデーション"""
        valid_qualifications = ('shindan', 'shindan_1ji', 'shindan_2ji', 'toukei', 'boki', 'kihon_joho', 'other')
        if self.qualification not in valid_qualifications:
            raise ValueError(f"Invalid qualification: {self.qualification}")
        if self.time_hours < 0:
            raise ValueError(f"time_hours must be >= 0: {self.time_hours}")
        if not self.subject:
            raise ValueError("subject is required")
