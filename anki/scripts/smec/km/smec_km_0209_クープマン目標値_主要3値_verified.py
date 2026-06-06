"""
Ankiカード: クープマン目標値（主要3値: 73.9% / 41.7% / 26.1%）
科目: 中小企業診断士_企業経営理論
セクション: 02_競争戦略
作成日: 2026-04-23
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS_NO_TABLE

model_id = 1702090001
deck_id = 1702090002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_クープマン目標値_主要3値',
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
    '中小企業診断士_企業経営理論::02_競争戦略::クープマン目標値_主要3値'
)

question = '''<span class="important">クープマン山の頂上3キャラ</span>を思い出せ。<br>　① ナナサンキュー大王<br>　② ヨイナ公爵<br>　③ ニロイチ豪傑<br><br>それぞれの <b>%</b> と、<b>戦略上の意味</b>は？<br><br>（Hint: 3人の上下関係を"頂上ディナー"シーンで再生）'''

answer = '''<b>Upper 3 of Koopman's Target Values</b>（主要3値）

<div class="formula">
<b>① ナナサンキュー大王 → 73.9%</b><br>
<b>【上限目標値・独占的寡占 / Upper Target Share】</b><br>
玉座で独りディナー、家臣が "Thank you!" と跪く<br>
<b>意味:</b> 残り全員束になっても届かない<b>絶対独占</b>。新規参入を事実上封鎖できるライン。
</div>

<div class="formula">
<b>② ヨイナ公爵 → 41.7%</b><br>
<b>【安定目標値・相対的安定 / Stable Target Share】</b><br>
高塔で紅茶、風が頬を撫で椅子が揺るがない<br>
<b>意味:</b> 3社以上の競合下で<b>実質トップ</b>。逆転されにくい"安定1位"の最低ライン。<br>
<span class="important">★ビジネスで「シェアNo.1」を語れる閾値★</span>
</div>

<div class="formula">
<b>③ ニロイチ豪傑 → 26.1%</b><br>
<b>【下限目標値・市場影響 / Lower Target Share】</b><br>
宴会で肉2切れ掲げ「肉一番！」と吠える<br>
<b>意味:</b> トップ争いに参加できる<b>最低ライン</b>。これを切ると"影響力ある競合"から脱落。<br>
<b>強者 vs 弱者の数学的分岐点</b>。
</div>

<div class="example">
<b>■ 数学的根拠</b><br>
ランチェスター第二法則から導出。<br>
・73.9% と 26.1% は 足すと <b>100%</b>（独占者 vs 残り全員）<br>
・41.7% は 3社均衡の破れ点（3社均等 = 33.3% を超えて安定圏へ）
</div>

<div class="example">
<b>■ シーン再生フック「頂上ディナー事件」</b><br>
頂上で大王が独食 → 塔から公爵が「良いな〜」と眺める<br>
　→ 3階層で豪傑が「肉一番！」と肉を掲げ下克上開始<br>
3人が<b>縦1本のピラミッド</b>に並ぶ
</div>

<div class="source">出典: 田岡信夫『ランチェスター戦略』、JMR生活総合研究所、戦国マーケティング「クープマンモデルと市場シェアの科学」、シナプス マーケティング用語集</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/smec/km/smec_km_0209_クープマン目標値_主要3値_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
