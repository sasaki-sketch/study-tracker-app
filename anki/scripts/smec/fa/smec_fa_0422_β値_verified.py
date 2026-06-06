"""
β値（ベータ値） - 中小企業診断士 財務会計
Beta (CAPM)

作成日: 2026-03-05
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1740927301
DECK_ID = 1740927302

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_β値',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
    }],
    css=CARD_CSS
)

deck = genanki.Deck(DECK_ID, '中小企業診断士_財務会計::04_ファイナンス::β値')

question = """CAPM分野におけるβ値の定義・計算式・解釈を答えよ"""

answer = """<b>Beta / β</b>（ベータ値）

<b>定義</b>: 市場全体に対する個別証券の<b>システマティックリスク</b>の大きさを示す指標

<b>計算式</b>:
<div class="formula">
\\(\\beta_i = \\frac{\\sigma_{im}}{\\sigma_m^2} = \\frac{\\text{個別証券}i\\text{と市場の共分散}}{\\text{市場の分散}}\\)
</div>

<b>β値の解釈</b>:
<table>
<tr><th>β値</th><th>意味</th><th>値動き</th></tr>
<tr><td>β &gt; 1</td><td>市場より<b>ハイリスク</b></td><td>市場の振れ幅より大きい</td></tr>
<tr><td>β = 1</td><td>市場と同等</td><td>市場と同じ動き</td></tr>
<tr><td>0 &lt; β &lt; 1</td><td>市場より<b>ローリスク</b></td><td>市場の振れ幅より小さい</td></tr>
<tr><td>β = 0</td><td>リスクフリー資産</td><td>市場と無相関</td></tr>
<tr><td>β &lt; 0</td><td>市場と逆方向</td><td>市場が上がると下がる</td></tr>
</table>

<b>CAPMでの使われ方</b>:
<div class="formula">
\\(E(R_i) = R_f + \\beta_i \\times (E(R_m) - R_f)\\)
</div>

<div class="important">注意:</div>
<ul>
<li>βが測定するのは<b>システマティックリスクのみ</b>（分散投資で消せないリスク）</li>
<li>アンシステマティックリスク（個別リスク）は分散投資で消去可能なためβには含まれない</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、みずほ証券 ファイナンス用語集</div>
"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0422_β値_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
