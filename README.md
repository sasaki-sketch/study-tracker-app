# 診断士学習記録アプリ v3

中小企業診断士・統計検定2級の学習記録を管理するStreamlitアプリケーション

**バージョン**: 3.0
**最終更新**: 2026年1月5日
**開発者**: sasaki

## ✨ 特徴

### 主要機能
- **📝 日次記録入力**: 複数科目対応、セッションベースの詳細記録
- **📊 ダッシュボード**: リアルタイム進捗、KPI可視化、今日のミッション表示
- **📈 分析機能**: 週次・月次統計、科目別進捗、Plotlyグラフ可視化
- **📖 イベント記録**: 過去問演習・教材周回・模試記録の管理
- **🐦 X投稿文自動生成**: Anthropic Claude APIによる投稿文作成
- **📓 Obsidian連携**: Markdown形式での自動出力
- **🔗 n8n連携**: Webhook経由でのデータ送信（週次サマリー対応）
- **📦 アーカイブ**: 過去取得資格の記録管理

## 📁 ディレクトリ構成

```
~/study_app/
├── app_v3.py                      # メインアプリケーション (1,787行)
├── requirements.txt               # Python依存パッケージ
├── study_records.db              # SQLiteデータベース
├── README.md                     # このファイル
├── CLAUDE.md                     # Claude Code開発ルール
├── DESIGN_SPEC.md               # 設計仕様書
├── DEPLOYMENT.md                # デプロイメント手順
│
├── components/                   # UIコンポーネント
│   ├── __init__.py
│   ├── daily_input.py           # 日次記録入力フォーム
│   ├── event_forms.py           # イベント記録フォーム（過去問・教材・模試）
│   ├── analytics_charts.py      # 分析グラフ（Plotly）
│   ├── roadmap.py               # ロードマップ表示
│   ├── review.py                # 週次・月次レビュー
│   ├── subjects.py              # 科目別進捗表示
│   ├── subject_settings.py      # 科目設定画面
│   ├── kpi_dashboard.py         # KPIダッシュボード
│   └── tweet_char_counter.py    # 文字数カウンター
│
├── services/                     # ビジネスロジック層
│   ├── database.py              # データベース操作（CRUD）
│   ├── analytics.py             # 分析サービス（統計計算）
│   ├── record_handler.py        # 記録処理ハンドラー
│   ├── obsidian.py              # Obsidian出力サービス
│   ├── obsidian_sync.py         # Obsidian同期サービス
│   └── tweet.py                 # X投稿文生成サービス
│
├── models/                       # データモデル
│   └── record.py                # StudyRecord, StudySession, CumulativeStats
│
├── utils/                        # ユーティリティ
│   ├── __init__.py
│   ├── stats.py                 # 統計計算関数
│   ├── subjects.py              # 科目マスタデータ
│   ├── phase.py                 # 学習フェーズ判定
│   ├── quotes.py                # 名言データ
│   ├── roadmap.py               # ロードマップ定義
│   ├── event_stats.py           # イベント統計計算
│   ├── visualizations.py        # グラフ生成関数
│   ├── image_generator.py       # SNS投稿画像生成
│   ├── tweet_generator.py       # 投稿文生成補助
│   ├── tweet_prompts.py         # AIプロンプト定義
│   └── webhook.py               # n8n Webhook連携
│
├── database/
│   └── init_db.py               # データベース初期化スクリプト
│
├── config/                       # 設定ファイル
│   ├── constants.py             # 定数定義
│   └── subjects.py              # 科目設定
│
├── docs/                         # ドキュメント
│   └── (各種設計ドキュメント)
│
├── logs/                         # ログファイル
│
└── test_*.py                     # テストスクリプト
```

## 🚀 セットアップ

### 1. 依存パッケージのインストール

```bash
cd ~/study_app
pip3 install -r requirements.txt
```

**必要なパッケージ**:
- streamlit==1.51.0
- pyperclip==1.11.0
- pandas==2.3.3
- plotly>=5.18.0

### 2. 環境変数の設定

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

※ X投稿文の自動生成にはAnthropic Claude APIキーが必要です

### 3. データベース初期化

```bash
python3 database/init_db.py
```

データベーステーブル:
- `records` - 日次学習記録
- `study_sessions` - セッション別詳細記録
- `subjects` - 科目マスタ
- `events` - イベント記録（過去問・教材・模試）
- `materials` - 教材マスタ

