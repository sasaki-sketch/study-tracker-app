"""
Ankiカード: クライシスマネジメント
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略
作成日: 2026-03-07
検証済み: Yes
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1709010101
model = genanki.Model(
    model_id,
    'SMEC_KM_クライシスマネジメント',
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
deck_id = 2709010101
deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::01_経営戦略::クライシスマネジメント',
)

# カード作成
question = 'クライシスマネジメントの定義・リスクマネジメントとの違いを答えよ'

answer = '''<b>Crisis Management</b>（クライシスマネジメント / 危機管理）

<ul>
<li><b>定義</b>: 企業の存続を脅かす<b>予期せぬ危機</b>（大規模災害、重大事故、不祥事等）が発生した際に、被害を最小限にとどめ、二次被害の回避・早期復旧を図る経営管理手法</li>
<li><b>対象</b>: 想定外の事態（<b>事後対応</b>が中心）</li>
</ul>

<div class="formula">
<b>リスクマネジメントとの比較</b>
<table>
<tr><th></th><th>リスクマネジメント</th><th>クライシスマネジメント</th></tr>
<tr><td><b>英語</b></td><td>Risk Management</td><td>Crisis Management</td></tr>
<tr><td><b>タイミング</b></td><td>事前（予防）</td><td>事後（対応）</td></tr>
<tr><td><b>対象</b></td><td>想定可能なリスク</td><td>想定外の危機</td></tr>
<tr><td><b>目的</b></td><td>リスクの回避・軽減</td><td>被害最小化・早期復旧</td></tr>
<tr><td><b>手法</b></td><td>リスク分析・予防策策定</td><td>初動対応・情報開示・復旧計画</td></tr>
</table>
</div>

<div class="example">
<b>関連概念</b>
<ul>
<li><b>BCP（Business Continuity Plan）</b>: 事業継続計画。危機発生時に事業を継続・早期復旧するための計画</li>
<li><b>コンティンジェンシープラン</b>: 不測の事態に備えた緊急時対応計画</li>
</ul>
</div>

<b>注意</b>: リスクマネジメントは「事前・予防」、クライシスマネジメントは「事後・対応」という対比が頻出。BCPとの関連も問われやすい。

<div class="source">出典: リスキル、カオナビ、日本通運</div>'''

note = genanki.Note(
    model=model,
    fields=[question, answer],
)

deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0101_クライシスマネジメント_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f'Generated: {output_path}')
