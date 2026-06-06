"""
クリーンサープラス関係 - 中小企業診断士 財務会計
Clean Surplus Relationship

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394207
DECK_ID = 1709394208

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_クリーンサープラス',
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
    '中小企業診断士_財務会計::05_企業価値::クリーンサープラス'
)

# カード内容
question = """クリーンサープラス関係の定義・計算式・意義を答えよ"""

answer = """<b>Clean Surplus Relationship</b>（クリーンサープラス関係）

<div class="formula">
\\[B_t = B_{t-1} + NI_t - D_t\\]
</div>

<table>
<tr><th>記号</th><th>意味</th></tr>
<tr><td>\\(B_t\\)</td><td>期末純資産（株主資本）</td></tr>
<tr><td>\\(B_{t-1}\\)</td><td>期首純資産</td></tr>
<tr><td>\\(NI_t\\)</td><td>当期純利益</td></tr>
<tr><td>\\(D_t\\)</td><td>配当金</td></tr>
</table>

<b>定義</b>: P/Lの当期純利益とB/Sの純資産増減額が一致する関係

<b>意義</b>: この関係が成立する場合、<b>配当割引モデル</b>と<b>残余利益モデル</b>が一致する

<div class="important">注意:</div>
<ul>
<li><b>その他包括利益（OCI）</b>がP/Lを経由せず純資産に直入される場合、厳密には成立しない</li>
<li>増資・減資など資本取引は除外して考える</li>
</ul>

<b>企業価値評価での活用</b>:
<ul>
<li>配当割引モデル → 残余利益モデルへの導出に使用</li>
<li>配当ゼロでも株式価値算定が可能になる</li>
</ul>

<div class="source">出典: みずほ証券 ファイナンス用語集、過去問ドットコム R4 問18</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0501_クリーンサープラス_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
