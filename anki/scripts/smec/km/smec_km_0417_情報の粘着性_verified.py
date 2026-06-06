"""
Ankiカード: 情報の粘着性
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704170001
deck_id = 1704170002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_情報の粘着性',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::情報の粘着性'
)

# カード内容
question = '''フォン・ヒッペルが提唱した「情報の粘着性」の定義と、<span class="important">ユーザー・イノベーション</span>が発生する条件を答えよ'''

answer = '''<b>Sticky Information</b>（情報の粘着性）

<p>フォン・ヒッペル（E. von Hippel, MIT）が提唱。<b>情報をその発生場所から他の場所へ移転するのに必要なコスト</b>の大きさを示す概念。コストが高いほど「粘着性が高い」という。</p>

<div class="formula">
<b>2種類の情報と粘着性:</b>
<table>
<tr><th>情報の種類</th><th>内容</th><th>粘着性が高い場合</th></tr>
<tr><td><b>ニーズ情報</b></td><td>顧客が「何を求めているか」</td><td>ユーザーの暗黙知・使用文脈に埋め込まれており、<b>メーカーに伝えにくい</b></td></tr>
<tr><td><b>技術情報（シーズ情報）</b></td><td>「どう作れるか」の技術知識</td><td>専門的すぎて<b>ユーザーに伝えにくい</b></td></tr>
</table>
</div>

<div class="example">
<b>ユーザー・イノベーションが発生する条件:</b><br>
・ニーズ情報の粘着性が<b>高い</b> → メーカーがユーザーの本当のニーズを把握できない<br>
・技術情報の粘着性が<b>低い</b> → ユーザーが技術を比較的容易に入手・活用できる<br>
→ <b>ユーザー自身が製品を開発・改良</b>する方が効率的になる<br><br>

<b>具体例:</b><br>
・<b>マウンテンバイク</b>: サイクリスト自身が市販品を改造して山岳走行用の自転車を開発 → メーカーが製品化<br>
・<b>手術器具</b>: 外科医が自身の手術ニーズに合わせて器具を改良 → 医療機器メーカーが採用<br>
・<b>OSS</b>: 開発者自身がユーザーとして必要な機能を実装
</div>

<p><b>注意</b>: 情報の粘着性は固定的ではなく、ITの発展により低下することがある（例: 3Dプリンタの普及で技術情報の粘着性が低下し、ユーザー・イノベーションが促進）。また、粘着性が高い情報は<b>暗黙知</b>と重なる概念であり、SECIモデルの表出化（暗黙知→形式知）の困難さとも関連する。</p>

<div class="source">出典: 神戸大学MBA 情報の粘着性、ユーザーイノベーション教室、玄場研究室 粘着性の克服</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0417_情報の粘着性_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
