"""
債券価格（割引債・利付債） - 中小企業診断士 財務会計
Bond Price (Zero Coupon Bond / Coupon Bond)

作成日: 2026-03-02
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740825801
DECK_ID = 1740825802

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_債券価格',
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
    '中小企業診断士_財務会計::04_ファイナンス::債券価格'
)

# カード内容
question = """債券価格（割引債・利付債）の定義・計算式・金利との関係を答えよ"""

answer = """<b>Bond Price</b>（債券価格）

<b>定義</b>: 債券の理論価格は、将来受け取る<b>キャッシュフローの現在価値の合計</b>。

<b>割引債（Zero Coupon Bond）</b>:
利息なし。満期に額面金額のみを受け取る。
<div class="formula">
\\[P = \\frac{F}{(1+r)^n}\\]

例: 額面100万、利回り5%、3年 → \\(P = \\frac{100}{(1.05)^3} = 86.4\\)万円
</div>

<b>利付債（Coupon Bond）</b>:
毎年利息（クーポン）を受け取り、満期に額面を償還。
<div class="formula">
\\[P = \\sum_{t=1}^{n} \\frac{C}{(1+r)^t} + \\frac{F}{(1+r)^n}\\]
</div>

<table>
<tr><th>記号</th><th>意味</th></tr>
<tr><td>\\(P\\)</td><td>債券価格</td></tr>
<tr><td>\\(C\\)</td><td>毎年のクーポン（利息）</td></tr>
<tr><td>\\(F\\)</td><td>額面（償還価格）</td></tr>
<tr><td>\\(r\\)</td><td>最終利回り（割引率）</td></tr>
<tr><td>\\(n\\)</td><td>残存年数</td></tr>
</table>

<div class="formula">
例: クーポン3万/年、額面100万、利回り5%、3年

\\[P = \\frac{3}{1.05} + \\frac{3}{1.05^2} + \\frac{103}{1.05^3} = 94.6\\text{万円}\\]
</div>

<b>金利と債券価格の関係</b>:
<table>
<tr><th>金利の変動</th><th>債券価格</th><th>理由</th></tr>
<tr><td>金利↑</td><td><b>価格↓</b></td><td>割引率↑ → 現在価値↓</td></tr>
<tr><td>金利↓</td><td><b>価格↑</b></td><td>割引率↓ → 現在価値↑</td></tr>
</table>

→ <b>金利と債券価格は逆の関係（シーソー）</b>

<div class="important">注意:</div>
残存年数が長いほど金利変動の影響が大きい。また日本の実務では利付債は単利、割引債は複利で利回りを計算するのが慣行だが、試験では問題文の指示に従うこと。

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、みずほ証券、SMBC日興証券</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0411_債券価格_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
