"""
Ankiカード: 多角化4分類の選択シーン
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703050001
deck_id = 1703050002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_多角化選択シーン',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::多角化の選択シーン'
)

# カード内容
question = '''多角化の4分類（水平型・垂直型・集中型・集成型）は、それぞれ<span class="important">どのようなシーンで選択すべきか</span>、選択条件と企業例を答えよ'''

answer = '''<b>Diversification Strategy - Selection Criteria</b>（多角化戦略の選択基準）

<p>自社の経営資源・期待するシナジー・リスク許容度に応じて選択する。</p>

<div class="formula">
<table>
<tr><th>分類</th><th>選択すべきシーン</th><th>期待するシナジー</th></tr>
<tr><td><b>水平型</b></td><td>既存の技術・販売網を活かして<b>同一顧客層</b>に新製品を投入したい時</td><td>販売・生産シナジー</td></tr>
<tr><td><b>垂直型</b></td><td>バリューチェーンの<b>川上/川下を内製化</b>し、コスト削減・品質管理を強化したい時</td><td>生産・投資シナジー</td></tr>
<tr><td><b>集中型</b></td><td>既存技術に強みがあり、それを<b>異なる市場に転用</b>したい時</td><td>投資シナジー</td></tr>
<tr><td><b>集成型</b></td><td>既存事業の<b>リスク分散</b>が最優先で、新たな収益源を確保したい時</td><td>低い（経営シナジー程度）</td></tr>
</table>
</div>

<div class="example">
<b>企業例:</b><br>
・<b>水平型</b>: 本田技研（バイク→自動車）― 既存のエンジン技術と販売網を活用<br>
・<b>垂直型</b>: ユニクロ（企画〜製造〜販売のSPA）― 川上から川下まで一貫統合<br>
・<b>集中型</b>: 富士フイルム（フィルム技術→化粧品・医療機器）― 技術の同心円的展開<br>
・<b>集成型</b>: ソニー（電機→音楽・金融・保険）― 業種にこだわらない事業ポートフォリオ構築
</div>

<p><b>注意</b>: 中小企業の場合、経営資源が限られるため、まず水平型・集中型のようにシナジーが高い類型から着手し、段階的にリスクの高い多角化へ進むことが望ましい。集成型は資金力・経営力のある大企業向きの戦略である。</p>

<div class="source">出典: BCJ 多角化戦略4つの型、日本M&Aセンター、NRI</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0305_多角化の選択シーン_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
