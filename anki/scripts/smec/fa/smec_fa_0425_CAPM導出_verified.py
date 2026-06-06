"""
個別リスクプレミアムとβ → CAPM導出 - 中小企業診断士 財務会計
Individual Risk Premium & CAPM Derivation

作成日: 2026-03-05
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1740927601
DECK_ID = 1740927602

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_CAPM導出',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
    }],
    css=CARD_CSS
)

deck = genanki.Deck(DECK_ID, '中小企業診断士_財務会計::04_ファイナンス::CAPM導出')

question = """個別リスクプレミアム（Ri）とβの関係、およびCAPMの導出を答えよ"""

answer = """<b>Individual Risk Premium & CAPM Derivation</b>（個別リスクプレミアムとCAPM導出）

<div class="formula">
\\(R_i = \\beta \\cdot R_m\\)
</div>

<b>個別リスクプレミアム = β × 市場リスクプレミアム</b>

これを \\(E_i = R_f + R_i\\) に代入すると:

<div class="formula" style="font-size: 1.1em;">
\\(\\boxed{E_i = R_f + \\beta(E_m - R_f)}\\)
</div>

<b>βの解釈</b>:
<table>
<tr><th>β値</th><th>意味</th></tr>
<tr><td>β &gt; 1</td><td>市場より<b>ハイリスク</b>（振れ幅が大きい）</td></tr>
<tr><td>β = 1</td><td>市場と同じ動き</td></tr>
<tr><td>β &lt; 1</td><td>市場より<b>ローリスク</b>（振れ幅が小さい）</td></tr>
</table>

<div class="important">注意:</div>
<ul>
<li>βには<b>ビジネスリスク</b>と<b>財務リスク</b>の両方が反映される</li>
<li>負債比率が高い企業ほどβが大きくなる（財務レバレッジ効果）</li>
</ul>

<table>
<tr><th>記号</th><th>英語</th><th>意味</th></tr>
<tr><td><b>R</b>i</td><td><b>R</b>isk premium, <b>i</b>ndividual</td><td>個別証券のリスクプレミアム</td></tr>
<tr><td><b>β</b></td><td><b>B</b>eta</td><td>市場に対する感応度</td></tr>
<tr><td><b>R</b>m</td><td><b>R</b>isk premium, <b>m</b>arket</td><td>市場のリスクプレミアム</td></tr>
</table>

<div class="source">出典: 中小企業診断士試験 R7第15問</div>
"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0425_CAPM導出_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
