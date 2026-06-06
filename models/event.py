"""
イベントモデル定義
"""
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, Literal

EventType = Literal['past_exam', 'material_lap', 'mock_exam']
ExamType = Literal['1次試験', '2次試験']
MaterialType = Literal['テキスト', '問題集', '講義動画', 'その他']

@dataclass
class StudyEvent:
    """学習イベント基底クラス"""
    id: Optional[int] = None
    event_type: EventType = ''
    date: date = field(default_factory=date.today)
    subject: str = ''
    memo: Optional[str] = None

    def validate(self) -> tuple[bool, str]:
        """バリデーション実行"""
        if not self.event_type:
            return False, "イベントタイプが未選択です"
        if not self.subject:
            return False, "科目が未選択です"
        return True, ""


@dataclass
class PastExamEvent(StudyEvent):
    """過去問演習イベント"""
    exam_year: str = ''              # 例: "令和5年度(2023年)"
    question_range: str = ''         # 例: "第1問〜第5問"
    correct_count: int = 0           # 正答数
    total_count: int = 0             # 総問題数
    time_spent: Optional[int] = None # 所要時間(分)

    def __post_init__(self):
        self.event_type = 'past_exam'

    @property
    def correct_rate(self) -> float:
        """正答率計算"""
        if self.total_count == 0:
            return 0.0
        return round(self.correct_count / self.total_count * 100, 1)

    @property
    def is_pass_level(self) -> bool:
        """合格水準判定(70%以上)"""
        return self.correct_rate >= 70.0

    def validate(self) -> tuple[bool, str]:
        """バリデーション"""
        valid, msg = super().validate()
        if not valid:
            return valid, msg

        if not self.exam_year:
            return False, "年度が未選択です"
        if self.correct_count < 0 or self.total_count < 0:
            return False, "問題数は0以上で入力してください"
        if self.correct_count > self.total_count:
            return False, "正答数が総問題数を超えています"
        if self.time_spent is not None and self.time_spent < 0:
            return False, "所要時間は0以上で入力してください"

        return True, ""


@dataclass
class MaterialLapEvent(StudyEvent):
    """教材周回イベント"""
    material_id: int = 0             # 教材ID(外部キー)
    start_page: Optional[int] = None # 開始ページ
    end_page: Optional[int] = None   # 終了ページ
    time_spent: int = 0              # 所要時間(分)
    understanding: int = 3           # 理解度(1〜5)

    def __post_init__(self):
        self.event_type = 'material_lap'

    def validate(self) -> tuple[bool, str]:
        """バリデーション"""
        valid, msg = super().validate()
        if not valid:
            return valid, msg

        if self.material_id == 0:
            return False, "教材が未選択です"
        if self.time_spent < 0:
            return False, "所要時間は0以上で入力してください"
        if not (1 <= self.understanding <= 5):
            return False, "理解度は1〜5で選択してください"
        if self.start_page and self.end_page:
            if self.start_page > self.end_page:
                return False, "開始ページが終了ページより大きいです"

        return True, ""


@dataclass
class MockExamEvent(StudyEvent):
    """模試・答練イベント"""
    exam_name: str = ''              # 試験名
    exam_type: ExamType = '1次試験'
    total_score: Optional[int] = None      # 総合得点(1次)
    max_score: Optional[int] = None        # 配点(1次)
    subject_scores: Optional[dict] = None  # 科目別得点(1次)
    case_grades: Optional[dict] = None     # 事例別評価(2次)

    def __post_init__(self):
        self.event_type = 'mock_exam'

    @property
    def score_rate(self) -> Optional[float]:
        """得点率計算(1次試験のみ)"""
        if self.exam_type == '1次試験' and self.max_score:
            return round(self.total_score / self.max_score * 100, 1)
        return None

    @property
    def is_pass_level(self) -> bool:
        """合格水準判定"""
        if self.exam_type == '1次試験':
            # 420点以上かつ各科目40点以上
            if self.total_score and self.total_score >= 420:
                if self.subject_scores:
                    return all(score >= 40 for score in self.subject_scores.values())
                return True
            return False
        else:
            # 2次: A評価2科目以上かつC以下なし
            if self.case_grades:
                grade_values = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
                grades = [grade_values[g] for g in self.case_grades.values()]
                return sum(1 for g in grades if g >= 4) >= 2 and min(grades) >= 2
            return False

    def validate(self) -> tuple[bool, str]:
        """バリデーション"""
        valid, msg = super().validate()
        if not valid:
            return valid, msg

        if not self.exam_name:
            return False, "試験名が未入力です"

        if self.exam_type == '1次試験':
            if self.total_score is None or self.max_score is None:
                return False, "得点と配点を入力してください"
            if self.total_score < 0 or self.max_score < 0:
                return False, "得点は0以上で入力してください"
            if self.total_score > self.max_score:
                return False, "得点が配点を超えています"
        else:  # 2次試験
            if not self.case_grades or len(self.case_grades) != 4:
                return False, "4事例すべての評価を入力してください"
            valid_grades = {'A', 'B', 'C', 'D'}
            if not all(g in valid_grades for g in self.case_grades.values()):
                return False, "評価はA/B/C/Dで入力してください"

        return True, ""


@dataclass
class Material:
    """教材マスタ"""
    id: Optional[int] = None
    name: str = ''                   # 教材名
    subject: str = ''                # 科目
    material_type: MaterialType = 'テキスト'
    target_laps: int = 3             # 目標周回数
    current_lap: int = 0             # 現在周回数
    total_time: float = 0.0          # 総学習時間
    avg_understanding: float = 0.0   # 平均理解度
    last_study_date: Optional[date] = None

    @property
    def progress_rate(self) -> float:
        """進捗率計算"""
        if self.target_laps == 0:
            return 0.0
        return round(self.current_lap / self.target_laps * 100, 1)

    def validate(self) -> tuple[bool, str]:
        """バリデーション"""
        if not self.name:
            return False, "教材名が未入力です"
        if not self.subject:
            return False, "科目が未選択です"
        if self.target_laps < 0:
            return False, "目標周回数は0以上で入力してください"

        return True, ""
