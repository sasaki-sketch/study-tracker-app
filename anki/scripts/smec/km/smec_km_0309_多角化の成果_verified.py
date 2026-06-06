"""
Ankiカード: 多角化の成果（成長性と収益性の関係）
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703090001
deck_id = 1703090002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_多角化の成果',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::多角化の成果'
)

# カード内容
question = '''多角化の程度と<span class="important">成長性・収益性の関係</span>、および関連型・非関連型の業績差を答えよ'''

answer = '''<b>Diversification and Performance</b>（多角化の成果）

<p>ルメルトや吉原英樹らの研究により、多角化の程度と企業業績の関係が明らかにされた。成長性と収益性は異なる動きをする。</p>

<div class="formula">
<b>多角化度と業績の関係:</b>
<table>
<tr><th></th><th>低い（専業・本業型）</th><th>中程度（関連型）</th><th>高い（非関連型）</th></tr>
<tr><td><b>成長性</b></td><td>低い</td><td>中</td><td><span class="important">高い</span></td></tr>
<tr><td><b>収益性</b></td><td>中</td><td><span class="important">最も高い</span></td><td>低い</td></tr>
</table>
<br>→ 多角化度が高まるほど<b>成長性は上昇</b>するが、<b>収益性は逆U字型</b>（中程度で最大、高すぎると低下）
</div>

<div class="example">
<b>なぜこうなるか:</b><br>
・<b>関連型（収益性が高い）</b>: 事業間のシナジー効果が効き、経営資源を効率的に共有できる。特に集約型は全事業がコア資源に紐づくため高収益<br>
・<b>非関連型（成長性は高いが収益性が低い）</b>: 新市場への進出で売上は伸びるが、シナジーが効きにくく、経営の複雑性が増大。コングロマリット・ディスカウント（多角化しすぎて企業価値が割り引かれる現象）も発生しうる
</div>

<p><b>注意</b>: 「多角化＝収益向上」ではない。成長性と収益性はトレードオフの関係にあり、最適な多角化度が存在する。診断士試験では「関連集約型の収益性が最も高い」というルメルトの知見が頻出。</p>

<div class="source">出典: 中小企業診断士独学攻略ブログ、一発合格まとめシート R4第1問、東大OCW 経営戦略講義資料</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0309_多角化の成果_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
