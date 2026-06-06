"""
Ankiカード: 組織的知識創造の5つの促進要因（Enabling Conditions）
科目: 中小企業診断士_企業経営理論
セクション: 05_組織構造・組織論
作成日: 2026-03-20
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1705020001
deck_id = 1705020002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_知識創造促進要因',
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

my_deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::05_組織構造・組織論::知識創造促進要因'
)

# カード内容
question = '''野中郁次郎の知識創造理論における<span class="important">組織的知識創造の5つの促進要因（Enabling Conditions）</span>の定義・内容・それぞれの役割を答えよ'''

answer = '''<b>Organizational Knowledge Creation Enabling Conditions</b>（組織的知識創造の促進要因）

<p>野中郁次郎・竹内弘高（1995）『知識創造企業』において、SECIモデルの知識スパイラルを組織レベルで機能させるために提示した<b>5つの条件</b>:</p>

<div class="formula">
<table>
<tr><th>#</th><th>促進要因</th><th>英語</th><th>内容</th></tr>
<tr><td>1</td><td><b>意図</b></td><td>Intention</td><td>組織の戦略的方向性・ビジョン。経営者の「思い」が知識創造を方向づける</td></tr>
<tr><td>2</td><td><b>自律性</b></td><td>Autonomy</td><td>個人に行動の自由を認める。予期しない発見を可能にする（≠放任）</td></tr>
<tr><td>3</td><td><b>ゆらぎと創造的カオス</b></td><td>Fluctuation &amp; Creative Chaos</td><td>既存の認知枠組みを揺さぶる。外部環境の変化や挑戦的目標の設定</td></tr>
<tr><td>4</td><td><b>冗長性</b></td><td>Redundancy</td><td>当面不要な情報を意図的に重複共有。共通の認知基盤を形成し暗黙知共有を促進</td></tr>
<tr><td>5</td><td><b>最小有効多様性</b></td><td>Requisite Variety</td><td>組織内部に環境と同程度の多様性を確保（アシュビーの法則）。多様な視点・経験で複雑な環境に対応</td></tr>
</table>
</div>

<div class="example">
<b>冗長性 vs 最小有効多様性（頻出混同ポイント）:</b>
<table>
<tr><th>観点</th><th>冗長性（Redundancy）</th><th>最小有効多様性（Requisite Variety）</th></tr>
<tr><td><b>焦点</b></td><td>情報の<b>重なり</b></td><td>情報・能力の<b>広がり</b></td></tr>
<tr><td><b>イメージ</b></td><td>同じことをみんなが知っている</td><td>違うことをみんなが知っている</td></tr>
<tr><td><b>目的</b></td><td>共通の認知基盤→暗黙知共有</td><td>環境の複雑性への対応力</td></tr>
<tr><td><b>促進SECI</b></td><td>共同化(S)・表出化(E)</td><td>連結化(C)</td></tr>
<tr><td><b>具体例</b></td><td>他部門の業務内容を全員が把握</td><td>複数の役割経験、多様な専門チーム</td></tr>
</table>
</div>

<p><b>注意:</b> 試験では促進要因を「阻害する」と逆に記述する引っかけが頻出。「自律性を与えると統制が取れなくなるので阻害」「冗長な情報共有はコミュニケーション混乱を招くので阻害」等はいずれも<b>誤り</b>。5つはすべて知識創造を<b>促進</b>する要因である。</p>

<div class="source">出典: 野中郁次郎・竹内弘高『知識創造企業 (The Knowledge-Creating Company)』(1995)、中小企業診断士試験 R4第10問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0502_知識創造促進要因_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
