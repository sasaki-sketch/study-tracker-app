import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1702010110
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

question_html = """<div style="font-size:14px; color:#888; margin-bottom:8px;">porter23 Ch3 Q3</div>
どうすれば顧客に「有意差」を感じさせられるか"""

answer_html = """<p>有意差を感じさせたいのは「自社」ではなく「ターゲット顧客」である。顧客にはっきりと差を感じてもらう必要がある。</p>

<p><b>「"違い"を生み出せ。極端な"違い"を」</b>（マーティ・ニューマイヤー）</p>

<p>違いを生み出すためには「良さ」ではなく「違い」を意識する必要がある。</p>
<ul>
<li><b>良さ</b>: 機能の豊富さ、使い勝手、安さ → 高評価だが差別化が効かない</li>
<li><b>違い</b>: 意外性、新規性、驚き、違和感 → 低評価を受けやすく採用を見送られがち</li>
</ul>

<p>多くの日本企業は①「良いが違いはない」領域を狙い、同質化競争に陥る。</p>

<p>有意差を生み出すには、図表24の②と④の間にある<b>⑤「違いがあるが賛否両論」</b>を狙うのがよい。消費者は最初「違い」に違和感を持つが、次第に「良さ」「特徴」だと認識するようになる。高い市場シェアは望めないが、安定した市場シェアを獲得できる。</p>

<div class="example">
<b>補足</b><br>
⑤が機能する理由は「認知の転換」にある。初期の違和感がロイヤルカスタマーの定着につながり、結果として②「良くて違いもある」へ移行する現実的なパスとなる。最初から②を狙うのは非現実的であり、⑤を経由するのが戦略的に正しい。
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第3章「顧客に『有意差』を感じさせられるか」図表24・25
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

script_dir = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mm/porter23/'
output_path = f'{script_dir}mba_mm_porter23_ch3q03_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
