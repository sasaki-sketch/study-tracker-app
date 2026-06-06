"""
Ankiカード: クープマン目標値（概念・背景・根拠）
科目: 中小企業診断士_企業経営理論
セクション: 02_競争戦略
作成日: 2026-04-23
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS_NO_TABLE

model_id = 1702080001
deck_id = 1702080002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_クープマン目標値_概念',
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
    '中小企業診断士_企業経営理論::02_競争戦略::クープマン目標値_概念'
)

question = '''市場シェアの階段目標<span class="important">「クープマン目標値」</span>は、<b>誰が</b>・<b>何の法則を根拠に</b>・<b>どんな市場で使う</b>理論か？<br><br>（★ クープマン大陸の"7キャラ物語"の主舞台はどっちの山？）'''

answer = '''<b>Koopman's Market Share Target Values</b>（クープマン目標値）

<div class="formula">
<b>■ 誰が作ったか（系譜）</b><br>
<b>F.W.ランチェスター</b>（英・1916 空戦数式化）<br>
　↓ 第一・第二法則を提唱<br>
<b>B.O.クープマン</b>（米・WWII軍事OR）<br>
　↓ 戦力比から目標シェア導出<br>
<b>田岡信夫 × 斧田太公望</b>（日本・1960s）<br>
　↓ マーケ戦略として市場シェア理論に応用<br>
現在: 中小企業診断士・MBA競争戦略の基礎
</div>

<div class="formula">
<b>■ 根拠</b><br>
<span class="important">ランチェスター「第二法則」</span>（近代確率戦）<br>
→ 戦力差は兵力の<b>二乗</b>で効く<br>
→ 確率論から3つの閾値（73.9% / 41.7% / 26.1%）が数学的に導出される
</div>

<div class="example">
<b>■ 使う市場（★重要）</b><br>
✅ <b>成熟市場</b>（パイ固定）… シェア争いが意味を持つ ＝ <b>クープマン山</b><br>
⚠️ <b>成長市場</b>（パイ拡大）… BYD的後発参入が通用 ＝ <b>フロンティア山</b>（別ルール）<br><br>
<b>■ 主舞台</b><br>
クープマン山（成熟市場）<br>
└ 頂上のナナサンキュー大王（73.9%）から<br>
　麓のニッパチスパイ（2.8%）まで<br>
　<b>7階層の下克上物語</b>
</div>

<div class="source">出典: 田岡信夫『ランチェスター戦略』、JMR生活総合研究所マーケティング用語集、三菱UFJリサーチ&amp;コンサルティング、戦国マーケティング「クープマンモデルと市場シェアの科学」</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/smec/km/smec_km_0208_クープマン目標値_概念_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
