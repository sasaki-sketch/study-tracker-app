"""
Ankiカード: ポジショニングアプローチとリソース・ベースド・ビュー（RBV）
科目: 中小企業診断士_企業経営理論
セクション: 02 競争戦略
作成日: 2026-03-13
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390203
DECK_ID = 1610390203

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_ポジショニングアプローチとRBV',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::02_競争戦略::ポジショニングアプローチとRBV')

# --- カード ---
question = """ポジショニングアプローチとリソース・ベースド・ビュー（RBV）の違いを答えよ"""

answer = """<b>Positioning Approach / Resource-Based View（RBV）</b>

<table>
<tr><th></th><th>ポジショニングアプローチ</th><th>リソース・ベースド・ビュー</th></tr>
<tr><td><b>提唱者</b></td><td>ポーター（Porter, 1980）</td><td>バーニー（Barney, 1991）</td></tr>
<tr><td><b>競争優位の源泉</b></td><td>企業の<b>外部環境</b>（業界構造・市場での位置づけ）</td><td>企業の<b>内部資源</b>（経営資源・ケイパビリティ）</td></tr>
<tr><td><b>問い</b></td><td>「どの業界・どのポジションを選ぶか」</td><td>「自社にどんな強みがあるか」</td></tr>
<tr><td><b>代表的フレームワーク</b></td><td>5フォース分析、3つの基本戦略</td><td>VRIOフレームワーク</td></tr>
</table>

<b>VRIOフレームワーク（RBVの分析ツール）:</b>
<ul>
<li><b>V</b>alue（経済価値）: その資源は機会を活かし脅威を無力化できるか</li>
<li><b>R</b>arity（希少性）: その資源を持つ企業は少数か</li>
<li><b>I</b>nimitability（模倣困難性）: その資源の獲得・開発コストは高いか</li>
<li><b>O</b>rganization（組織）: その資源を活用する組織体制が整っているか</li>
</ul>

<div class="example">
<b>ポジショニング例</b>: 成長市場でニッチな領域を選び参入→外部の「どこで戦うか」<br>
<b>RBV例</b>: トヨタ生産方式（TPS）は他社が簡単に模倣できない組織的ケイパビリティ→内部の「何で勝つか」
</div>

<div class="important">両者は対立概念ではなく<b>補完関係</b>。外部環境の分析（ポジショニング）と内部資源の分析（RBV）の両面から戦略を検討することが重要。R2第1問、R5第2問等で出題。</div>

<div class="source">出典: Porter『Competitive Strategy』(1980), Barney「Firm Resources and Sustained Competitive Advantage」JoM(1991), たかぴーの中小企業診断士試験 攻略ブログ</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0203_ポジショニングアプローチとRBV_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
