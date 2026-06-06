import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1702010101
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
porter23 Ch1 Q2
</div>
事業戦略の基本パターンには何があるのか"""

answer_html = """<b>M. ポーターの3つの基本戦略（Generic Strategies）:</b>

<ol>
<li><b>コストリーダーシップ（Cost Leadership）</b><br>
対象: 市場全体 &times; 低コスト<br>
源泉: 経験曲線効果、スケールメリット、低コスト仕入れ</li>

<li><b>差別化（Differentiation）</b><br>
対象: 市場全体 &times; 独自性<br>
顧客が認める「違い」で競争優位を構築</li>

<li><b>集中（Focus）</b><br>
対象: 特定セグメント<br>
コスト集中 or 差別化集中の2バリエーション</li>
</ol>

<div class="example">
<b>補足</b><br>
この3パターンは「定石」であり、いずれかを明確に選択することが前提。いずれも選ばない「どっちつかず（Stuck in the Middle）」は競争劣位に陥る。集中戦略はコストリーダーシップ・差別化と排他的ではなく、ターゲットの広さの違いである点に注意。
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第1章「なぜ事業戦略は機能しないのか？」
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/mba/mm/porter23/mba_mm_porter23_ch1q02_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
