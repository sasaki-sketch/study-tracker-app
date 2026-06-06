# Ankiカードスタイル改善ガイド

## 🎯 目的
ギリシャ文字カードの記憶術と使用例のフォントを大きく読みやすくします。

---

## 📋 手順(2分で完了)

### 1. Ankiアプリでカードブラウザを開く

1. Ankiを起動
2. メニューから「ブラウズ」をクリック (⌘+B)
3. 左側のリストで「Greek Letters (Enhanced)」を選択

---

### 2. ノートタイプを編集

1. 上部メニューから「カード...」をクリック
2. 左下の「カード」ボタンをクリック → 「ノートタイプを管理」を選択
3. 「Greek Letters (Enhanced)」を選択して「カード」ボタンをクリック

---

### 3. スタイリング(CSS)を更新

1. ウィンドウ下部の「スタイル」タブをクリック
2. 以下の2つのセクションを探して、フォントサイズを変更:

#### 📝 変更箇所1: ニーモニック(記憶術)

**変更前:**
```css
.mnemonic {
    background: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 15px;
    margin: 15px 0;
    border-radius: 5px;
}

.mnemonic strong {
    color: #856404;
}
```

**変更後:**
```css
.mnemonic {
    background: #fff9e6;
    border-left: 5px solid #ffc107;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
}

.mnemonic strong {
    color: #856404;
    font-size: 22px;
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
}

.mnemonic p {
    color: #333;
    font-size: 20px;
    line-height: 1.7;
    margin: 0;
    font-weight: 500;
}
```

---

#### 📊 変更箇所2: 使用例

**変更前:**
```css
.context {
    background: #d1ecf1;
    border-left: 4px solid #17a2b8;
    padding: 15px;
    margin: 15px 0;
    border-radius: 5px;
}

.context strong {
    color: #0c5460;
}
```

**変更後:**
```css
.context {
    background: #e8f4f8;
    border-left: 5px solid #17a2b8;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
}

.context strong {
    color: #0c5460;
    font-size: 22px;
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
}

.context p {
    color: #333;
    font-size: 20px;
    line-height: 1.7;
    margin: 0;
    font-weight: 500;
}
```

---

### 4. 保存して確認

1. 「保存」ボタンをクリック
2. ウィンドウを閉じる
3. 任意のカードを開いて確認

---

## ✨ 改善内容

| 項目 | 変更前 | 変更後 |
|------|--------|--------|
| 記憶術のフォントサイズ | 16px (デフォルト) | **20px** |
| 使用例のフォントサイズ | 16px (デフォルト) | **20px** |
| タイトルのフォントサイズ | なし | **22px** |
| フォントの太さ | 標準 | **中太 (500)** |
| 行間 | 1.0 | **1.7** |
| パディング | 15px | **20px** |
| 背景色 | やや薄い | **はっきり** |

---

## 🚀 もっと簡単な方法: 完全版CSSをコピペ

スタイルタブの**すべての内容**を以下に置き換えることもできます:

```css
/* ギリシャ文字学習カード用スタイル（改善版） */
.card {
    font-family: -apple-system, BlinkMacSystemFont, 'Hiragino Sans', 'Yu Gothic', 'Meiryo', sans-serif;
    text-align: center;
    padding: 30px 20px;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    font-size: 20px;
    line-height: 1.6;
    max-width: 800px;
    margin: 0 auto;
}

/* 記号表示 */
.symbol {
    font-size: 96px;
    color: #2c3e50;
    margin: 30px 0;
    font-weight: bold;
}

/* 読み方 */
.reading h2 {
    font-size: 56px;
    color: #3498db;
    margin: 20px 0;
    font-weight: bold;
}

.english {
    font-size: 28px;
    color: #7f8c8d;
    font-style: italic;
    margin-top: 10px;
}

/* 質問スタイル */
.question {
    background: white;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.question h3 {
    font-size: 32px;
    color: #2c3e50;
    font-weight: bold;
    line-height: 1.5;
}

/* 回答スタイル */
.answer {
    text-align: left;
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.meaning {
    color: #e74c3c;
    font-size: 24px;
    font-weight: bold;
    border-bottom: 3px solid #e74c3c;
    padding-bottom: 15px;
    margin-bottom: 20px;
    line-height: 1.6;
}

/* ニーモニック(記憶術) - フォント改善 */
.mnemonic {
    background: #fff9e6;
    border-left: 5px solid #ffc107;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
}

.mnemonic strong {
    color: #856404;
    font-size: 22px;
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
}

.mnemonic p {
    color: #333;
    font-size: 20px;
    line-height: 1.7;
    margin: 0;
    font-weight: 500;
}

/* 使用例 - フォント改善 */
.context {
    background: #e8f4f8;
    border-left: 5px solid #17a2b8;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
}

.context strong {
    color: #0c5460;
    font-size: 22px;
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
}

.context p {
    color: #333;
    font-size: 20px;
    line-height: 1.7;
    margin: 0;
    font-weight: 500;
}

/* 補足情報 */
.info {
    margin-top: 25px;
    padding-top: 15px;
    border-top: 2px solid #ddd;
}

.info small {
    color: #6c757d;
    font-size: 18px;
}

.note {
    font-size: 22px;
    color: #6c757d;
    margin: 15px 0;
    font-weight: 500;
}

.hint {
    font-size: 19px;
    color: #95a5a6;
    line-height: 1.6;
}

/* モバイル対応 */
@media (max-width: 600px) {
    .card {
        padding: 20px 15px;
        font-size: 18px;
    }

    .symbol {
        font-size: 72px;
    }

    .reading h2 {
        font-size: 42px;
    }

    .question h3 {
        font-size: 26px;
    }

    .meaning {
        font-size: 20px;
    }

    .mnemonic strong,
    .context strong {
        font-size: 19px;
    }

    .mnemonic p,
    .context p {
        font-size: 18px;
    }
}
```

---

## ❓ トラブルシューティング

### Q: スタイルタブが見つからない
A: カードブラウザ → 上部メニュー「カード...」→ 下部の「スタイル」タブ

### Q: 変更が反映されない
A: 「保存」ボタンを押してからAnkiを再起動してみてください

### Q: 元に戻したい
A: 上記手順で再度編集し、フォントサイズを元の値に戻します

---

## 📸 ビフォー/アフター

### Before:
- 記憶術: 小さい文字 (16px)
- 使用例: 小さい文字 (16px)
- 行間が詰まっている

### After:
- 記憶術: **大きい文字 (20px)**
- 使用例: **大きい文字 (20px)**
- タイトルが目立つ (22px)
- **行間が広くて読みやすい (1.7)**
- **太字で見やすい (font-weight: 500)**

---

この手順で、すべてのカード(72枚)に自動的に新しいスタイルが適用されます!
