"""
Ankiカード: ドメインコンセンサス
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
model_id = 1709010104
model = genanki.Model(
    model_id,
    'SMEC_KM_ドメインコンセンサス',
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
deck_id = 2709010104
deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::01_経営戦略::ドメインコンセンサス',
)

# カード作成
question = 'ドメインコンセンサスの定義・外部/内部コンセンサスの違いを答えよ'

answer = '''<b>Domain Consensus</b>（ドメインコンセンサス）

<ul>
<li><b>定義</b>: 企業のドメイン（事業領域）について、組織の内外の関係者との間で形成される<b>共通認識・合意</b></li>
<li><b>意義</b>: ドメインは経営者が定義するだけでは不十分で、ステークホルダーとのコンセンサスがなければ成立・存続しない</li>
</ul>

<div class="formula">
<b>外部コンセンサスと内部コンセンサス</b>
<table>
<tr><th></th><th>内部コンセンサス</th><th>外部コンセンサス</th></tr>
<tr><td><b>対象</b></td><td>経営幹部・従業員</td><td>顧客・株主・社会等</td></tr>
<tr><td><b>効果</b></td><td>組織の方向性の共有・一体感形成</td><td>社会的存在意義の明確化・理解と共感の獲得</td></tr>
<tr><td><b>形成するもの</b></td><td><b>内的アイデンティティ</b></td><td><b>外的アイデンティティ</b></td></tr>
</table>
</div>

<div class="example">
<b>組織の正当性（Legitimacy）との関連</b><br>
ドメインコンセンサスが得られることで、企業は社会から<b>正当性</b>を認められる。正当性がなければ経営資源の調達や顧客からの支持が得られず、事業の継続が困難になる。
</div>

<b>注意</b>: ドメインの定義（エーベルの3次元等）とセットで出題されやすい。ドメインは「定義すること」だけでなく「コンセンサスを得ること」が重要という点が問われる。

<div class="source">出典: iFinance、イマセ総合経営研究所、NRI</div>'''

note = genanki.Note(
    model=model,
    fields=[question, answer],
)

deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0104_ドメインコンセンサス_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f'Generated: {output_path}')
