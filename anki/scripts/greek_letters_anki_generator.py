#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ギリシャ文字学習用Ankiカード生成スクリプト
24文字 × 3タイプ = 72枚のカードを生成
"""

import csv

# PDFから抽出したギリシャ文字の正確な情報
greek_letters_data = [
    {
        "uppercase": "Α", "lowercase": "α", "name_jp": "アルファ", "name_en": "alpha",
        "meaning": "第1種の過誤の確率、有意水準、回帰モデルの切片、クロンバックのアルファ",
        "priority": "S",
        "mnemonic": "アルファ = 'アタック基準' - 研究で仮説を攻撃的に棄却する閾値(通常5%)",
        "context": "α=0.05 は「5%の危険率で帰無仮説を棄却する」ことを意味する"
    },
    {
        "uppercase": "Β", "lowercase": "β", "name_jp": "ベータ", "name_en": "beta",
        "meaning": "ベータ関数(大文字)、第2種の過誤の確率、偏回帰係数",
        "priority": "S",
        "mnemonic": "ベータ = 'ベンリな係数' - 回帰分析で変数の影響力を示す / '2番目のエラー'",
        "context": "β₁ は説明変数が1単位増えたときの目的変数の変化量を表す"
    },
    {
        "uppercase": "Γ", "lowercase": "γ", "name_jp": "ガンマ", "name_en": "gamma",
        "meaning": "ガンマ関数(大文字)、グッドマン=クラスカルのガンマ",
        "priority": "B",
        "mnemonic": "ガンマ = 'がっちり関連' - 順序変数間の関連性を測る統計量",
        "context": "γは-1から1の値を取り、順序関係の一致度を示す"
    },
    {
        "uppercase": "Δ", "lowercase": "δ", "name_jp": "デルタ", "name_en": "delta",
        "meaning": "変化量(大文字)、差、変化量",
        "priority": "B",
        "mnemonic": "デルタ = 'デル(delete)前後の差' - Δx = 変化量、差分を表す記号",
        "context": "Δt は時間の変化量、δは微小な変化を表す"
    },
    {
        "uppercase": "Ε", "lowercase": "ε", "name_jp": "イプシロン", "name_en": "epsilon",
        "meaning": "回帰モデルの誤差項",
        "priority": "B",
        "mnemonic": "イプシロン = 'いっぱいエラー' - 予測値と実測値のズレ(残差)",
        "context": "y = β₀ + β₁x + ε のεは説明できない誤差成分"
    },
    {
        "uppercase": "Ζ", "lowercase": "ζ", "name_jp": "ツェータ", "name_en": "zeta",
        "meaning": "(統計学では使用頻度低)",
        "priority": "C",
        "mnemonic": "ツェータ = 'Z音' - ラテン文字Zに対応するギリシャ文字",
        "context": "高度な数学や物理で使用されるが統計では稀"
    },
    {
        "uppercase": "Η", "lowercase": "η", "name_jp": "イータ", "name_en": "eta",
        "meaning": "相関比(η²)",
        "priority": "B",
        "mnemonic": "イータ = '良い(いい)相関' - 分散分析での効果量を示す指標",
        "context": "η²は全体の分散のうち要因で説明できる割合"
    },
    {
        "uppercase": "Θ", "lowercase": "θ", "name_jp": "シータ", "name_en": "theta",
        "meaning": "母数、定数、推定値",
        "priority": "A",
        "mnemonic": "シータ = '知らない値' - 未知の母数を一般的に表す記号",
        "context": "θ̂(シータハット)は母数θの推定値を意味する"
    },
    {
        "uppercase": "Ι", "lowercase": "ι", "name_jp": "イオタ", "name_en": "iota",
        "meaning": "(統計学では使用頻度低)",
        "priority": "C",
        "mnemonic": "イオタ = 'i(アイ)に似てる' - 英語iとほぼ同じ形",
        "context": "数学の添字などで使用されることがある"
    },
    {
        "uppercase": "Κ", "lowercase": "κ", "name_jp": "カッパ", "name_en": "kappa",
        "meaning": "コーエンのカッパ係数",
        "priority": "B",
        "mnemonic": "カッパ = 'かぶり率チェック' - 評価者間の一致度を測る係数",
        "context": "κ=1なら完全一致、κ=0なら偶然一致と同程度"
    },
    {
        "uppercase": "Λ", "lowercase": "λ", "name_jp": "ラムダ", "name_en": "lambda",
        "meaning": "ウィルクスのラムダ(大文字)、グッドマン=クラスカルのラムダ、ポアソン分布のパラメータ、固有値",
        "priority": "A",
        "mnemonic": "ラムダ = 'ランダム事象の率' - ポアソン分布で単位時間あたりの発生率",
        "context": "λ=3 なら平均して3回/単位時間で事象が起こる"
    },
    {
        "uppercase": "Μ", "lowercase": "μ", "name_jp": "ミュー", "name_en": "mu",
        "meaning": "母平均",
        "priority": "S",
        "mnemonic": "ミュー = 'みんなの平均(Mean)' - 母集団全体の算術平均",
        "context": "標本平均x̄は母平均μの推定値として使われる"
    },
    {
        "uppercase": "Ν", "lowercase": "ν", "name_jp": "ニュー", "name_en": "nu",
        "meaning": "自由度",
        "priority": "A",
        "mnemonic": "ニュー = '新しい(new)計算の数' - t検定やχ²検定で必要な自由度",
        "context": "n個のデータでk個の制約があるとき自由度=n-k"
    },
    {
        "uppercase": "Ξ", "lowercase": "ξ", "name_jp": "グザイ", "name_en": "xi",
        "meaning": "(統計学では使用頻度低)",
        "priority": "C",
        "mnemonic": "グザイ = '具(ぐ)体性ない変数' - 特殊な文脈で使われる",
        "context": "確率過程や特性関数などの高度な分野で登場"
    },
    {
        "uppercase": "Ο", "lowercase": "ο", "name_jp": "オミクロン", "name_en": "omicron",
        "meaning": "(統計学では使用頻度低)",
        "priority": "C",
        "mnemonic": "オミクロン = 'O(オー)と同じ' - 英語のOと区別がつかない",
        "context": "使用されることは極めて稀"
    },
    {
        "uppercase": "Π", "lowercase": "π", "name_jp": "パイ", "name_en": "pi",
        "meaning": "総乗(大文字)、円周率",
        "priority": "A",
        "mnemonic": "パイ = 'パイを割る(3.14...)' - 円周率 or 確率の積",
        "context": "統計では母比率や同時確率の計算で使用"
    },
    {
        "uppercase": "Ρ", "lowercase": "ρ", "name_jp": "ロー", "name_en": "rho",
        "meaning": "相関係数",
        "priority": "S",
        "mnemonic": "ロー = 'ロープで結ぶ' - 2変数間の関連性の強さ(-1〜1)",
        "context": "ρ=0なら無相関、ρ=±1なら完全相関"
    },
    {
        "uppercase": "Σ", "lowercase": "σ", "name_jp": "シグマ", "name_en": "sigma",
        "meaning": "総和(大文字)、母分散(σ²)、母標準偏差、分散共分散行列",
        "priority": "S",
        "mnemonic": "シグマ = 'しぐさ(散らばり)' - データのバラツキ度合いを表す",
        "context": "σ²は分散、σは標準偏差。Σは合計を表す"
    },
    {
        "uppercase": "Τ", "lowercase": "τ", "name_jp": "タウ", "name_en": "tau",
        "meaning": "ケンドールのタウ、グッドマン=クラスカルのタウ",
        "priority": "B",
        "mnemonic": "タウ = 'たう(倒)れない順序関係' - 順位相関係数の一種",
        "context": "τは外れ値に強い順位相関の指標"
    },
    {
        "uppercase": "Υ", "lowercase": "υ", "name_jp": "ウプシロン", "name_en": "upsilon",
        "meaning": "(統計学では使用頻度低)",
        "priority": "C",
        "mnemonic": "ウプシロン = 'ウッと悩む文字' - 使用頻度が低い",
        "context": "物理学などで使用されるが統計では稀"
    },
    {
        "uppercase": "Φ", "lowercase": "φ", "name_jp": "ファイ", "name_en": "phi",
        "meaning": "自由度、ファイ係数",
        "priority": "A",
        "mnemonic": "ファイ = 'ファイル(φ)で関連度を記録' - 2×2分割表の関連係数",
        "context": "φ係数はχ²統計量を標準化した値"
    },
    {
        "uppercase": "Χ", "lowercase": "χ", "name_jp": "カイ", "name_en": "chi",
        "meaning": "カイ二乗分布の検定統計量(χ²)",
        "priority": "S",
        "mnemonic": "カイ = '怪しい(かいしい)差を検定' - カテゴリデータの独立性検定",
        "context": "χ²検定は観測度数と期待度数のズレを評価"
    },
    {
        "uppercase": "Ψ", "lowercase": "ψ", "name_jp": "プサイ", "name_en": "psi",
        "meaning": "対比(多重比較)",
        "priority": "C",
        "mnemonic": "プサイ = 'プッシュ(押す)して比較' - 分散分析後の特定比較",
        "context": "計画対比で特定の群間差を検定する"
    },
    {
        "uppercase": "Ω", "lowercase": "ω", "name_jp": "オメガ", "name_en": "omega",
        "meaning": "根元事象、全事象",
        "priority": "C",
        "mnemonic": "オメガ = '終わり(omega)=全部' - 標本空間全体を表す",
        "context": "確率論でΩはすべての可能な結果の集合"
    },
]


def generate_anki_cards():
    """72枚のAnkiカードをCSV形式で生成"""
    cards = []

    for data in greek_letters_data:
        lowercase = data["lowercase"]
        uppercase = data["uppercase"]
        name_jp = data["name_jp"]
        name_en = data["name_en"]
        meaning = data["meaning"]
        priority = data["priority"]
        mnemonic = data["mnemonic"]
        context = data["context"]

        # タグ生成
        tags = f"greek-alphabet priority-{priority}"
        if priority == "S":
            tags += " essential"

        # カードタイプ1: 記号 → 読み方
        card1_front = f"{lowercase}"
        card1_back = f"""<div class='reading'>
