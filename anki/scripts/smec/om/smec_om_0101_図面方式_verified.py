"""
Ankiカード: 図面の取引方式（貸与図・委託図・承認図）
科目: 中小企業診断士_運営管理
セクション: 01_生産管理
作成日: 2026-03-20
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1708010101
deck_id = 1708010102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_運営管理_図面方式',
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
    '中小企業診断士_運営管理::01_生産管理::図面方式'
)

# カード内容
question = '''完成品メーカーとサプライヤ間の図面方式（<span class="important">貸与図・委託図・承認図</span>）の違いと、デザインインの定義を答えよ'''

answer = '''<b>Drawing Supply Methods</b>（図面の取引方式）

<div class="formula">
<table>
<tr><th></th><th>製造</th><th>詳細設計</th><th>図面の所有権</th><th>メーカーの責任</th><th>サプライヤの責任</th></tr>
<tr><td><b>貸与図方式</b></td><td>サプライヤ</td><td>メーカー</td><td>メーカー</td><td>大 ■■■</td><td>小 ■□□</td></tr>
<tr><td><b>委託図方式</b></td><td>サプライヤ</td><td>サプライヤ</td><td>メーカー</td><td>中 ■■□</td><td>中 ■■□</td></tr>
<tr><td><b>承認図方式</b></td><td>サプライヤ</td><td>サプライヤ</td><td>サプライヤ</td><td>小 ■□□</td><td>大 ■■■</td></tr>
</table>
<br>
<b>覚え方: 貸与図→承認図で、責任がメーカーからサプライヤへ移っていく</b>
</div>

<div class="example">
<b>ポイント:</b><br>
・<b>委託図方式</b>は中間的性格: 設計は承認図的（サプライヤ）、所有権は貸与図的（メーカー）<br>
・<b>承認図方式</b>が日本で最も主流（約70%）<br>
・必要能力: 貸与図＝製造のみ、委託図・承認図＝製造＋設計開発能力<br>
・転注: 貸与図・委託図＝容易（図面はメーカー所有）、承認図＝困難
</div>

<p><b>Design-In</b>（デザインイン）: サプライヤが開発の<b>初期段階</b>からメーカーと共同開発し、自社部品を設計に組み込んでもらう活動。承認図方式と親和性が高い。</p>

<div class="source">出典: 中小企業診断士試験 H30第7問、藤本隆宏『製品開発力』</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/om/smec_om_0101_図面方式_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
