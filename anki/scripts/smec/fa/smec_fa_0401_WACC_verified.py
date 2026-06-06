"""
WACC（加重平均資本コスト）- 中小企業診断士 財務会計
セクション: 04_ファイナンス
作成日: 2026-02-28
検証済み: Yes
出典: 中小企業診断士 財務会計 過去問解説（R6第14問）
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS_NO_TABLE

# モデルID（ランダム生成、固定値として使用）
MODEL_ID = 1708901011
DECK_ID = 1708901012

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
    '中小企業診断士_財務会計::04_ファイナンス::WACC'
)

# カードデータ
cards_data = [
    {
        'question': 'WACC（加重平均資本コスト）の定義・計算式を答えよ',
        'answer': '''<strong>Weighted Average Cost of Capital</strong>（加重平均資本コスト）

<div class="formula">
<strong>【計算式】</strong><br>
\\[WACC = r_E \\times \\frac{E}{D+E} + r_D \\times (1-T) \\times \\frac{D}{D+E}\\]
</div>

<ul>
<li>\\(r_E\\): 株主資本コスト</li>
<li>\\(r_D\\): 負債コスト</li>
<li>\\(E\\): 株主資本、\\(D\\): 負債</li>
<li>\\(T\\): 実効税率</li>
</ul>

<p><strong>【定義】</strong><br>
株主資本コストと負債コストの加重平均</p>

<p class="important">【ポイント】負債コストに\\((1-T)\\)を乗じる → 利子の節税効果</p>''',
        'source': '中小企業診断士 財務会計 過去問解説（R6第14問）'
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
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0401_WACC_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Cards: {len(cards_data)}")
