"""
株主資本配当率 - 中小企業診断士 財務会計
Dividend on Equity Ratio (DOE)

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740825101
DECK_ID = 1740825102

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_株主資本配当率',
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
    '中小企業診断士_財務会計::01_経営分析::株主資本配当率'
)

# カード内容
question = """株主資本配当率（DOE）の定義・計算式・配当性向との違いを答えよ"""

answer = """<b>Dividend on Equity Ratio</b>（DOE / 株主資本配当率）

<b>定義</b>: 株主資本に対してどれだけの配当を支払っているかを示す指標。利益ではなく<b>株主資本を基準</b>とするため、業績変動に左右されにくい。

<div class="formula">
\\[DOE（\\%） = \\frac{\\text{年間配当総額}}{\\text{株主資本}} \\times 100\\]

<b>分解式</b>:
\\[DOE = ROE \\times \\text{配当性向}\\]

例: ROE 10%、配当性向 30% → DOE = 10% × 30% = <b>3.0%</b>
</div>

<b>配当性向・配当利回りとの比較</b>:
<table>
<tr><th>項目</th><th>DOE</th><th>配当性向</th><th>配当利回り</th></tr>
<tr><td>分母</td><td><b>株主資本</b></td><td><b>当期純利益</b></td><td><b>株価</b></td></tr>
<tr><td>意味</td><td>資本に対する配当割合</td><td>利益に対する配当割合</td><td>投資額に対する配当割合</td></tr>
<tr><td>安定性</td><td><b>安定</b>（資本は変動小）</td><td>不安定（利益は変動大）</td><td>不安定（株価は変動大）</td></tr>
<tr><td>視点</td><td>企業の還元姿勢</td><td>利益配分方針</td><td>投資家のリターン</td></tr>
</table>

<b>DOE採用が増えている理由</b>:
<ul>
<li>当期純利益は特別損益等で変動が大きい</li>
<li>株主資本は安定しており、<b>長期的な配当方針</b>の指標として適切</li>
<li>近年、中期経営計画でDOE目標を掲げる企業が増加</li>
</ul>

<div class="important">注意:</div>
DOEが高すぎる場合、内部留保が不足し成長投資に支障をきたす可能性がある。ROEと配当性向の掛け算で分解できるため、DOEが高い要因がROEの高さによるものか、配当性向の高さによるものかを見極めることが重要。

<div class="source">出典: 野村證券、SMBC日興証券、OANDA証券</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0116_株主資本配当率_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
