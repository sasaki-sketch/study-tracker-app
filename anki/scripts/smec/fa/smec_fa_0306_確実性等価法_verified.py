"""
確実性等価法 - 中小企業診断士 財務会計
Certainty Equivalent Method

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740824401
DECK_ID = 1740824402

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_確実性等価法',
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
    '中小企業診断士_財務会計::03_意思決定会計::確実性等価法'
)

# カード内容
question = """確実性等価法の定義・計算式・リスク調整割引率法との違いを答えよ"""

answer = """<b>Certainty Equivalent Method</b>（確実性等価法）

<b>定義</b>: 不確実な期待CFを確実性等価係数で調整し、確実なCFに変換してからリスクフリーレートで割り引く方法。<b>分子（CF）でリスクを調整</b>する。

<div class="formula">
\\[PV = \\sum_{t=1}^{n} \\frac{\\alpha_t \\times E(CF_t)}{(1 + r_f)^t}\\]

\\(\\alpha_t\\): 確実性等価係数（\\(0 &lt; \\alpha_t \\leq 1\\)）
\\(r_f\\): リスクフリーレート
</div>

<b>確実性等価係数 \\(\\alpha_t\\) の意味</b>:
<table>
<tr><th>\\(\\alpha_t\\) の値</th><th>リスクの程度</th></tr>
<tr><td>1に近い</td><td>リスクが低い（CFがほぼ確実）</td></tr>
<tr><td>0に近い</td><td>リスクが高い（CFが不確実）</td></tr>
</table>

<b>リスク調整割引率法との比較</b>:
<table>
<tr><th>項目</th><th>確実性等価法</th><th>リスク調整割引率法</th></tr>
<tr><td>リスク調整箇所</td><td><b>分子</b>（CF × \\(\\alpha_t\\)）</td><td><b>分母</b>（割引率 + \\(\\alpha\\)）</td></tr>
<tr><td>割引率</td><td>\\(r_f\\)</td><td>\\(r_f + \\alpha\\)</td></tr>
<tr><td>各期のリスク</td><td><b>期ごとに異なる \\(\\alpha_t\\) を設定可能</b></td><td>全期間一律のリスクプレミアム</td></tr>
<tr><td>実務での利用</td><td>少ない</td><td><b>多い</b></td></tr>
</table>

<div class="important">注意:</div>
理論上は両手法とも同じ結果になる。確実性等価法は各期のリスクを個別に反映できる利点があるが、\\(\\alpha_t\\) の推定が難しいため実務ではリスク調整割引率法が多用される。

<div class="source">出典: iFinance、ブルームキャピタル、一発合格まとめシート</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0306_確実性等価法_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
