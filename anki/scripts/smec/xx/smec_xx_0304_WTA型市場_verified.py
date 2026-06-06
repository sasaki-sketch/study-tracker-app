"""
WTA型市場（Winner Take All） - 中小企業診断士 企業戦略論
Winner Take All, Network Externality, Information Goods, Critical Mass

作成日: 2026-03-06
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1741185601
DECK_ID = 1741185602

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_WTA型市場',
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
    '中小企業診断士_企業戦略論::03_競争戦略::WTA型市場'
)

# カード内容
question = """WTA（Winner Take All）型市場の定義、発生条件、情報財の特性を答えよ"""

answer = """<b>Winner Take All</b>（WTA型市場 / 一人勝ち市場）

<b>定義</b>: ネットワーク外部性により、勝者が市場をほぼ独占する構造

<b>発生メカニズム</b>:
<ol>
<li>ネットワーク外部性でユーザーが増えるほど価値が増大</li>
<li>正のフィードバックループ（ユーザー増 → 価値増 → さらにユーザー増）</li>
<li>臨界点（<b>クリティカルマス</b>）を超えると一気に市場を支配</li>
</ol>

<b>情報財の特性</b>（WTAが起きやすい背景）:
<table>
<tr><th>特性</th><th>内容</th></tr>
<tr><td><b>高い固定費用・低い限界費用</b></td><td>開発コストは大きいが、複製コストはほぼゼロ</td></tr>
<tr><td><b>収穫逓増</b></td><td>規模が大きくなるほど利益率が上昇</td></tr>
</table>

例: Google検索、Windows OS、Amazon

<div class="important">注意:</div>
ネットワーク外部性が大きい市場では、顧客数が増えても製品価値は<b>希薄化しない</b>（むしろ増大する）。この点がR3第12問で誤答選択肢として出題

<div class="source">出典: 慶應義塾大学 WTA研究、スタディング R2第13問解説</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/xx/smec_xx_0304_WTA型市場_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
