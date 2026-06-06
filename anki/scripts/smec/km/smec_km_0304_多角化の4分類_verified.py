"""
Ankiカード: 多角化の4分類（深掘り）
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703040001
deck_id = 1703040002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_多角化4分類',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::多角化の4分類'
)

# カード内容
question = '''アンゾフの多角化戦略の4分類について、それぞれの<span class="important">技術・市場との関連性</span>、<span class="important">リスクの大小</span>、および具体的な企業例を答えよ'''

answer = '''<b>Diversification Strategy</b>（多角化戦略の4分類）

<p>アンゾフが分類した、既存事業との関連性に基づく多角化の4類型。</p>

<div class="formula">
<table>
<tr><th>分類</th><th>技術</th><th>市場</th><th>リスク</th><th>別名</th></tr>
<tr><td><b>水平型</b></td><td>関連あり</td><td>同一顧客層</td><td>低</td><td>―</td></tr>
<tr><td><b>垂直型</b></td><td>川上/川下</td><td>関連あり</td><td>中</td><td>前方的/後方的</td></tr>
<tr><td><b>集中型</b></td><td>関連あり</td><td>新規</td><td>中〜高</td><td>同心円的多角化</td></tr>
<tr><td><b>集成型</b></td><td>無関連</td><td>無関連</td><td><span class="important">最高</span></td><td>コングロマリット型</td></tr>
</table>
</div>

<div class="example">
<b>企業例:</b><br>
・<b>水平型</b>: 本田技研工業（バイク → 自動車）既存技術・同一顧客層を活用<br>
・<b>垂直型</b>: 成城石井（食品小売 → 飲食事業）川下への前方的多角化<br>
・<b>集中型</b>: 富士フイルム（フィルム技術 → 化粧品）既存技術を新市場に転用<br>
・<b>集成型</b>: 楽天（ECモール → 金融・旅行・保険）既存事業と無関連の分野へ展開
</div>

<p><b>注意</b>: 集中型多角化は「同心円的多角化」とも呼ばれ、自社の強み（技術・ノウハウ）を中心軸として同心円状に事業を拡大する。既存カードの4象限マトリクスでは多角化は1象限だが、その中にこの4類型がある点を区別すること。</p>

<div class="source">出典: NRI アンゾフの多角化戦略、中小企業庁、武蔵野コンサルティング</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0304_多角化の4分類_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
