"""
Ankiカード: アンゾフの成長マトリクス
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-07
検証済み: Yes
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1709030101
model = genanki.Model(
    model_id,
    'SMEC_KM_アンゾフの成長マトリクス',
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
    css=CARD_CSS,
)

# デッキ定義
deck_id = 2709030101
deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::アンゾフの成長マトリクス',
)

# カード作成
question = 'アンゾフの成長マトリクスの定義・4つの成長戦略・多角化の4分類を答えよ'

answer = '''<b>Ansoff Growth Matrix</b>（アンゾフの成長マトリクス / 成長ベクトル）

<ul>
<li><b>提唱者</b>: イゴール・アンゾフ（Igor Ansoff）</li>
<li><b>定義</b>: <b>製品</b>（既存/新規）と<b>市場</b>（既存/新規）の2軸で事業拡大の方向性を4分類するフレームワーク</li>
</ul>

<div class="formula">
<b>4つの成長戦略</b>
<table>
<tr><th></th><th>既存製品</th><th>新規製品</th></tr>
<tr><td><b>既存市場</b></td><td><b>市場浸透</b>（リスク小）</td><td><b>新製品開発</b></td></tr>
<tr><td><b>新規市場</b></td><td><b>新市場開拓</b></td><td><b>多角化</b>（リスク大）</td></tr>
</table>
</div>

<div class="example">
<b>多角化戦略の4分類</b>
<ul>
<li><b>水平型多角化</b>: 同業種の類似分野へ展開（既存技術を活用）</li>
<li><b>垂直型多角化</b>: バリューチェーンの川上・川下へ展開</li>
<li><b>集中型多角化</b>: 既存技術と関連する新分野へ展開</li>
<li><b>集成型（コングロマリット）多角化</b>: 既存事業と無関連の分野へ展開（最もリスク大）</li>
</ul>
</div>

<b>注意</b>: 左上（市場浸透）→右下（多角化）に向かうほど<b>リスクが高い</b>。多角化の4分類では、集成型が最もリスクが高く、水平型が最もリスクが低い。シナジー効果との関連も問われやすい。

<div class="source">出典: 中小企業庁、大和総研、カオナビ</div>'''

note = genanki.Note(
    model=model,
    fields=[question, answer],
)

deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0301_アンゾフの成長マトリクス_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f'Generated: {output_path}')
