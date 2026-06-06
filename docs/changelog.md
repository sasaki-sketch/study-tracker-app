# データベース変更履歴

## 2026-01-05

### データベーススキーマ変更

#### 追加カラム
```sql
ALTER TABLE subjects ADD COLUMN standard_hours REAL DEFAULT 0;
ALTER TABLE subjects ADD COLUMN target_score INTEGER DEFAULT 0;
ALTER TABLE subjects ADD COLUMN notes TEXT;
```

#### 変更内容
| 科目 | 変更項目 | 変更前 | 変更後 |
|---|---|---|---|
| 財務・会計 | target_hours | 100.0 | 80.0 |
| 財務・会計 | standard_hours | - | 150.0 |
| 財務・会計 | target_score | - | 80 |
| 財務・会計 | notes | - | 簿記2級保有による削減 |
| 経営情報システム | target_hours | 70.0 | 50.0 |
| 経営情報システム | standard_hours | - | 80.0 |
| 経営情報システム | target_score | - | 80 |
| 企業経営理論 | target_hours | 90.0 | 100.0 |
| 企業経営理論 | standard_hours | - | 150.0 |
| 企業経営理論 | target_score | - | 75 |
| 運営管理 | target_hours | 80.0 | 150.0 |
| 運営管理 | standard_hours | - | 150.0 |
| 運営管理 | target_score | - | 60 |
| 経済学・経済政策 | target_hours | 90.0 | 70.0 |
| 経済学・経済政策 | standard_hours | - | 90.0 |
| 経済学・経済政策 | target_score | - | 60 |
| 経営法務 | target_hours | 70.0 | 60.0 |
| 経営法務 | standard_hours | - | 80.0 |
| 経営法務 | target_score | - | 75 |
| 中小企業経営・政策 | target_hours | 100.0 | 60.0 |
| 中小企業経営・政策 | standard_hours | - | 60.0 |
| 中小企業経営・政策 | target_score | - | 70 |

### バックアップ作成
- 作業前バックアップ: `study_records_backup_20260105_010734.db`
- 作業後バックアップ: (これから作成)

### 備考
- baseline_hoursは全て0に設定（1/1から学習リスタートのため）
- 詳細な設定根拠は `subject_settings.md` を参照
