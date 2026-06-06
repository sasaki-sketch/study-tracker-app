"""
Ankiカード: イノベーションのジレンマ
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704100001
deck_id = 1704100002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_イノベーションのジレンマ',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::イノベーションのジレンマ'
)

# カード内容
question = '''クリステンセンの「イノベーションのジレンマ」の定義、<span class="important">持続的・破壊的イノベーションの違い</span>、破壊的イノベーションの<span class="important">2つのタイプ</span>、およびジレンマが生じるメカニズムを答えよ'''

answer = '''<b>The Innovator's Dilemma</b>（イノベーションのジレンマ）

<p>クリステンセン（C.M. Christensen, 1997）が提唱。<b>優良企業が合理的に正しい経営判断をした結果、かえって破壊的イノベーションへの対応が遅れ、市場地位を失う</b>という逆説。</p>

<div class="formula">
<b>持続的 vs 破壊的イノベーション:</b>
<table>
<tr><th></th><th>持続的（Sustaining）</th><th>破壊的（Disruptive）</th></tr>
<tr><td><b>対象顧客</b></td><td>既存顧客</td><td>非顧客・過剰満足の下位層</td></tr>
<tr><td><b>価値提案</b></td><td>既存の価値軸で性能向上</td><td><b>従来とは異なる価値軸</b>を提示</td></tr>
<tr><td><b>初期性能</b></td><td>高い</td><td><b>低い</b>（既存製品より劣る）</td></tr>
<tr><td><b>価格</b></td><td>同等〜高い</td><td><b>安い・シンプル</b></td></tr>
</table>
<br>
<b>破壊的イノベーションの2タイプ:</b><br>
・<b>ローエンド型</b>: 既存市場の下位層を低価格で奪う（例: 格安航空LCC、QBハウス）<br>
・<b>新市場型</b>: 従来非消費だった層に新たな市場を創出（例: 初期のPC、スマホ）
</div>

<div class="example">
<b>ジレンマが生じるメカニズム:</b><br>
1. 優良企業は<b>既存顧客の声</b>を聞き、持続的イノベーションに資源を集中する（合理的判断）<br>
2. 破壊的技術は初期性能が低く、<b>既存の主要顧客が求めない</b>ため投資対象にならない<br>
3. 小規模な新興市場は<b>大企業の成長ニーズを満たせない</b>ため参入が見送られる<br>
4. 破壊的技術の性能が向上し、既存市場を侵食し始めた時には<b>手遅れ</b><br><br>

例: デジカメ登場時、コダックはフィルム事業の顧客・利益率を優先し、デジカメへの転換が遅れて経営破綻
</div>

<p><b>注意</b>: 破壊的イノベーション ≠ ラディカルイノベーション。破壊的は「既存企業の競争優位を無力化するか」という<b>市場への影響</b>で分類し、ラディカルは「技術の新規性」で分類する。技術的にはインクリメンタルでも、市場構造を破壊すれば「破壊的」となりうる。</p>

<div class="source">出典: C.M. Christensen (1997)『The Innovator's Dilemma』、GLOBIS 用語集、Coral Capital 破壊的イノベーション再考</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0410_イノベーションのジレンマ_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
