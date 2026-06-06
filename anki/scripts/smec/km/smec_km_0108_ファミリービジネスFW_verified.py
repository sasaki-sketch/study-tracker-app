"""
Ankiカード: ファミリービジネスのフレームワーク（4C・スリーサークル・スリーディメンション・PPP）
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略（ドメイン・全社戦略）
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1701080101
deck_id = 1701080102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_ファミリービジネスFW',
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
    '中小企業診断士_企業経営理論::01_経営戦略::ファミリービジネスFW'
)

question = '''ファミリービジネスを分析する<span class="important">4つのフレームワーク</span>（4Cモデル・スリーサークル・スリーディメンション・PPPモデル）を答えよ'''

answer = '''<b>Family Business Frameworks</b>

<div class="formula">
<table>
<tr><th>モデル</th><th>内容</th><th>目的</th></tr>
<tr><td><b>4Cモデル</b></td><td>長寿ファミリービジネスに欠かせない<b>4つのC</b>を定義</td><td>持続的成長の要素を把握</td></tr>
<tr><td><b>スリーサークルモデル</b></td><td><b>家族・所有・経営</b>の3つの円で関係性と課題を可視化</td><td>利害関係者の立場を整理</td></tr>
<tr><td><b>スリーディメンションモデル</b></td><td>スリーサークルの3軸に<b>時間軸</b>を追加</td><td>家族・所有・経営が<b>時間とともにどう変化するか</b>を分析</td></tr>
<tr><td><b>PPPモデル</b><br>Parallel Planning Process</td><td>プライベート（家）とビジネス（事業）の<b>将来設計を並行</b>して進める</td><td>家と仕事という<b>相反する計画を円滑に両立</b></td></tr>
</table>
</div>

<div class="formula">
<b>4Cモデルの4つのC:</b>
<table>
<tr><th>C</th><th>英語</th><th>意味</th></tr>
<tr><td><b>C</b>ontinuity</td><td>持続性</td><td>長期的な視点での事業継続</td></tr>
<tr><td><b>C</b>ommunity</td><td>コミュニティ</td><td>地域社会との関わり</td></tr>
<tr><td><b>C</b>onnection</td><td>コネクション</td><td>ステークホルダーとのつながり</td></tr>
<tr><td><b>C</b>ommand</td><td>コマンド</td><td>経営の意思決定力・統率力</td></tr>
</table>
</div>

<div class="example">
<b>試験での引っかけ:</b><br>
・「4CモデルのCはCommitment」→ <b>×</b> 正しくは<b>Connection</b><br>
・「スリーサークルモデルの利害関係は変わらない」→ <b>×</b> 事業承継とともに<b>変化し得る</b><br>
・「スリーディメンションモデルは現在の状況のみ分析」→ <b>×</b> <b>時間軸</b>を加えて変化も分析<br>
・「創業者で所有も経営もしていない者はファミリーの一員ではない」→ <b>×</b> 親族・従兄弟も<b>広義のファミリーに含まれる</b>
</div>

<div class="source">出典: 中小企業診断士試験 R5再試第6問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0108_ファミリービジネスFW_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
