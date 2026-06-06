"""
ネットワーク外部性（Network Externality） - 中小企業診断士 企業戦略論
Network Externality, Direct/Indirect, De facto Standard

作成日: 2026-03-05
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1741185301
DECK_ID = 1741185302

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_ネットワーク外部性',
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

# デッキ定義
deck = genanki.Deck(
    DECK_ID,
    '中小企業診断士_企業戦略論::03_競争戦略::ネットワーク外部性'
)

# カード内容
question = """ネットワーク外部性の定義、2つのタイプ（直接的・間接的）の違いと具体例を答えよ"""

answer = """<b>Network Externality</b>（ネットワーク外部性）

<b>定義</b>: 利用者が増えるほど、製品・サービスの<b>価値が高まる</b>現象

<table>
<tr><th>タイプ</th><th>定義</th><th>例</th></tr>
<tr><td><b>直接的</b></td><td>同じ製品のユーザー同士が<b>直接つながる</b>ことで価値が増す</td><td>電話、LINE、Fax</td></tr>
<tr><td><b>間接的</b></td><td>ユーザー増加により<b>補完財</b>が充実・低価格化し価値が増す</td><td>Windows→ソフト増加、PS5→ゲーム増加</td></tr>
</table>

<b>デファクトスタンダードとの関係</b>:
<ul>
<li>ネットワーク外部性で早期にユーザー数を拡大 → <b>事実上の業界標準</b>に</li>
<li>ユーザー数を競合より<b>早期に増やす</b>ことが有効な競争戦略</li>
</ul>

<div class="important">注意:</div>
<ul>
<li>デファクトスタンダードは<b>最も優れた製品・技術とは限らない</b>。販売戦略や初期普及速度が決定要因となる</li>
<li>直接的 = ユーザー同士の直接接続、間接的 = 補完財を介した間接的恩恵（この区別が頻出）</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、Wikipedia - Network effect</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/xx/smec_xx_0301_ネットワーク外部性_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
