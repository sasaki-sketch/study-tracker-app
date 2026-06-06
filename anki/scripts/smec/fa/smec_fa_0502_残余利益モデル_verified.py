"""
残余利益モデル - 中小企業診断士 財務会計
Residual Income Model

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394209
DECK_ID = 1709394210

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_残余利益モデル',
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
    '中小企業診断士_財務会計::05_企業価値::残余利益モデル'
)

# カード内容
question = """残余利益モデルの定義・計算式・特徴を答えよ"""

answer = """<b>Residual Income Model</b>（残余利益モデル）

<div class="formula">
\\[V_0 = B_0 + \\sum_{t=1}^{\\infty} \\frac{RI_t}{(1+r_e)^t}\\]
\\[RI_t = NI_t - r_e \\times B_{t-1}\\]
</div>

<table>
<tr><th>記号</th><th>意味</th></tr>
<tr><td>\\(V_0\\)</td><td>株式価値</td></tr>
<tr><td>\\(B_0\\)</td><td>現時点の株主資本簿価</td></tr>
<tr><td>\\(RI_t\\)</td><td>t期の残余利益</td></tr>
<tr><td>\\(NI_t\\)</td><td>t期の当期純利益</td></tr>
<tr><td>\\(r_e\\)</td><td>株主資本コスト</td></tr>
</table>

<b>定義</b>: 会計利益を用いて株主価値を算定するモデル

<b>残余利益</b>: 当期純利益から株主の期待利益を差し引いた超過利益

<b>別表現</b>:
<div class="formula">
\\[RI = (ROE - r_e) \\times B\\]
</div>

<div class="important">特徴:</div>
<ul>
<li><b>クリーンサープラス関係</b>が成立すれば配当割引モデルと同値</li>
<li>実績値（簿価）を使用するため<b>予想誤差が小さい</b></li>
<li><b>配当ゼロ</b>でも株式価値を算定可能</li>
</ul>

<div class="source">出典: みずほ証券 ファイナンス用語集</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0502_残余利益モデル_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
