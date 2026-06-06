"""
IRR（内部収益率）- 中小企業診断士 財務会計
Internal Rate of Return

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394203
DECK_ID = 1709394204

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_IRR',
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
    '中小企業診断士_財務会計::04_ファイナンス::IRR'
)

# カード内容
question = """IRR（内部収益率）の定義・計算式・判断基準を答えよ"""

answer = """<b>Internal Rate of Return</b>（内部収益率）

<div class="formula">
\\[\\sum_{t=1}^{n} \\frac{CF_t}{(1+\\text{IRR})^t} - I_0 = 0\\]
</div>

→ <b>NPVがゼロになる割引率</b>を求める

<table>
<tr><th>記号</th><th>意味</th></tr>
<tr><td>\\(CF_t\\)</td><td>t期のキャッシュフロー</td></tr>
<tr><td>\\(I_0\\)</td><td>初期投資額</td></tr>
</table>

<b>定義</b>: 投資案の年平均期待収益率（NPV=0となる割引率）

<b>判断基準</b>:
<ul>
<li>IRR &gt; 資本コスト → 投資採択</li>
<li>IRR &lt; 資本コスト → 投資棄却</li>
</ul>

<div class="important">注意:</div>
<ul>
<li><b>投資規模を考慮しない</b>（金額ベースで比較できない）</li>
<li>CFパターンにより<b>複数解</b>が存在する場合あり</li>
<li>相互排他的投資案では<b>NPVで検証が必要</b></li>
</ul>

<b>NPVとの違い</b>:
<ul>
<li>NPV: 絶対値（金額）で評価</li>
<li>IRR: 相対値（収益率）で評価</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、M&Aキャピタルパートナーズ</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0402_IRR_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
