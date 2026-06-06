"""
リスクフリーレート - 中小企業診断士 財務会計
Risk-Free Rate

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740823801
DECK_ID = 1740823802

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_リスクフリーレート',
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
    '中小企業診断士_財務会計::04_ファイナンス::リスクフリーレート'
)

# カード内容
question = """リスクフリーレートの定義・代表的指標・使われる場面を答えよ"""

answer = """<b>Risk-Free Rate</b>（リスクフリーレート / 無リスク利子率）

<b>定義</b>: リスクが限りなくゼロに近い金融商品から得られる利回り。すべての投資のリターンの出発点（ベースライン）となる。

<b>代表的指標</b>:
<table>
<tr><th>国</th><th>採用される指標</th></tr>
<tr><td>日本</td><td><b>10年物国債利回り</b></td></tr>
<tr><td>米国</td><td>米国財務省証券（10年物T-Bond）利回り</td></tr>
</table>

<b>10年国債が選ばれる理由</b>: 元本・利子の支払いを国が保証しており、長期投資の期間と整合する

<b>使われる場面</b>:
<table>
<tr><th>理論・指標</th><th>使い方</th></tr>
<tr><td>CAPM</td><td>\\(R_e = R_f + \\beta \\times (R_m - R_f)\\)</td></tr>
<tr><td>WACC</td><td>CAPMで求めた株主資本コストをWACC算出に使用</td></tr>
<tr><td>リスクプレミアム</td><td>\\(\\text{リスクプレミアム} = R_m - R_f\\)</td></tr>
</table>

\\(R_f\\): リスクフリーレート、\\(R_m\\): 市場期待収益率、\\(\\beta\\): 個別株式の感応度

<div class="important">注意:</div>
完全に無リスクな資産は理論上存在しない（国家デフォルトリスク等）。あくまで「限りなく無リスクに近い」概念として扱う。

<div class="source">出典: グロービス経営大学院、野村證券、オリックス銀行</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0404_リスクフリーレート_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
