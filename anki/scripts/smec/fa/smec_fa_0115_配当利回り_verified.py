"""
配当利回り - 中小企業診断士 財務会計
Dividend Yield

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740825001
DECK_ID = 1740825002

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_配当利回り',
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
    '中小企業診断士_財務会計::01_経営分析::配当利回り'
)

# カード内容
question = """配当利回りの定義・計算式・配当性向との違いを答えよ"""

answer = """<b>Dividend Yield</b>（配当利回り）

<b>定義</b>: 株価に対して年間でどれだけの配当を受け取れるかを示す指標。<b>投資額に対する配当のリターン</b>を測定する。

<div class="formula">
\\[\\text{配当利回り（\\%）} = \\frac{\\text{1株当たり年間配当金}}{\\text{株価}} \\times 100\\]

例: 配当金50円、株価2,000円 → 50 ÷ 2,000 × 100 = <b>2.5%</b>
</div>

<b>目安</b>:
<table>
<tr><th>水準</th><th>判断</th></tr>
<tr><td>2%前後</td><td>全業種の中央値付近</td></tr>
<tr><td>3〜4%以上</td><td>高配当銘柄</td></tr>
</table>

<b>配当性向との違い</b>:
<table>
<tr><th>項目</th><th>配当利回り</th><th>配当性向</th></tr>
<tr><td>意味</td><td>株価に対する配当の割合</td><td>利益に対する配当の割合</td></tr>
<tr><td>計算式</td><td>配当金 ÷ <b>株価</b></td><td>配当金 ÷ <b>当期純利益</b></td></tr>
<tr><td>視点</td><td><b>投資家</b>（リターン）</td><td><b>企業</b>（利益配分）</td></tr>
</table>

<div class="important">注意:</div>
株価が下落すると配当利回りは上昇するため、高配当利回り＝優良銘柄とは限らない。業績悪化による株価下落で見かけ上の利回りが高くなっている場合がある。配当の持続可能性は配当性向と合わせて判断すること。

<div class="source">出典: 野村證券、みずほ証券、Funda Navi</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0115_配当利回り_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
