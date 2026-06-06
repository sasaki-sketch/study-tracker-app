"""
サステナブル成長率_ロジック - 中小企業診断士 財務会計
Sustainable Growth Rate - Calculation Logic

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740825401
DECK_ID = 1740825402

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_サステナブル成長率_ロジック',
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
    '中小企業診断士_財務会計::01_経営分析::サステナブル成長率_ロジック'
)

# カード内容
question = """サステナブル成長率の計算ロジック（なぜ ROE × (1−配当性向) で求まるか）を説明せよ"""

answer = """<b>Sustainable Growth Rate - 計算ロジック</b>

<b>結論</b>: サステナブル成長率 = <b>自己資本が毎期どれだけ膨らむかの率</b>

<b>式の意味</b>:
<table>
<tr><th>要素</th><th>意味</th><th>例</th></tr>
<tr><td>ROE</td><td>自己資本から利益を生む<b>効率</b></td><td>10%</td></tr>
<tr><td>\\(1 - \\text{配当性向}\\)</td><td>利益のうち会社に残す<b>割合</b></td><td>60%</td></tr>
<tr><td>掛け算</td><td>自己資本が毎期膨らむ率</td><td><b>6%</b></td></tr>
</table>

<b>因果の流れ</b>: 利益を出す → そのうち残した分 → 自己資本が成長

<b>数値で確認</b>（自己資本1,000万、ROE 10%、配当性向 40%）:
<div class="formula">
\\[\\text{1. 純利益} = 1{,}000 \\times 10\\% = 100\\text{万}\\]
\\[\\text{2. 内部留保} = 100 \\times (1 - 0.4) = 60\\text{万}\\]
\\[\\text{3. 成長率} = \\frac{60}{1{,}000} = 6\\%\\]
</div>

<b>式の導出</b>:
<div class="formula">
\\[g = \\frac{\\text{内部留保}}{\\text{自己資本}} = \\frac{ROE \\times \\cancel{E} \\times (1 - d)}{\\cancel{E}}\\]

\\[\\therefore \\quad g = ROE \\times (1 - d)\\]

← 自己資本 \\(E\\) が約分で消える
</div>

<div class="important">注意:</div>
ROEが毎期一定という前提。ROEが変われば成長率も変わる。また財務レバレッジでROEを高めている場合、見かけ上のgは高くなるが負債リスクが増大する。

<div class="source">出典: 一発合格道場、シグマインベストメントスクール</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0118_サステナブル成長率_ロジック_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
