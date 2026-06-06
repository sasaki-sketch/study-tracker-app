import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1702010102
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
porter23 Ch1 Q3
</div>
コストリーダーシップを採用できる企業はどのような企業なのか。またコストリーダーシップと低価格戦略は同じ戦略なのか"""

answer_html = """<b>コストリーダーシップを採用できる企業:</b>
<ul>
<li><b>原則として業界1位の企業のみ</b>（経験曲線・スケールメリット・低コスト仕入れで圧倒的コスト優位を持つ）</li>
<li>それ以外の企業は差別化 or 集中を選択すべき</li>
<li>例外: ラディカルイノベーションで新市場を早期開拓した企業</li>
</ul>

<b>コストリーダーシップ &ne; 低価格戦略:</b><br><br>

<span class="important" style="font-size:19px;">コストリーダーシップは「コスト構造の優位性」であり、必ずしも低価格で売ることを意味しない。</span><br><br>

コスト優位を得た後の価格戦略は、競合状況に応じて判断する:

<table>
<tr><th>状況</th><th>あるべき姿</th></tr>
<tr><td><b>平時体制</b></td><td>利益最大化（価格を下げない）</td></tr>
<tr><td><b>戦時体制</b></td><td>低価格戦略で競合を消耗させる</td></tr>
<tr><td><b>市場成長期</b></td><td>シェア拡大 &rarr;「明日」の利益</td></tr>
<tr><td><b>市場成熟期</b></td><td>「今」の利益を確保</td></tr>
</table>

<div class="example">
<b>補足</b><br>
低価格戦略はコストリーダーシップの「使い方の一つ」に過ぎない。平時・成熟期には価格を据え置き利益を最大化するのが定石。低価格戦略を使うべき場面は「戦時体制」と「市場成長期」の2つだけ。
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第1章 図表5
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/mba/mm/porter23/mba_mm_porter23_ch1q03_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
