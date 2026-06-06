"""
デュポンシステム - 中小企業診断士 財務会計
DuPont System

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394223
DECK_ID = 1709394224

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_デュポンシステム',
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
    '中小企業診断士_財務会計::01_経営分析::デュポンシステム'
)

# カード内容
question = """デュポンシステム（ROEの3分解）を答えよ"""

answer = """<b>DuPont System</b>（デュポンシステム）

<b>【定義】</b>
ROEを収益性・効率性・安全性の3要素に分解し、企業の総合力を多角的に分析する手法。1920年代にDuPont社が開発。

<hr>

<b>【ROEの3分解】</b>
<div class="formula">
\\[ROE = 売上高純利益率 \\times 総資本回転率 \\times 財務レバレッジ\\]
</div>

<div class="formula">
\\[= \\frac{純利益}{売上高} \\times \\frac{売上高}{総資本} \\times \\frac{総資本}{自己資本}\\]
</div>

<hr>

<b>【各要素】</b>
<table>
<tr><th>指標</th><th>計算式</th><th>分析視点</th></tr>
<tr><td><b>売上高純利益率</b></td><td>純利益 ÷ 売上高</td><td>収益性（P/L）</td></tr>
<tr><td><b>総資本回転率</b></td><td>売上高 ÷ 総資本</td><td>効率性（B/S借方）</td></tr>
<tr><td><b>財務レバレッジ</b></td><td>総資本 ÷ 自己資本</td><td>安全性（B/S貸方）</td></tr>
</table>

<hr>

<b>【活用】</b>
<ul>
<li>ROEが高い要因を3視点で特定</li>
<li>同業他社比較で強み・弱みを分析</li>
<li>財務レバレッジでROEを高めている場合、負債依存のリスクに注意</li>
</ul>

<div class="source">出典: 過去問.com</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0107_デュポンシステム_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
