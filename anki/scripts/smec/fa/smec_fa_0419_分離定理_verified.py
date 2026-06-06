"""
トービンの分離定理 - 中小企業診断士 財務会計
Tobin's Separation Theorem

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740927001
DECK_ID = 1740927002

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_分離定理',
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
    '中小企業診断士_財務会計::04_ファイナンス::分離定理'
)

# カード内容
question = """トービンの分離定理の定義・2段階の意思決定プロセス・ポートフォリオ理論上の意義を答えよ"""

answer = """<b>Tobin's Separation Theorem</b>（トービンの分離定理）

<b>定義</b>: 安全資産が存在する場合、リスク資産のポートフォリオ構成は投資家のリスク選好と<b>無関係</b>に決まるという定理

<b>2段階の意思決定プロセス</b>:
<table>
<tr><th>段階</th><th>内容</th><th>リスク選好の影響</th></tr>
<tr><td><b>第1段階</b></td><td>リスク資産のみで最適ポートフォリオを構成<br>（= <b>接点ポートフォリオ</b>）</td><td><b>無関係</b>（全投資家共通）</td></tr>
<tr><td><b>第2段階</b></td><td>接点ポートフォリオと安全資産の<b>配分比率</b>を決定</td><td><b>影響あり</b>（個人差で調整）</td></tr>
</table>

<b>ポイント</b>:
<ul>
<li>全ての合理的投資家は<b>同一の</b>リスク資産ポートフォリオ（= 市場ポートフォリオ）を保有</li>
<li>リスク回避度の違いは、安全資産との<b>配分比率のみ</b>で調整</li>
<li>CML上のどの位置を選ぶかが第2段階の意思決定</li>
</ul>

<table>
<tr><th>投資家タイプ</th><th>CML上の位置</th><th>安全資産比率</th></tr>
<tr><td>リスク回避的</td><td>接点より<b>左</b></td><td>高い（貸付）</td></tr>
<tr><td>リスク愛好的</td><td>接点より<b>右</b></td><td>負（借入）</td></tr>
</table>

<div class="important">注意:</div>
<ul>
<li>「分離」= リスク資産の最適構成と、個人のリスク選好を<b>分けて</b>考えられること</li>
<li>接点ポートフォリオ = 市場ポートフォリオ = CMLと効率的フロンティアの接点</li>
<li>前提条件: 安全資産への投資（貸付）・借入が自由に可能</li>
</ul>

<div class="source">出典: みずほ証券 ファイナンス用語集、kinikuk.com</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0419_分離定理_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
