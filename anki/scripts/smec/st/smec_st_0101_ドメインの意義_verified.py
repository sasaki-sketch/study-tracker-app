"""
ドメインの意義 - 中小企業診断士 企業戦略論
Domain Definition & Significance

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1740928101
DECK_ID = 1740928102

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_ドメインの意義',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
    }],
    css=CARD_CSS
)

deck = genanki.Deck(DECK_ID, '中小企業診断士_企業戦略論::01_ドメイン::ドメインの意義')

question = """ドメインの定義と、ドメインを定義する3つの意義を答えよ"""

answer = """<b>Domain</b>（ドメイン / 事業領域）

<b>定義</b>: 企業が活動する事業領域・競争領域を定めたもの

<b>ドメイン定義の3つの意義</b>:
<table>
<tr><th>#</th><th>意義</th><th>説明</th></tr>
<tr><td>1</td><td><b>意思決定の方向性</b></td><td>経営層の注意の焦点が定まり、業界動向への感度が上がる</td></tr>
<tr><td>2</td><td><b>経営資源の集中</b></td><td>必要な人・モノ・金・情報が明確になり、適切に配分できる</td></tr>
<tr><td>3</td><td><b>組織の一体化</b></td><td>従業員の動機付け・企業全体の一体感が生まれる</td></tr>
</table>

<div class="important">注意:</div>
ドメインは毎年のように出題される最重要論点。3つの意義はセットで覚える。

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、スタディング H23第1問</div>
"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/st/smec_st_0101_ドメインの意義_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
