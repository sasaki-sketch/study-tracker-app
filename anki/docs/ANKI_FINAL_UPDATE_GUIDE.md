# 🎨 Ankiカード最終改善ガイド（v2.0）

## 🎯 改善内容

スクリーンショットで確認された問題を**完全に解決**します:

### ✅ 修正された問題
1. ❌ **表面のギリシャ文字が小さい** → ✅ **180pxに大幅拡大**
2. ❌ **カタカナ読み方が見づらい** → ✅ **72pxに拡大 + 鮮やかな青色**
3. ❌ **英語表記が薄い** → ✅ **36pxに拡大 + 濃いグレー**
4. ❌ **記憶術・使用例が読みづらい** → ✅ **22pxに拡大 + ほぼ黒文字**

---

## 📊 改善の詳細

| 要素 | 変更前 | 変更後 | 改善率 |
|------|--------|--------|--------|
| **ギリシャ文字** | 72px | **180px** | **+150%** |
| **カタカナ読み** | 48px | **72px** | **+50%** |
| **英語読み** | 24px | **36px** | **+50%** |
| **記憶術テキスト** | 16px | **22px** | **+38%** |
| **使用例テキスト** | 16px | **22px** | **+38%** |
| **文字色** | グレー系 | **ほぼ黒(#1a1a1a)** | 視認性MAX |
| **背景** | グラデーション | **シンプル白** | コントラスト向上 |

---

## 🚀 更新手順（1分で完了）

### ステップ1: Ankiでスタイルエディタを開く

1. Ankiを起動
2. **ブラウズ**(⌘+B)をクリック
3. 左側で **Greek Letters (Enhanced)** を選択
4. 上部メニュー → **カード...** をクリック
5. 下部の **「スタイル」タブ** をクリック

### ステップ2: CSSを全て置き換え

1. エディタ内の **全テキストを選択** (⌘+A)
2. **削除** (Delete)
3. 以下の**改善版CSS v2.0**を貼り付け
4. **保存**ボタンをクリック

---

## 📋 改善版CSS v2.0（全文コピペ用）

```css
/* ギリシャ文字学習カード用スタイル（最終改善版 v2.0） */

.card {
    font-family: -apple-system, BlinkMacSystemFont, 'Hiragino Sans', 'Yu Gothic', 'Meiryo', sans-serif;
    text-align: center;
    padding: 40px 25px;
    background: #ffffff;  /* シンプルな白背景 */
    font-size: 20px;
    line-height: 1.6;
    max-width: 900px;
    margin: 0 auto;
}

/* カード表面: 1文字だけのシンプル表示 */
.card {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 300px;
}

/* 記号表示 - 超大型化 */
.symbol {
    font-size: 180px;  /* 超巨大! */
    color: #1a1a1a;    /* ほぼ黒 */
    margin: 40px 0;
    font-weight: bold;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* 読み方表示 */
.reading {
    background: #f8f9fa;
    padding: 50px;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}

.reading h2 {
    font-size: 72px;   /* カタカナ大型化 */
    color: #2563eb;    /* 鮮やかな青 */
    margin: 20px 0;
    font-weight: bold;
    text-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.english {
    font-size: 36px;   /* 英語も大きく */
    color: #4b5563;    /* 濃いグレー */
    font-style: italic;
    margin-top: 15px;
    font-weight: 500;
}

/* 質問形式のカード */
.question {
    background: #f8f9fa;
    padding: 50px;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin: 20px 0;
}

.question h3 {
    font-size: 36px;
    color: #1a1a1a;
    font-weight: bold;
    line-height: 1.6;
}

/* 回答スタイル */
.answer {
    text-align: left;
    background: #ffffff;
    padding: 35px;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin: 20px 0;
}

.meaning {
    color: #dc2626;
    font-size: 26px;
    font-weight: bold;
    border-bottom: 4px solid #dc2626;
    padding-bottom: 18px;
    margin-bottom: 25px;
    line-height: 1.7;
}

/* ニーモニック(記憶術) - 大幅改善 */
.mnemonic {
    background: #fffbeb;
    border-left: 6px solid #f59e0b;
    padding: 25px;
    margin: 25px 0;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.mnemonic strong {
    color: #92400e;
    font-size: 24px;
    display: block;
    margin-bottom: 12px;
    font-weight: bold;
}

.mnemonic p {
    color: #1a1a1a;     /* ほぼ黒で読みやすく */
    font-size: 22px;
    line-height: 1.8;
    margin: 0;
    font-weight: 500;
}

/* 使用例 - 大幅改善 */
.context {
    background: #eff6ff;
    border-left: 6px solid #3b82f6;
    padding: 25px;
    margin: 25px 0;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.context strong {
    color: #1e3a8a;
    font-size: 24px;
    display: block;
    margin-bottom: 12px;
    font-weight: bold;
}

.context p {
    color: #1a1a1a;     /* ほぼ黒で読みやすく */
    font-size: 22px;
    line-height: 1.8;
    margin: 0;
    font-weight: 500;
}

/* 補足情報 */
.info {
    margin-top: 30px;
    padding-top: 20px;
    border-top: 2px solid #e5e7eb;
}

.info small {
    color: #6b7280;
    font-size: 20px;
}

.note {
    font-size: 24px;
    color: #4b5563;
    margin: 18px 0;
    font-weight: 500;
}

.hint {
    font-size: 21px;
    color: #6b7280;
    line-height: 1.7;
}

/* モバイル対応 */
@media (max-width: 600px) {
    .card {
        padding: 25px 15px;
        font-size: 18px;
    }

    .symbol {
        font-size: 120px;
    }

    .reading h2 {
        font-size: 52px;
    }

    .english {
        font-size: 28px;
    }

    .question h3 {
        font-size: 28px;
    }

    .meaning {
        font-size: 22px;
    }

    .mnemonic strong,
    .context strong {
        font-size: 21px;
    }

    .mnemonic p,
    .context p {
        font-size: 20px;
    }
}

/* 高コントラストモード */
@media (prefers-contrast: high) {
    .symbol {
        color: #000000;
    }

    .reading h2 {
        color: #0047ab;
    }

    .mnemonic {
        background: #fff5cc;
        border-left-color: #cc7a00;
    }

    .context {
        background: #e0f0ff;
        border-left-color: #0066cc;
    }
}
```

---

## ✨ Before / After 比較

### 📱 カード表面（読み方カード）

#### Before:
```
υ              ← 小さい(72px)、薄いグレー
ウプシロン      ← 普通サイズ(48px)、薄い青
upsilon        ← 小さい(24px)、薄いグレー
```

#### After:
```
υ              ← 超巨大(180px)、ほぼ黒
ウプシロン      ← 大きい(72px)、鮮やかな青
upsilon        ← 大きい(36px)、濃いグレー
```

### 📝 カード裏面（意味+記憶術）

#### Before:
- 記憶術: 16px、薄いグレー、読みづらい
- 使用例: 16px、薄いグレー、読みづらい

#### After:
- 記憶術: **22px**、**ほぼ黒**、**太字**、明るい黄色背景
- 使用例: **22px**、**ほぼ黒**、**太字**、明るい青色背景

---

## 🎯 更新後の確認方法

1. Ankiで任意のカードを開く
2. **表面**: ギリシャ文字が画面いっぱいに大きく表示
3. **裏面**: 記憶術と使用例が読みやすい大きさ
4. **色**: すべて濃い色ではっきり見える

---

## 💡 さらにカスタマイズしたい場合

### もっと大きくしたい:
```css
.symbol {
    font-size: 220px;  /* 180px → 220px */
}
```

### 背景を変えたい:
```css
.card {
    background: #f0f9ff;  /* 薄い青背景 */
}
```

### 文字をもっと濃くしたい:
```css
.mnemonic p,
.context p {
    color: #000000;  /* 完全な黒 */
}
```

---

## ❓ トラブルシューティング

### Q: 保存ボタンが見つからない
A: スタイルエディタの下部にあります。見つからない場合はウィンドウをスクロールしてください。

### Q: エラーが出る
A: CSS全体をコピーできているか確認してください。途中で切れていないか確認。

### Q: 変更が反映されない
A: 保存後、カードを一度閉じて再度開いてください。それでもダメならAnkiを再起動。

---

## 🎉 完成!

この更新で、すべてのカード(72枚)が**一瞬で**読みやすくなります!

質問があれば、遠慮なくお知らせください。
