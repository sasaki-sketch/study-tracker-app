import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

# model_id_base(1702010100) + question_index(4) = 1702010104
MODEL_ID = 1702010104
# deck_id_base(2702010100) + chapter.number(2) = 2702010102
DECK_ID = 2702010102

my_model = genanki.Model(
    MODEL_ID,
    'NUCB_EMBA Textbook QA',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>'
    }],
    css=CARD_CSS
)

my_deck = genanki.Deck(
    DECK_ID,
    'NUCB_EMBA::Marketing_Management::ポーター23問::Ch2_競争の戦略'
)

question_html = """<div style="font-size:14px; color:#888; margin-bottom:8px;">porter23 Ch2 Q1</div>
なぜ『競争の戦略』は実際のビジネスの事業戦略策定で使いこなすのが非常に難しいのか"""

answer_html = """<b>結論: 知識が不十分な状態で戦略策定するからである。</b><br><br>

<b>一般的な見方（アウトプットの問題）:</b><br>
・事業計画よりも市場変化のほうが早く陳腐化してしまう<br>
・戦略立案者が現場を知らず、戦略と現場の不整合を起こす<br><br>

<b>牧田氏の主張（インプットの問題）:</b><br>
・戦略立案の基礎が不十分な状態で、応用的な戦略を立てることが根本原因<br>
・事業戦略立案の前に現状分析の手法（5Forces等）を学ぶべき<br>

<div class="example">
<b>補足</b><br>
<b>前提知識:</b> BCGのアドバンテージマトリクス（業界特性: 規模型/分散型/特化型/手詰まり型）<br><br>
<b>基本戦略策定の順序:</b><br>
1. ポジション把握（リーダー、チャレンジャー、フォロワー、ニッチャー）<br>
2. ポジショニング設定（コストリーダーシップ、差別化、集中）<br><br>
この順番で分析→戦略のプロセスを踏まないと、業界構造分析と戦略基本パターンの「接続」ができず、機能しない戦略が生まれる。<br><br>
<b>『競争の戦略』を使いこなすための2つの視点:</b><br>
1. 業界構造分析と戦略基本パターンをつなげる、具体的な「当てはめ」のし方を習得する<br>
2. どのようなポジションの企業が、どの戦略基本パターンを採るべきか明らかにする<br><br>
<b>図表12: 業界構造分析と戦略基本パターンをつなげる</b><br>
A業界の構造分析 → コストリーダーシップが成功の条件<br>
B業界の構造分析 → 差別化が成功の条件<br>
C業界の構造分析 → 集中が成功の条件<br>
※「つなげ方」「当てはめ方」がわかれば、事業戦略は機能する
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第2章「なぜ『競争の戦略』を使いこなせないのか」
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

script_dir = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mm/porter23/'
output_path = f'{script_dir}mba_mm_porter23_ch2q01_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
