"""
Obsidianファイル出力サービス
"""
from datetime import date
from pathlib import Path
from typing import Optional

from models.record import StudyRecord, CumulativeStats

# Obsidian Vault パス
OBSIDIAN_VAULT = Path.home() / "Documents" / "01_Knowledge" / "obsidian-vault" / "03_Projects" / "診断士2026_一発合格" / "09_学習記録"


class ObsidianService:
    """Obsidianファイル出力クラス"""

    def __init__(self):
        self.vault_path = OBSIDIAN_VAULT
        # ディレクトリが存在しない場合は作成
        self.vault_path.mkdir(parents=True, exist_ok=True)

    def generate_frontmatter(self, record: StudyRecord, stats: CumulativeStats) -> str:
        """YAMLフロントマターを生成"""
        frontmatter = f"""---
date: {record.date.isoformat()}
phase: {record.phase}
shindan_time: {record.shindan_time}
shindan_subject: {record.shindan_subject}
shindan_cumulative: {stats.shindan_total}
toukei_time: {record.toukei_time}
toukei_cumulative: {stats.toukei_total}
progress: {stats.shindan_progress}
tags:
  - 学習記録
  - 中小企業診断士
  - 統計検定2級
---
"""
        return frontmatter

    def generate_markdown_body(self, record: StudyRecord, stats: CumulativeStats) -> str:
        """Markdownボディを生成"""
        body_parts = []

        # タイトル
        body_parts.append(f"# {record.date.strftime('%Y年%m月%d日')}の学習記録\n")

        # フェーズ
        body_parts.append(f"**フェーズ**: {record.phase}\n")

        # 中小企業診断士セクション
        body_parts.append("## 中小企業診断士\n")
        body_parts.append(f"**学習時間**: {record.shindan_time}h\n")

        if record.shindan_subject:
            body_parts.append(f"**科目**: {record.shindan_subject}\n")

        if record.shindan_content:
            body_parts.append(f"**学習内容**:\n{record.shindan_content}\n")

        if record.shindan_issue:
            body_parts.append(f"**課題**:\n{record.shindan_issue}\n")

        # 累計表示
        body_parts.append(f"**累計時間**: {stats.shindan_total}h / {stats.shindan_goal}h ({stats.shindan_progress}%)\n")

        # 統計検定2級セクション
        body_parts.append("## 統計検定2級\n")
        body_parts.append(f"**学習時間**: {record.toukei_time}h\n")

        if record.toukei_content:
            body_parts.append(f"**学習内容**:\n{record.toukei_content}\n")

        if record.toukei_issue:
            body_parts.append(f"**課題**:\n{record.toukei_issue}\n")

        # 累計表示
        body_parts.append(f"**累計時間**: {stats.toukei_total}h\n")

        return "\n".join(body_parts)

    def export_to_obsidian(self, record: StudyRecord, stats: CumulativeStats) -> Path:
        """Obsidianファイルとして出力"""
        # ファイル名: YYYY-MM-DD.md
        filename = f"{record.date.isoformat()}.md"
        file_path = self.vault_path / filename

        # フロントマター生成
        frontmatter = self.generate_frontmatter(record, stats)

        # ボディ生成
        body = self.generate_markdown_body(record, stats)

        # ファイル書き込み
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write("\n")
            f.write(body)

        return file_path

    def read_existing_record(self, target_date: date) -> Optional[dict]:
        """既存のObsidianファイルから記録を読み込み"""
        filename = f"{target_date.isoformat()}.md"
        file_path = self.vault_path / filename

        if not file_path.exists():
            return None

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # YAMLフロントマターをパース（簡易版）
        if not content.startswith('---'):
            return None

        # フロントマター部分を抽出
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None

        frontmatter_text = parts[1]

        # 簡易的なYAMLパース
        record_data = {}
        for line in frontmatter_text.strip().split('\n'):
            if ':' in line and not line.strip().startswith('-'):
                key, value = line.split(':', 1)
                record_data[key.strip()] = value.strip()

        return record_data
