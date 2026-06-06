"""
Ankiカード: ミンツバーグの戦略の定義（5つのP）
科目: 中小企業診断士_企業経営理論
セクション: 01 経営戦略（ドメイン・全社戦略）
作成日: 2026-03-13
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390108
DECK_ID = 1610390108

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_ミンツバーグの戦略5P',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::01_経営戦略::ミンツバーグの戦略5P')

# --- カード ---
question = """ミンツバーグの戦略の定義（5つのP）を答えよ"""

answer = """<b>Mintzberg's 5Ps of Strategy</b>（ミンツバーグの戦略5P, 1987）

<b>① Plan</b>（計画）: 未来に向けた方針・指針
<b>② Pattern</b>（パターン）: 過去の行動から形成された一貫性
<b>③ Position</b>（ポジション）: 市場における独自の位置づけ
<b>④ Perspective</b>（ものの見方）: 企業の理念・世界観
<b>⑤ Ploy</b>（策略）: 競合を出し抜くための計略

<div class="example">
チャンドラーの定義（計画・資源配分）→ <b>Plan</b>に相当<br>
ポーターの定義（差別化）→ <b>Position</b>に相当<br>
ミンツバーグは戦略を単一の視点で捉えず<b>多面的に定義</b>した
</div>

<div class="important">創発的戦略もミンツバーグの重要な主張。事前の計画(Plan)だけでなく、現場の行動から事後的にPatternとして戦略が形成されるという考え方。</div>

<div class="source">出典: Mintzberg「The Strategy Concept I: Five Ps for Strategy」CMR(1987), 『戦略サファリ』(東洋経済新報社, 1999)</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0108_ミンツバーグの戦略5P_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
