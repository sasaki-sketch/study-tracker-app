"""
市場の期待収益率の構成 - 中小企業診断士 財務会計
Expected Return of Market

作成日: 2026-03-05
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1740927501
DECK_ID = 1740927502

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_市場の期待収益率の構成',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
    }],
    css=CARD_CSS
)

deck = genanki.Deck(DECK_ID, '中小企業診断士_財務会計::04_ファイナンス::市場の期待収益率の構成')

question = """市場の期待収益率（Em）は何で構成されるか答えよ"""

answer = """<b>Expected Return of Market</b>（市場の期待収益率）

<div class="formula">
\\(E_m = R_f + R_m\\)
</div>

<b>市場の期待収益率 = リスクフリーレート + 市場リスクプレミアム</b>

<table>
<tr><th>記号</th><th>英語</th><th>意味</th></tr>
<tr><td><b>E</b>m</td><td><b>E</b>xpected return, <b>m</b>arket</td><td>市場の期待収益率</td></tr>
<tr><td><b>R</b>f</td><td><b>R</b>ate, risk-<b>f</b>ree</td><td>リスクフリーレート</td></tr>
<tr><td><b>R</b>m</td><td><b>R</b>isk premium, <b>m</b>arket</td><td>市場のリスクプレミアム</td></tr>
</table>

<div class="source">出典: 中小企業診断士試験 R7第15問</div>
"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0424_市場の期待収益率の構成_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
