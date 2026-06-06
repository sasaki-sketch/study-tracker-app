"""
企業価値 - 中小企業診断士 財務会計
Enterprise Value (EV)

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740825601
DECK_ID = 1740825602

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_企業価値',
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
    '中小企業診断士_財務会計::05_企業価値::企業価値'
)

# カード内容
question = """企業価値（EV）の定義・計算式・意味を答えよ"""

answer = """<b>Enterprise Value</b>（EV / 企業価値）

<b>定義</b>: <b>企業を丸ごと買収するのにかかる実質コスト</b>。株主と債権者の両方に帰属する企業全体の価値。

<div class="formula">
\\[EV = \\text{株式時価総額} + \\text{有利子負債} - \\text{現金及び預金}\\]
</div>

<b>なぜこの式になるか（買収の視点）</b>:
<table>
<tr><th>項目</th><th>意味</th></tr>
<tr><td>株式時価総額</td><td>株主に払う金額（株を全部買い取る）</td></tr>
<tr><td>+ 有利子負債</td><td>買収後に引き継ぐ借金</td></tr>
<tr><td>− 現金</td><td>買収したら手に入る現金（実質的に戻ってくる）</td></tr>
</table>

<b>家の購入に例えると</b>:
<ul>
<li>売買価格（株式時価総額）= 3,000万</li>
<li>ローン残高（有利子負債）= 2,000万 ← 引き継ぐ</li>
<li>金庫の現金（現金）= 200万 ← 手に入る</li>
<li>→ 実質コスト（EV）= 3,000 + 2,000 − 200 = <b>4,800万</b></li>
</ul>

<b>EV/EBITDA倍率</b>:
<div class="formula">
\\[\\frac{EV}{EBITDA} = \\text{買収コストの回収年数（簡易指標）}\\]

目安: 8〜10倍程度が一般的
</div>

<div class="important">注意:</div>
EVはB/Sの会計等式ではなく市場価値ベースの概念。株式時価総額は純資産の簿価とは異なり、市場が評価した株主価値である。

<div class="source">出典: 野村證券、SMBC日興証券、M&Aキャピタルパートナーズ</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0502_企業価値_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
