"""
Ankiカード: 集成型多角化のメリットと選択条件
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS_NO_TABLE

# モデル定義
model_id = 1703060001
deck_id = 1703060002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_集成型多角化',
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
    css=CARD_CSS_NO_TABLE
)

my_deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::集成型多角化のメリットと選択条件'
)

# カード内容
question = '''集成型（コングロマリット型）多角化を選択する<span class="important">合理的なシーン</span>と、そのメリット・限界を答えよ'''

answer = '''<b>Conglomerate Diversification</b>（集成型多角化）

<p>既存事業と技術・市場ともに無関連な分野へ進出する多角化。4類型の中で最もリスクが高いが、特定の条件下では合理的な選択となる。</p>

<div class="formula">
<b>選択する合理的なシーン:</b><br><br>
1. <b>余剰資金が潤沢</b>: 既存事業に再投資先がなく、内部資本市場として他事業に資金を配分したい（例: GE、旧財閥系）<br><br>
2. <b>既存事業の衰退リスクが高い</b>: 本業の市場が縮小しており、異なる成長市場に活路を求める（例: JT タバコ→食品・医薬）<br><br>
3. <b>景気循環の逆相関を狙う</b>: 好不況で逆の動きをする事業を組み合わせ、収益を平準化（例: ソニー 電機＋金融・保険）
</div>

<div class="example">
<b>楽天のケースに注意:</b><br>
楽天（EC→金融・旅行・モバイル）は一見集成型だが、「楽天経済圏」として顧客データ・ブランド・決済基盤というプラットフォーム資産を共有している。厳密には顧客基盤の共有があるため、<b>集中型に近い</b>という議論もある。
</div>

<p><b>注意</b>: 集成型はシナジー効果が低いため、成功には<b>強力な経営管理能力</b>（経営シナジー）と<b>豊富な資金力</b>が不可欠。中小企業には不向きであり、大企業でも「コングロマリット・ディスカウント」（多角化しすぎて企業価値が割り引かれる現象）のリスクがある。</p>

<div class="source">出典: 日本M&Aセンター、NRI アンゾフの多角化戦略、NumberAnalytics Conglomerate Diversification</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0306_集成型多角化のメリットと選択条件_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
