"""
Ankiカード: 垂直統合（前方統合・後方統合）と水平統合
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703060301
deck_id = 1703060302

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_垂直統合',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
        },
    ],
    css=CARD_CSS
)

my_deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::垂直統合'
)

question = '''<span class="important">垂直統合（前方統合・後方統合）</span>と水平統合の定義・方向・違いを答えよ'''

answer = '''<b>Vertical &amp; Horizontal Integration</b>（垂直統合・水平統合）

<div class="formula">
<b>サプライチェーンの流れで理解する:</b><br><br>
原材料 → 製造 → 卸売 → 小売 → 消費者<br>
←<b>後方統合</b>（川上へ）　　　<b>前方統合</b>（川下へ）→
</div>

<div class="formula">
<table>
<tr><th></th><th>前方統合</th><th>後方統合</th><th>水平統合</th></tr>
<tr><td><b>英語</b></td><td>Forward Integration</td><td>Backward Integration</td><td>Horizontal Integration</td></tr>
<tr><td><b>方向</b></td><td><b>川下</b>（消費者側）へ</td><td><b>川上</b>（原材料側）へ</td><td><b>ヨコ</b>（同じ段階）</td></tr>
<tr><td><b>目的</b></td><td>販売チャネルの支配</td><td>原材料の安定確保</td><td>規模の経済</td></tr>
<tr><td><b>例（ワイン会社）</b></td><td>酒販店を買収、自社Webで直販</td><td>農家と専属契約、ブドウ栽培を開始</td><td>他のワイン会社と合併</td></tr>
</table>
</div>

<div class="example">
<b>具体例で覚える:</b>
<table>
<tr><th>やること</th><th>方向</th></tr>
<tr><td>メーカーが<b>小売店を買収</b>・<b>自社ECで直販</b></td><td><b>前方</b>統合（消費者に近づく）</td></tr>
<tr><td>メーカーが<b>原料を自社栽培</b>・<b>仕入先と専属契約</b></td><td><b>後方</b>統合（原材料を確保）</td></tr>
</table>
</div>

<p><b>反対概念:</b><br>
・垂直統合の反対 → <b>アウトソーシング</b>（外注）、工程の分離<br>
・水平統合の反対 → <b>事業売却</b>、選択と集中</p>

<div class="example">
<b>試験での引っかけ:</b><br>
・「仕入先の買収は前方統合」→ <b>×</b> 仕入先（川上）は<b>後方</b>統合<br>
・「消費者に直接販売するのは後方統合」→ <b>×</b> 消費者側（川下）は<b>前方</b>統合<br>
・「仕入価格を事前に固定するのは垂直統合」→ <b>×</b> 価格の事前決定は<b>リスク回避策</b>（5フォースの買い手の脅威/4Pの価格戦略）
</div>

<div class="source">出典: 中小企業診断士試験 R4第6問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0306_垂直統合_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
