"""
生産性分析の指標 - 中小企業診断士 財務会計
Productivity Analysis

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394219
DECK_ID = 1709394220

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_生産性分析',
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
    '中小企業診断士_財務会計::01_経営分析::生産性分析'
)

# カード内容
question = """生産性分析の労働生産性と3分解を答えよ"""

answer = """<b>Productivity Analysis</b>（生産性分析）

<b>【労働生産性】</b>
<div class="formula">
\\[労働生産性 = \\frac{付加価値額}{従業員数}\\]
</div>

<hr>

<b>【3分解パターン】</b>

<b>① 売上高分解</b>
<div class="formula">
\\[= \\frac{売上高}{従業員数} \\times \\frac{付加価値額}{売上高} = 1人当たり売上高 \\times 付加価値率\\]
</div>
<table>
<tr><th>指標</th><th>計算式</th></tr>
<tr><td>1人当たり売上高</td><td>売上高 ÷ 従業員数</td></tr>
<tr><td>付加価値率</td><td>付加価値額 ÷ 売上高</td></tr>
</table>

<hr>

<b>② 有形固定資産分解</b>
<div class="formula">
\\[= \\frac{有形固定資産}{従業員数} \\times \\frac{付加価値額}{有形固定資産} = 労働装備率 \\times 資本生産性\\]
</div>
<table>
<tr><th>指標</th><th>計算式</th></tr>
<tr><td>労働装備率</td><td>有形固定資産 ÷ 従業員数</td></tr>
<tr><td>資本生産性</td><td>付加価値額 ÷ 有形固定資産</td></tr>
</table>

<hr>

<b>③ 人件費分解</b>
<div class="formula">
\\[= \\frac{人件費}{従業員数} \\div \\frac{人件費}{付加価値額} = 1人当たり人件費 \\div 労働分配率\\]
</div>
<table>
<tr><th>指標</th><th>計算式</th></tr>
<tr><td>1人当たり人件費</td><td>人件費 ÷ 従業員数</td></tr>
<tr><td>労働分配率</td><td>人件費 ÷ 付加価値額（目安: 50〜60%）</td></tr>
</table>

<hr>

※付加価値の計算方法は別カード参照

<div class="source">出典: 過去問.com</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0105_生産性分析_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