## 💻 使い方

### 起動方法

#### 方法1: コマンドラインから起動

```bash
cd ~/study_app
streamlit run app_v3.py
```

ブラウザで自動的に `http://localhost:8501` が開きます。

#### 方法2: スタートアップスクリプト使用

```bash
cd ~/study_app
./start_streamlit.sh
```

#### 方法3: Raycastから起動（推奨）

1. Raycastを起動: `⌥Space`
2. コマンド入力: `学習記録`
3. アプリが自動起動します

## 📖 主要機能の詳細

### 🏠 ダッシュボード

#### 今日のミッション
- 統計検定2級・診断士の今日の学習目標時間を表示
- リアルタイムで進捗率を可視化（プログレスバー）
- 残り日数に基づいた動的な目標時間計算

#### 試験日カウントダウン
- 統計検定2級: 2026年2月1日
- 診断士一次試験: 2026年8月5日
- 必要な学習ペース（h/日）を自動計算
- 継続日数（連続学習記録）
- 学習実施率（開始日からの実績）

#### 診断士7科目チェックリスト
- 財務会計、企業経営理論、運営管理、経済学、経営情報システム、経営法務、中小企業経営政策
- 各科目の学習時間・進捗率・ステータスを可視化
- 未着手科目の警告表示

#### その他の表示
- 累計進捗（目標 vs 実績グラフ）
- 週次・月次学習状況
- 過去問・教材・模試の記録サマリー
- 学習データ可視化（Plotlyグラフ）
- ロードマップ表示
- 過去の学習成果

### ✏️ 日次記録入力（複数科目対応）

#### 入力方式
- **複数セッション対応**: 同じ日に複数科目を記録可能
- **セッション追加**: 「+ セッション追加」ボタンで動的に入力欄を増やす
- **科目選択**: プルダウンで診断士7科目 or 統計検定2級を選択

#### 入力項目
1. **日付選択**: カレンダーから記録日を選択
2. **学習フェーズ**: 基礎固め期/応用力強化期/直前追い込み期/2次試験対策
3. **各セッション**:
   - 資格選択（診断士一次/二次、統計検定）
   - 科目選択
   - 学習時間（h）
   - 学習内容（例: 過去問15問 正答率70%）
   - 気づき・課題（例: 固変分解の理解が不足）

#### 保存オプション
- **保存してX投稿文生成**: Claude APIで投稿文を自動生成し、クリップボードにコピー
- **保存のみ**: データベースに保存のみ（投稿文生成なし）

### 📊 分析画面

#### KPIメトリクス
- 総学習時間
- 平均学習時間（日次・週次）
- 学習日数・実施率
- フェーズ別目標達成率

#### グラフ可視化（Plotly）
- **時系列グラフ**: 日次学習時間の推移（診断士・統計を色分け）
- **週次比較グラフ**: 過去4週間の学習時間比較
- **科目別グラフ**: 各科目の学習時間を横棒グラフで表示

#### インサイト表示
- 学習傾向の分析
- 改善提案
- モチベーションメッセージ

#### 学習履歴テーブル
- 日付・フェーズ・科目別の詳細記録
- セッション単位での表示
- 投稿文の再生成機能

#### 資格フィルタ
- 現在の学習（診断士＋統計）
- 診断士（一次＋二次）
- 診断士一次試験のみ
- 診断士二次試験のみ
- 統計検定のみ
- 全て（過去資格含む）

### 📝 イベント記録

#### 📖 過去問演習
- 年度・科目・問題番号の記録
- 正答数・総問題数・正答率の自動計算
- メモ・振り返りの記録
- 最近の過去問実施履歴表示
- 平均正答率・合格水準達成率の統計表示

#### 📚 教材周回
- 教材マスタ登録（教材名・科目・種別・目標周回数）
- 周回記録（日付・周回番号・学習時間・理解度・メモ）
- 進捗率の自動計算（現在周回数/目標周回数）
- 教材一覧と周回履歴の表示
- 完了教材の統計

#### 📊 模試・答練
- 一次試験：7科目の得点・満点・得点率を記録
- 二次試験：事例Ⅰ〜Ⅳの得点・ランク（A〜D）を記録
- 主催者・試験名・受験日の記録
- 全体評価・振り返りメモ
- 最近の模試履歴・パフォーマンス分析

### 📜 サイドバー：最近の学習記録

