"""
Ankiカード: ESG関連用語（統合報告書・ダイベストメント・グリーンウォッシュ・インパクト投資）
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略（ドメイン・全社戦略）
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1701060101
deck_id = 1701060102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_ESG関連用語',
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
    '中小企業診断士_企業経営理論::01_経営戦略::ESG関連用語'
)

question = '''ESG投資に関連する用語（<span class="important">統合報告書・ダイベストメント・グリーンウォッシュ・インパクト投資</span>）の定義を答えよ'''

answer = '''<b>ESG-Related Terms</b>（ESG関連用語）

<div class="formula">
<table>
<tr><th>用語</th><th>定義</th><th>ポイント</th></tr>
<tr><td><b>統合報告書</b><br>Integrated Report</td><td>従来の財務情報（売上高・資産等）に加え、<b>非財務情報</b>（温室効果ガス排出量、有給取得率、経営者報酬等）をまとめた報告書</td><td>財務諸表だけでは見えない企業の<b>ESGへの取り組み</b>を開示</td></tr>
<tr><td><b>ダイベストメント</b><br>Divestment</td><td>環境・社会問題への取り組みが不十分な企業の<b>株式や債券を売却</b>して圧力をかける行為</td><td>投資の<b>逆</b>（invest ↔ divest）。「投資を引き揚げる」ことで企業に行動変容を促す</td></tr>
<tr><td><b>グリーンウォッシュ</b><br>Greenwash</td><td>環境に適切な対応をしているように<b>見せかけて</b>、実態は伴っていない企業・行為</td><td>Green（環境）+ Whitewash（うわべを取り繕う）。<b>見せかけだけのエコ</b></td></tr>
<tr><td><b>インパクト投資</b><br>Impact Investing</td><td>社会・環境にポジティブなインパクトを生み出す企業に、<b>経済的リターンも求めて</b>投資する</td><td>「リターンを求めない」は<b>誤り</b>。財務リターンと社会的インパクトの<b>両立</b></td></tr>
</table>
</div>

<div class="formula">
<b>ESG投資手法の強度（弱→強）:</b><br><br>
ネガティブスクリーニング（問題企業を除外）<br>
　→ ESGインテグレーション（ESG要素を投資判断に組込み）<br>
　　→ インパクト投資（社会的成果を測定・追求）<br>
　　　→ ダイベストメント（不十分な企業から投資引揚げ）
</div>

<div class="example">
<b>試験での引っかけ:</b><br>
・「インパクト投資は経済的リターンを求めない」→ <b>×</b> <b>両立</b>が前提<br>
・「統合報告書は財務情報のみ記載」→ <b>×</b> 非財務情報（ESG指標）も<b>含む</b><br>
・「ダイベストメントは新たに投資すること」→ <b>×</b> 逆。投資を<b>引き揚げる</b>こと<br>
・「グリーンウォッシュは環境に貢献している企業」→ <b>×</b> <b>見せかけだけ</b>の企業
</div>

<div class="source">出典: 中小企業診断士試験 R6第12問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0106_ESG関連用語_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
