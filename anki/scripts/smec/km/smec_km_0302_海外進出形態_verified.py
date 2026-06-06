"""
Ankiカード: 海外進出形態
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-20
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703020301
deck_id = 1703020302

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_海外進出形態',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::海外進出形態'
)

# カード内容
question = '''企業の<span class="important">海外進出形態</span>の種類・特徴・リスクを答えよ'''

answer = '''<b>Foreign Market Entry Modes</b>（海外進出形態）

<div class="formula">
<table>
<tr><th>形態</th><th>内容</th><th>速度</th><th>コスト</th><th>リスク</th></tr>
<tr><td><b>輸出</b></td><td>国内生産→海外販売</td><td>速</td><td>低</td><td>低</td></tr>
<tr><td><b>ライセンシング</b></td><td>技術・商標等の使用権を供与</td><td>速</td><td>低</td><td>中</td></tr>
<tr><td><b>フランチャイジング</b></td><td>ビジネスモデル全体を供与</td><td>速</td><td>低</td><td>中</td></tr>
<tr><td><b>戦略的提携</b></td><td>出資を伴わない協力関係</td><td>中</td><td>中</td><td>中</td></tr>
<tr><td><b>JV（合弁）</b></td><td>現地パートナーと共同出資で設立</td><td>中</td><td>中</td><td>中</td></tr>
<tr><td><b>クロスボーダーM&amp;A</b><br>（ブラウンフィールド）</td><td>海外の既存企業を買収</td><td><b>速</b></td><td><b>高</b></td><td>高</td></tr>
<tr><td><b>グリーンフィールド投資</b></td><td>海外に完全子会社を新設</td><td><b>遅</b></td><td><b>高</b></td><td>高</td></tr>
</table>
</div>

<div class="example">
<b>頻出ポイント:</b><br>
・<b>グリーンフィールド</b>＝新設、<b>ブラウンフィールド</b>＝既存企業の買収・再活用（混同注意）<br>
・ライセンシングのリスク: 契約失効後に<b>ライセンシーが競合化</b>する<br>
・戦略的提携≠ジョイントベンチャー: 提携は出資不要、JVは共同出資<br>
・1980年代の日本企業の海外進出＝<b>グリーンフィールド</b>が主流
</div>

<div class="mnemonic">
<b>覚え方:</b><br>
・グリーン（Green＝緑＝更地）→ <b>新しく建てる</b><br>
・ブラウン（Brown＝茶＝使用済みの土地）→ <b>既存を買って使う</b>
</div>

<div class="source">出典: 中小企業診断士試験 R4第11問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0302_海外進出形態_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