- 最新5件の学習記録をカード表示
- クリックでX投稿文プレビューを表示
- 投稿文の編集・再生成機能
- Xへの投稿リンク・クリップボードコピー
- プロンプトのカスタマイズ機能

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

### 🐦 X投稿文自動生成（Anthropic Claude API）

#### 生成フロー
1. **プロンプト作成**: カスタマイズ可能なAIプロンプトを自動生成
2. **Claude API呼び出し**: `claude-sonnet-4-20250514` モデルで投稿文を生成
3. **プレビュー表示**: テキストエリアで編集可能
4. **文字数カウント**: X/Twitter の文字数制限（280文字 or 4,000文字）に対応
5. **アクション**:
   - Xで投稿する（X Intent URLで開く）
   - クリップボードにコピー
   - プロンプトを編集して再生成

#### 投稿文の形式例

```
✒️サマリ
1月5日 / Day 5：中小企業診断士への積み上げ
⏱️本日の学習時間：3.0h（中小企業診断士2.0h + 統計検定2級1.0h）

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

🏢 中小企業診断士
🎯 学習進捗：財務会計 過去問15問 正答率70%
💡 気付き：固変分解の理解が不足
⏱️ 学習時間累計（基礎固め期）：50.0h/240h

ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

📈 統計検定2級
🎯 学習進捗：推定演習
💡 気付き：信頼区間の計算方法を復習
⏱️ 学習時間累計：15.0h/80h

#中小企業診断士 #まとめシート #統計検定2級 #勉強垢
```

投稿文は自動的にクリップボードにコピーされます。

#### 🎨 SNS投稿用画像生成
- 週次サマリー画像を自動生成（PNG形式）
- 過去問・教材・学習時間の統計を美しく可視化
- ダウンロードボタンでローカル保存

### 📦 アーカイブ

過去に取得した資格（簿記、基本情報技術者など）の学習記録を管理
- 資格別の学習実績表示
- 科目別詳細テーブル
- データ分類状況の確認

### ⚙️ 設定

#### 科目設定
- 科目のカスタマイズ（追加・削除・目標時間設定）
- 診断士一次試験7科目の管理

#### データベース管理
- 総記録数・総学習時間の表示
- 生データビューアー（全セッションデータの閲覧・削除）

#### データバックアップ
- 日々の記録をCSVエクスポート
- イベント記録をCSVエクスポート
- 教材マスタをCSVエクスポート

#### n8n連携
- イベント登録時の自動Webhook送信
- 週次サマリーの手動送信

## 🗄️ データベース構造

### SQLite データベース
- **保存場所**: `~/study_app/study_records.db`
- **バックアップ**: 自動バックアップファイル生成

### テーブル構成

#### `records` - 日次学習記録
- `id`, `date`, `phase`
- `shindan_time`, `shindan_subject`, `shindan_content`, `shindan_issue`
- `toukei_time`, `toukei_content`, `toukei_issue`

#### `study_sessions` - セッション別詳細記録
- `id`, `record_id`
- `qualification` (shindan_1ji, shindan_2ji, toukei, boki, kihon_joho, other)
- `subject`, `time_hours`, `content`, `issue`

#### `subjects` - 科目マスタ
- `id`, `name`, `abbreviation`, `recommended_hours`

#### `events` - イベント記録
- `id`, `event_type` (past_exam, material_lap, mock_exam)
- `date`, `subject`, `details` (JSON), `memo`

#### `materials` - 教材マスタ
- `id`, `name`, `subject`, `material_type`
- `target_laps`, `current_lap`, `total_time`, `avg_understanding`

### 診断士一次試験 科目マスタ（7科目）

1. 財務会計（目標: 100h）
2. 企業経営理論（目標: 90h）
3. 運営管理（目標: 80h）
4. 経済学（目標: 100h）
5. 経営情報システム（目標: 70h）
6. 経営法務（目標: 80h）
7. 中小企業経営政策（目標: 80h）

**合計目標時間**: 600h（一次試験）+ 170h（二次試験）= 770h

## 🎯 学習フェーズ

月によって自動判定:

- **1〜3月**: 基礎固め期（目標: 240h）
- **4〜5月**: 応用力強化期（目標: 400h）
- **6〜7月**: 直前追い込み期（目標: 570h）
- **8月以降**: 2次試験対策（目標: 240h）

