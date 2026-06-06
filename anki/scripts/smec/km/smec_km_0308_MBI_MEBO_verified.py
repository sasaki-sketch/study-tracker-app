"""
Ankiカード: MBI・MEBOとバイアウト類型の全体像
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703080301
deck_id = 1703080302

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_MBI_MEBO',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::MBI_MEBO'
)

question = '''<span class="important">MBI（Management Buy-In）・MEBO</span>の定義・具体例と、バイアウト類型の全体像を答えよ'''

answer = '''<b>MBI &amp; MEBO</b>

<div class="formula">
<b>MBI（Management Buy-In）:</b>
<table>
<tr><th>項目</th><th>内容</th></tr>
<tr><td><b>定義</b></td><td>投資家・ファンドが企業を買収し、<b>外部からプロ経営者を送り込む</b></td></tr>
<tr><td><b>目的</b></td><td>経営再建、企業価値向上→売却益（キャピタルゲイン）</td></tr>
<tr><td><b>特徴</b></td><td>既存経営陣は<b>退陣</b>することが多い。日本では少ない</td></tr>
</table>
</div>

<div class="example">
<b>MBIの代表事例 − カネボウ（2004年）:</b><br><br>
① 多角化の失敗で経営破綻状態<br>
　↓<br>
② 産業再生機構が介入を決定<br>
　↓<br>
③ 既存経営陣を<b>全員退陣</b>させる<br>
　↓<br>
④ <b>外部から再建チームを送り込む</b>（＝Buy-In）<br>
　↓<br>
⑤ 化粧品事業は花王が約4,100億円で買収<br>
　残りはクラシエHDとして再建
</div>

<div class="formula">
<b>MEBO（Management and Employee Buy-Out）:</b>
<table>
<tr><th>項目</th><th>内容</th></tr>
<tr><td><b>定義</b></td><td><b>経営陣＋従業員</b>が共同出資で自社株を買い取る</td></tr>
<tr><td><b>特徴</b></td><td>全員が株主→士気向上、事業の安定性が高い</td></tr>
<tr><td><b>事例</b></td><td>日本レーザー（2007年）: 全従業員が株主に。退職者ゼロ・無借金経営を実現</td></tr>
</table>
</div>

<div class="formula">
<b>バイアウト類型の全体像:</b>
<table>
<tr><th>類型</th><th>誰が買う？</th><th>Out/Inの意味</th></tr>
<tr><td><b>MBO</b></td><td>現経営陣</td><td>既存株主を<b>Out</b>（追い出す）</td></tr>
<tr><td><b>MBI</b></td><td>外部経営者</td><td>外部から<b>In</b>（入り込む）</td></tr>
<tr><td><b>EBO</b></td><td>従業員</td><td>既存株主を<b>Out</b>（追い出す）</td></tr>
<tr><td><b>MEBO</b></td><td>経営陣+従業員</td><td>MBO＋EBOのハイブリッド</td></tr>
<tr><td><b>LBO</b></td><td>誰でも可</td><td><b>借入金</b>で買収（資金調達手法。上記と組み合わせ可）</td></tr>
</table>
</div>

<div class="source">出典: 中小企業診断士試験、カネボウ再建事例、日本レーザーMEBO事例</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0308_MBI_MEBO_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
