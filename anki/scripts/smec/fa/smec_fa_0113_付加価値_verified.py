"""
付加価値 - 中小企業診断士 財務会計
Value Added

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394235
DECK_ID = 1709394236

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_付加価値',
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
    '中小企業診断士_財務会計::01_経営分析::付加価値'
)

# カード内容
question = """付加価値の定義・計算方法を答えよ"""

answer = """<b>Value Added</b>（付加価値）

<b>【定義】</b>
企業が生産活動・サービス活動で新たに生み出した価値。

<hr>

<b>【計算方法（加算法・日銀方式）】</b>
<div class="formula">
\\[付加価値 = 経常利益 + 人件費 + 賃貸料 + 金融費用 + 租税公課 + 減価償却費\\]
</div>

→ 利害関係者へ分配される金額を合計する考え方

<hr>

<b>【活用指標】</b>
<ul>
<li>労働生産性 = 付加価値 ÷ 従業員数</li>
<li>付加価値率 = 付加価値 ÷ 売上高</li>
<li>労働分配率 = 人件費 ÷ 付加価値</li>
</ul>

<b>【試験での注意】</b>
付加価値額は問題文で与えられることが多い

<div class="source">出典: 過去問.com</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0113_付加価値_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
