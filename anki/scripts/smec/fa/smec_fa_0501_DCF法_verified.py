"""
DCF法（割引キャッシュフロー法）- 中小企業診断士 財務会計
セクション: 05_企業価値
作成日: 2026-02-28
検証済み: Yes
出典: 中小企業診断士 財務会計 過去問解説
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS_NO_TABLE

# モデルID（ランダム生成、固定値として使用）
MODEL_ID = 1708901005
DECK_ID = 1708901006

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
    '中小企業診断士_財務会計::05_企業価値::DCF法'
)

# カードデータ
cards_data = [
    {
        'question': 'DCF法の定義・計算式・関連用語を答えよ',
        'answer': '''<strong>Discounted Cash Flow</strong>（割引キャッシュフロー法）

<p><strong>【定義】</strong><br>
将来のFCFを現在価値に割り引いて企業価値を算出する手法</p>

<div class="formula">
<strong>【企業価値】</strong><br>
\\[\\text{企業価値} = \\frac{FCF}{WACC}\\]
</div>

<div class="formula">
<strong>【FCF（Free Cash Flow）】</strong><br>
\\[FCF = 営業利益 \\times (1-税率) + 減価償却費 - 投資 - 運転資本増加額\\]
</div>

<p><strong>【関連】</strong></p>
<ul>
<li><strong>WACC</strong>: Weighted Average Cost of Capital（加重平均資本コスト）</li>
<li><strong>企業価値</strong> = 株式価値 + 負債価値</li>
</ul>''',
        'source': '中小企業診断士 財務会計 過去問解説'
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
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0501_DCF法_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Cards: {len(cards_data)}")
