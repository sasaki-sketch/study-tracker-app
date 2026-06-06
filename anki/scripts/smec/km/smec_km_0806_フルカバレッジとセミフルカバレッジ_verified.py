"""
Ankiカード: フルカバレッジとセミフルカバレッジ（コトラーの競争地位別戦略）
科目: 中小企業診断士_企業経営理論
セクション: 08_マーケティング概論・戦略
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1708060001
deck_id = 1708060002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_フルカバレッジ',
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
    '中小企業診断士_企業経営理論::08_マーケティング概論・戦略::フルカバレッジとセミフルカバレッジ'
)

# カード内容
question = '''コトラーの競争地位別戦略における「フルカバレッジ」と「セミフルカバレッジ」の定義・違いと、各競争地位の<span class="important">ターゲット範囲・戦略定石</span>を答えよ'''

answer = '''<b>Full Coverage / Semi-Full Coverage</b>（フルカバレッジ／セミフルカバレッジ）

<p>コトラーの競争地位別戦略における、ターゲット市場の範囲を示す概念。</p>

<div class="formula">
<b>フルカバレッジ</b>: 市場に存在する<b>全ての顧客</b>を対象とする（リーダー）<br>
<b>セミフルカバレッジ</b>: 市場の<b>大部分</b>の顧客を対象とするが、全てではない（チャレンジャー）
</div>

<div class="example">
<table>
<tr><th>地位</th><th>ターゲット</th><th>戦略定石</th></tr>
<tr><td><b>リーダー</b></td><td>フルカバレッジ</td><td>周辺需要拡大、非価格対応、同質化、最適シェア維持</td></tr>
<tr><td><b>チャレンジャー</b></td><td>セミフルカバレッジ</td><td>リーダーとの<b>差別化</b></td></tr>
<tr><td><b>フォロワー</b></td><td>中・低価格志向層</td><td>模倣・低価格化</td></tr>
<tr><td><b>ニッチャー</b></td><td>特定セグメント</td><td>集中・ミニリーダー</td></tr>
</table>
</div>

<p><b>注意</b>: リーダーは同質化戦略で競合の差別化を無力化する。そのためチャレンジャーはリーダーが模倣しにくい独自の差別化（特に4Pよりドメインの差別化）が重要となる。リーダーが非価格対応を採るのは、価格競争は利潤縮小とブランド毀損を招くためである。</p>

<div class="source">出典: たかぴーの中小企業診断士試験攻略ブログ、中小企業診断士独学攻略ブログ</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0806_フルカバレッジとセミフルカバレッジ_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
