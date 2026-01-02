# 診断士学習記録アプリ

中小企業診断士・統計検定2級の学習記録を管理するStreamlitアプリケーション

## 特徴

- **日次記録入力**: 診断士・統計の学習時間と内容を記録
- **累計統計表示**: リアルタイムで進捗状況を確認
- **Obsidian連携**: Markdown形式でObsidianに自動出力
- **X投稿文生成**: 自動で学習記録をX投稿用テキストに変換
- **履歴管理**: 過去の学習記録を一覧表示
- **Raycast統合**: ホットキーで素早くアプリを起動

## ディレクトリ構成

```
~/study_app/
├── app.py                    # Streamlitメインアプリ
├── requirements.txt          # Python依存パッケージ
├── test_app.py              # テストスクリプト
│
├── database/
│   └── init_db.py           # データベース初期化
│
├── models/
│   └── record.py            # データモデル (StudyRecord, CumulativeStats)
│
├── services/
│   ├── database.py          # データベース操作サービス
│   ├── obsidian.py          # Obsidianファイル出力
│   └── tweet.py             # X投稿文生成
│
└── utils/
    └── phase.py             # 学習フェーズ判定
```

## インストール

### 1. 依存パッケージのインストール

```bash
cd ~/study_app
pip3 install -r requirements.txt
```

### 2. データベース初期化

```bash
python3 database/init_db.py
```

## 使い方

### 方法1: コマンドラインから起動

```bash
cd ~/study_app
streamlit run app.py
```

ブラウザで自動的に `http://localhost:8501` が開きます。

### 方法2: Raycastから起動

1. Raycastを起動: `⌥Space`
2. コマンド入力: `学習記録`
3. アプリが自動起動します

## 主な機能

### 日次記録入力

1. **日付選択**: カレンダーから記録日を選択
2. **診断士セクション**:
   - 学習時間（h）
   - 科目選択（財務会計、企業経営理論など）
   - 学習内容（例: 過去問15問 正答率70%）
   - 課題（例: 固変分解の理解）
3. **統計セクション**:
   - 学習時間（h）
   - 学習内容（例: 推定演習）
   - 課題（例: 信頼区間の理解）
4. **保存オプション**:
   - 「保存してX投稿文生成」: 記録を保存してX投稿文を自動生成
   - 「保存のみ」: X投稿文生成なしで保存

### 累計統計（サイドバー）

- 診断士累計時間と進捗率（目標630h）
- 統計累計時間
- 現在の学習フェーズ（基礎固め期/応用力強化期/直前追い込み期）

### 履歴表示

過去の学習記録を日付降順で一覧表示

### Obsidian出力

以下のパスにMarkdownファイルを自動生成:

```
~/Documents/01_Knowledge/obsidian-vault/03_Projects/診断士2026_一発合格/09_学習記録/YYYY-MM-DD.md
```

#### ファイル形式

```yaml
---
date: 2026-01-02
phase: 基礎固め期
shindan_time: 3.0
shindan_subject: 財務会計
shindan_cumulative: 3.0
toukei_time: 1.0
toukei_cumulative: 1.0
progress: 0.5
tags:
  - 学習記録
  - 中小企業診断士
  - 統計検定2級
---

# 2026年01月02日の学習記録
...
```

### X投稿文生成

論語引用をランダムに含めた投稿文を自動生成:

```
今日の積み上げ(基礎固め期)

★中小企業診断士:3.0h
  財務会計
  過去問15問 正答率70%
  累計:3.0h/630.0h(0.5%)

★統計検定2級:1.0h
  推定演習
  累計:1.0h

学而時習之、不亦説乎

試験日:統計検定2/1、中小企業診断士8月
#中小企業診断士 #統計検定2級
```

投稿文は自動的にクリップボードにコピーされます。

## データベース

- **形式**: SQLite
- **保存場所**: `~/study_app/study_records.db`
- **テーブル**:
  - `records`: 学習記録
  - `subjects`: 科目マスタ（7科目）

### 科目マスタ

1. 財務会計
2. 企業経営理論
3. 運営管理
4. 経済学
5. 経営情報システム
6. 経営法務
7. 中小企業経営政策

## 学習フェーズ

月によって自動判定:

- **1〜3月**: 基礎固め期
- **4〜5月**: 応用力強化期
- **6〜7月**: 直前追い込み期
- **その他**: 基礎固め期（デフォルト）

## トラブルシューティング

### Streamlitが起動しない

```bash
pip3 install --upgrade streamlit
```

### データベースエラー

データベースを再初期化:

```bash
rm ~/study_app/study_records.db
python3 ~/study_app/database/init_db.py
```

### Obsidianファイルが作成されない

出力先ディレクトリを確認:

```bash
ls ~/Documents/01_Knowledge/obsidian-vault/03_Projects/診断士2026_一発合格/09_学習記録/
```

ディレクトリがない場合は手動で作成:

```bash
mkdir -p ~/Documents/01_Knowledge/obsidian-vault/03_Projects/診断士2026_一発合格/09_学習記録/
```

## テスト

動作確認用のテストスクリプト:

```bash
cd ~/study_app
python3 test_app.py
```

すべてのコンポーネント（DB保存、統計計算、Obsidian出力、投稿文生成）をテストします。

## 今後の拡張予定

### Phase 2: 機能追加
- 週次・月次サマリー表示
- グラフによる可視化（学習時間の推移、科目別分析）
- 統計ダッシュボード

### Phase 3: 連携強化
- Raycastからの直接入力
- 自動起動設定

### Phase 4: デプロイ
- Dockerコンテナ化
- Streamlit Cloudへのデプロイ

## ライセンス

個人用プロジェクト

## 開発情報

- **開発日**: 2026年1月2日
- **バージョン**: 1.0 (Phase 1 MVP)
- **技術スタック**: Python, Streamlit, SQLite
- **開発者**: sasaki