### 動的な目標時間計算
- 残り日数から1日あたりの必要学習時間を自動計算
- 統計検定試験前: 統計優先（統計2.5h + 診断士0.5h = 合計3h/日）
- 1次試験対策期間: 診断士のみ（3h/日）
- 2次試験対策期間: 診断士2次のみ（3h/日）

## 🔧 技術仕様

### フロントエンド
- **フレームワーク**: Streamlit 1.51.0
- **レスポンシブ対応**: モバイル・タブレット最適化CSS
- **UI/UXデザイン**: カスタムCSS、グラデーション、プログレスバー

### バックエンド
- **言語**: Python 3.x
- **データベース**: SQLite3
- **データ処理**: Pandas 2.3.3

### 可視化
- **グラフライブラリ**: Plotly 5.18.0+
- **画像生成**: PIL (Pillow)

### 外部連携
- **AI**: Anthropic Claude API (claude-sonnet-4-20250514)
- **Webhook**: n8n (REST API)
- **ノート**: Obsidian (Markdown出力)
- **クリップボード**: pyperclip 1.11.0

### アーキテクチャ
- **レイヤー構成**:
  - Presentation Layer: `components/`
  - Business Logic Layer: `services/`
  - Data Access Layer: `database/`, `models/`
  - Utility Layer: `utils/`, `config/`

## 🧪 テスト

### テストスクリプト
```bash
cd ~/study_app
python3 test_app.py              # 基本動作テスト
python3 test_integration.py      # 統合テスト
python3 test_edge_cases.py       # エッジケーステスト
python3 test_webhook.py          # Webhook連携テスト
python3 test_image_gen.py        # 画像生成テスト
```

すべてのコンポーネント（DB保存、統計計算、Obsidian出力、投稿文生成）をテストします。

## 🐛 トラブルシューティング

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

### X投稿文が生成されない
環境変数を確認:
```bash
echo $ANTHROPIC_API_KEY
```

未設定の場合:
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### n8n Webhookエラー
- n8nワークフローが起動しているか確認
- Webhook URLが正しいか確認（`utils/webhook.py`）
- ネットワーク接続を確認

## 📊 現在の開発状況

### ✅ 完了した機能（v3.0）
- [x] 複数科目対応の日次記録入力
- [x] セッションベースの詳細記録
- [x] リアルタイムダッシュボード（KPI、今日のミッション）
- [x] 診断士7科目チェックリスト
- [x] 分析機能（週次・月次統計、Plotlyグラフ）
- [x] イベント記録（過去問・教材・模試）
- [x] X投稿文自動生成（Claude API）
- [x] SNS投稿画像生成
- [x] Obsidian連携
- [x] n8n Webhook連携
- [x] アーカイブ機能
- [x] データバックアップ（CSV エクスポート）
- [x] モバイル対応（レスポンシブCSS）
- [x] 科目設定画面

### 🚧 今後の拡張予定

#### Phase 4: UX改善
- [ ] Raycastからの直接入力機能
- [ ] ダークモード対応
- [ ] キーボードショートカット

#### Phase 5: 分析強化
- [ ] 学習効率分析（時間あたりの進捗）
- [ ] 予測機能（目標達成予測）
- [ ] AIによる学習アドバイス

#### Phase 6: 連携拡張
- [ ] Notion連携
- [ ] Google Calendar連携
- [ ] Slack通知

#### Phase 7: デプロイ
- [ ] Dockerコンテナ化
- [ ] VPS/クラウドへのデプロイ
- [ ] マルチユーザー対応

## 📝 バージョン履歴

- **v3.0** (2026-01-05): セッションベース記録、イベント管理、分析強化
- **v2.0** (2026-01-02): ダッシュボード追加、グラフ可視化
- **v1.0** (2026-01-02): Phase 1 MVP リリース

## 📄 ライセンス

個人用プロジェクト

## 👤 作成者

sasaki (@your-twitter-handle)

## 🚨 重要：開発ルール

### Anthropic API使用制限（絶対遵守）

- **`anthropic.Anthropic()` および `client.messages.create()` の使用は、X投稿文生成（`services/record_handler.py`内）のみ許可**
- それ以外の場所では**絶対に使用禁止**
- 理由: 従量課金APIのため、X投稿文生成以外でコストをかけないため

### 詳細ルール

プロジェクトルートの `CLAUDE.md` を参照してください。

## 開発情報

- **開発日**: 2026年1月2日
- **バージョン**: 1.0 (Phase 1 MVP)
- **技術スタック**: Python, Streamlit, SQLite
- **開発者**: sasaki
