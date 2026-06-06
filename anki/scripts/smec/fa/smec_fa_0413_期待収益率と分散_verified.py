"""
期待収益率と分散の計算（好況・普通・不況シナリオ） - 中小企業診断士 財務会計
Expected Return & Variance

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740926401
DECK_ID = 1740926402

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_期待収益率と分散',
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
    '中小企業診断士_財務会計::04_ファイナンス::期待収益率と分散'
)

# カード内容
question = """好況・普通・不況の各シナリオにおける期待収益率と分散・標準偏差の計算式・計算例を答えよ"""

answer = """<b>Expected Return & Variance</b>（期待収益率と分散）

<b>期待収益率</b>（確率加重平均）:
<div class="formula">
\\[E(r) = \\sum_{i=1}^{n} p_i \\times r_i\\]
</div>

<b>分散</b>:
<div class="formula">
\\[\\sigma^2 = \\sum_{i=1}^{n} p_i \\times (r_i - E(r))^2\\]
</div>

<b>標準偏差</b>:
<div class="formula">
\\[\\sigma = \\sqrt{\\sigma^2}\\]
</div>

<b>計算例</b>:
<table>
<tr><th>経済状態</th><th>確率 \\(p_i\\)</th><th>収益率 \\(r_i\\)</th></tr>
<tr><td>好況</td><td>0.3</td><td>20%</td></tr>
<tr><td>普通</td><td>0.5</td><td>10%</td></tr>
<tr><td>不況</td><td>0.2</td><td>-5%</td></tr>
</table>

<b>Step 1: 期待収益率</b>
<div class="formula">
\\[E(r) = 0.3 \\times 20\\% + 0.5 \\times 10\\% + 0.2 \\times (-5\\%) = 6 + 5 - 1 = 10\\%\\]
</div>

<b>Step 2: 分散</b>
<div class="formula">
\\[\\sigma^2 = 0.3(20-10)^2 + 0.5(10-10)^2 + 0.2(-5-10)^2\\]
\\[= 0.3 \\times 100 + 0 + 0.2 \\times 225 = 30 + 45 = 75 \\text{ (%²)}\\]
</div>

<b>Step 3: 標準偏差</b>
<div class="formula">
\\[\\sigma = \\sqrt{75} \\approx 8.66\\%\\]
</div>

<div class="important">注意:</div>
<ul>
<li>分散の計算では「<b>偏差の2乗 × 確率</b>」を合計する（単なる平均ではない）</li>
<li><b>標準偏差</b>がリスクの指標として使われる</li>
<li>試験では確率の合計が1になることを必ず確認</li>
</ul>

<div class="source">出典: 一発合格まとめシート H29第16問、Wall Street Prep</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0413_期待収益率と分散_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
