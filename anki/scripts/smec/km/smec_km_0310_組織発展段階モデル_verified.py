"""
Ankiカード: ガルブレイスとネサンソンの組織発展段階モデル
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703100001
deck_id = 1703100002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_組織発展段階モデル',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::組織発展段階モデル'
)

# カード内容
question = '''ガルブレイスとネサンソンの組織発展段階モデルにおける、<span class="important">戦略と組織構造の対応関係</span>を答えよ'''

answer = '''<b>Galbraith &amp; Nathanson's Organizational Development Stage Model</b>（組織発展段階モデル）

<p>ガルブレイスとネサンソン（1978）が『Strategy Implementation』で提唱。チャンドラーの「組織は戦略に従う」を発展させ、戦略の変化に応じた組織構造の進化を段階的に示した。</p>

<div class="formula">
<b>戦略と組織構造の対応関係:</b>
<table>
<tr><th>段階</th><th>戦略</th><th>組織構造</th><th>企業例</th></tr>
<tr><td>1</td><td>単一製品</td><td><b>単純組織</b>（社長が全て指揮）</td><td>創業期のスタートアップ</td></tr>
<tr><td>2</td><td>単一製品（規模拡大）</td><td><b>職能別組織</b>（営業部・製造部等に分化）</td><td>ヤクルト（乳酸菌飲料に特化）</td></tr>
<tr><td>3</td><td>垂直統合</td><td><b>集権的職能別組織</b>（川上〜川下を本社が集権管理）</td><td>ユニクロ（企画〜製造〜販売のSPA）</td></tr>
<tr><td>4</td><td>関連多角化</td><td><b>事業部制組織</b>（事業ごとに権限委譲）</td><td>トヨタ（自動車・金融・住宅等を事業部で運営）</td></tr>
<tr><td>5</td><td>非関連多角化</td><td><b>持株会社</b>（各事業を独立法人化、財務管理中心）</td><td>ソフトバンクG（通信・投資・AI等を子会社で展開）</td></tr>
</table>
</div>

<div class="example">
<b>職能別組織からの3つの分岐:</b><br>
・<b>垂直統合</b> → 集権的職能別組織: ユニクロのように川上〜川下を本社がコントロール<br>
・<b>関連多角化（内部成長）</b> → 事業部制: トヨタのように関連事業ごとに自律的に運営<br>
・<b>非関連多角化（買収・外部成長）</b> → 持株会社: ソフトバンクGのように無関連な事業を子会社として傘下に置く
</div>

<p><b>注意</b>: チャンドラーは「事業部制が最終形態」と結論したが、ガルブレイスとネサンソンは<b>持株会社形態</b>まで含めて発展段階を拡張した点が異なる。また、関連多角化は内部成長（自社開発）、非関連多角化は外部成長（買収）で進む傾向がある。</p>

<div class="source">出典: J.R. Galbraith &amp; D.A. Nathanson (1978)『Strategy Implementation』、一発合格まとめシート R2第17問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0310_組織発展段階モデル_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
