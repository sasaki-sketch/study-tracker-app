"""
Ankiカード: ポーターの5フォース分析
科目: 中小企業診断士_企業経営理論
セクション: 02 競争戦略
作成日: 2026-03-14
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390204
DECK_ID = 1610390204

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_5フォース分析',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::02_競争戦略::5フォース分析')

# --- カード ---
question = """ポーターの5フォース分析の5つの競争要因と、各要因が強まる条件を答えよ"""

answer = """<b>Porter's Five Forces</b>（ポーター, 1979）

業界の<b>収益性</b>を決定する5つの競争要因を分析するフレームワーク。5つの力が強いほど業界の収益性は低くなる。

<b>5つの競争要因:</b>

<b>① 業界内の競合（既存企業間の敵対関係）</b>
<ul><li>強まる条件: 同規模の競合が多数、業界の成長が遅い、固定費が高い、製品差別化が小さい、退出障壁が高い</li></ul>

<b>② 新規参入の脅威</b>
<ul><li>強まる条件: 参入障壁が低い（規模の経済が不要、資本投下が少ない、規制が緩い、スイッチングコストが低い）</li></ul>

<b>③ 代替品の脅威</b>
<ul>
<li>強まる条件: 代替品の価格性能比が高い、買い手のスイッチングコストが低い</li>
<li>例: 映画館に対する動画配信サービス</li>
</ul>

<b>④ 買い手の交渉力</b>
<ul><li>強まる条件: 買い手が少数・大口、製品が標準化されている、スイッチングコストが低い</li></ul>

<b>⑤ 売り手（供給業者）の交渉力</b>
<ul><li>強まる条件: 売り手が少数・寡占的、代替の供給源がない、自社にとって重要な資材</li></ul>

<div class="example">
<b>具体例（コンビニ業界）:</b><br>
①競合: 大手3社が激しく競争→強い ②新規参入: ブランド力・立地確保が必要→弱い ③代替品: スーパー・ネット通販→やや強い ④買い手: 消費者は多数で個々の力は弱い→弱い ⑤売り手: メーカーは多数あり→弱い
</div>

<div class="important">5フォースは<b>業界全体の収益性</b>を分析するもの（個別企業の分析ではない）。「退出障壁が高い＝競争が激化する」は頻出の引っかけポイント。</div>

<div class="source">出典: Porter『Competitive Strategy』(1980), NRI用語解説</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0204_5フォース分析_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
