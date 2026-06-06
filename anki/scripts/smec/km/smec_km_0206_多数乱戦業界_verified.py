"""
Ankiカード: 多数乱戦業界（分散型事業）
科目: 中小企業診断士_企業経営理論
セクション: 02 競争戦略
作成日: 2026-03-14
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390206
DECK_ID = 1610390206

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_多数乱戦業界',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::02_競争戦略::多数乱戦業界')

# --- カード ---
question = """ポーターの多数乱戦業界（分散型事業）の定義・特徴・克服戦略を答えよ"""

answer = """<b>Fragmented Industry</b>（多数乱戦業界 / 分散型事業）— ポーター

事実上<b>大企業が存在せず</b>、多数の中小企業が競争する業界構造。規模の経済が働きにくく、優位性の構築が困難。

<b>なぜ大企業が支配できないのか（発生原因）:</b>
<ul>
<li>参入障壁が低い</li>
<li>規模の経済が効きにくい（現場の資質・個性が重要）</li>
<li>顧客ニーズが多様で標準化が困難</li>
<li>地域密着型のサービスが求められる</li>
</ul>

<b>業界の具体例:</b>
<table>
<tr><th>業界</th><th>乱戦になる理由</th></tr>
<tr><td>飲食業（そば屋・ラーメン店・居酒屋）</td><td>味・雰囲気の好みが多様、店主の腕が決め手</td></tr>
<tr><td>美容院・理容室</td><td>スタイリスト個人の技術・接客に依存</td></tr>
<tr><td>クリーニング店</td><td>地域密着、配送範囲が限定的</td></tr>
<tr><td>建設・工務店</td><td>地域ごとの許認可、現場対応力が重要</td></tr>
<tr><td>介護・福祉施設</td><td>地域密着、自治体ごとの規制、個別ケア</td></tr>
<tr><td>アパレル（小規模）</td><td>デザイナーの個性・感性に依存</td></tr>
<tr><td>学習塾・個人教室</td><td>講師の質、地域の生徒ニーズが異なる</td></tr>
</table>

<b>共通点:</b> 「人の技術・感性」「地域密着」「個別対応」が価値の源泉 → 大量生産・標準化で代替できない

<b>克服（集約化）戦略:</b>
<ul>
<li><b>フランチャイズ化</b>: チェーン展開で一括仕入れ等の規模の経済を実現（例: マクドナルド、コンビニ）</li>
<li><b>業界の統合・M&A</b>: 買収により市場を集約</li>
<li><b>特定セグメントへの集中</b>: ニッチ市場で差別化</li>
</ul>

<div class="important">試験頻出ポイント（H30第5問）:<br>「すべての活動で規模の経済性が欠如」→ <b>誤り</b>。FC等で一括仕入れの規模の経済は成立する。<br>「集約・統合戦略は適さない」→ <b>誤り</b>。多数乱戦業界でも集約化は可能。</div>

<div class="source">出典: Porter『Competitive Strategy』, 中小企業診断士H30第5問</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0206_多数乱戦業界_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
