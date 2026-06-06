"""
NPV（正味現在価値）- 中小企業診断士 財務会計
Net Present Value

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394201
DECK_ID = 1709394202

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_NPV',
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
    '中小企業診断士_財務会計::04_ファイナンス::NPV'
)

# カード内容
question = """NPV（正味現在価値）の定義・計算式・判断基準を答えよ"""

answer = """<b>Net Present Value</b>（正味現在価値）

<div class="formula">
\\[\\text{NPV} = \\sum_{t=1}^{n} \\frac{CF_t}{(1+r)^t} - I_0\\]
</div>

<table>
<tr><th>記号</th><th>意味</th></tr>
<tr><td>\\(CF_t\\)</td><td>t期のキャッシュフロー</td></tr>
<tr><td>\\(r\\)</td><td>割引率（資本コスト）</td></tr>
<tr><td>\\(I_0\\)</td><td>初期投資額</td></tr>
</table>

<b>定義</b>: 将来キャッシュフローの現在価値合計から初期投資額を差し引いた値

<b>判断基準</b>:
<ul>
<li>NPV &gt; 0 → 投資採択（企業価値を増大）</li>
<li>NPV &lt; 0 → 投資棄却（損失となる）</li>
</ul>

<div class="important">注意:</div>
<ul>
<li><b>利益ではなくキャッシュフロー</b>を使用する</li>
<li>相互排他的投資案の比較ではIRRより<b>NPVが信頼性高い</b></li>
<li>回収期間法と異なり、回収後のCFも考慮</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、一発合格まとめシート</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0401_NPV_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
