"""
成長性分析の指標 - 中小企業診断士 財務会計
Growth Analysis

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394221
DECK_ID = 1709394222

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_成長性分析',
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
    '中小企業診断士_財務会計::01_経営分析::成長性分析'
)

# カード内容
question = """成長性分析の主要指標・計算式・目安を答えよ"""

answer = """<b>Growth Analysis</b>（成長性分析）

<table>
<tr><th>指標</th><th>計算式</th></tr>
<tr><td><b>売上高成長率</b></td><td>(当期売上高 − 前期売上高) ÷ 前期売上高 × 100</td></tr>
<tr><td><b>営業利益成長率</b></td><td>(当期営業利益 − 前期営業利益) ÷ 前期営業利益 × 100</td></tr>
<tr><td><b>経常利益成長率</b></td><td>(当期経常利益 − 前期経常利益) ÷ 前期経常利益 × 100</td></tr>
<tr><td><b>総資本成長率</b></td><td>(当期総資本 − 前期総資本) ÷ 前期総資本 × 100</td></tr>
<tr><td><b>従業員成長率</b></td><td>(当期従業員数 − 前期従業員数) ÷ 前期従業員数 × 100</td></tr>
</table>

<b>共通計算式</b>:
<div class="formula">
\\[成長率 = \\frac{当期 - 前期}{前期} \\times 100\\]
</div>

<b>目安</b>:
<ul>
<li><b>プラス</b> → 成長</li>
<li><b>マイナス</b> → 衰退</li>
<li>業界平均との比較が重要</li>
</ul>

<b>解釈</b>:
<ul>
<li>売上↑ 利益↓ → コスト増・価格競争</li>
<li>売上↓ 利益↑ → 効率化・高付加価値化</li>
<li>売上↑ 利益↑ → 理想的な成長</li>
</ul>

<div class="important">注意:</div>
<ul>
<li><b>単年ではなく複数年の推移</b>で判断</li>
<li><b>同業他社比較</b>・<b>市場成長率との比較</b>が重要</li>
</ul>

<div class="source">出典: freee、ジンジャー</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0106_成長性分析_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
