"""
Ankiカード: クープマン目標値（下位4値: 19.3% / 10.9% / 6.8% / 2.8%）
科目: 中小企業診断士_企業経営理論
セクション: 02_競争戦略
作成日: 2026-04-23
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS_NO_TABLE

model_id = 1702100001
deck_id = 1702100002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_クープマン目標値_下位4値',
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
    '中小企業診断士_企業経営理論::02_競争戦略::クープマン目標値_下位4値'
)

question = '''<span class="important">クープマン山の下界4キャラ</span>を思い出せ。<br>　④ イクミ戦士<br>　⑤ テンキュー魔術師<br>　⑥ ロクヤ小人<br>　⑦ ニッパチスパイ<br><br>それぞれの <b>%</b> と、<b>戦略上の意味</b>は？<br><br>（Hint: 麓から頂上へ這い上がる"成り上がりナイト"を下から再生）'''

answer = '''<b>Lower 4 of Koopman's Target Values</b>（下位4値）<br>
<b>＊下から上へ（麓→頂上）の順で再生</b>

<div class="formula">
<b>⑦ ニッパチスパイ → 2.8%</b><br>
<b>【拠点目標値・橋頭堡 / Foothold Target Share】</b><br>
ニッパーで鉄条網をチョキン、冷たい金属の感触<br>
<b>意味:</b> 市場に"足場"を作る<b>最低ライン</b>。新規参入の第一目標。これ以下は存在しないのと同じ。
</div>

<div class="formula">
<b>⑥ ロクヤ小人 → 6.8%</b><br>
<b>【存在目標値・市場存在 / Presence Target Share】</b><br>
六夜（月夜）に6人でこっそり踊る、虫の声<br>
<b>意味:</b> 市場に"いること"を示す最低ライン。まだ競合からは<b>無視される</b>規模。
</div>

<div class="formula">
<b>⑤ テンキュー魔術師 → 10.9%</b><br>
<b>【影響目標値・市場認知 / Recognition Target Share】</b><br>
杖を振り "Thank you!"、金色の光で存在認知<br>
<b>意味:</b> 競合から"<b>意識される存在</b>"になる閾値。一桁台 → 二桁台は認知ジャンプ。
</div>

<div class="formula">
<b>④ イクミ戦士 → 19.3%</b><br>
<b>【上位目標値・上位グループ / Upper-Tier Target Share】</b><br>
「行くぞ幾三！」汗だく階段ダッシュ<br>
<b>意味:</b> 弱者グループの中の"<b>上位</b>"に入るライン。次は 26.1% のニロイチ豪傑（挑戦権）が見える。
</div>

<div class="example">
<b>■ 成り上がりの階段戦略</b><br>
新規参入 → <b>2.8</b> → <b>6.8</b> → <b>10.9</b> → <b>19.3</b><br>
　→ <span class="important">(壁)</span> → <b>26.1</b> でついに"影響力ある競合"へ<br>
この"壁"を越えるのが<b>弱者戦略の勝負所</b>。
</div>

<div class="example">
<b>■ シーン再生フック「下界の成り上がりナイト」</b><br>
麓でニッパチがニッパ入刀 → ロクヤが月夜に集結<br>
　→ テンキューが光で認識 → イクミが階段ダッシュ<br>
　→ 壁を越えて頂上組（ニロイチ豪傑）へ
</div>

<div class="source">出典: 田岡信夫『ランチェスター戦略』、JMR生活総合研究所、戦国マーケティング「クープマンモデルと市場シェアの科学」、シナプス マーケティング用語集</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/smec/km/smec_km_0210_クープマン目標値_下位4値_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
