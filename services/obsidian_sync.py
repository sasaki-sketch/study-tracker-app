"""
Obsidian自動連携サービス
日次ノートから学習記録を抽出してデータベースに同期
"""
import re
from datetime import date, datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple

from models.record import StudyRecord
from services.database import DatabaseService
from utils.phase import get_current_phase
from utils.subjects import normalize_subject_name


class ObsidianSyncService:
    """Obsidian Vaultとの同期を管理"""

    def __init__(self, vault_path: Optional[Path] = None):
        """
        Args:
            vault_path: Obsidian Vaultのパス（デフォルト: ~/02_Knowledge/Obsidian/）
        """
        if vault_path is None:
            vault_path = Path.home() / "02_Knowledge" / "Obsidian"

        self.vault_path = vault_path
        self.daily_notes_path = vault_path / "21_資格学習統合支援システム" / "10_Daily"
        self.db_service = DatabaseService()

    def parse_study_log(self, content: str) -> List[Dict[str, any]]:
        """学習ログセクションから記録を抽出

        Args:
            content: デイリーノートの内容

        Returns:
            [{'subject': '科目名', 'duration_hours': 1.5, 'type': 'shindan'|'toukei'}, ...]
        """
        logs = []

        # dur:: と subject:: パターンを検索
        # 例: "dur:: 25m subject:: 財務会計" または "dur:: 1h subject:: 統計検定"
        pattern = r'dur::\s*(\d+(?:\.\d+)?)\s*(h|m)\s+subject::\s*([^\n|#]+)'
        matches = re.finditer(pattern, content, re.IGNORECASE)

        for match in matches:
            value = float(match.group(1))
            unit = match.group(2).lower()
            subject_raw = match.group(3).strip()

            # 科目名を正規化（略称や別名を正式名称に変換）
            subject = normalize_subject_name(subject_raw)

            # 正規化に失敗した場合（未知の科目名）はスキップ
            if subject is None:
                continue

            # 時間に変換
            if unit == 'm':
                hours = value / 60.0
            else:
                hours = value

            # 科目タイプを判定（統計検定 or 診断士科目）
            if '統計検定' in subject or subject == '統計検定2級':
                study_type = 'toukei'
            else:
                study_type = 'shindan'

            logs.append({
                'subject': subject,
                'duration_hours': round(hours, 2),
                'type': study_type
            })

        return logs

    def aggregate_logs_by_type(self, logs: List[Dict]) -> Tuple[float, str, float]:
        """ログを診断士/統計検定で集計

        Returns:
            (shindan_time, shindan_subject, toukei_time)
        """
        shindan_time = 0.0
        toukei_time = 0.0
        shindan_subjects = []

        for log in logs:
            if log['type'] == 'shindan':
                shindan_time += log['duration_hours']
                if log['subject'] not in shindan_subjects:
                    shindan_subjects.append(log['subject'])
            else:
                toukei_time += log['duration_hours']

        # 複数科目がある場合は最初の科目を代表として使用
        shindan_subject = shindan_subjects[0] if shindan_subjects else ''

        return round(shindan_time, 2), shindan_subject, round(toukei_time, 2)

    def sync_daily_note(self, target_date: date) -> Tuple[bool, str]:
        """指定日のデイリーノートをデータベースに同期

        Args:
            target_date: 同期対象の日付

        Returns:
            (成功/失敗, メッセージ)
        """
        # ファイル名: YYYY-MM-DD.md
        daily_file = self.daily_notes_path / f"{target_date.isoformat()}.md"

        if not daily_file.exists():
            return False, f"ファイルが見つかりません: {daily_file}"

        try:
            # ファイル読み込み
            with open(daily_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 学習ログを抽出
            logs = self.parse_study_log(content)

            if not logs:
                return False, "学習記録が見つかりませんでした"

            # 診断士/統計検定で集計
            shindan_time, shindan_subject, toukei_time = self.aggregate_logs_by_type(logs)

            # フェーズ判定（現在日付ベース）
            phase = get_current_phase()

            # 既存レコードを確認
            existing_record = self.db_service.get_record_by_date(target_date)

            if existing_record:
                # 既存レコードを更新（内容・課題はそのまま保持）
                record = StudyRecord(
                    id=existing_record.id,
                    date=target_date,
                    phase=phase,
                    shindan_time=shindan_time,
                    shindan_subject=shindan_subject,
                    shindan_content=existing_record.shindan_content,
                    shindan_issue=existing_record.shindan_issue,
                    toukei_time=toukei_time,
                    toukei_content=existing_record.toukei_content,
                    toukei_issue=existing_record.toukei_issue
                )
            else:
                # 新規レコード作成
                record = StudyRecord(
                    date=target_date,
                    phase=phase,
                    shindan_time=shindan_time,
                    shindan_subject=shindan_subject,
                    shindan_content='',
                    shindan_issue='',
                    toukei_time=toukei_time,
                    toukei_content='',
                    toukei_issue=''
                )

            # 保存
            self.db_service.save_record(record)

            return True, f"同期完了: 診断士 {shindan_time}h, 統計検定 {toukei_time}h"

        except Exception as e:
            return False, f"エラー: {str(e)}"

    def sync_date_range(self, start_date: date, end_date: date) -> Dict[str, any]:
        """期間内のデイリーノートを一括同期

        Args:
            start_date: 開始日
            end_date: 終了日

        Returns:
            {'success_count': int, 'failed_count': int, 'messages': [str, ...]}
        """
        results = {
            'success_count': 0,
            'failed_count': 0,
            'messages': []
        }

        current = start_date
        while current <= end_date:
            success, message = self.sync_daily_note(current)

            if success:
                results['success_count'] += 1
            else:
                results['failed_count'] += 1

            results['messages'].append(f"{current.isoformat()}: {message}")

            # 次の日へ
            from datetime import timedelta
            current += timedelta(days=1)

        return results

    def get_available_daily_notes(self) -> List[date]:
        """利用可能なデイリーノートの日付リストを取得

        Returns:
            [date, ...] ソート済み
        """
        if not self.daily_notes_path.exists():
            return []

        dates = []
        pattern = re.compile(r'(\d{4}-\d{2}-\d{2})\.md')

        for file in self.daily_notes_path.glob('*.md'):
            match = pattern.match(file.name)
            if match:
                try:
                    date_obj = date.fromisoformat(match.group(1))
                    dates.append(date_obj)
                except ValueError:
                    continue

        return sorted(dates)
