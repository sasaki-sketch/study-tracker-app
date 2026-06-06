"""
収益性分析の指標 - 中小企業診断士 財務会計
Profitability Analysis

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394213
DECK_ID = 1709394214

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_収益性分析',
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
    '中小企業診断士_財務会計::01_経営分析::収益性分析'
)

# カード内容
question = """収益性分析の主要指標・計算式・目安を答えよ"""

answer = """<b>Profitability Analysis</b>（収益性分析）

<table>
<tr><th>指標</th><th>計算式</th><th>目安</th></tr>
<tr><td><b>売上高総利益率</b></td><td>売上総利益 ÷ 売上高</td><td>業種により異なる</td></tr>
<tr><td><b>売上高営業利益率</b></td><td>営業利益 ÷ 売上高</td><td>5%以上で優良</td></tr>
<tr><td><b>売上高経常利益率</b></td><td>経常利益 ÷ 売上高</td><td>5%以上で優良</td></tr>
<tr><td><b>ROA（総資産利益率）</b></td><td>当期純利益 ÷ 総資産</td><td><b>5%以上</b>で優良</td></tr>
<tr><td><b>ROE（自己資本利益率）</b></td><td>当期純利益 ÷ 自己資本</td><td><b>8%以上</b>で優良</td></tr>
</table>

<b>分解式</b>:
<ul>
<li>\\(ROA = 売上高純利益率 \\times 総資本回転率\\)</li>
<li>\\(ROE = 売上高純利益率 \\times 総資本回転率 \\times 財務レバレッジ\\)</li>
</ul>

<b>解釈</b>:
<ul>
<li><b>売上高利益率</b> → マージン（利幅）の大きさ</li>
<li><b>ROA</b> → 総資産の運用効率（債権者+株主視点）</li>
<li><b>ROE</b> → 株主資本の運用効率（株主視点）</li>
</ul>

<div class="important">注意:</div>
<ul>
<li>ROEは財務レバレッジで高められるが<b>財務リスク増</b></li>
<li>ROA・ROEは<b>業種比較</b>で判断</li>
</ul>

<div class="source">出典: 髙野総合会計事務所、freee</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0102_収益性分析_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
