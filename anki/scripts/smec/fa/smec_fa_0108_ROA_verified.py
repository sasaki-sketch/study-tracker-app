"""
ROA（総資本利益率） - 中小企業診断士 財務会計
Return On Assets

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394225
DECK_ID = 1709394226

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_ROA',
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
    '中小企業診断士_財務会計::01_経営分析::ROA'
)

# カード内容
question = """ROA（総資本利益率）の定義・計算式・分解を答えよ"""

answer = """<b>Return On Assets</b>（総資本利益率）

<b>【定義】</b>
総資本（総資産）に対してどれだけ利益を生み出したかを示す収益性指標。

<hr>

<b>【計算式】</b>
<div class="formula">
\\[ROA = \\frac{利益}{総資本} \\times 100\\]
</div>

<b>【利益の種類】</b>（問題文で指定）
<table>
<tr><th>利益</th><th>計算式</th></tr>
<tr><td>事業利益</td><td>営業利益 + 受取利息・配当金</td></tr>
<tr><td>経常利益</td><td>営業利益 + 営業外収益 − 営業外費用</td></tr>
<tr><td>当期純利益</td><td>税引後の最終利益</td></tr>
</table>

<hr>

<b>【ROAの分解】</b>
<div class="formula">
\\[ROA = \\frac{利益}{売上高} \\times \\frac{売上高}{総資本} = 売上高利益率 \\times 総資本回転率\\]
</div>

<hr>

<b>【ROEとの関係】</b>
<div class="formula">
\\[ROE = ROA \\times 財務レバレッジ\\]
</div>

<b>【目安】</b>
5%〜10%が標準

<div class="source">出典: 過去問.com</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0108_ROA_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
