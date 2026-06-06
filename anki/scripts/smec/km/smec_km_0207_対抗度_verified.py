"""
Ankiカード: 既存競争業者間の対抗度（差別化の文脈）
科目: 中小企業診断士_企業経営理論
セクション: 02_競争戦略
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS_NO_TABLE

# モデル定義
model_id = 1702070001
deck_id = 1702070002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_対抗度',
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
    css=CARD_CSS_NO_TABLE
)

my_deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::02_競争戦略::対抗度'
)

# カード内容
question = '''ポーターの5フォース分析における「既存競争業者間の対抗度」の定義と、対抗度が<span class="important">高まる条件</span>、および<span class="important">差別化戦略との関係</span>を答えよ'''

answer = '''<b>Rivalry Among Existing Competitors</b>（既存競争業者間の対抗度）

<p>ポーターの5つの競争要因（Five Forces）の一つ。業界内の既存企業同士の競争の激しさを示す。</p>

<div class="formula">
<b>対抗度が高まる（競争が激化する）条件:</b><br>
・同規模の競合が多数存在する<br>
・業界の成長率が低い<br>
・固定費・在庫コストが高い<br>
・<span class="important">製品の差別化が乏しい（スイッチングコストが低い）</span><br>
・撤退障壁が高い
</div>

<div class="example">
<b>差別化戦略との関係:</b><br>
製品差別化は、競合との直接的な価格競争を<b>回避</b>し、自社独自の市場を構築する手段となる。差別化によりブランドロイヤルティが高まると、スイッチングコストが上昇し、対抗度（rivalry）は<b>低下</b>する。<br><br>
逆に、差別化製品と標準製品の機能差が縮小すると、顧客忠誠度が低下し、対抗度が再び高まるリスクがある。
</div>

<p><b>注意</b>: 差別化戦略は既存企業間の対抗度だけでなく、買い手の交渉力・新規参入の脅威・代替品の脅威にも影響する。ただし代替品の出現に対しては差別化の効果が限定的である点に注意。</p>

<div class="source">出典: M.E.ポーター『競争の戦略』、スタディング 中小企業診断士 H29第7問解説、NRI ポーターの5フォース</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0207_対抗度_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
