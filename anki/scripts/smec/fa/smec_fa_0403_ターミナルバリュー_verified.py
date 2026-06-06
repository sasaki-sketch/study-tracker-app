"""
ターミナルバリュー（継続価値）- 中小企業診断士 財務会計
Terminal Value

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394205
DECK_ID = 1709394206

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_ターミナルバリュー',
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
    '中小企業診断士_財務会計::04_ファイナンス::ターミナルバリュー'
)

# カード内容
question = """ターミナルバリュー（継続価値）の定義・計算式・ポイントを答えよ"""

answer = """<b>Terminal Value</b>（継続価値 / 残存価値）

<div class="formula">
\\[TV = \\frac{FCF_{n} \\times (1+g)}{r - g} = \\frac{FCF_{n+1}}{r - g}\\]
</div>

<table>
<tr><th>記号</th><th>意味</th></tr>
<tr><td>\\(FCF_n\\)</td><td>予測期間最終年度のFCF</td></tr>
<tr><td>\\(g\\)</td><td>永久成長率</td></tr>
<tr><td>\\(r\\)</td><td>割引率（WACC）</td></tr>
</table>

<b>定義</b>: 予測期間以降に企業が生み出す価値の現在価値（DCF法で使用）

<b>永久成長率ゼロの場合</b>: \\(TV = \\frac{FCF}{r}\\)

<div class="important">注意:</div>
<ul>
<li>企業価値全体の<b>60〜80%</b>を占めることが多い</li>
<li>計算ミスは<b>致命的</b>（全体への影響大）</li>
<li>\\(r > g\\) が必須条件（\\(r \\leq g\\) だと計算不能）</li>
</ul>

<b>DCF法での位置づけ</b>:
<div class="formula">
\\[企業価値 = \\sum_{t=1}^{n} \\frac{FCF_t}{(1+r)^t} + \\frac{TV}{(1+r)^n}\\]
</div>

<div class="source">出典: DYZO Consulting、上原FAS</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0403_ターミナルバリュー_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
