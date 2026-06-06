import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1702010109
DECK_ID = 2702010103

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
    'NUCB_EMBA::Marketing_Management::ポーター23問::Ch3_有意差'
)

question_html = """<div style="font-size:14px; color:#888; margin-bottom:8px;">porter23 Ch3 Q2</div>
ターゲット顧客に当事者意識を持って、肌感覚を持って、憑依することができるか"""

answer_html = """<p>ここでいう「ターゲット顧客」はマス層ではなく、差別化の対象である特定市場のターゲットである。</p>

<p>この前提において、グラフやチャートでの分析は平均像と傾向値を重視するため、特定市場ターゲットのニーズ把握には不向きである。平均値に還元される過程で、個別顧客の切実な課題が消えてしまうからだ。</p>

<p>また顧客ニーズは常に顕在化しているわけではない。そのため、ターゲット顧客自身に憑依し、どのような問題を抱えているのかを顧客になりきって紐解いていくことが求められる。このプロセスを経て初めて顧客ニーズを掴むことができる。</p>

<p>グラフやチャート作りではなく、戦略立案担当者は<b>ターゲット顧客の「顔探し」</b>をするべきである。そこから差別化を機能させることができれば、ターゲット顧客から支持を得られる。</p>

<div class="example">
<b>補足</b><br>
「憑依」とは単なるペルソナ設定ではなく、顧客の生活・行動・感情を追体験するレベルの没入を指す。「その人が朝起きて何に困り、何を我慢しているか」まで想像できるかが問われる。戦略立案担当者自身がターゲット顧客と同じ体験をすること（同じ店で買い物する、同じサービスを使う等）が有効な実践方法となる。
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第3章「顧客に『有意差』を感じさせられるか」
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

script_dir = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mm/porter23/'
output_path = f'{script_dir}mba_mm_porter23_ch3q02_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
