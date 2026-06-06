"""
収益性指数法 - 中小企業診断士 財務会計
Profitability Index

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740823601
DECK_ID = 1740823602

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_収益性指数法',
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
    '中小企業診断士_財務会計::03_意思決定会計::収益性指数法'
)

# カード内容
question = """収益性指数法（PI）の定義・計算式・特徴を答えよ"""

answer = """<b>Profitability Index</b>（収益性指数法）

<b>定義</b>: 投資によって得られる将来キャッシュフローの現在価値が、初期投資額の何倍になるかを示す指標

<div class="formula">
\\[PI = \\frac{\\text{将来CFの現在価値合計}}{\\text{初期投資額}} = \\frac{\\sum_{t=1}^{n} \\frac{CF_t}{(1+r)^t}}{I_0}\\]
</div>

<b>判断基準</b>: PI &gt; 1 → 採択 / PI &lt; 1 → 棄却（PI = 1 は損益分岐点）

<b>NPVとの関係</b>:
<div class="formula">
\\[PI = 1 + \\frac{NPV}{I_0}\\]
→ NPV &gt; 0 ⇔ PI &gt; 1（判断結果は常に一致）
</div>

<b>メリット</b>:
<ul>
<li>比率で評価するため、<b>投資規模が異なる案件の比較</b>に有用</li>
<li><b>資本制約がある場合</b>の優先順位付けに適する</li>
</ul>

<b>デメリット</b>:
<ul>
<li>投資額の絶対額を考慮しないため、規模の大きい案件を過小評価する可能性</li>
<li>相互排他的案件ではNPVと順位が異なることがある → <b>NPVを優先</b></li>
</ul>

<div class="important">注意:</div>
IRRと同様に「率」で評価する手法。資本制約下（キャピタル・レーショニング）で複数案件を選定する場面で特に有効。

<div class="source">出典: ロロント、経営を学ぶ、mtame</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0303_収益性指数法_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