<h2>{name_jp}</h2>
<p class='english'>{name_en}</p>
</div>"""
        cards.append([card1_front, card1_back, tags + " type-symbol-to-reading"])

        # カードタイプ2: 記号 → 統計的意味+ニーモニック(最も重要)
        card2_front = f"""<div class='question'>
<h3>{lowercase} の統計学での意味は?</h3>
</div>"""

        card2_back = f"""<div class='answer'>
<h3 class='meaning'>{meaning}</h3>

<div class='mnemonic'>
<strong>💡 記憶術:</strong>
<p>{mnemonic}</p>
</div>

<div class='context'>
<strong>📊 使用例:</strong>
<p>{context}</p>
</div>

<div class='info'>
<small>読み方: {name_jp} ({name_en})</small>
</div>
</div>"""
        cards.append([card2_front, card2_back, tags + " type-meaning-with-mnemonic"])

        # カードタイプ3: 読み方 → 記号
        card3_front = f"""<div class='question'>
<h3>「{name_jp}」のギリシャ文字は?</h3>
</div>"""

        card3_back = f"""<div class='answer'>
<h2 class='symbol'>{lowercase}</h2>
<p class='note'>大文字: {uppercase}</p>
<p class='hint'>{meaning}</p>
</div>"""
        cards.append([card3_front, card3_back, tags + " type-reading-to-symbol"])

    return cards


def save_to_csv(cards, filename="greek_letters_anki.csv"):
    """CSVファイルに保存"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')  # Ankiはタブ区切りを推奨
        writer.writerow(['Front', 'Back', 'Tags'])  # ヘッダー
        writer.writerows(cards)
    print(f"✅ {len(cards)}枚のカードを {filename} に保存しました")


