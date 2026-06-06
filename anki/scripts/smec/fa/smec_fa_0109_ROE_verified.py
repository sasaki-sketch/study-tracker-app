"""
ROE（自己資本利益率） - 中小企業診断士 財務会計
Return On Equity

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394227
DECK_ID = 1709394228

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_ROE',
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
    '中小企業診断士_財務会計::01_経営分析::ROE'
)

# カード内容
question = """ROE（自己資本利益率）の定義・計算式・分解を答えよ"""

answer = """<b>Return On Equity</b>（自己資本利益率）

<b>【定義】</b>
自己資本に対してどれだけ利益を生み出したかを示す指標。株主視点の収益性。

<hr>

<b>【計算式】</b>
<div class="formula">
\\[ROE = \\frac{当期純利益}{自己資本} \\times 100\\]
</div>

※実務では期首・期末の平均自己資本を使用

<hr>

<b>【ROEの分解】</b>

<b>① ROAとの関係</b>
<div class="formula">
\\[ROE = ROA \\times 財務レバレッジ\\]
</div>

<b>② デュポン分解</b>
<div class="formula">
\\[ROE = \\frac{純利益}{売上高} \\times \\frac{売上高}{総資本} \\times \\frac{総資本}{自己資本}\\]
\\[= 売上高純利益率 \\times 総資本回転率 \\times 財務レバレッジ\\]
</div>

<hr>

<b>【目安】</b>
10%程度（中小企業平均: 約10%）

<b>【注意】</b>
財務レバレッジでROEを高めている場合、負債依存のリスクに注意

<div class="source">出典: 過去問.com</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0109_ROE_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
