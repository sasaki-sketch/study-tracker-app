import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1702010103
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
porter23 Ch1 Q4
</div>
差別化を採用すべき企業はどのような企業なのか。差別化と集中は何が違うのか"""

answer_html = """<b>業界1位以外は差別化 or 集中</b>を選ぶ。違う競争軸で1位からシェアを奪うのが目的。<br><br>

<b>差別化のターゲット:</b> 全市場ではなく<b>特定セグメント</b>（全市場&asymp;マスマーケティングで差別化と矛盾する）<br><br>

<b>差別化と集中の違い = 割り切り:</b>
<ul>
<li>全体市場に後ろ髪を引かれる &rarr; 差別化は機能せず失敗</li>
<li>最初から特定顧客に絞り込む &rarr; それが<b>集中</b></li>
</ul>

<div class="example">
<b>補足</b><br>
低価格戦略は「機能を絞った差別化」の一種。コストリーダーシップ（業界1位のコスト構造優位）とは別物。
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第1章「なぜ事業戦略は機能しないのか？」
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/mba/mm/porter23/mba_mm_porter23_ch1q04_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
