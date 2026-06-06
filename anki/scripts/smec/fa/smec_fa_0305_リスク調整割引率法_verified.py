"""
リスク調整割引率法 - 中小企業診断士 財務会計
Risk-Adjusted Discount Rate Method

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740824301
DECK_ID = 1740824302

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_リスク調整割引率法',
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
    '中小企業診断士_財務会計::03_意思決定会計::リスク調整割引率法'
)

# カード内容
question = """リスク調整割引率法の定義・計算式・確実性等価法との違いを答えよ"""

answer = """<b>Risk-Adjusted Discount Rate Method</b>（リスク調整割引率法）

<b>定義</b>: 割引率にリスクプレミアムを上乗せすることで、将来CFの不確実性を反映させる方法。<b>分母（割引率）でリスクを調整</b>する。

<div class="formula">
\\[PV = \\sum_{t=1}^{n} \\frac{E(CF_t)}{(1 + r_f + \\alpha)^t}\\]

\\(r_f\\): リスクフリーレート、\\(\\alpha\\): リスクプレミアム
</div>

→ リスクが高いほど \\(\\alpha\\) ↑ → 割引率↑ → 現在価値↓

<b>確実性等価法との比較</b>:
<table>
<tr><th>項目</th><th>リスク調整割引率法</th><th>確実性等価法</th></tr>
<tr><td>リスク調整箇所</td><td><b>分母</b>（割引率）</td><td><b>分子</b>（CF）</td></tr>
<tr><td>割引率</td><td>\\(r_f + \\alpha\\)</td><td>\\(r_f\\)（リスクフリーレート）</td></tr>
<tr><td>CF</td><td>期待CF（そのまま）</td><td>確実性等価CF（\\(\\alpha_t \\times E(CF_t)\\)）</td></tr>
<tr><td>実務での利用</td><td><b>多い</b></td><td>少ない</td></tr>
</table>

<b>理論上は両手法とも同じ結果</b>になる

<div class="important">注意:</div>
不確実性が高いほどリスクプレミアム \\(\\alpha\\) は大きくなる。CAPMで算出した資本コストをリスク調整割引率として用いるのが一般的。

<div class="source">出典: 一発合格まとめシート、過去問ドットコム、EY Japan</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0305_リスク調整割引率法_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
