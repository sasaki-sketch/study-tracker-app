"""
Ankiカード: ダイナミック・ケイパビリティとオーディナリー・ケイパビリティの関係
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略（ドメイン・全社戦略）
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1701130001
deck_id = 1701130002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_DCとOCの関係',
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
    '中小企業診断士_企業経営理論::01_経営戦略::DCとOCの関係'
)

# カード内容
question = '''ダイナミック・ケイパビリティ（DC）とオーディナリー・ケイパビリティ（OC）の<span class="important">強み・弱み・リスク</span>、および両者の<span class="important">関係性</span>を答えよ'''

answer = '''<b>Dynamic Capability &amp; Ordinary Capability - Relationship</b>（DCとOCの関係）

<p>両者は優劣の関係ではなく、OCが土台、DCがそれを再構成する<b>階層関係</b>にある。</p>

<div class="formula">
<table>
<tr><th></th><th>オーディナリー（OC）</th><th>ダイナミック（DC）</th></tr>
<tr><td><b>強み</b></td><td>効率性が高い、安定的な利益</td><td>環境変化に適応、持続的競争優位</td></tr>
<tr><td><b>弱み</b></td><td>模倣されやすい、環境変化に弱い</td><td>構築に時間がかかる、購入不可</td></tr>
<tr><td><b>リスク</b></td><td><span class="important">コア・リジディティ</span>（過剰最適化で硬直化）</td><td>変革を追いすぎると組織が不安定に</td></tr>
<tr><td><b>組織特性</b></td><td>堅固・効率的</td><td>柔軟・適応的</td></tr>
</table>
</div>

<div class="example">
<b>なぜ両方必要か:</b><br>
・<b>OCなしのDC</b>: 再構成する対象（土台）がなければ変革しようがない<br>
・<b>OCだけ</b>: ベストプラクティスは業界に普及し模倣される。効率を極めるほど<b>コア・リジディティ</b>（かつての強みが硬直化して足かせになる現象）に陥る<br>
・<b>DCを重視する企業はOCも同時に重視している</b>（両利きの経営に通じる）<br><br>

<b>企業規模との傾向:</b><br>
大企業はOCが高い（効率的だが硬直化リスク）、中堅・ベンチャーはDCが高い（柔軟だが基盤が弱い）
</div>

<p><b>注意</b>: ヘルファット＆ウインター（2011）は「両者の違いは本質的ではなく程度の差」と批判。OCも日常的に小さな変化に対応しており、明確な線引きは困難という学術的議論がある。2020年版ものづくり白書（経産省）は不確実性の時代にはDC強化が必要と提言。</p>

<div class="source">出典: DHBR DC論の2つの問題、データのじかん、経産省 2020年版ものづくり白書</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0113_DCとOCの関係_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
