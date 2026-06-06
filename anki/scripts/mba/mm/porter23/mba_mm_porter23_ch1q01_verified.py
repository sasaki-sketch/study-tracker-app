import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1702010100
DECK_ID = 2702010101

my_model = genanki.Model(
    MODEL_ID,
    'NUCB_EMBA Textbook QA',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>'
    }],
    css=CARD_CSS
)

my_deck = genanki.Deck(
    DECK_ID,
    'NUCB_EMBA::Marketing_Management::ポーター23問::Ch1_事業戦略'
)

question_html = """<div style="font-size:14px; color:#888; margin-bottom:8px;">
porter23 Ch1 Q1
</div>
日本企業が策定する事業戦略は、なぜ結果を出せないケースが多いのか"""

answer_html = """<b>主な原因:</b>
<ul>
<li><b>戦略策定のスピードが遅い</b> &mdash; 環境変化に追いつかない</li>
<li><b>事業ごとに環境に応じた戦略になっていない</b> &mdash; 画一的なアプローチ</li>
</ul>

<b>根本原因:</b> 戦略の基本パターン（コストリーダーシップ・差別化・集中）を正しく理解しておらず、定石から外れた戦略を策定しているため。

<div class="example">
<b>補足</b><br>
牧田はポーターの3つの基本戦略を「定石」と位置づけている。多くの日本企業は定石を踏まえず、結果として「どっちつかず（Stuck in the Middle）」に陥りやすい。コスト優位でも差別化でもない中途半端な戦略は、競争優位を生まない。
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第1章「なぜ事業戦略は機能しないのか？」
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/mba/mm/porter23/mba_mm_porter23_ch1q01_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
