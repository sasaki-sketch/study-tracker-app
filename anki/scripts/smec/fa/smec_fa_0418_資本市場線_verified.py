"""
資本市場線（CML） - 中小企業診断士 財務会計
Capital Market Line

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740926901
DECK_ID = 1740926902

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_資本市場線',
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
    '中小企業診断士_財務会計::04_ファイナンス::資本市場線'
)

# カード内容
question = """資本市場線（CML）の定義・計算式・市場ポートフォリオとの関係を答えよ"""

answer = """<b>Capital Market Line / CML</b>（資本市場線）

<b>定義</b>: 安全資産と市場ポートフォリオを結ぶ直線。安全資産を含む場合の<b>効率的フロンティア</b>

<b>計算式</b>:
<div class="formula">
\\[E(R_p) = R_f + \\frac{E(R_m) - R_f}{\\sigma_m} \\times \\sigma_p\\]
</div>

<table>
<tr><th>記号</th><th>意味</th></tr>
<tr><td>\\(R_f\\)</td><td>リスクフリーレート（安全資産の収益率）</td></tr>
<tr><td>\\(E(R_m)\\)</td><td>市場ポートフォリオの期待収益率</td></tr>
<tr><td>\\(\\sigma_m\\)</td><td>市場ポートフォリオの標準偏差</td></tr>
<tr><td>\\(\\sigma_p\\)</td><td>ポートフォリオの標準偏差</td></tr>
</table>

<b>CMLの傾き = シャープレシオ</b>（リスクの市場価格）:
<div class="formula">
\\[\\frac{E(R_m) - R_f}{\\sigma_m}\\]
</div>
→ リスク1単位あたりの超過リターン

<b>グラフ上の構造</b>（横軸: σ、縦軸: E(R)）:
<table>
<tr><th>点</th><th>意味</th></tr>
<tr><td>Y切片</td><td>安全資産（\\(R_f\\), σ=0）</td></tr>
<tr><td>接点</td><td><b>市場ポートフォリオ</b>（効率的フロンティアとの接点）</td></tr>
<tr><td>接点より左</td><td>安全資産＋リスク資産の組合せ（<b>貸付</b>）</td></tr>
<tr><td>接点より右</td><td>安全資産を借入してリスク資産に投資（<b>借入</b>）</td></tr>
</table>

<div class="important">注意:</div>
<ul>
<li>市場ポートフォリオは投資家のリスク回避度と<b>無関係</b>に決まる（接点は1つ）</li>
<li>投資家のリスク回避度はCML上の<b>ポジション</b>（安全資産との配分比率）を決定</li>
<li>CMLは<b>効率的ポートフォリオのみ</b>に適用（個別証券には<b>SML</b>を使用）</li>
<li>CMLの傾き（シャープレシオ）が大きいほど、リスク対比のリターンが良い</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、スタディング R3第20問</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0418_資本市場線_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
