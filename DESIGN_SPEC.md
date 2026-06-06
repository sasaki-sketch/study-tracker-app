# イベントページ詳細設計書 v1.0

**作成日**: 2026-01-03
**対象アプリ**: 診断士学習記録アプリ
**設計者**: UIUX Designer / PM / 中小企業診断士講師・コンサルタント

---

## 目次

1. [設計方針](#1-設計方針)
2. [情報アーキテクチャ](#2-情報アーキテクチャ)
3. [詳細UI/UXデザイン](#3-詳細uiuxデザイン)
4. [データフロー設計](#4-データフロー設計)
5. [既存ダッシュボード統合設計](#5-既存ダッシュボード統合設計)
6. [実装仕様書（エンジニア向け)](#6-実装仕様書エンジニア向け)
7. [データモデル最終設計](#7-データモデル最終設計)
8. [バリデーションルール](#8-バリデーションルール)
9. [エラーハンドリング](#9-エラーハンドリング)
10. [テスト仕様](#10-テスト仕様)

---

## 1. 設計方針

### 1.1 ビジネス目標
- **問題**: 日々の学習時間は記録できるが、具体的な問題演習の進捗や教材の周回状況を可視化できない
- **目標**: 過去問演習と教材周回を詳細に記録・分析し、試験合格に向けた戦略的な学習を支援する
- **KPI**:
  - イベント記録率 80%以上/月
  - 過去問正答率 70%以上達成
  - 教材3周回以上達成

### 1.2 UX原則
1. **モバイルファースト**: iPhoneでの入力を最優先
2. **3タップルール**: 主要操作は3タップ以内で完結
3. **即座のフィードバック**: 入力完了時に進捗を可視化
4. **学習モチベーション向上**: ゲーミフィケーション要素で継続を促進
5. **既存UIとの一貫性**: 現行ダッシュボードのデザインシステムを継承

### 1.3 技術的制約
- Streamlit 1.51.0の機能範囲内で実装
- SQLite3データベース（既存スキーマとの互換性維持）
- モバイルブラウザでの動作保証（Safari/Chrome iOS）
- レスポンシブデザイン（320px〜1920px対応）

---

## 2. 情報アーキテクチャ

### 2.1 ナビゲーション構造

```
アプリトップ
├── 🏠 ダッシュボード（既存）
├── ✏️ 今日の記録（既存）
├── 📊 分析（既存）
├── 📝 イベント記録（NEW）← 新規タブ
│   ├── 過去問演習記録
│   ├── 教材周回記録
│   └── 模試・答練記録
└── ⚙️ 設定（既存）
```

### 2.2 イベントページ内構造

```
📝 イベント記録タブ
├── [サブタブ1] 📖 過去問演習
│   ├── 新規記録フォーム
│   └── 最近の記録（5件）
├── [サブタブ2] 🔄 教材周回
│   ├── 新規記録フォーム
│   └── 周回進捗一覧
└── [サブタブ3] 🎯 模試・答練
    ├── 新規記録フォーム
    └── 成績推移グラフ
```

---

## 3. 詳細UI/UXデザイン

### 3.1 デザインシステム

#### カラーパレット（既存アプリから継承）
```css
/* プライマリカラー */
--primary-blue: #1f77b4;      /* メインアクション */
--primary-green: #2ecc71;     /* 成功・達成 */
--primary-orange: #ff7f0e;    /* 警告・注意 */
--primary-red: #d62728;       /* エラー・未達成 */

/* セカンダリカラー */
--secondary-cyan: #17becf;    /* 統計検定 */
--secondary-purple: #9467bd;  /* 強調 */

/* ニュートラルカラー */
--text-primary: #2c3e50;      /* 本文 */
--text-secondary: #7f8c8d;    /* 補助テキスト */
--bg-card: #ffffff;           /* カード背景 */
--bg-app: #f8f9fa;            /* アプリ背景 */
--border-light: #e0e0e0;      /* ボーダー */

/* フィードバックカラー */
--success: #27ae60;           /* 正解 */
--warning: #f39c12;           /* 要復習 */
--error: #e74c3c;             /* 不正解 */
--info: #3498db;              /* 情報 */
```

#### タイポグラフィ
```css
/* フォントファミリー */
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans JP", sans-serif;

/* フォントサイズスケール */
--font-size-xs: 12px;    /* キャプション */
--font-size-sm: 14px;    /* 本文小 */
--font-size-md: 16px;    /* 本文 */
--font-size-lg: 18px;    /* 小見出し */
--font-size-xl: 20px;    /* 見出し */
--font-size-2xl: 24px;   /* 大見出し */

/* 行高さ */
--line-height-tight: 1.25;
--line-height-normal: 1.5;
--line-height-relaxed: 1.75;
```

#### スペーシング
```css
/* 8pxグリッドシステム */
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
--space-2xl: 48px;
```

#### ボーダー半径
```css
--radius-sm: 4px;    /* ボタン・タグ */
--radius-md: 8px;    /* カード・入力欄 */
--radius-lg: 12px;   /* モーダル */
```

#### シャドウ
```css
--shadow-sm: 0 1px 3px rgba(0,0,0,0.12);
--shadow-md: 0 4px 6px rgba(0,0,0,0.1);
--shadow-lg: 0 10px 20px rgba(0,0,0,0.15);
```

### 3.2 コンポーネント詳細設計

---

#### 3.2.1 過去問演習記録フォーム

```
┌─────────────────────────────────────────┐
│ 📖 過去問演習を記録                      │
├─────────────────────────────────────────┤
│                                         │
│ 日付 *                                  │
│ ┌─────────────────────────────────────┐ │
│ │ 📅 2026-01-03              ▼        │ │ ← date_input
│ └─────────────────────────────────────┘ │
│                                         │
│ 科目 *                                  │
│ ┌─────────────────────────────────────┐ │
│ │ 財務・会計                ▼        │ │ ← selectbox
│ └─────────────────────────────────────┘ │
│                                         │
│ 年度・回 *                              │
│ ┌─────────────────────────────────────┐ │
│ │ 令和5年度(2023年)          ▼        │ │ ← selectbox
│ └─────────────────────────────────────┘ │
│                                         │
│ 問題範囲                                │
│ ┌─────────────────────────────────────┐ │
│ │ 第1問〜第5問                        │ │ ← text_input
│ └─────────────────────────────────────┘ │
│                                         │
│ 正答数 / 総問題数 *                      │
│ ┌────────────┐   ┌────────────┐        │
│ │    18      │ / │    25      │        │ ← number_input × 2
│ └────────────┘   └────────────┘        │
│                                         │
│ 正答率: 72.0% ✓ 目標達成!               │ ← 即時計算表示
│                                         │
│ 所要時間（分）                           │
│ ┌─────────────────────────────────────┐ │
│ │    45                               │ │ ← number_input
│ └─────────────────────────────────────┘ │
│                                         │
│ 苦手論点・復習メモ                       │
│ ┌─────────────────────────────────────┐ │
│ │ ・資本コスト計算でミス              │ │
│ │ ・CVP分析の固変分解要復習           │ │ ← text_area
│ │                                     │ │   (3行、拡張可能)
│ └─────────────────────────────────────┘ │
│                                         │
│         ┌───────────────┐               │
│         │  💾 記録する   │               │ ← primary button
│         └───────────────┘               │
│                                         │
└─────────────────────────────────────────┘
```

**デザイン仕様:**
- カード幅: モバイル 100%、タブレット+ 600px中央配置
- パディング: 24px (モバイル 16px)
- 入力欄高さ: 44px（タッチターゲット最小サイズ）
- ボタン高さ: 48px、幅200px、中央配置
- 正答率表示:
  - 70%以上: 緑色（`--success`）+ ✓アイコン
  - 50-69%: オレンジ色（`--warning`）+ ⚠アイコン
  - 50%未満: 赤色（`--error`）+ ✗アイコン

**インタラクション:**
1. 正答数/総問題数入力時、リアルタイムで正答率計算
2. 正答率70%以上で「目標達成!」メッセージ表示
3. 保存成功時: 緑色トースト通知「✓ 過去問記録を保存しました」
4. 保存後、フォームリセットして最近の記録を更新

---

#### 3.2.2 教材周回記録フォーム

```
┌─────────────────────────────────────────┐
│ 🔄 教材周回を記録                        │
├─────────────────────────────────────────┤
│                                         │
│ 教材選択                                │
│ ┌─────────────────────────────────────┐ │
│ │ ● 新規教材を追加                     │ │ ← radio button
│ │ ○ 既存教材から選択                   │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ 【新規教材の場合】                       │
│                                         │
│ 教材名 *                                │
│ ┌─────────────────────────────────────┐ │
│ │ スピードテキスト 財務・会計         │ │ ← text_input
│ └─────────────────────────────────────┘ │
│                                         │
│ 科目 *                                  │
│ ┌─────────────────────────────────────┐ │
│ │ 財務・会計                ▼        │ │ ← selectbox
│ └─────────────────────────────────────┘ │
│                                         │
│ 教材タイプ *                            │
│ ┌─────────────────────────────────────┐ │
│ │ テキスト                  ▼        │ │ ← selectbox
│ └─────────────────────────────────────┘ │   (テキスト/問題集/講義/動画)
│                                         │
│ 目標周回数                              │
│ ┌─────────────────────────────────────┐ │
│ │     3                               │ │ ← number_input
│ └─────────────────────────────────────┘ │
│                                         │
│ ─────────────────────────────────────── │
│                                         │
│ 日付 *                                  │
│ ┌─────────────────────────────────────┐ │
│ │ 📅 2026-01-03              ▼        │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ 開始ページ                              │
│ ┌─────────┐   終了ページ  ┌─────────┐  │
│ │   50    │               │   120   │  │ ← number_input × 2
│ └─────────┘               └─────────┘  │
│                                         │
│ 所要時間（分）*                          │
│ ┌─────────────────────────────────────┐ │
│ │    90                               │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ 理解度                                  │
│ ⭐️⭐️⭐️⭐️☆                              │ ← 5段階評価
│                                         │
│ メモ                                    │
│ ┌─────────────────────────────────────┐ │
│ │ WACC計算を重点的に復習              │ │
│ └─────────────────────────────────────┘ │
│                                         │
│         ┌───────────────┐               │
│         │  💾 記録する   │               │
│         └───────────────┘               │
│                                         │
└─────────────────────────────────────────┘
```

**デザイン仕様:**
- ラジオボタン切り替えで「新規教材」「既存教材」フォーム表示切替
- 既存教材選択時は教材名のselectboxのみ表示（他項目は自動入力）
- 理解度: クリック可能な星アイコン（1〜5個点灯）
- ページ範囲: 2つの入力欄を「〜」で視覚的に接続

---

#### 3.2.3 模試・答練記録フォーム

```
┌─────────────────────────────────────────┐
│ 🎯 模試・答練を記録                      │
├─────────────────────────────────────────┤
│                                         │
│ 実施日 *                                │
│ ┌─────────────────────────────────────┐ │
│ │ 📅 2026-01-03              ▼        │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ 試験名 *                                │
│ ┌─────────────────────────────────────┐ │
│ │ TBC模試 第3回                       │ │ ← text_input
│ └─────────────────────────────────────┘ │
│                                         │
│ 試験タイプ *                            │
│ ┌─────────────────────────────────────┐ │
│ │ ● 1次試験                           │ │ ← radio button
│ │ ○ 2次試験                           │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ 【1次試験の場合】                        │
│                                         │
│ 科目別得点                              │
│ ┌──────────────────┬────────┬────────┐ │
│ │ 科目             │ 得点   │ 配点   │ │
│ ├──────────────────┼────────┼────────┤ │
│ │ 財務・会計        │   56   │  100   │ │ ← 7科目分の入力欄
│ │ 企業経営理論      │   68   │  100   │ │
│ │ 運営管理          │   72   │  100   │ │
│ │ ...              │        │        │ │
│ └──────────────────┴────────┴────────┘ │
│                                         │
│ 総合得点: 420点 / 700点（60.0%）         │ ← 自動計算
│ 合格ライン: 420点以上 ✓ クリア!         │
│                                         │
│ 【2次試験の場合】                        │
│                                         │
│ 事例別得点                              │
│ ┌──────────────────┬────────────────┐  │
│ │ 事例I（組織）     │   A         ▼ │  │ ← A/B/C/D評価
│ │ 事例II（マーケ）  │   B         ▼ │  │
│ │ 事例III（生産）   │   B         ▼ │  │
│ │ 事例IV（財務）    │   C         ▼ │  │
│ └──────────────────┴────────────────┘  │
│                                         │
│ 総合評価: B（合格圏内）                  │
│                                         │
│ 振り返りメモ *                           │
│ ┌─────────────────────────────────────┐ │
│ │ ・事例IVの資本コスト計算でミス      │ │
│ │ ・記述量が不足気味、要スピードUP    │ │
│ └─────────────────────────────────────┘ │
│                                         │
│         ┌───────────────┐               │
│         │  💾 記録する   │               │
│         └───────────────┘               │
│                                         │
└─────────────────────────────────────────┘
```

**デザイン仕様:**
- 試験タイプ選択で表示フォーム切替（1次/2次）
- 1次試験: 科目別得点入力テーブル
  - 自動で7科目表示、各科目100点満点
  - 総合得点リアルタイム計算
  - 420点以上で「✓ クリア!」表示（緑色）
- 2次試験: A/B/C/D評価セレクトボックス
  - 総合評価ロジック: A以上×2科目以上かつC以下なし→合格圏内

---

#### 3.2.4 最近の記録表示（過去問演習例）

```
┌─────────────────────────────────────────┐
│ 📋 最近の過去問演習（直近5件）            │
├─────────────────────────────────────────┤
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │ 📅 2026-01-03                       │ │
│ │ 財務・会計 │ 令和5年度              │ │
│ │                                     │ │
│ │ ┌─────────────────────────────────┐ │ │
│ │ │ 正答率 72%  ●●●●●●●○○○        │ │ │ ← プログレスバー
│ │ └─────────────────────────────────┘ │ │
│ │                                     │ │
│ │ 18問正解 / 25問 (45分)              │ │
│ │                                     │ │
│ │ 💭 資本コスト計算でミス...           │ │
│ │                                     │ │
│ │           ┌──────┐  ┌──────┐       │ │
│ │           │ 編集 │  │ 削除 │       │ │ ← 操作ボタン
│ │           └──────┘  └──────┘       │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │ 📅 2026-01-02                       │ │
│ │ 企業経営理論 │ 令和4年度            │ │
│ │ ...                                 │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ （他3件省略）                            │
│                                         │
└─────────────────────────────────────────┘
```

**デザイン仕様:**
- カードレイアウト（margin-bottom: 16px）
- 正答率プログレスバー:
  - 70%以上: 緑色
  - 50-69%: オレンジ色
  - 50%未満: 赤色
- メモは最初の50文字表示、超過時「...」で省略
- 編集/削除ボタン: 小サイズ（height: 32px）、右寄せ

---

#### 3.2.5 教材周回進捗一覧

```
┌─────────────────────────────────────────┐
│ 📚 教材周回進捗                          │
├─────────────────────────────────────────┤
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │ スピードテキスト 財務・会計          │ │
│ │ テキスト │ 目標3周                  │ │
│ │                                     │ │
│ │ 現在の周回数: 2周目                  │ │
│ │                                     │ │
│ │ ┌─────────────────────────────────┐ │ │
│ │ │ 進捗 67%  ●●●●●●●○○○          │ │ │ ← 周回プログレスバー
│ │ └─────────────────────────────────┘ │ │
│ │                                     │ │
│ │ 総学習時間: 18.5時間                 │ │
│ │ 平均理解度: ⭐️⭐️⭐️⭐️☆ (4.2/5.0)      │ │
│ │                                     │ │
│ │ 最終学習日: 2026-01-03               │ │
│ │                                     │ │
│ │     ┌──────────┐  ┌──────────┐     │ │
│ │     │ 詳細表示 │  │ 記録追加 │     │ │
│ │     └──────────┘  └──────────┘     │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │ 過去問完全マスター 企業経営理論      │ │
│ │ 問題集 │ 目標3周                   │ │
│ │ ...                                 │ │
│ └─────────────────────────────────────┘ │
│                                         │
└─────────────────────────────────────────┘
```

**デザイン仕様:**
- 周回プログレスバー: `(現在周回数 / 目標周回数) × 100%`
- 理解度: 全記録の平均値を星で表示
- 「詳細表示」クリック時: 展開して周回履歴リスト表示
- 「記録追加」クリック時: 該当教材が選択済みのフォームを表示

---

#### 3.2.6 模試成績推移グラフ

```
┌─────────────────────────────────────────┐
│ 📈 模試成績推移                          │
├─────────────────────────────────────────┤
│                                         │
│ 【1次試験】                              │
│                                         │
│  得点                                   │
│  (点)                                   │
│   700 ┌─────────────────────────────┐   │
│       │                             │   │
│   600 │           ●─────●           │   │ ← 折れ線グラフ
│       │       ●──╯     ╰──●         │   │   (Plotly)
│   500 │   ●──╯               ╰──●   │   │
│       │                             │   │
│   400 ├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │   │ ← 420点合格ライン
│       │                             │   │
│       └─────────────────────────────┘   │
│         12/1  12/15 12/29  1/12  1/26   │
│                  実施日                  │
│                                         │
│ 【2次試験】                              │
│                                         │
│  評価                                   │
│   A  ┌─────────────────────────────┐   │
│      │     ●         ●             │   │
│   B  │ ●─────●   ●─────●           │   │ ← 事例別推移
│      │                             │   │   (4本の折れ線)
│   C  │                         ●   │   │
│      │                             │   │
│   D  └─────────────────────────────┘   │
│        12/1  12/15 12/29  1/12  1/26   │
│                                         │
│      ■ 事例I  ■ 事例II               │
│      ■ 事例III ■ 事例IV              │   │ ← 凡例
│                                         │
└─────────────────────────────────────────┘
```

**デザイン仕様:**
- Plotly使用、インタラクティブグラフ
- 1次試験: 総合得点の折れ線 + 420点合格ライン
- 2次試験: 事例別（A/B/C/D→4/3/2/1点換算）の4本折れ線
- ホバー表示: 日付、得点、科目別内訳
- レスポンシブ: モバイルで縦スクロール可能

---

### 3.3 レイアウト仕様

#### 3.3.1 モバイルレイアウト（〜768px）

```css
.event-page {
  padding: 12px;
  max-width: 100%;
}

.event-form-card {
  width: 100%;
  padding: 16px;
  margin-bottom: 16px;
  border-radius: 8px;
  box-shadow: var(--shadow-sm);
}

.form-group {
  margin-bottom: 16px;
}

.form-label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 4px;
  color: var(--text-primary);
}

.form-input {
  width: 100%;
  height: 44px;
  padding: 8px 12px;
  font-size: 16px; /* iOS zoom防止 */
  border: 1px solid var(--border-light);
  border-radius: 4px;
}

.btn-primary {
  width: 100%;
  height: 48px;
  font-size: 16px;
  font-weight: 600;
  background: var(--primary-blue);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
```

#### 3.3.2 タブレット・デスクトップレイアウト（768px〜）

```css
.event-page {
  padding: 24px;
  max-width: 1200px;
  margin: 0 auto;
}

.event-form-card {
  width: 600px;
  margin: 0 auto 24px;
  padding: 24px;
}

.form-row {
  display: flex;
  gap: 16px;
}

.form-col-6 {
  flex: 1;
}

.btn-primary {
  width: 200px;
  margin: 0 auto;
  display: block;
}
```

---

## 4. データフロー設計

### 4.1 過去問演習記録のデータフロー

```
【入力フロー】
┌──────────┐
│ ユーザー  │
└─────┬────┘
      │ 1. フォーム入力
      ▼
┌────────────────────┐
│ Streamlit UI       │
│ - 日付選択         │
│ - 科目選択         │
│ - 正答数入力       │
│ - メモ入力         │
└─────┬──────────────┘
      │ 2. バリデーション
      ▼
┌────────────────────┐
│ StudyEvent model   │
│ - データ検証       │
│ - 正答率計算       │
└─────┬──────────────┘
      │ 3. DB保存
      ▼
┌────────────────────┐
│ DatabaseService    │
│ save_event()       │
└─────┬──────────────┘
      │ 4. INSERT
      ▼
┌────────────────────┐
│ SQLite DB          │
│ study_events table │
└────────────────────┘

【出力フロー】
┌────────────────────┐
│ SQLite DB          │
└─────┬──────────────┘
      │ 1. SELECT
      ▼
┌────────────────────┐
│ DatabaseService    │
│ get_recent_events()│
│ get_subject_stats()│
└─────┬──────────────┘
      │ 2. データ集計
      ▼
┌────────────────────┐
│ Analytics Service  │
│ - 平均正答率計算   │
│ - 傾向分析         │
└─────┬──────────────┘
      │ 3. 可視化
      ▼
┌────────────────────┐
│ Streamlit UI       │
│ - カード表示       │
│ - グラフ描画       │
│ - KPI表示          │
└─────┬──────────────┘
      │ 4. レンダリング
      ▼
┌──────────┐
│ ユーザー  │
└──────────┘
```

### 4.2 教材周回記録のデータフロー

```
【新規教材登録】
User Input → Material model → DatabaseService.save_material() → materials table

【周回記録】
User Input → StudyEvent model → DatabaseService.save_event() → study_events table

【進捗表示】
materials table ←┐
                 ├→ DatabaseService.get_material_progress() → UI表示
study_events ←───┘
(GROUP BY material_id, COUNT lap cycles)
```

### 4.3 データ整合性チェックフロー

```
保存前バリデーション:
1. 必須項目チェック（日付、科目、得点etc）
2. 型チェック（数値範囲、日付形式）
3. 論理チェック（正答数 ≤ 総問題数）
4. 重複チェック（同一日・同一試験の重複記録防止）

保存後処理:
1. セッション状態更新
2. キャッシュクリア
3. 成功トースト表示
4. フォームリセット
```

---

## 5. 既存ダッシュボード統合設計

### 5.1 ダッシュボード新規KPIカード

既存のダッシュボード（`show_dashboard()`関数）に以下のKPIカードを追加:

```
┌─────────────────────────────────────────────────────────┐
│ 🏠 ダッシュボード                                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐        │
│ │ 📊 診断士    │ │ 📈 統計検定  │ │ 🎯 総学習    │        │ ← 既存
│ │ 累計465.5h   │ │ 累計120.0h   │ │ 累計585.5h   │        │
│ └─────────────┘ └─────────────┘ └─────────────┘        │
│                                                         │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐        │
│ │ 📖 過去問    │ │ 🔄 教材周回  │ │ 🎯 模試      │        │ ← NEW
│ │ 平均72%      │ │ 5教材 2周目  │ │ 総合58%      │        │
│ │ ↑ +3%       │ │ 進捗67%      │ │ ↓ -2%       │        │
│ └─────────────┘ └─────────────┘ └─────────────┘        │
│                                                         │
│ 📊 学習進捗グラフ（既存）                                │
│ ...                                                     │
│                                                         │
│ 📝 最近のイベント（NEW）                                 │
│ ┌───────────────────────────────────────────────────┐   │
│ │ 📅 01/03 │ 財務 令和5年度 72% ✓                    │   │
│ │ 📅 01/02 │ スピテキ財務 2周目完了 ⭐️⭐️⭐️⭐️          │   │
│ │ 📅 01/01 │ TBC模試3回 420点 合格ライン達成!       │   │
│ └───────────────────────────────────────────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 5.2 追加KPIカード仕様

#### 📖 過去問正答率カード

```python
def show_exam_performance_card():
    """
    表示内容:
    - 直近5回の平均正答率（%）
    - 前回比較（↑/↓ +/-X%）
    - クリック時: イベント記録タブの過去問演習へ遷移

    データ取得:
    SELECT AVG(correct_rate)
    FROM study_events
    WHERE event_type = 'past_exam'
    AND date >= date('now', '-30 days')
    """
    # 実装詳細は後述
```

#### 🔄 教材周回カード

```python
def show_material_progress_card():
    """
    表示内容:
    - 進行中教材数
    - 平均周回数
    - 全体進捗率（現在周回数/目標周回数の平均）

    データ取得:
    SELECT
      COUNT(DISTINCT material_id) as material_count,
      AVG(current_lap / target_laps * 100) as avg_progress
    FROM materials
    WHERE target_laps > 0
    """
```

#### 🎯 模試成績カード

```python
def show_mock_exam_card():
    """
    表示内容:
    - 最新模試の総合得点率（1次）or 総合評価（2次）
    - 前回比較

    データ取得:
    SELECT total_score, max_score, exam_type
    FROM study_events
    WHERE event_type = 'mock_exam'
    ORDER BY date DESC
    LIMIT 2
    """
```

### 5.3 「最近のイベント」タイムラインコンポーネント

```python
def show_recent_events_timeline(limit=5):
    """
    直近のイベント（過去問/教材/模試）を統合表示

    UI仕様:
    - カード型リスト
    - イベントタイプ別アイコン
    - 日付降順
    - 各イベントの主要指標をサマリー表示

    クリック動作:
    - イベントカードクリック時、該当イベントの詳細モーダル表示
    """
    events = db.get_recent_events(limit=limit)

    for event in events:
        with st.container():
            col1, col2 = st.columns([1, 5])
            with col1:
                st.write(event.get_icon())  # 📖/🔄/🎯
            with col2:
                st.markdown(f"**{event.date}** | {event.get_summary()}")
                # 過去問: "財務 令和5年度 72% ✓"
                # 教材: "スピテキ財務 2周目完了 ⭐⭐⭐⭐"
                # 模試: "TBC模試3回 420点 合格ライン達成!"
```

### 5.4 既存グラフへの統合

既存の「学習時間推移グラフ」に、イベント記録のマーカーを追加:

```
学習時間
(時間)
  10 ┌───────────────────────────────┐
     │           🎯                  │ ← 模試実施日にマーカー
   8 │       ●───●                   │
     │   ●──╯   ╰──●                │
   6 │ ●╯           ╰──●             │
     │                               │
   4 ├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │
     │                               │
     └───────────────────────────────┘
       12/1  12/15 12/29  1/12  1/26
```

実装方法:
```python
# Plotlyグラフにannotation追加
fig.add_annotation(
    x=event_date,
    y=study_hours,
    text="🎯",
    showarrow=True,
    arrowhead=2
)
```

---

## 6. 実装仕様書（エンジニア向け）

### 6.1 ファイル構成

```
study_app/
├── app_v3.py                  # メインアプリ（修正）
├── models/
│   ├── record.py             # 既存
│   └── event.py              # NEW: イベントモデル
├── services/
│   ├── database.py           # 既存（拡張）
│   └── analytics.py          # NEW: 分析サービス
├── database/
│   ├── init_db.py            # 既存（拡張）
│   └── migrations/
│       └── 001_add_events.sql # NEW: マイグレーションSQL
├── components/
│   ├── event_forms.py        # NEW: イベント入力フォーム
│   ├── event_displays.py     # NEW: イベント表示コンポーネント
│   └── dashboard_widgets.py  # NEW: ダッシュボードウィジェット
└── utils/
    ├── validators.py         # NEW: バリデーション関数
    └── formatters.py         # NEW: データフォーマッタ
```

### 6.2 モデル定義

#### models/event.py

```python
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
    time_spent: Optional[int] = None # 所要時間（分）

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
        """合格水準判定（70%以上）"""
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
    material_id: int = 0             # 教材ID（外部キー）
    start_page: Optional[int] = None # 開始ページ
    end_page: Optional[int] = None   # 終了ページ
    time_spent: int = 0              # 所要時間（分）
    understanding: int = 3           # 理解度（1〜5）

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
    total_score: Optional[int] = None      # 総合得点（1次）
    max_score: Optional[int] = None        # 配点（1次）
    subject_scores: Optional[dict] = None  # 科目別得点（1次）
    case_grades: Optional[dict] = None     # 事例別評価（2次）

    def __post_init__(self):
        self.event_type = 'mock_exam'

    @property
    def score_rate(self) -> Optional[float]:
        """得点率計算（1次試験のみ）"""
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
```

### 6.3 データベースサービス拡張

#### services/database.py（追加メソッド）

```python
"""
データベース操作サービス（拡張）
"""
import json
from typing import List, Optional
from models.event import StudyEvent, PastExamEvent, MaterialLapEvent, MockExamEvent, Material

class DatabaseService:
    # ... 既存メソッド ...

    # ============================================
    # イベント関連メソッド
    # ============================================

    def save_event(self, event: StudyEvent) -> int:
        """イベント保存

        Args:
            event: 保存するイベント

        Returns:
            保存したレコードのID
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # イベント共通データ
            base_data = {
                'event_type': event.event_type,
                'date': event.date.isoformat(),
                'subject': event.subject,
                'memo': event.memo
            }

            # イベントタイプ別の詳細データをJSON化
            if isinstance(event, PastExamEvent):
                details = {
                    'exam_year': event.exam_year,
                    'question_range': event.question_range,
                    'correct_count': event.correct_count,
                    'total_count': event.total_count,
                    'time_spent': event.time_spent
                }
            elif isinstance(event, MaterialLapEvent):
                details = {
                    'material_id': event.material_id,
                    'start_page': event.start_page,
                    'end_page': event.end_page,
                    'time_spent': event.time_spent,
                    'understanding': event.understanding
                }
            elif isinstance(event, MockExamEvent):
                details = {
                    'exam_name': event.exam_name,
                    'exam_type': event.exam_type,
                    'total_score': event.total_score,
                    'max_score': event.max_score,
                    'subject_scores': event.subject_scores,
                    'case_grades': event.case_grades
                }
            else:
                details = {}

            cursor.execute('''
                INSERT INTO study_events
                (event_type, date, subject, memo, details, created_at)
                VALUES (?, ?, ?, ?, ?, datetime('now'))
            ''', (
                base_data['event_type'],
                base_data['date'],
                base_data['subject'],
                base_data['memo'],
                json.dumps(details, ensure_ascii=False)
            ))

            return cursor.lastrowid

    def get_events_by_type(self, event_type: str, limit: int = 5) -> List[StudyEvent]:
        """イベントタイプ別取得

        Args:
            event_type: 'past_exam' | 'material_lap' | 'mock_exam'
            limit: 取得件数

        Returns:
            イベントリスト
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM study_events
                WHERE event_type = ?
                ORDER BY date DESC
                LIMIT ?
            ''', (event_type, limit))

            rows = cursor.fetchall()
            return [self._row_to_event(row) for row in rows]

    def get_recent_events(self, limit: int = 10) -> List[StudyEvent]:
        """最近のイベント取得（全タイプ混合）

        Args:
            limit: 取得件数

        Returns:
            イベントリスト
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM study_events
                ORDER BY date DESC, created_at DESC
                LIMIT ?
            ''', (limit,))

            rows = cursor.fetchall()
            return [self._row_to_event(row) for row in rows]

    def get_subject_exam_stats(self, subject: str) -> dict:
        """科目別過去問統計

        Args:
            subject: 科目名

        Returns:
            統計データ {
                'avg_correct_rate': 平均正答率,
                'total_attempts': 試行回数,
                'recent_trend': 直近5回の正答率推移
            }
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT details
                FROM study_events
                WHERE event_type = 'past_exam' AND subject = ?
                ORDER BY date DESC
            ''', (subject,))

            rows = cursor.fetchall()

            if not rows:
                return {
                    'avg_correct_rate': 0.0,
                    'total_attempts': 0,
                    'recent_trend': []
                }

            rates = []
            for row in rows:
                details = json.loads(row['details'])
                if details['total_count'] > 0:
                    rate = details['correct_count'] / details['total_count'] * 100
                    rates.append(round(rate, 1))

            return {
                'avg_correct_rate': round(sum(rates) / len(rates), 1) if rates else 0.0,
                'total_attempts': len(rates),
                'recent_trend': rates[:5]
            }

    def delete_event(self, event_id: int) -> bool:
        """イベント削除

        Args:
            event_id: イベントID

        Returns:
            削除成功したか
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('DELETE FROM study_events WHERE id = ?', (event_id,))

            return cursor.rowcount > 0

    # ============================================
    # 教材関連メソッド
    # ============================================

    def save_material(self, material: Material) -> int:
        """教材保存

        Args:
            material: 教材データ

        Returns:
            保存したレコードのID
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            if material.id:
                # 更新
                cursor.execute('''
                    UPDATE materials SET
                        name = ?, subject = ?, material_type = ?,
                        target_laps = ?, current_lap = ?,
                        total_time = ?, avg_understanding = ?,
                        last_study_date = ?, updated_at = datetime('now')
                    WHERE id = ?
                ''', (
                    material.name, material.subject, material.material_type,
                    material.target_laps, material.current_lap,
                    material.total_time, material.avg_understanding,
                    material.last_study_date.isoformat() if material.last_study_date else None,
                    material.id
                ))
                return material.id
            else:
                # 新規登録
                cursor.execute('''
                    INSERT INTO materials
                    (name, subject, material_type, target_laps, current_lap,
                     total_time, avg_understanding, last_study_date, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
                ''', (
                    material.name, material.subject, material.material_type,
                    material.target_laps, material.current_lap,
                    material.total_time, material.avg_understanding,
                    material.last_study_date.isoformat() if material.last_study_date else None
                ))
                return cursor.lastrowid

    def get_all_materials(self) -> List[Material]:
        """全教材取得"""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM materials
                ORDER BY last_study_date DESC NULLS LAST, name
            ''')

            rows = cursor.fetchall()
            return [self._row_to_material(row) for row in rows]

    def get_material_by_id(self, material_id: int) -> Optional[Material]:
        """教材ID検索"""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM materials WHERE id = ?', (material_id,))
            row = cursor.fetchone()

            return self._row_to_material(row) if row else None

    def update_material_progress(self, material_id: int):
        """教材進捗更新（イベント記録時に自動実行）

        study_eventsテーブルから該当教材の統計を再計算してmaterialsを更新
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # 周回数と統計の計算
            cursor.execute('''
                SELECT
                    COUNT(*) as lap_count,
                    SUM(json_extract(details, '$.time_spent')) as total_time,
                    AVG(json_extract(details, '$.understanding')) as avg_understanding,
                    MAX(date) as last_date
                FROM study_events
                WHERE event_type = 'material_lap'
                  AND json_extract(details, '$.material_id') = ?
            ''', (material_id,))

            row = cursor.fetchone()

            if row and row['lap_count'] > 0:
                cursor.execute('''
                    UPDATE materials SET
                        current_lap = ?,
                        total_time = ?,
                        avg_understanding = ?,
                        last_study_date = ?,
                        updated_at = datetime('now')
                    WHERE id = ?
                ''', (
                    row['lap_count'],
                    row['total_time'] or 0.0,
                    round(row['avg_understanding'], 1) if row['avg_understanding'] else 0.0,
                    row['last_date'],
                    material_id
                ))

    # ============================================
    # ヘルパーメソッド
    # ============================================

    def _row_to_event(self, row: sqlite3.Row) -> StudyEvent:
        """DB行をイベントオブジェクトに変換"""
        event_type = row['event_type']
        details = json.loads(row['details']) if row['details'] else {}

        base_kwargs = {
            'id': row['id'],
            'date': date.fromisoformat(row['date']),
            'subject': row['subject'],
            'memo': row['memo']
        }

        if event_type == 'past_exam':
            return PastExamEvent(
                **base_kwargs,
                exam_year=details.get('exam_year', ''),
                question_range=details.get('question_range', ''),
                correct_count=details.get('correct_count', 0),
                total_count=details.get('total_count', 0),
                time_spent=details.get('time_spent')
            )
        elif event_type == 'material_lap':
            return MaterialLapEvent(
                **base_kwargs,
                material_id=details.get('material_id', 0),
                start_page=details.get('start_page'),
                end_page=details.get('end_page'),
                time_spent=details.get('time_spent', 0),
                understanding=details.get('understanding', 3)
            )
        elif event_type == 'mock_exam':
            return MockExamEvent(
                **base_kwargs,
                exam_name=details.get('exam_name', ''),
                exam_type=details.get('exam_type', '1次試験'),
                total_score=details.get('total_score'),
                max_score=details.get('max_score'),
                subject_scores=details.get('subject_scores'),
                case_grades=details.get('case_grades')
            )
        else:
            return StudyEvent(**base_kwargs)

    def _row_to_material(self, row: sqlite3.Row) -> Material:
        """DB行を教材オブジェクトに変換"""
        return Material(
            id=row['id'],
            name=row['name'],
            subject=row['subject'],
            material_type=row['material_type'],
            target_laps=row['target_laps'],
            current_lap=row['current_lap'],
            total_time=row['total_time'],
            avg_understanding=row['avg_understanding'],
            last_study_date=date.fromisoformat(row['last_study_date']) if row['last_study_date'] else None
        )
```

### 6.4 コンポーネント実装

#### components/event_forms.py

```python
"""
イベント入力フォームコンポーネント
"""
import streamlit as st
from datetime import date
from models.event import PastExamEvent, MaterialLapEvent, MockExamEvent, Material
from services.database import DatabaseService

db = DatabaseService()

def render_past_exam_form():
    """過去問演習記録フォーム"""
    st.markdown("### 📖 過去問演習を記録")

    with st.form("past_exam_form", clear_on_submit=True):
        # 日付
        exam_date = st.date_input(
            "日付 *",
            value=date.today(),
            format="YYYY-MM-DD"
        )

        # 科目
        subjects = db.get_subjects()
        subject = st.selectbox(
            "科目 *",
            options=[s[0] for s in subjects]
        )

        # 年度
        current_year = date.today().year
        years = [f"令和{y-2018}年度({y}年)" for y in range(current_year, current_year-10, -1)]
        exam_year = st.selectbox("年度・回 *", options=years)

        # 問題範囲
        question_range = st.text_input(
            "問題範囲",
            placeholder="例: 第1問〜第5問"
        )

        # 正答数/総問題数
        col1, col2 = st.columns(2)
        with col1:
            correct_count = st.number_input(
                "正答数 *",
                min_value=0,
                value=0,
                step=1
            )
        with col2:
            total_count = st.number_input(
                "総問題数 *",
                min_value=1,
                value=25,
                step=1
            )

        # 正答率表示
        if total_count > 0:
            correct_rate = round(correct_count / total_count * 100, 1)
            if correct_rate >= 70:
                st.success(f"✓ 正答率: {correct_rate}% - 目標達成!")
            elif correct_rate >= 50:
                st.warning(f"⚠ 正答率: {correct_rate}% - もう一歩!")
            else:
                st.error(f"✗ 正答率: {correct_rate}% - 復習必要")

        # 所要時間
        time_spent = st.number_input(
            "所要時間（分）",
            min_value=0,
            value=60,
            step=5
        )

        # メモ
        memo = st.text_area(
            "苦手論点・復習メモ",
            placeholder="例: 資本コスト計算でミス、CVP分析要復習",
            height=100
        )

        # 送信ボタン
        submitted = st.form_submit_button("💾 記録する", use_container_width=True)

        if submitted:
            # イベント作成
            event = PastExamEvent(
                date=exam_date,
                subject=subject,
                exam_year=exam_year,
                question_range=question_range,
                correct_count=correct_count,
                total_count=total_count,
                time_spent=time_spent if time_spent > 0 else None,
                memo=memo if memo else None
            )

            # バリデーション
            valid, error_msg = event.validate()
            if not valid:
                st.error(f"❌ {error_msg}")
                return

            # 保存
            try:
                event_id = db.save_event(event)
                st.success("✅ 過去問記録を保存しました!")
                st.balloons()  # お祝いアニメーション

                # セッション状態更新（ダッシュボード再読み込み用）
                if 'events_updated' not in st.session_state:
                    st.session_state.events_updated = 0
                st.session_state.events_updated += 1

            except Exception as e:
                st.error(f"❌ 保存に失敗しました: {str(e)}")


def render_material_lap_form():
    """教材周回記録フォーム"""
    st.markdown("### 🔄 教材周回を記録")

    # 教材選択モード
    material_mode = st.radio(
        "教材選択",
        options=["新規教材を追加", "既存教材から選択"],
        horizontal=True
    )

    with st.form("material_lap_form", clear_on_submit=True):
        material_id = None

        if material_mode == "新規教材を追加":
            # 新規教材入力
            st.markdown("#### 新規教材情報")

            material_name = st.text_input(
                "教材名 *",
                placeholder="例: スピードテキスト 財務・会計"
            )

            subjects = db.get_subjects()
            material_subject = st.selectbox(
                "科目 *",
                options=[s[0] for s in subjects]
            )

            material_type = st.selectbox(
                "教材タイプ *",
                options=["テキスト", "問題集", "講義動画", "その他"]
            )

            target_laps = st.number_input(
                "目標周回数",
                min_value=1,
                value=3,
                step=1
            )

        else:
            # 既存教材選択
            materials = db.get_all_materials()
            if not materials:
                st.warning("登録済み教材がありません。「新規教材を追加」を選択してください。")
                st.stop()

            material_options = {f"{m.name} ({m.subject})": m.id for m in materials}
            selected_material = st.selectbox(
                "教材を選択 *",
                options=list(material_options.keys())
            )
            material_id = material_options[selected_material]

            # 選択した教材の情報表示
            material = db.get_material_by_id(material_id)
            st.info(f"現在の周回数: {material.current_lap}/{material.target_laps}周")

        st.markdown("---")
        st.markdown("#### 学習記録")

        # 日付
        lap_date = st.date_input(
            "日付 *",
            value=date.today(),
            format="YYYY-MM-DD"
        )

        # ページ範囲
        col1, col2 = st.columns(2)
        with col1:
            start_page = st.number_input(
                "開始ページ",
                min_value=0,
                value=0,
                step=1
            )
        with col2:
            end_page = st.number_input(
                "終了ページ",
                min_value=0,
                value=0,
                step=1
            )

        # 所要時間
        time_spent = st.number_input(
            "所要時間（分）*",
            min_value=0,
            value=60,
            step=10
        )

        # 理解度
        st.markdown("理解度")
        understanding = st.select_slider(
            "理解度",
            options=[1, 2, 3, 4, 5],
            value=3,
            format_func=lambda x: "⭐" * x,
            label_visibility="collapsed"
        )

        # メモ
        memo = st.text_area(
            "メモ",
            placeholder="学習内容や気づきをメモ",
            height=80
        )

        # 送信ボタン
        submitted = st.form_submit_button("💾 記録する", use_container_width=True)

        if submitted:
            # 新規教材の場合は先に教材を登録
            if material_mode == "新規教材を追加":
                new_material = Material(
                    name=material_name,
                    subject=material_subject,
                    material_type=material_type,
                    target_laps=target_laps
                )

                valid, error_msg = new_material.validate()
                if not valid:
                    st.error(f"❌ {error_msg}")
                    return

                material_id = db.save_material(new_material)

            # 周回イベント作成
            event = MaterialLapEvent(
                date=lap_date,
                subject=material_subject if material_mode == "新規教材を追加" else material.subject,
                material_id=material_id,
                start_page=start_page if start_page > 0 else None,
                end_page=end_page if end_page > 0 else None,
                time_spent=time_spent,
                understanding=understanding,
                memo=memo if memo else None
            )

            # バリデーション
            valid, error_msg = event.validate()
            if not valid:
                st.error(f"❌ {error_msg}")
                return

            # 保存
            try:
                event_id = db.save_event(event)

                # 教材進捗更新
                db.update_material_progress(material_id)

                st.success("✅ 教材周回記録を保存しました!")

                # 進捗表示
                updated_material = db.get_material_by_id(material_id)
                st.info(f"📊 現在の進捗: {updated_material.current_lap}/{updated_material.target_laps}周 ({updated_material.progress_rate}%)")

                # セッション状態更新
                if 'events_updated' not in st.session_state:
                    st.session_state.events_updated = 0
                st.session_state.events_updated += 1

            except Exception as e:
                st.error(f"❌ 保存に失敗しました: {str(e)}")


def render_mock_exam_form():
    """模試・答練記録フォーム"""
    st.markdown("### 🎯 模試・答練を記録")

    with st.form("mock_exam_form", clear_on_submit=True):
        # 実施日
        exam_date = st.date_input(
            "実施日 *",
            value=date.today(),
            format="YYYY-MM-DD"
        )

        # 試験名
        exam_name = st.text_input(
            "試験名 *",
            placeholder="例: TBC模試 第3回"
        )

        # 試験タイプ
        exam_type = st.radio(
            "試験タイプ *",
            options=["1次試験", "2次試験"],
            horizontal=True
        )

        subject_scores = None
        case_grades = None
        total_score = None
        max_score = None

        if exam_type == "1次試験":
            st.markdown("#### 科目別得点")

            # 7科目の入力欄
            subjects_1st = [
                "経済学・経済政策",
                "財務・会計",
                "企業経営理論",
                "運営管理",
                "経営法務",
                "経営情報システム",
                "中小企業経営・政策"
            ]

            subject_scores = {}
            total = 0

            for subj in subjects_1st:
                score = st.number_input(
                    f"{subj}",
                    min_value=0,
                    max_value=100,
                    value=60,
                    step=1,
                    key=f"score_{subj}"
                )
                subject_scores[subj] = score
                total += score

            total_score = total
            max_score = 700

            # 総合得点表示
            score_rate = round(total_score / max_score * 100, 1)
            st.markdown(f"**総合得点**: {total_score}点 / {max_score}点 ({score_rate}%)")

            if total_score >= 420 and all(s >= 40 for s in subject_scores.values()):
                st.success("✓ 合格ライン到達!")
            else:
                st.warning("⚠ 合格ラインまであと少し")

        else:  # 2次試験
            st.markdown("#### 事例別評価")

            cases = ["事例I（組織）", "事例II（マーケティング）", "事例III（生産）", "事例IV（財務）"]
            case_grades = {}

            for case in cases:
                grade = st.selectbox(
                    case,
                    options=["A", "B", "C", "D"],
                    index=1,  # デフォルトB
                    key=f"grade_{case}"
                )
                case_grades[case] = grade

            # 総合評価判定
            grade_values = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
            grades = [grade_values[g] for g in case_grades.values()]
            a_count = sum(1 for g in grades if g >= 4)
            has_low = any(g < 2 for g in grades)

            if a_count >= 2 and not has_low:
                st.success("✓ 総合評価: A（合格圏内）")
            elif sum(grades) / len(grades) >= 3:
                st.info("総合評価: B（合格可能性あり）")
            else:
                st.warning("総合評価: C（要努力）")

        # 振り返りメモ
        memo = st.text_area(
            "振り返りメモ *",
            placeholder="試験を振り返って気づいたこと、改善点など",
            height=120
        )

        # 送信ボタン
        submitted = st.form_submit_button("💾 記録する", use_container_width=True)

        if submitted:
            # イベント作成
            event = MockExamEvent(
                date=exam_date,
                subject="総合",  # 模試は科目「総合」
                exam_name=exam_name,
                exam_type=exam_type,
                total_score=total_score,
                max_score=max_score,
                subject_scores=subject_scores,
                case_grades=case_grades,
                memo=memo
            )

            # バリデーション
            valid, error_msg = event.validate()
            if not valid:
                st.error(f"❌ {error_msg}")
                return

            # 保存
            try:
                event_id = db.save_event(event)
                st.success("✅ 模試記録を保存しました!")

                if event.is_pass_level:
                    st.balloons()
                    st.success("🎉 合格水準達成おめでとうございます!")

                # セッション状態更新
                if 'events_updated' not in st.session_state:
                    st.session_state.events_updated = 0
                st.session_state.events_updated += 1

            except Exception as e:
                st.error(f"❌ 保存に失敗しました: {str(e)}")
```

---

## 7. データモデル最終設計

### 7.1 テーブル定義

#### study_eventsテーブル

```sql
CREATE TABLE IF NOT EXISTS study_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT NOT NULL,  -- 'past_exam' | 'material_lap' | 'mock_exam'
    date DATE NOT NULL,
    subject TEXT NOT NULL,     -- 科目名
    memo TEXT,                 -- メモ・振り返り
    details TEXT NOT NULL,     -- JSON形式の詳細データ
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_events_type_date ON study_events(event_type, date DESC);
CREATE INDEX idx_events_subject ON study_events(subject);
```

**detailsカラムのJSON構造例**:

```json
// 過去問演習
{
  "exam_year": "令和5年度(2023年)",
  "question_range": "第1問〜第5問",
  "correct_count": 18,
  "total_count": 25,
  "time_spent": 45
}

// 教材周回
{
  "material_id": 1,
  "start_page": 50,
  "end_page": 120,
  "time_spent": 90,
  "understanding": 4
}

// 模試（1次試験）
{
  "exam_name": "TBC模試 第3回",
  "exam_type": "1次試験",
  "total_score": 456,
  "max_score": 700,
  "subject_scores": {
    "経済学・経済政策": 64,
    "財務・会計": 68,
    ...
  }
}

// 模試（2次試験）
{
  "exam_name": "MMC模試 第2回",
  "exam_type": "2次試験",
  "case_grades": {
    "事例I（組織）": "A",
    "事例II（マーケティング）": "B",
    "事例III（生産）": "B",
    "事例IV（財務）": "A"
  }
}
```

#### materialsテーブル

```sql
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,           -- 教材名
    subject TEXT NOT NULL,        -- 科目
    material_type TEXT NOT NULL,  -- 'テキスト' | '問題集' | '講義動画' | 'その他'
    target_laps INTEGER DEFAULT 3,    -- 目標周回数
    current_lap INTEGER DEFAULT 0,    -- 現在周回数（自動計算）
    total_time REAL DEFAULT 0.0,      -- 総学習時間（自動計算）
    avg_understanding REAL DEFAULT 0.0, -- 平均理解度（自動計算）
    last_study_date DATE,             -- 最終学習日（自動更新）
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name, subject)  -- 同一科目で同名教材の重複防止
);

CREATE INDEX idx_materials_subject ON materials(subject);
```

### 7.2 マイグレーションSQL

#### database/migrations/001_add_events.sql

```sql
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
```

### 7.3 database/init_db.py 拡張

```python
"""
データベース初期化（拡張版）
"""
import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "study_app" / "study_records.db"

def init_database():
    """データベース初期化"""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 既存テーブル作成（省略: 既存のCREATE TABLE文）
    # ...

    # マイグレーションSQL実行
    migration_file = Path(__file__).parent / "migrations" / "001_add_events.sql"
    if migration_file.exists():
        with open(migration_file, 'r', encoding='utf-8') as f:
            migration_sql = f.read()
            cursor.executescript(migration_sql)

    conn.commit()
    conn.close()

    print(f"✅ データベース初期化完了: {DB_PATH}")

if __name__ == "__main__":
    init_database()
```

---

## 8. バリデーションルール

### 8.1 共通バリデーション

| 項目 | ルール | エラーメッセージ |
|------|--------|------------------|
| 日付 | 必須、未来日不可 | "日付を選択してください" / "未来の日付は選択できません" |
| 科目 | 必須、subjects テーブルに存在 | "科目を選択してください" |
| メモ | 任意、1000文字以内 | "メモは1000文字以内で入力してください" |

### 8.2 過去問演習バリデーション

| 項目 | ルール | エラーメッセージ |
|------|--------|------------------|
| 年度 | 必須 | "年度を選択してください" |
| 正答数 | 必須、0以上整数 | "正答数は0以上で入力してください" |
| 総問題数 | 必須、1以上整数 | "総問題数は1以上で入力してください" |
| 正答数 ≤ 総問題数 | true | "正答数が総問題数を超えています" |
| 所要時間 | 任意、0以上整数 | "所要時間は0以上で入力してください" |

### 8.3 教材周回バリデーション

| 項目 | ルール | エラーメッセージ |
|------|--------|------------------|
| 教材ID | 必須、materials テーブルに存在 | "教材を選択してください" |
| 教材名（新規時） | 必須、100文字以内 | "教材名を入力してください" / "教材名は100文字以内" |
| 目標周回数 | 1以上整数 | "目標周回数は1以上で入力してください" |
| 所要時間 | 必須、0以上整数 | "所要時間を入力してください" |
| 理解度 | 必須、1〜5の整数 | "理解度を選択してください" |
| 開始ページ ≤ 終了ページ | true（両方入力時） | "開始ページが終了ページより大きいです" |

### 8.4 模試バリデーション

| 項目 | ルール | エラーメッセージ |
|------|--------|------------------|
| 試験名 | 必須、100文字以内 | "試験名を入力してください" |
| 試験タイプ | 必須、1次 or 2次 | "試験タイプを選択してください" |
| **1次試験** |||
| 総合得点 | 必須、0〜700の整数 | "得点を入力してください" / "得点は0〜700点で入力" |
| 科目別得点 | 各0〜100の整数 | "各科目の得点は0〜100点で入力してください" |
| **2次試験** |||
| 事例別評価 | 必須、4事例すべてA/B/C/D | "4事例すべての評価を入力してください" |
| 振り返りメモ | 必須、2000文字以内 | "振り返りメモを入力してください" |

---

## 9. エラーハンドリング

### 9.1 エラー種別と対処

| エラー種別 | 発生場所 | 対処方法 | UI表示 |
|------------|----------|----------|--------|
| バリデーションエラー | フォーム送信時 | ユーザー修正待ち | `st.error()` で赤色メッセージ |
| DB接続エラー | DatabaseService | リトライ3回、失敗時エラー表示 | `st.error("データベース接続エラー")` |
| DB保存エラー | save系メソッド | ロールバック、エラーログ出力 | `st.error("保存に失敗しました")` |
| データ不整合 | データ取得時 | デフォルト値返却 | 警告ログ出力（ユーザーに非表示） |
| 権限エラー | ファイル操作時 | エラーメッセージ表示 | `st.error("ファイルアクセス権限がありません")` |

### 9.2 エラーメッセージ実装例

```python
# utils/validators.py

def validate_past_exam_event(event: PastExamEvent) -> tuple[bool, str]:
    """過去問演習イベントのバリデーション"""

    if not event.subject:
        return False, "❌ 科目を選択してください"

    if not event.exam_year:
        return False, "❌ 年度を選択してください"

    if event.correct_count < 0 or event.total_count < 0:
        return False, "❌ 問題数は0以上で入力してください"

    if event.correct_count > event.total_count:
        return False, "❌ 正答数が総問題数を超えています"

    if event.time_spent is not None and event.time_spent < 0:
        return False, "❌ 所要時間は0以上で入力してください"

    return True, ""


def safe_db_operation(func):
    """データベース操作のデコレータ（エラーハンドリング）"""
    def wrapper(*args, **kwargs):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except sqlite3.OperationalError as e:
                if attempt < max_retries - 1:
                    time.sleep(0.5)  # 0.5秒待ってリトライ
                    continue
                else:
                    st.error("❌ データベース接続エラーが発生しました。しばらくしてから再度お試しください。")
                    logging.error(f"DB Error after {max_retries} retries: {str(e)}")
                    return None
            except Exception as e:
                st.error(f"❌ エラーが発生しました: {str(e)}")
                logging.error(f"Unexpected error in {func.__name__}: {str(e)}")
                return None
    return wrapper
```

---

## 10. テスト仕様

### 10.1 単体テスト

#### models/event.py のテスト

```python
# tests/test_event_models.py

import pytest
from datetime import date
from models.event import PastExamEvent, MaterialLapEvent, MockExamEvent, Material

class TestPastExamEvent:
    def test_correct_rate_calculation(self):
        """正答率計算のテスト"""
        event = PastExamEvent(
            date=date.today(),
            subject="財務・会計",
            exam_year="令和5年度",
            correct_count=18,
            total_count=25
        )
        assert event.correct_rate == 72.0

    def test_correct_rate_zero_division(self):
        """総問題数0の場合のテスト"""
        event = PastExamEvent(
            correct_count=0,
            total_count=0
        )
        assert event.correct_rate == 0.0

    def test_is_pass_level(self):
        """合格水準判定のテスト"""
        event_pass = PastExamEvent(correct_count=18, total_count=25)  # 72%
        event_fail = PastExamEvent(correct_count=12, total_count=25)  # 48%

        assert event_pass.is_pass_level == True
        assert event_fail.is_pass_level == False

    def test_validation_success(self):
        """正常データのバリデーション"""
        event = PastExamEvent(
            date=date.today(),
            subject="財務・会計",
            exam_year="令和5年度",
            correct_count=18,
            total_count=25,
            time_spent=45
        )
        valid, msg = event.validate()
        assert valid == True
        assert msg == ""

    def test_validation_negative_count(self):
        """負の問題数のバリデーション"""
        event = PastExamEvent(
            subject="財務・会計",
            exam_year="令和5年度",
            correct_count=-5,
            total_count=25
        )
        valid, msg = event.validate()
        assert valid == False
        assert "0以上" in msg

    def test_validation_correct_exceeds_total(self):
        """正答数 > 総問題数のバリデーション"""
        event = PastExamEvent(
            subject="財務・会計",
            exam_year="令和5年度",
            correct_count=30,
            total_count=25
        )
        valid, msg = event.validate()
        assert valid == False
        assert "超えています" in msg


class TestMaterial:
    def test_progress_rate_calculation(self):
        """進捗率計算のテスト"""
        material = Material(
            name="スピテキ財務",
            subject="財務・会計",
            target_laps=3,
            current_lap=2
        )
        assert material.progress_rate == 66.7

    def test_progress_rate_zero_target(self):
        """目標0の場合のテスト"""
        material = Material(
            name="テスト教材",
            subject="財務・会計",
            target_laps=0,
            current_lap=1
        )
        assert material.progress_rate == 0.0
```

### 10.2 統合テスト

#### DatabaseServiceのテスト

```python
# tests/test_database_service.py

import pytest
from datetime import date
from services.database import DatabaseService
from models.event import PastExamEvent, Material

@pytest.fixture
def db():
    """テスト用データベース"""
    db = DatabaseService()
    db.db_path = ":memory:"  # インメモリDB使用
    # テーブル作成
    # ...
    return db

class TestDatabaseService:
    def test_save_and_get_past_exam_event(self, db):
        """過去問イベントの保存と取得"""
        event = PastExamEvent(
            date=date.today(),
            subject="財務・会計",
            exam_year="令和5年度",
            correct_count=18,
            total_count=25
        )

        # 保存
        event_id = db.save_event(event)
        assert event_id > 0

        # 取得
        events = db.get_events_by_type('past_exam', limit=1)
        assert len(events) == 1
        assert events[0].correct_count == 18
        assert events[0].correct_rate == 72.0

    def test_get_subject_exam_stats(self, db):
        """科目別統計取得テスト"""
        # テストデータ投入
        for i, correct in enumerate([18, 20, 15, 22, 19]):
            event = PastExamEvent(
                date=date(2026, 1, i+1),
                subject="財務・会計",
                exam_year="令和5年度",
                correct_count=correct,
                total_count=25
            )
            db.save_event(event)

        # 統計取得
        stats = db.get_subject_exam_stats("財務・会計")

        assert stats['total_attempts'] == 5
        assert 70.0 <= stats['avg_correct_rate'] <= 80.0  # 平均74.8%
        assert len(stats['recent_trend']) == 5

    def test_update_material_progress(self, db):
        """教材進捗更新テスト"""
        # 教材作成
        material = Material(
            name="スピテキ財務",
            subject="財務・会計",
            target_laps=3
        )
        material_id = db.save_material(material)

        # 周回記録を3件追加
        for i in range(3):
            event = MaterialLapEvent(
                date=date(2026, 1, i+1),
                subject="財務・会計",
                material_id=material_id,
                time_spent=90,
                understanding=4
            )
            db.save_event(event)
            db.update_material_progress(material_id)

        # 教材取得
        updated_material = db.get_material_by_id(material_id)

        assert updated_material.current_lap == 3
        assert updated_material.total_time == 270.0
        assert updated_material.avg_understanding == 4.0
        assert updated_material.progress_rate == 100.0
```

### 10.3 UIテスト（手動テスト項目）

| テスト項目 | 手順 | 期待結果 |
|-----------|------|----------|
| 過去問フォーム送信 | 1. 全項目入力<br>2. 記録ボタンクリック | ✅成功メッセージ表示、最近の記録に追加 |
| 正答率リアルタイム計算 | 正答数/総問題数を変更 | 即座に正答率が再計算・表示 |
| 教材新規登録 | 1. 新規教材選択<br>2. 教材情報入力<br>3. 記録ボタン | 教材マスタに追加、周回記録も保存 |
| 教材進捗表示 | 教材周回進捗一覧を表示 | 周回数、進捗率、平均理解度が正しく表示 |
| 模試フォーム切替 | 試験タイプを1次⇔2次切替 | フォーム表示が切り替わる |
| ダッシュボードKPI更新 | イベント記録後、ダッシュボード表示 | KPIカードに最新データ反映 |
| モバイル表示 | iPhoneでアクセス | 全フォームがタッチ操作可能 |
| バリデーションエラー | 必須項目未入力で送信 | 赤色エラーメッセージ表示 |

---

## 次のステップ

この詳細設計書をもとに、エンジニアは以下の順序で実装を進めます:

### フェーズ1: データベース・モデル構築（1-2日）
1. `database/migrations/001_add_events.sql` 作成
2. `database/init_db.py` 拡張
3. `models/event.py` 実装
4. 単体テスト作成・実行

### フェーズ2: データベースサービス拡張（2-3日）
1. `services/database.py` に新規メソッド追加
2. 統合テスト作成・実行
3. エラーハンドリング実装

### フェーズ3: UIコンポーネント実装（3-4日）
1. `components/event_forms.py` 実装
2. `components/event_displays.py` 実装
3. `components/dashboard_widgets.py` 実装
4. CSSスタイル適用

### フェーズ4: 既存アプリ統合（2-3日）
1. `app_v3.py` にイベントタブ追加
2. ダッシュボードにKPIカード追加
3. ナビゲーション調整

### フェーズ5: テスト・デバッグ（2-3日）
1. 手動UIテスト
2. モバイル動作確認
3. パフォーマンステスト
4. バグ修正

**総見積もり**: 10〜15営業日

---

以上、詳細設計書を完成させました。エンジニアが実装に着手できる状態になっています。
