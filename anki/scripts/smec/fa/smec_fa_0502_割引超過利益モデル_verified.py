"""
割引超過利益モデル（残余利益モデル）- 中小企業診断士 財務会計
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
MODEL_ID = 1708901007
DECK_ID = 1708901008

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
    '中小企業診断士_財務会計::05_企業価値::割引超過利益モデル'
)

# カードデータ
cards_data = [
    {
        'question': '割引超過利益モデルの定義・計算式を答えよ',
        'answer': '''<strong>Residual Income Model</strong>（残余利益モデル）

<div class="formula">
<strong>【株式価値】</strong><br>
\\[\\text{株式価値} = \\text{株主資本簿価} + \\text{超過利益の現在価値}\\]
</div>

<div class="formula">
<strong>【超過利益（残余利益）】</strong><br>
\\[\\text{超過利益} = 当期純利益 - r_E \\times 期首株主資本\\]
\\[= (ROE - r_E) \\times 期首株主資本\\]
</div>

<ul>
<li>\\(r_E\\): 株主資本コスト</li>
</ul>

<p><strong>【特徴】</strong></p>
<ul>
<li>配当割引モデルと理論上等価</li>
<li>ROE &gt; \\(r_E\\) なら株式価値 &gt; 簿価</li>
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
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0502_割引超過利益モデル_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Cards: {len(cards_data)}")
