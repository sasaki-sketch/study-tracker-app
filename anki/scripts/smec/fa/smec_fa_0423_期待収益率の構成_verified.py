"""
個別証券の期待収益率の構成 - 中小企業診断士 財務会計
Expected Return of Individual Security

作成日: 2026-03-05
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1740927401
DECK_ID = 1740927402

IMAGE_NAME = 'smec_fa_0423_capm_derivation.png'
SCRIPT_DIR = '/Users/sasaki/study_app/anki/scripts/smec/fa/'
IMAGE_PATH = SCRIPT_DIR + IMAGE_NAME

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_期待収益率の構成',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
    }],
    css=CARD_CSS
)

deck = genanki.Deck(DECK_ID, '中小企業診断士_財務会計::04_ファイナンス::期待収益率の構成')

question = """個別証券の期待収益率（Ei）は何で構成されるか答えよ"""

answer = f"""<b>Expected Return of Individual Security</b>（個別証券の期待収益率）

<div style="text-align: center; margin: 15px 0;">
<img src="{IMAGE_NAME}" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">
</div>

<div class="formula">
\\(E_i = R_f + R_i\\)
</div>

<b>期待収益率 = リスクフリーレート + 個別リスクプレミアム</b>

<table>
<tr><th>記号</th><th>英語</th><th>意味</th></tr>
<tr><td><b>E</b>i</td><td><b>E</b>xpected return, <b>i</b>ndividual</td><td>個別証券の期待収益率</td></tr>
<tr><td><b>R</b>f</td><td><b>R</b>ate, risk-<b>f</b>ree</td><td>リスクフリーレート</td></tr>
<tr><td><b>R</b>i</td><td><b>R</b>isk premium, <b>i</b>ndividual</td><td>個別証券のリスクプレミアム</td></tr>
</table>

<div class="source">出典: 中小企業診断士試験 R7第15問</div>
"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

output_path = SCRIPT_DIR + 'smec_fa_0423_期待収益率の構成_verified.apkg'
package = genanki.Package(deck)
package.media_files = [IMAGE_PATH]
package.write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Media included: {IMAGE_NAME}")
