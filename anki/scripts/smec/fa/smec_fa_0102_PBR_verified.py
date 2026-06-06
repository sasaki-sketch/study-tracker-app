"""
PBR（株価純資産倍率）- 中小企業診断士 財務会計
セクション: 01_経営分析
作成日: 2026-02-28
検証済み: Yes
出典: 三菱UFJ銀行、松井証券
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS_NO_TABLE

# モデルID（ランダム生成、固定値として使用）
MODEL_ID = 1708901003
DECK_ID = 1708901004

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_基本',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Source'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '''{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>
<div class="source">{{Source}}</div>''',
        },
    ],
    css=CARD_CSS_NO_TABLE
)

# デッキ作成
deck = genanki.Deck(
    DECK_ID,
    '中小企業診断士_財務会計::01_経営分析::PBR'
)

# カードデータ
cards_data = [
    {
        'question': 'PBR（株価純資産倍率）の定義・計算式・目安を答えよ',
        'answer': '''<strong>Price Book-value Ratio</strong>（株価純資産倍率）

<div class="formula">
\\[\\text{PBR} = \\frac{\\text{株価}}{\\text{BPS（1株あたり純資産）}}\\]
</div>

<ul>
<li><strong>定義</strong>: 株価が純資産の何倍かを示す指標</li>
<li><strong>目安</strong>: 1倍（下回れば割安、上回れば割高）</li>
</ul>

<p class="important">注意: PER（利益）と混同しないこと。PBRは<strong>B</strong>ook-value（純資産）</p>''',
        'source': '三菱UFJ銀行、松井証券'
    },
]

# カード追加
for card_data in cards_data:
    note = genanki.Note(
        model=model,
        fields=[
            card_data['question'],
            card_data['answer'],
            card_data['source']
        ]
    )
    deck.add_note(note)

# .apkgファイル出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0102_PBR_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Cards: {len(cards_data)}")
