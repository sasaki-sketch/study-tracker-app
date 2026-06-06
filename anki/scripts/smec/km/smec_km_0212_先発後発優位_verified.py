"""
Ankiカード: 先発優位 vs 後発優位（ハタタテ開拓者 vs マネマネ猿）
科目: 中小企業診断士_企業経営理論
セクション: 02_競争戦略
作成日: 2026-04-23
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

model_id = 1702120001
deck_id = 1702120002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_先発後発優位',
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
    '中小企業診断士_企業経営理論::02_競争戦略::先発後発優位'
)

question = '''<span class="important">ハタタテ開拓者（先発）</span> vs <span class="important">マネマネ猿（後発）</span>。<br><br>それぞれの<b>戦略原理・提唱者・代表例</b>、そして<br><b>先発者失敗率とファストフォロワー成功率の衝撃的な数字</b>は？<br><br>どちらが有利という結論？'''

answer = '''<b>First-Mover Advantage vs Fast-Follower Strategy</b>

<div class="formula">
<b>① ハタタテ開拓者 → 先発優位 (First-Mover Advantage)</b><br>
<b>提唱:</b> Lieberman &amp; Montgomery（UCLA, <b>1988</b>）<br>
<b>武器:</b> 技術特許・ブランド先取り・スイッチングコスト・学習曲線<br>
<b>代表例:</b> iPhone（スマホ市場を定義）、Tesla（EV高級化）、Amazon（EC）
</div>

<div class="formula">
<b>② マネマネ猿 → 後発優位 / ファストフォロワー (Fast Follower)</b><br>
<b>武器:</b> 先発者の失敗観察 ＋ 改良投入 ＋ スケール投資<br>
<b>代表例:</b> Google（←Yahoo）、Facebook（←MySpace）、Microsoft Teams（←Slack）
</div>

<div class="example">
<b>★衝撃の実証研究★ — Golder &amp; Tellis (1993)</b><br>
500社 × 50カテゴリを分析:<br>
・先発者（Pioneer）の失敗率 <span class="important">47%</span><br>
・ファストフォロワー成功率 <span class="important">92%</span>（平均13年遅れの参入）<br><br>
→ <b>1998年、Lieberman自身が追跡研究</b>で<br>
「<b>先発は必ずしも有利ではない、むしろ危険になり得る</b>」と認める。
</div>

<div class="example">
<b>■ 使い分け（どちらが有利か？）</b>
<table>
<tr><th>先発有利な条件</th><th>後発有利な条件</th></tr>
<tr><td>・強いネットワーク効果あり<br>・特許で守れる<br>・スイッチングコスト高い<br>・学習曲線が急<br>・ブランドロイヤルティ構築可</td><td>・市場の不確実性が高い<br>・技術変化が速い<br>・模倣コストが低い<br>・先発者が失敗を晒す<br>・標準化前の混乱期</td></tr>
</table>
</div>

<div class="example">
<b>■ シーン再生フック（フロンティア山）</b><br>
<b>ハタタテ開拓者</b>が誰もいない溶岩台地に最初の旗を立てる。<br>
その様子を<b>マネマネ猿</b>が木の上から観察→改良版で超高速追い抜き。<br>
→ 平均13年後に追いつき、成功率92%で逆転。
</div>

<div class="source">出典: Lieberman &amp; Montgomery "First-Mover Advantages" (1988) &amp; "FMA: Retrospective on a Retrospective" (1998); Golder &amp; Tellis "Pioneer Advantage: Marketing Logic or Marketing Legend?" Journal of Marketing Research (1993)</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/smec/km/smec_km_0212_先発後発優位_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
