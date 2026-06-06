"""
EAC（年間等価コスト） - 中小企業診断士 財務会計
Equivalent Annual Cost

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740824801
DECK_ID = 1740824802

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_EAC',
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
    '中小企業診断士_財務会計::03_意思決定会計::EAC'
)

# カード内容
question = """EAC（年間等価コスト）の定義・計算式・使い方を答えよ"""

answer = """<b>Equivalent Annual Cost</b>（EAC / 年間等価コスト / 均等年間費用）

<b>定義</b>: 投資プロジェクトの総コストの現在価値を、<b>毎年均等な年間コストに換算</b>したもの。耐用年数が異なる設備の比較に用いる。

<div class="formula">
\\[EAC = \\frac{\\text{総コストの現在価値（NPV）}}{\\text{年金現価係数}}\\]

\\[\\text{年金現価係数} = \\frac{1 - (1+r)^{-n}}{r}\\]
</div>

<b>使い方</b>:
<table>
<tr><th>場面</th><th>内容</th></tr>
<tr><td>経済命数の決定</td><td>使用年数を変えてEACを計算し、<b>最小となる年数</b> = 経済命数</td></tr>
<tr><td>異なる耐用年数の比較</td><td>耐用年数が異なる設備をEACで比較（NPVだけでは比較不可）</td></tr>
<tr><td>取替投資の判断</td><td>旧設備EAC vs 新設備EAC → 新設備EAC &lt; 旧設備EAC なら取替が有利</td></tr>
</table>

<b>計算例</b>:
設備A: 取得原価100万円、耐用年数3年、年間維持費20万円、割引率10%
<ul>
<li>総コストのNPV = 100 + 20 × 年金現価係数(3年) = 100 + 20 × 2.4869 = 149.7万円</li>
<li>EAC = 149.7 / 2.4869 = <b>60.2万円/年</b></li>
</ul>

<b>NPVとの使い分け</b>:
<table>
<tr><th>条件</th><th>使う指標</th></tr>
<tr><td>耐用年数が同じ</td><td>NPVで比較可能</td></tr>
<tr><td><b>耐用年数が異なる</b></td><td><b>EACで比較</b></td></tr>
</table>

<div class="important">注意:</div>
EACは経済命数の計算で必須のツール。NPVは耐用年数が異なる案件の比較には不向きであり、EACに換算して年間ベースで比較する必要がある。

<div class="source">出典: 知っとく会計学、中小企業診断士ブログ、過去問.com</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0308_EAC_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
