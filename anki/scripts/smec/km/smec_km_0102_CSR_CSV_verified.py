"""
Ankiカード: CSR・CSV・フィランソロフィー・メセナ
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略（ドメイン・全社戦略）
作成日: 2026-03-20
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1701020101
deck_id = 1701020102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_CSR_CSV',
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
    '中小企業診断士_企業経営理論::01_経営戦略::CSR_CSV'
)

question = '''<span class="important">CSR・CSV・フィランソロフィー・メセナ</span>の定義・包含関係・違いを答えよ'''

answer = '''<b>Corporate Social Responsibility &amp; Related Concepts</b>

<div class="formula">
<b>包含関係:</b><br><br>
CSR（企業の社会的責任）<br>
　├─ <b>CSV</b>（本業で社会課題解決）<br>
　└─ <b>フィランソロフィー</b>（本業外の慈善活動）<br>
　　　└─ <b>メセナ</b>（文化・芸術支援に限定）
</div>

<div class="formula">
<table>
<tr><th>用語</th><th>本業との関係</th><th>利益との関係</th><th>具体例</th></tr>
<tr><td><b>CSR</b><br>Corporate Social Responsibility</td><td>本業＋本業外</td><td>直接の利益は問わない</td><td>環境配慮、法令遵守、地域貢献全般</td></tr>
<tr><td><b>CSV</b><br>Creating Shared Value</td><td><b>本業そのもの</b></td><td><b>利益と社会価値を同時に</b></td><td>トヨタのHV開発、ネスレの途上国農家支援</td></tr>
<tr><td><b>フィランソロフィー</b><br>Philanthropy</td><td><b>本業外</b></td><td>見返りを求めない</td><td>災害義援金、ボランティア派遣</td></tr>
<tr><td><b>メセナ</b><br>Mécénat（仏語）</td><td><b>本業外</b></td><td>見返りを求めない</td><td>美術館運営、音楽コンサート協賛</td></tr>
</table>
</div>

<div class="example">
<b>試験での引っかけパターン:</b><br>
・「CSVは利益を犠牲にして社会貢献する活動」→ <b>×</b> CSVは利益と社会価値の<b>両立</b><br>
・「メセナはスポーツ支援を含む」→ <b>×</b> メセナは<b>文化・芸術</b>限定（スポーツはフィランソロフィー）<br>
・「CSRの一環としてCSVがある」→ <b>○</b> CSVはCSRの<b>発展形</b><br>
・「フィランソロフィーは本業を通じた社会貢献」→ <b>×</b> 本業を通じるのは<b>CSV</b>
</div>

<div class="source">出典: M.E.ポーター&amp;クラマー(2011)「CSV」、中小企業診断士試験</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0102_CSR_CSV_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
