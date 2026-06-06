"""
Ankiカード: ハーフィンダル・ハーシュマン指数（HHI）
科目: 中小企業診断士_企業経営理論
セクション: 02 競争戦略
作成日: 2026-03-13
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390201
DECK_ID = 1610390201

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_HHI',
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

# --- デッキ定義 ---
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::02_競争戦略::HHI')

# --- カード ---
question = """ハーフィンダル・ハーシュマン指数（HHI）の定義・計算式・判断基準を答えよ"""

answer = """<b>Herfindahl-Hirschman Index（HHI）</b>

市場の<b>集中度</b>を測る指標。各企業の市場シェア（%）の<b>2乗の総和</b>。

<div class="formula">
\\[HHI = \\sum_{i=1}^{n} s_i^2\\]
\\(s_i\\): 各企業の市場シェア（%）、\\(n\\): 企業数
</div>

<ul>
<li><b>範囲</b>: 0（完全競争）〜 10,000（完全独占）</li>
<li>企業数が<b>少ない</b>ほど、シェアの<b>偏り</b>が大きいほど、HHIは高くなる</li>
</ul>

<b>公正取引委員会のセーフハーバー基準（企業結合審査）:</b>
<ul>
<li>HHI <b>1,500以下</b> → 競争上問題なし</li>
<li>HHI <b>1,500超〜2,500以下</b> かつ 増分250以下 → 問題なし</li>
<li>HHI <b>2,500超</b> かつ 増分150以下 → 問題なし</li>
</ul>

<div class="example">
<b>具体例: 飲料市場3社の比較</b><br><br>
【競争的な市場】A社 35%, B社 35%, C社 30%<br>
\\(HHI = 35^2 + 35^2 + 30^2 = 1225 + 1225 + 900 = 3{,}350\\)<br><br>
【寡占的な市場】A社 70%, B社 20%, C社 10%<br>
\\(HHI = 70^2 + 20^2 + 10^2 = 4900 + 400 + 100 = 5{,}400\\)<br><br>
→ 同じ3社でもシェアが偏るとHHIは大きく上昇する
</div>

<div class="important">単純な企業数やCR（上位集中度）と異なり、HHIはシェアの<b>偏り</b>も反映する。シェアの大きい企業ほど2乗により影響が大きくなる。</div>

<div class="source">出典: 公正取引委員会 用語解説, 統計WEB</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0201_HHI_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
