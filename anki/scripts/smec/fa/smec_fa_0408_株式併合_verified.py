"""
株式併合 - 中小企業診断士 財務会計
Reverse Stock Split

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740824601
DECK_ID = 1740824602

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_株式併合',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
        },
    ],
    css=CARD_CSS
)

# デッキ定義
deck = genanki.Deck(
    DECK_ID,
    '中小企業診断士_財務会計::04_ファイナンス::株式併合'
)

# カード内容
question = """株式併合の定義・手続き・スクイーズアウトとの関係を答えよ"""

answer = """<b>Reverse Stock Split</b>（株式併合）

<b>定義</b>: 複数の株式を1株にまとめて、<b>発行済株式数を減少</b>させること。1株あたりの価値は比例して増加する。

<div class="formula">
\\[\\text{併合後の株価} = \\text{併合前の株価} \\times \\text{併合比率}\\]

例: 10株→1株の併合 → 株価は理論上10倍に
</div>

<b>主な目的</b>:
<table>
<tr><th>目的</th><th>内容</th></tr>
<tr><td>株価調整</td><td>低位株の株価を引き上げ、投資単位を適正化</td></tr>
<tr><td>管理コスト削減</td><td>株主数・株式数を減らし管理負担を軽減</td></tr>
<tr><td><b>スクイーズアウト</b></td><td><b>少数株主を排除し、完全子会社化を実現</b></td></tr>
</table>

<b>スクイーズアウト（Squeeze Out）とは</b>:
支配株主が<b>少数株主の保有株式を強制的に取得</b>し、少数株主を会社から締め出す手法の総称。M&A後の100%子会社化などで用いられる。

<b>株式併合によるスクイーズアウトの仕組み</b>:
大幅な併合比率（例: 100万株→1株）を設定 → 少数株主の持株が<b>1株未満の端数</b>に → 端数は金銭で精算 → <b>少数株主が強制的に排除</b>される

<b>手続き</b>:
<ul>
<li>株主総会の<b>特別決議</b>（2/3以上の賛成）</li>
<li>事前開示書面の備置き</li>
<li>反対株主の<b>株式買取請求権</b>あり</li>
<li>効力発生日に併合の効力が生じる</li>
</ul>

<b>他のスクイーズアウト手法との比較</b>:
<table>
<tr><th>手法</th><th>特徴</th></tr>
<tr><td><b>株式併合</b></td><td>手続きがシンプル、特別決議で実施可能</td></tr>
<tr><td>株式等売渡請求</td><td>特別支配株主（90%以上保有）が利用可能</td></tr>
<tr><td>全部取得条項付種類株式</td><td>種類株式への変更が必要でやや複雑</td></tr>
</table>

<div class="important">注意:</div>
2015年会社法改正により株式併合でのスクイーズアウト時にも<b>反対株主の株式買取請求権</b>・<b>事前開示手続き</b>が整備され、少数株主保護が強化された。

<div class="source">出典: 日本取引所グループ、M&A Online、BUSINESS LAWYERS</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0408_株式併合_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
