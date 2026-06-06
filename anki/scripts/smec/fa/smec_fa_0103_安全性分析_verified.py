"""
安全性分析の指標 - 中小企業診断士 財務会計
Safety Analysis

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394215
DECK_ID = 1709394216

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_安全性分析',
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
    '中小企業診断士_財務会計::01_経営分析::安全性分析'
)

# カード内容
question = """安全性分析の主要指標・計算式・目安を答えよ"""

answer = """<b>Safety Analysis</b>（安全性分析）

<b>【短期安全性】</b>
<table>
<tr><th>指標</th><th>計算式</th><th>目安</th></tr>
<tr><td><b>流動比率</b></td><td>流動資産 ÷ 流動負債</td><td><b>200%以上</b>理想、100%以上必須</td></tr>
<tr><td><b>当座比率</b></td><td>当座資産 ÷ 流動負債</td><td><b>100%以上</b>で安全</td></tr>
</table>

※当座資産 = 流動資産 − 棚卸資産

<b>【長期安全性】</b>
<table>
<tr><th>指標</th><th>計算式</th><th>目安</th></tr>
<tr><td><b>固定比率</b></td><td>固定資産 ÷ 自己資本</td><td><b>100%以下</b>で安全</td></tr>
<tr><td><b>固定長期適合率</b></td><td>固定資産 ÷ (自己資本+固定負債)</td><td><b>100%以下</b>必須</td></tr>
</table>

<b>【資本構成】</b>
<table>
<tr><th>指標</th><th>計算式</th><th>目安</th></tr>
<tr><td><b>自己資本比率</b></td><td>自己資本 ÷ 総資本</td><td><b>50%以上</b>良好、30%以上確保</td></tr>
<tr><td><b>負債比率</b></td><td>負債 ÷ 自己資本</td><td><b>100%未満</b>が望ましい</td></tr>
</table>

<b>解釈</b>:
<ul>
<li>短期 → 1年以内の支払能力</li>
<li>長期 → 設備投資の健全性</li>
<li>資本構成 → 財務体質の安定性</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0103_安全性分析_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
