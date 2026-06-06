"""
Ankiカード: VRIO分析
科目: 中小企業診断士_企業経営理論
セクション: 02 競争戦略
作成日: 2026-03-13
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390202
DECK_ID = 1610390202

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_VRIO分析',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::02_競争戦略::VRIO分析')

# --- カード ---
question = """VRIO分析の4つの問いと評価結果、模倣困難性の要因を答えよ"""

answer = """<b>VRIO Framework</b>（バーニー, 1991）— RBVの分析ツール

経営資源を<b>V→R→I→Oの順</b>に評価し、競争優位の程度を判定する:

<b>① Value（経済価値）</b>: 機会を活かし脅威に対応できるか？
→ No → <b>競争劣位</b>

<b>② Rarity（希少性）</b>: その資源を持つ企業は少数か？
→ No → <b>競争均衡</b>（他社と同等）

<b>③ Inimitability（模倣困難性）</b>: 他社が模倣するコストは高いか？
→ No → <b>一時的な競争優位</b>

<b>④ Organization（組織）</b>: 資源を活用する組織体制が整っているか？
→ No → 持続的競争優位の<b>未実現</b>（宝の持ち腐れ）
→ Yes → <b>持続的な競争優位</b>

<div class="formula">
<b>模倣困難性を生む4つの要因:</b><br>
1. <b>歴史的経路依存性</b>: 長年の蓄積で形成され、時間を巻き戻せない（時間圧縮の不経済性）<br>
2. <b>因果曖昧性</b>: なぜ成功しているか外部から分からない（ブラックボックス）<br>
3. <b>社会的複雑性</b>: チームワーク・組織文化・取引先との関係性など、複雑すぎて模倣困難<br>
4. <b>特許</b>: 法的に模倣が制約される
</div>

<div class="example">
<b>具体例（トヨタ生産方式）:</b><br>
V=Yes（コスト削減・品質向上）、R=Yes（他社にない仕組み）、I=Yes（長年の改善文化＝歴史的経路＋社会的複雑性）、O=Yes（全社的に組織化）→ 持続的競争優位
</div>

<div class="important">評価は必ず<b>V→R→I→Oの順</b>。Oが欠けると資源があっても優位性を実現できない。R2第1問、R5第2問等で出題。</div>

<div class="source">出典: Barney『Gaining and Sustaining Competitive Advantage』, たかぴーの中小企業診断士試験 攻略ブログ</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0202_VRIO分析_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
