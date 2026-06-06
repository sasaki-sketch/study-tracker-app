"""
企業ドメインと事業ドメイン - 中小企業診断士 企業戦略論
Corporate Domain vs Business Domain

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1740928201
DECK_ID = 1740928202

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_企業ドメインと事業ドメイン',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
    }],
    css=CARD_CSS
)

deck = genanki.Deck(DECK_ID, '中小企業診断士_企業戦略論::01_ドメイン::企業ドメインと事業ドメイン')

question = """企業ドメインと事業ドメインの違いを答えよ"""

answer = """<b>Corporate Domain vs Business Domain</b>（企業ドメインと事業ドメイン）

<table>
<tr><th></th><th>企業ドメイン</th><th>事業ドメイン</th></tr>
<tr><td>対象</td><td><b>企業全体</b></td><td><b>個別事業</b></td></tr>
<tr><td>戦略レベル</td><td>企業戦略（全社戦略）</td><td>事業戦略（競争戦略）</td></tr>
<tr><td>決定内容</td><td>事業ポートフォリオ・多角化の程度</td><td>日常オペレーション・差別化方針</td></tr>
<tr><td>利害関係者</td><td><b>外部</b>（株主・債権者等）</td><td><b>内部</b>（事業関係者）</td></tr>
<tr><td>抽象度</td><td>高い</td><td>低い（具体的）</td></tr>
</table>

<div class="important">注意:</div>
<ul>
<li>企業ドメインは個々の事業ドメインの<b>単純な足し合わせではない</b>（試験頻出）</li>
<li>試験では両者の説明を<b>入れ替えて</b>出題されることが多い</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、LEC直前対策講座</div>
"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/st/smec_st_0102_企業ドメインと事業ドメイン_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