def generate_css_template():
    """Ankiカードテンプレート用CSSを生成"""
    css = """/* ギリシャ文字学習カード用スタイル */

.card {
    font-family: 'Hiragino Sans', 'Yu Gothic', 'Meiryo', sans-serif;
    text-align: center;
    padding: 20px;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

/* 記号表示 */
.symbol {
    font-size: 72px;
    color: #2c3e50;
    margin: 20px 0;
}

/* 読み方 */
.reading h2 {
    font-size: 48px;
    color: #3498db;
    margin: 10px 0;
}

.english {
    font-size: 24px;
    color: #7f8c8d;
    font-style: italic;
}

/* 質問スタイル */
.question {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.question h3 {
    font-size: 28px;
    color: #2c3e50;
}

/* 回答スタイル */
.answer {
    text-align: left;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.meaning {
    color: #e74c3c;
    font-size: 20px;
    border-bottom: 2px solid #e74c3c;
    padding-bottom: 10px;
}

/* ニーモニック(記憶術) */
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

/* 使用例 */
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

/* 補足情報 */
.info {
    margin-top: 20px;
    padding-top: 10px;
    border-top: 1px solid #ddd;
    color: #6c757d;
}

.note {
    font-size: 18px;
    color: #6c757d;
    margin: 10px 0;
}

.hint {
    font-size: 16px;
    color: #95a5a6;
}
"""

    with open("anki_card_styling.css", 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ CSSテンプレートを anki_card_styling.css に保存しました")


def generate_import_instructions():
    """インポート手順書を生成"""
    instructions = """# Ankiへのインポート手順

## 1. CSVファイルのインポート

1. Ankiを起動
2. 「ファイル」→「読み込み」を選択
3. `greek_letters_anki.csv` を選択
4. 以下の設定を確認:
   - フィールドの区切り: **タブ**
   - 1行目をフィールド名として使用: **オン**
   - HTMLを許可: **オン**

## 2. ノートタイプの設定

### フィールド構成:
- Front (表面)
- Back (裏面)
- Tags (タグ)

### カードテンプレート:

#### 表面テンプレート:
```html
{{Front}}
```

#### 裏面テンプレート:
```html
{{Front}}
<hr id=answer>
{{Back}}
```

#### スタイリング:
`anki_card_styling.css` の内容をコピー&ペースト

## 3. 学習スケジュール推奨設定

- 新規カード/日: 10-15枚(初週), 5-10枚(2週目以降)
- 復習上限: 制限なし
- 新規カード順序: 追加順
- 表示順序: ランダム

## 4. タグを活用した学習

### 優先度別フィルタ:
- `tag:priority-S` → 最重要5文字
- `tag:priority-A` → 重要10文字
- `tag:essential` → 最優先で学習

### カードタイプ別フィルタ:
- `tag:type-symbol-to-reading` → 記号→読み方
- `tag:type-meaning-with-mnemonic` → 意味+記憶術
- `tag:type-reading-to-symbol` → 読み方→記号

## 5. 学習のコツ

1. **初日**: priority-Sの文字だけに集中(α,β,μ,σ,ρ)
2. **1週目**: 毎日10枚ずつ追加、ニーモニックを声に出して読む
3. **2-3週目**: 復習中心、統計の文脈で使ってみる
4. **4週目**: 全カード復習、実際の統計問題で確認

## 6. カスタマイズ

### 自分だけのニーモニックを追加:
カードを編集して「記憶術」セクションに追記できます。

### 画像の追加:
文字の書き順や形状の画像を追加すると記憶効果が向上します。
"""

    with open("IMPORT_INSTRUCTIONS.md", 'w', encoding='utf-8') as f:
        f.write(instructions)
    print("✅ インポート手順書を IMPORT_INSTRUCTIONS.md に保存しました")


def main():
    """メイン実行"""
    print("=" * 60)
    print("ギリシャ文字 Ankiカード生成スクリプト")
    print("=" * 60)
    print()

    # カード生成
    print("📝 カードを生成中...")
    cards = generate_anki_cards()

    # CSV保存
    save_to_csv(cards)

    # CSS生成
    generate_css_template()

    # 手順書生成
    generate_import_instructions()

    print()
    print("=" * 60)
    print("✨ すべてのファイルが生成されました!")
    print("=" * 60)
    print()
    print("📁 生成ファイル:")
    print("  1. greek_letters_anki.csv - Ankiインポート用(72枚)")
    print("  2. anki_card_styling.css - カードスタイル")
    print("  3. IMPORT_INSTRUCTIONS.md - インポート手順書")
    print()
    print("🚀 次のステップ:")
    print("  1. IMPORT_INSTRUCTIONS.md を読む")
    print("  2. Ankiで greek_letters_anki.csv をインポート")
    print("  3. 毎日の学習を開始!")
    print()

    # 統計情報
    priority_count = {"S": 0, "A": 0, "B": 0, "C": 0}
    for data in greek_letters_data:
        priority_count[data["priority"]] += 1

    print("📊 カード統計:")
    print(f"  重要度S(最優先): {priority_count['S']}文字 × 3 = {priority_count['S']*3}枚")
    print(f"  重要度A(高頻出): {priority_count['A']}文字 × 3 = {priority_count['A']*3}枚")
    print(f"  重要度B(中程度): {priority_count['B']}文字 × 3 = {priority_count['B']*3}枚")
    print(f"  重要度C(低頻度): {priority_count['C']}文字 × 3 = {priority_count['C']*3}枚")
    print(f"  合計: {len(greek_letters_data)}文字 × 3 = {len(cards)}枚")


if __name__ == "__main__":
    main()
