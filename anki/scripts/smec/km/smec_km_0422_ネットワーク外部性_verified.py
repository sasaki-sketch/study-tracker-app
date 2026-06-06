"""
Ankiカード: ネットワーク外部性（Network Externality）
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
検証済み: 2026-03-19
出典: 中小企業診断士 企業経営理論 R2第13問、R1第8問
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1710422001
deck_id = 1710422002

model = genanki.Model(
    model_id,
    'smec_km_0422_ネットワーク外部性',
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

deck = genanki.Deck(deck_id, '中小企業診断士_企業経営理論::04_技術経営・イノベーション::ネットワーク外部性')

question = '''ネットワーク外部性の定義と、直接的効果・間接的効果の違いを答えよ'''

answer = '''<b>Network Externality</b>（ネットワーク外部性）

<br><br>
<b>定義</b>: 利用者数が増加するほど、製品・サービスから得られる<span class="important">便益が増大</span>する現象

<br><br>
<table>
<tr><th></th><th>直接的効果</th><th>間接的効果</th></tr>
<tr><td><b>メカニズム</b></td><td>ユーザー数の増加が<b>そのまま</b>価値を高める</td><td>ユーザー数の増加で<b>補完財</b>が充実し価値が高まる</td></tr>
<tr><td><b>例</b></td><td>電話・FAX・SNS</td><td>ゲーム機（ハード普及→ソフト充実）、OS</td></tr>
</table>

<br>
<b>関連概念:</b>
<table>
<tr><th>概念</th><th>内容</th></tr>
<tr><td><b>クリティカルマス</b></td><td>ネットワークが機能するための最小ユーザー数</td></tr>
<tr><td><b>ロックイン</b></td><td>他製品への移行が困難になる状態</td></tr>
<tr><td><b>スイッチングコスト</b></td><td>他製品への切替に伴うコスト</td></tr>
<tr><td><b>デファクトスタンダード</b></td><td>市場競争の結果、事実上の標準となった規格</td></tr>
</table>

<br>
<div class="example">
<b>注意</b>: 補完財の充実は<b>間接的</b>効果（直接的効果ではない）。最も技術的に優れた製品がデファクトスタンダードになるとは限らない
</div>

<div class="source">出典: 中小企業診断士 企業経営理論 R2第13問、R1第8問</div>'''

note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ作成
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0422_ネットワーク外部性_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Created: {output_path}")
