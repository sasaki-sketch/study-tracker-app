-- Migration: 複数科目記録対応
-- Date: 2026-01-04
-- Description: study_sessions テーブルを追加し、1日に複数科目を記録できるようにする

-- 1. 新規テーブル作成
CREATE TABLE IF NOT EXISTS study_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    record_id INTEGER NOT NULL,
    qualification TEXT NOT NULL CHECK(qualification IN ('shindan', 'toukei')),
    subject TEXT NOT NULL,
    time_hours REAL NOT NULL CHECK(time_hours >= 0),
    content TEXT,
    issue TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (record_id) REFERENCES records(id) ON DELETE CASCADE
);

-- 2. インデックス作成（パフォーマンス最適化）
CREATE INDEX IF NOT EXISTS idx_study_sessions_record_id ON study_sessions(record_id);
CREATE INDEX IF NOT EXISTS idx_study_sessions_subject ON study_sessions(subject);
CREATE INDEX IF NOT EXISTS idx_study_sessions_qualification ON study_sessions(qualification);

-- 3. 既存データの移行
-- records テーブルから study_sessions へデータ移行
INSERT INTO study_sessions (record_id, qualification, subject, time_hours, content, issue, created_at, updated_at)
SELECT
    id as record_id,
    'shindan' as qualification,
    COALESCE(shindan_subject, '未分類') as subject,
    shindan_time as time_hours,
    shindan_content as content,
    shindan_issue as issue,
    created_at,
    updated_at
FROM records
WHERE shindan_time > 0;

-- 統計検定の既存データも移行
INSERT INTO study_sessions (record_id, qualification, subject, time_hours, content, issue, created_at, updated_at)
SELECT
    id as record_id,
    'toukei' as qualification,
    '統計検定2級' as subject,
    toukei_time as time_hours,
    toukei_content as content,
    toukei_issue as issue,
    created_at,
    updated_at
FROM records
WHERE toukei_time > 0;

-- 4. 既存カラムにコメント追加（SQLiteはCOMMENTをサポートしないため、メモとして記載）
-- records.shindan_time: 診断士学習の合計時間（自動集計値）
-- records.toukei_time: 統計検定学習の合計時間（自動集計値）
-- records.shindan_subject: レガシー対応（後方互換性のため残す、NULLable）
-- records.shindan_content: レガシー対応（後方互換性のため残す）
-- records.shindan_issue: レガシー対応（後方互換性のため残す）
