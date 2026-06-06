"""
Ankiカード: ESG・SDGs・インパクト投資・コーポレートガバナンス
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略（ドメイン・全社戦略）
作成日: 2026-03-20
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1701030101
deck_id = 1701030102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_ESG_SDGs',
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
    '中小企業診断士_企業経営理論::01_経営戦略::ESG_SDGs'
)

question = '''<span class="important">ESG・SDGs・インパクト投資・コーポレートガバナンス</span>の定義と関係を答えよ'''

answer = '''<b>ESG, SDGs &amp; Corporate Governance</b>

<div class="formula">
<b>関係の全体像:</b><br><br>
<b>SDGs</b>（国際社会の目標）<br>
　↓ 企業活動の指針として<br>
<b>CSR/CSV</b>（企業の取り組み）<br>
　↓ 投資家が評価する基準として<br>
<b>ESG</b>（評価の3観点）<br>
　↓ 投資手法として<br>
<b>ESG投資</b> → さらに発展 → <b>インパクト投資</b>
</div>

<div class="formula">
<table>
<tr><th>用語</th><th>誰の視点</th><th>定義</th><th>ポイント</th></tr>
<tr><td><b>SDGs</b><br>Sustainable Development Goals</td><td><b>国際社会</b></td><td>国連の持続可能な開発目標（17目標）</td><td>2030年期限。企業・国・個人すべてが対象</td></tr>
<tr><td><b>ESG</b><br>Environment, Social, Governance</td><td><b>投資家</b></td><td>環境・社会・ガバナンスで企業を評価</td><td>財務情報<b>以外</b>の判断基準</td></tr>
<tr><td><b>インパクト投資</b><br>Impact Investing</td><td><b>投資家</b></td><td>財務リターン＋社会的インパクトの両方を追求</td><td>ESG投資との違い: 社会的成果を<b>測定・報告</b></td></tr>
<tr><td><b>コーポレートガバナンス</b><br>Corporate Governance</td><td><b>企業統治</b></td><td>経営の透明性・公正性を確保する仕組み</td><td>ESGの「<b>G</b>」に該当</td></tr>
</table>
</div>

<div class="formula">
<b>ESGの3要素と具体例:</b>
<table>
<tr><th>E（環境）</th><th>S（社会）</th><th>G（ガバナンス）</th></tr>
<tr><td>CO2削減</td><td>労働環境改善</td><td>社外取締役の設置</td></tr>
<tr><td>再生可能エネルギー</td><td>ダイバーシティ</td><td>情報開示の透明性</td></tr>
<tr><td>廃棄物削減</td><td>人権配慮</td><td>内部統制・監査</td></tr>
</table>
</div>

<div class="example">
<b>試験での引っかけパターン:</b><br>
・「ESGは企業が自主的に取り組む活動」→ <b>×</b> ESGは<b>投資家側の評価基準</b>（企業の取り組みはCSR）<br>
・「SDGsは企業のみを対象とした目標」→ <b>×</b> <b>国・企業・個人すべて</b>が対象<br>
・「インパクト投資は財務リターンを犠牲にする」→ <b>×</b> 財務リターンと社会的インパクトの<b>両立</b><br>
・「コーポレートガバナンスはCSRの一部」→ <b>△</b> 独立概念だが、ESGのG要素でもある
</div>

<div class="source">出典: 国連SDGs、PRI（責任投資原則）、中小企業診断士試験</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0103_ESG_SDGs_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
