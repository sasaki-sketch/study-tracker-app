"""
経済命数 - 中小企業診断士 財務会計
Economic Life

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740824501
DECK_ID = 1740824502

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_経済命数',
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
    '中小企業診断士_財務会計::03_意思決定会計::経済命数'
)

# カード内容
question = """経済命数の定義・求め方・他の耐用年数との違いを答えよ"""

answer = """<b>Economic Life</b>（経済命数 / 経済的耐用年数）

<b>定義</b>: 固定資産を使用する際の<b>年間等価コスト（EAC）が最小となる使用期間</b>。経済的に最も有利な取替タイミングを示す。

<b>求め方（EAC法）</b>:
<div class="formula">
\\[EAC = \\frac{\\text{総コストの現在価値（NPV）}}{\\text{年金現価係数}}\\]

→ EACが<b>最小となる年数</b> = 経済命数
</div>

使用年数を1年、2年、3年…と変えてEACを計算し、最小値を探す。

<b>3つの耐用年数の違い</b>:
<table>
<tr><th>種類</th><th>定義</th><th>決定方法</th></tr>
<tr><td>法定耐用年数</td><td>税法で定められた減価償却期間</td><td>法律で規定</td></tr>
<tr><td>物理的耐用年数</td><td>物理的に使用可能な期間</td><td>素材・構造で決定</td></tr>
<tr><td><b>経済命数</b></td><td><b>経済的に最適な使用期間</b></td><td><b>EAC最小化で算出</b></td></tr>
</table>

一般に: 法定 &lt; <b>経済命数</b> &lt; 物理的

<b>取替投資での使い方</b>:
<ul>
<li>旧設備のEAC vs 新設備のEAC を比較</li>
<li>新設備のEAC &lt; 旧設備のEAC → <b>取替が有利</b></li>
</ul>

<div class="important">注意:</div>
経済命数は法定耐用年数と一致するとは限らない。設備が物理的に使えても、維持費の増大や陳腐化により経済命数が先に到来することが多い。

<div class="source">出典: 知っとく会計学、中小企業診断士ブログ、ナレッジ・ハブ大学</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0307_経済命数_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
