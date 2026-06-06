"""
財務レバレッジ - 中小企業診断士 財務会計
Financial Leverage

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394229
DECK_ID = 1709394230

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_財務レバレッジ',
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
    '中小企業診断士_財務会計::01_経営分析::財務レバレッジ'
)

# カード内容
question = """財務レバレッジの定義・計算式・自己資本比率との関係を答えよ"""

answer = """<b>Financial Leverage</b>（財務レバレッジ）

<b>【定義】</b>
自己資本の何倍の総資本を持っているかを示す指標。他人資本（負債）の活用度合いを表す。

<hr>

<b>【計算式】</b>
<div class="formula">
\\[財務レバレッジ = \\frac{総資本}{自己資本}\\]
</div>

<hr>

<b>【自己資本比率との関係】</b>
<div class="formula">
\\[財務レバレッジ = \\frac{1}{自己資本比率}\\]
</div>

<table>
<tr><th>自己資本比率</th><th>財務レバレッジ</th></tr>
<tr><td>50%</td><td>2倍</td></tr>
<tr><td>25%</td><td>4倍</td></tr>
<tr><td>20%</td><td>5倍</td></tr>
</table>

<hr>

<b>【ROEとの関係】</b>
<div class="formula">
\\[ROE = ROA \\times 財務レバレッジ\\]
</div>

<b>【目安】</b>
2倍以下が優良（自己資本比率50%以上に相当）

<b>【注意】</b>
財務レバレッジが高いほどROEは向上するが、負債依存度が高く財務リスクも増大する

<div class="source">出典: 過去問.com</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0110_財務レバレッジ_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
