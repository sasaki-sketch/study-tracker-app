"""
株式分割 - 中小企業診断士 財務会計
Stock Split

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740824701
DECK_ID = 1740824702

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_株式分割',
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
    '中小企業診断士_財務会計::04_ファイナンス::株式分割'
)

# カード内容
question = """株式分割の定義・目的・株式併合との違いを答えよ"""

answer = """<b>Stock Split</b>（株式分割）

<b>定義</b>: 既存の1株を複数株に分割し、<b>発行済株式数を増加</b>させること。1株あたりの価値は比例して減少する。

<div class="formula">
\\[\\text{分割後の株価} = \\frac{\\text{分割前の株価}}{\\text{分割比率}}\\]

例: 1株→2株の分割 → 株価は理論上1/2に
</div>

<b>主な目的</b>:
<table>
<tr><th>目的</th><th>内容</th></tr>
<tr><td>流動性向上</td><td>株価を引き下げ、売買しやすくする</td></tr>
<tr><td>投資単位の引下げ</td><td>個人投資家が購入しやすくなる</td></tr>
<tr><td>株主数の増加</td><td>上場維持基準（株主数）の充足</td></tr>
</table>

<b>影響を受けないもの</b>:
<ul>
<li><b>時価総額</b>: 変化なし（株価↓ × 株数↑）</li>
<li><b>純資産・資本金</b>: 変化なし</li>
<li><b>各株主の持分比率</b>: 変化なし</li>
</ul>

<b>影響を受ける指標</b>:
<ul>
<li><b>EPS</b>（1株当たり利益）: 分割比率に応じて低下</li>
<li><b>BPS</b>（1株当たり純資産）: 分割比率に応じて低下</li>
<li><b>PER・PBR</b>: 理論上は変化なし（株価もEPS/BPSも同比率で変動）</li>
</ul>

<b>株式併合との比較</b>:
<table>
<tr><th>項目</th><th>株式分割</th><th>株式併合</th></tr>
<tr><td>株式数</td><td>増加</td><td>減少</td></tr>
<tr><td>1株あたり価値</td><td>低下</td><td>上昇</td></tr>
<tr><td>決議要件</td><td><b>取締役会決議</b></td><td><b>株主総会特別決議</b></td></tr>
<tr><td>主な目的</td><td>流動性向上</td><td>株価調整・スクイーズアウト</td></tr>
</table>

<div class="important">注意:</div>
株式分割は<b>取締役会決議</b>のみで実施可能（株式併合は株主総会特別決議が必要）。経営指標の時系列比較では、分割前の数値を<b>遡及修正</b>して比較する必要がある。

<div class="source">出典: 日本取引所グループ、SMBC日興証券、大和証券</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0409_株式分割_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
