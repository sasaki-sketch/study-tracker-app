import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1702010107
DECK_ID = 2702010102

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
    'NUCB_EMBA::Marketing_Management::ポーター23問::Ch2_競争の戦略'
)

question_html = """<div style="font-size:14px; color:#888; margin-bottom:8px;">porter23 Ch2 Q4</div>
なぜ日本企業の戦略基本パターンは、違う競争軸を出せないのか"""

answer_html = """<b>日本企業は全体市場を志向する傾向が強いからである。</b><br><br>

<b>因果連鎖:</b><br>
1. 差別化を謳いながら、特定市場に限定した商品開発をしない<br>
2. 全体市場をターゲットにした機能付加的な商品が各企業で乱立<br>
3. 結果、価格以外で差別化ができなくなる<br>

<div class="example">
<b>補足</b><br>
根底には日本企業の「シェア至上主義」がある。シェアを最大化したいから特定市場に絞れず、全方位で機能を足す→競合も同じことをする→差がなくなるという悪循環。Ch1Q4で学んだ「差別化と集中の違い」がここで効く。集中（特定セグメントに絞る）を選ぶ覚悟がないから、差別化が機能しない。Ch3「有意差」ではこの問題の解決策を扱う。
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第2章「なぜ『競争の戦略』を使いこなせないのか」
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

script_dir = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mm/porter23/'
output_path = f'{script_dir}mba_mm_porter23_ch2q04_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
