"""
サステナブル成長率 - 中小企業診断士 財務会計
Sustainable Growth Rate

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740825301
DECK_ID = 1740825302

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_サステナブル成長率',
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
    '中小企業診断士_財務会計::01_経営分析::サステナブル成長率'
)

# カード内容
question = """サステナブル成長率の定義・計算式・意味を答えよ"""

answer = """<b>Sustainable Growth Rate</b>（サステナブル成長率 / 持続可能成長率）

<b>定義</b>: 外部資金調達（借入・増資）に頼らず、<b>内部留保のみで達成できる理論上の成長率</b>。

<div class="formula">
\\[g = ROE \\times b\\]

\\[g = ROE \\times (1 - \\text{配当性向})\\]

\\(g\\): サステナブル成長率、\\(b\\): 内部留保率（= 1 − 配当性向）

例: ROE 12%、配当性向 40% → g = 12% × (1 − 0.4) = <b>7.2%</b>
</div>

<b>成長率を高める要因</b>:
<table>
<tr><th>要因</th><th>方向</th><th>理由</th></tr>
<tr><td>ROE↑</td><td>g↑</td><td>利益効率が高い → 留保も増える</td></tr>
<tr><td>配当性向↓（内部留保率↑）</td><td>g↑</td><td>再投資に回す利益が増える</td></tr>
</table>

<b>ROEを分解すると</b>:
<div class="formula">
\\[g = \\frac{\\text{当期純利益}}{\\text{売上高}} \\times \\frac{\\text{売上高}}{\\text{総資産}} \\times \\frac{\\text{総資産}}{\\text{自己資本}} \\times (1 - \\text{配当性向})\\]
</div>

→ 売上高純利益率↑、総資産回転率↑、財務レバレッジ↑、内部留保率↑ のいずれかで成長率は向上

<div class="important">注意:</div>
サステナブル成長率を超えて成長するには外部資金調達が必要となる。また、財務レバレッジを高めればgは上昇するが、負債依存のリスクが増大する点に注意。

<div class="source">出典: 一発合格道場、シグマインベストメントスクール、バフェットコードマガジン</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0117_サステナブル成長率_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
