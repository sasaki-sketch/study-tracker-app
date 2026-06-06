-- イベントテーブル作成
CREATE TABLE IF NOT EXISTS study_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT NOT NULL CHECK(event_type IN ('past_exam', 'material_lap', 'mock_exam')),
    date DATE NOT NULL,
    subject TEXT NOT NULL,
    memo TEXT,
    details TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_events_type_date ON study_events(event_type, date DESC);
CREATE INDEX IF NOT EXISTS idx_events_subject ON study_events(subject);
CREATE INDEX IF NOT EXISTS idx_events_date ON study_events(date DESC);

-- 教材マスタテーブル作成
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    material_type TEXT NOT NULL CHECK(material_type IN ('テキスト', '問題集', '講義動画', 'その他')),
    target_laps INTEGER DEFAULT 3 CHECK(target_laps >= 0),
    current_lap INTEGER DEFAULT 0 CHECK(current_lap >= 0),
    total_time REAL DEFAULT 0.0 CHECK(total_time >= 0),
    avg_understanding REAL DEFAULT 0.0 CHECK(avg_understanding >= 0 AND avg_understanding <= 5),
    last_study_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name, subject)
);

CREATE INDEX IF NOT EXISTS idx_materials_subject ON materials(subject);
CREATE INDEX IF NOT EXISTS idx_materials_last_study ON materials(last_study_date DESC);
