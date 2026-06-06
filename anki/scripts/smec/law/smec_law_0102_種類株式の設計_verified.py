"""
Ankiカード: 種類株式の設計と発行手続き
科目: 中小企業診断士_経営法務
セクション: 01_会社法
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1710020101
deck_id = 1710020102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_経営法務_種類株式の設計',
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
    '中小企業診断士_経営法務::01_会社法::種類株式の設計'
)

question = '''<span class="important">種類株式の設計（組み合わせ）と発行手続き</span>を答えよ'''

answer = '''<b>Classified Shares Design &amp; Procedure</b>（種類株式の設計と発行手続き）

<p>9種類の権利内容を<b>自由に組み合わせて</b>1つの種類株式を設計できる。</p>

<div class="formula">
<b>実務での設計例 − スタートアップのA種優先株式:</b>
<table>
<tr><th>要素</th><th>設定内容</th><th>VCにとってのメリット</th></tr>
<tr><td>①剰余金の配当</td><td>普通株より<b>優先</b>して年5%</td><td>安定したリターン確保</td></tr>
<tr><td>②残余財産の分配</td><td>普通株より<b>優先</b>して投資額を回収</td><td>潰れても投資額は先に戻る</td></tr>
<tr><td>③議決権制限</td><td>なし（議決権あり）</td><td>経営に関与できる</td></tr>
<tr><td>④譲渡制限</td><td>取締役会の承認が必要</td><td>（会社側の都合）</td></tr>
<tr><td>⑤取得請求権付</td><td>株主がいつでも普通株への転換を請求可能</td><td>上場時に普通株に転換して売却</td></tr>
</table>
</div>

<div class="example">
<b>複数ラウンドでの発行例:</b><br><br>
シードラウンド → <b>A種優先株式</b>（配当優先＋残余財産優先＋取得請求権付）<br>
シリーズA → <b>B種優先株式</b>（A種より残余財産分配が優先＋拒否権付）<br>
シリーズB → <b>C種優先株式</b>（B種より残余財産分配が優先）<br><br>
※後のラウンドほど<b>優先順位が高い</b>のが一般的（後から入る投資家ほどリスクが高いため）
</div>

<div class="formula">
<b>発行手続きの流れ:</b><br><br>
① 定款に種類株式の内容を記載（<b>株主総会の特別決議</b>）<br>
　↓<br>
② 種類株式の発行要項を決定（取締役会決議等）<br>
　↓<br>
③ <b>登記</b>（種類株式の内容は登記事項）
</div>

<div class="example">
<b>試験での引っかけ:</b><br>
・「1つの種類株式には1つの権利しか付けられない」→ <b>×</b> <b>複数の権利を自由に組み合わせ</b>可能<br>
・「種類株式の内容は定款に記載不要」→ <b>×</b> <b>定款に記載が必須</b>（株主総会の特別決議）<br>
・「種類株式は1種類しか発行できない」→ <b>×</b> A種・B種・C種など<b>複数の種類</b>を発行可能
</div>

<div class="source">出典: 会社法108条・322条、中小企業診断士試験</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/law/smec_law_0102_種類株式の設計_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
