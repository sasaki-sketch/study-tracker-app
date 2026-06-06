"""
Ankiカード: 需要の交差弾力性
科目: 中小企業診断士_企業経営理論
セクション: 08 マーケティング概論・戦略
作成日: 2026-03-14
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390805
DECK_ID = 1610390805

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_需要の交差弾力性',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::08_マーケティング概論::需要の交差弾力性')

# --- カード ---
question = """需要の交差弾力性の定義・計算式と、代替財・補完財・独立財の判定基準を答えよ"""

answer = """<b>Cross Price Elasticity of Demand</b>（需要の交差弾力性）

A財の価格変化が<b>B財の需要量</b>にどの程度影響を与えるかを測定する指標。

<div class="formula">
\\[交差弾力性 = \\frac{B財の需要量の変化率}{A財の価格の変化率}\\]
</div>

<b>判定基準（符号で財の関係を判定）:</b>

<b>① 正（プラス）→ 代替財（Substitutes）</b>
<ul>
<li>A財の価格↑ → B財の需要↑（Aの代わりにBを買う）</li>
<li>例: コーヒーの価格上昇 → 紅茶の需要増加</li>
</ul>

<b>② 負（マイナス）→ 補完財（Complements）</b>
<ul>
<li>A財の価格↑ → B財の需要↓（一緒に使うものなので両方減る）</li>
<li>例: スマホの価格上昇 → 画面保護シールの需要減少</li>
</ul>

<b>③ ゼロ → 独立財（Independent Goods）</b>
<ul>
<li>A財の価格変化がB財の需要に影響しない</li>
<li>例: カレーライスと喫茶店のコーヒー</li>
</ul>

<div class="important">試験頻出ポイント:<br>製品差別化が実現されている場合、代替品との交差弾力性は<b>小さくなる</b>（代替されにくいため）。「大きくなる」は誤り。<br>交差弾力性の<b>絶対値が大きい</b>ほど、2財の関係が強い。</div>

<div class="source">出典: Kotler『Marketing Management』, 中小企業診断士R1第31問</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0805_需要の交差弾力性_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
