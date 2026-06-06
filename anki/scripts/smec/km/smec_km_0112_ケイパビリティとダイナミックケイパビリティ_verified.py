"""
Ankiカード: ケイパビリティとダイナミック・ケイパビリティ
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略（ドメイン・全社戦略）
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS_NO_TABLE

# モデル定義
model_id = 1701120001
deck_id = 1701120002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_ケイパビリティ',
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
    '中小企業診断士_企業経営理論::01_経営戦略::ケイパビリティとダイナミックケイパビリティ'
)

# カード内容
question = '''オーディナリー・ケイパビリティとダイナミック・ケイパビリティの定義・違い、およびティースが提唱した<span class="important">3つの能力</span>を答えよ'''

answer = '''<b>Ordinary Capability / Dynamic Capability</b>（オーディナリー・ケイパビリティ／ダイナミック・ケイパビリティ）

<p>ティース（D.J. Teece）が提唱した、企業の能力を2層に分類する概念。</p>

<div class="formula">
<b>オーディナリー・ケイパビリティ</b>（通常能力）<br>
= 「ものごとを<b>正しく行う</b>（doing things right）」能力<br>
→ 既存の経営資源を効率的に活用し、利益を最大化する能力<br>
→ ベストプラクティスとして業界内に普及しやすい<br><br>

<b>ダイナミック・ケイパビリティ</b>（動的能力）<br>
= 「<b>正しいことを行う</b>（doing the right things）」能力<br>
→ 環境変化に対応して、経営資源を統合・構築・再構成する自己変革能力<br>
→ 企業固有であり、模倣・購入が困難
</div>

<div class="example">
<b>ティースの3つの能力:</b><br><br>
1. <b>Sensing（感知）</b>: 脅威・機会を感知する能力<br>
2. <b>Seizing（捕捉）</b>: 機会を捉え、既存の資産・知識・技術を再構成して競争力を獲得する能力<br>
3. <b>Transforming（変革）</b>: 競争力を持続的にするため、組織全体を刷新・変容する能力
</div>

<p><b>注意</b>: オーディナリー・ケイパビリティは模倣可能で持続的競争優位にはなりにくい。ダイナミック・ケイパビリティは各企業の歴史・経験に根差す固有のものであり、RBV（資源ベース理論）を動的に発展させた概念である。</p>

<div class="source">出典: D.J. Teece (1997, 2007)、ドキュサイン ダイナミック・ケイパビリティ解説、やさしいビジネススクール</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0112_ケイパビリティとダイナミックケイパビリティ_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
