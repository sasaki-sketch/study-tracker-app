import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1702010108
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

question_html = """<div style="font-size:14px; color:#888; margin-bottom:8px;">porter23 Ch3 Q1</div>
機能する差別化を実現するために、日本企業が乗り越えなければならない課題はなにか"""

answer_html = """<b>差別化の実現 = マーケティングを機能させること（コトラーのSTPと4P）</b><br><br>

<b>課題1: セグメンテーション＆ターゲット</b><br>
・競合が市場を広く取っていても特定顧客にターゲットを絞ること<br>
・ターゲット顧客の感情に同化できるほど顧客理解すること<br><br>

<b>課題2: ポジショニング（4アクション）</b><br>
・増やす: 業界標準と比べて大胆に増やす<br>
・付け加える: 業界で提供されていない要素<br>
・取り除く: 業界の常識であるものを取り除く<br>
・減らす: 業界標準と比べて思い切り減らす<br>

<div class="example">
<b>補足</b><br>
4アクションはブルー・オーシャン戦略のERRC（Eliminate/Reduce/Raise/Create）と同一構造。牧田氏は「戦略キャンバス」の文脈で使用。特に「取り除く」「減らす」が日本企業にとって最も難しい。Ch2Q4の「全体市場志向＝何も捨てられない」問題の具体的解決策がこの4アクションとなる。
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第3章「顧客に『有意差』を感じさせられるか」
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

script_dir = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mm/porter23/'
output_path = f'{script_dir}mba_mm_porter23_ch3q01_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
