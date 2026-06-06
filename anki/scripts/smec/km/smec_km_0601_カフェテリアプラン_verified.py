"""
Ankiカード: カフェテリアプラン
科目: 中小企業診断士_企業経営理論
セクション: 06_組織行動・人的資源管理
作成日: 2026-03-07
検証済み: Yes
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS_NO_TABLE

# モデル定義
model_id = 1709060101
model = genanki.Model(
    model_id,
    'SMEC_KM_カフェテリアプラン',
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
    css=CARD_CSS_NO_TABLE,
)

# デッキ定義
deck_id = 2709060101
deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::06_組織行動・人的資源管理::カフェテリアプラン',
)

# カード作成
question = 'カフェテリアプランの定義・仕組み・メリット・デメリットを答えよ'

answer = '''<b>Cafeteria Plan / Flexible Benefits Plan</b>（カフェテリアプラン）

<ul>
<li><b>定義</b>: 企業が従業員に一定のポイント（カフェテリアポイント）を付与し、従業員が用意された福利厚生メニューから自分のニーズに合ったものを選択・利用する<b>選択型福利厚生制度</b></li>
<li><b>由来</b>: カフェテリアで好きな料理を選ぶように、福利厚生を自由に選べることから命名。1980年代に米国で普及、日本では1995年にベネッセが初導入</li>
</ul>

<div class="formula">
<b>メリット</b>
<ul>
<li>従業員の<b>多様なニーズ</b>に対応可能（ライフステージに応じた選択）</li>
<li>ポイントが均等付与のため<b>公平性</b>が高い</li>
<li>従業員満足度の向上・採用力強化</li>
<li>福利厚生コストの<b>総額管理</b>が容易</li>
</ul>
</div>

<div class="example">
<b>デメリット</b>
<ul>
<li>制度設計・運用の<b>管理コスト</b>が大きい</li>
<li>ポイントの<b>有効期限</b>があり、未使用分は失効（繰越不可が一般的）</li>
<li>従業員への制度周知・理解促進が必要</li>
</ul>
</div>

<b>注意</b>: 法定福利厚生（社会保険等）とは異なり、<b>法定外福利厚生</b>の一形態である。また、パッケージプラン（全員一律型）との対比で出題されやすい。

<div class="source">出典: リロクラブ、freee、日経人財グロース&コンサルティング</div>'''

note = genanki.Note(
    model=model,
    fields=[question, answer],
)

deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0601_カフェテリアプラン_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f'Generated: {output_path}')
