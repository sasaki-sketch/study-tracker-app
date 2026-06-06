"""
配当割引モデル - 中小企業診断士 財務会計
セクション: 05_企業価値
作成日: 2026-02-28
検証済み: Yes
出典: 中小企業診断士 財務会計 過去問解説（R3第21問）
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS_NO_TABLE

# モデルID（ランダム生成、固定値として使用）
MODEL_ID = 1708901009
DECK_ID = 1708901010

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
    '中小企業診断士_財務会計::05_企業価値::配当割引モデル'
)

# カードデータ
cards_data = [
    {
        'question': '配当割引モデルの定義・計算式を答えよ',
        'answer': '''<strong>Dividend Discount Model</strong>（配当割引モデル）

<div class="formula">
<strong>【ゼロ成長モデル】</strong> 配当が一定<br>
\\[P = \\frac{d}{r_E}\\]
</div>

<div class="formula">
<strong>【定率成長モデル】</strong> 配当が一定率で成長<br>
\\[P = \\frac{d_1}{r_E - g}\\]
</div>

<ul>
<li>\\(P\\): 株価</li>
<li>\\(d\\): 配当、\\(d_1\\): 1年後の配当</li>
<li>\\(r_E\\): 株主資本コスト（期待収益率）</li>
<li>\\(g\\): 成長率</li>
</ul>

<div class="formula">
<strong>【株主の期待収益率】</strong><br>
\\[r_E = \\frac{d_1}{P_0} + g\\]
（配当利回り + キャピタルゲイン）
</div>''',
        'source': '中小企業診断士 財務会計 過去問解説（R3第21問）'
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
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0503_配当割引モデル_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Cards: {len(cards_data)}")
