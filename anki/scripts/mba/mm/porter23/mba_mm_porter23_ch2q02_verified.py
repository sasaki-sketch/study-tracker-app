import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

# model_id_base(1702010100) + question_index(5) = 1702010105
MODEL_ID = 1702010105
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

question_html = """<div style="font-size:14px; color:#888; margin-bottom:8px;">porter23 Ch2 Q2</div>
どうすれば業界構造分析と戦略基本パターンをつなげることができるのか"""

answer_html = """<b>BCGのアドバンテージマトリクスの活用が有効。</b><br><br>

<b>切り口1: 4象限 → 戦略基本パターンの当てはめ（図表14）</b><br>
・規模型事業 → コストリーダーシップが成功の条件<br>
・特化型事業 → コストリーダーシップ or 差別化が成功の条件<br>
・分散型事業 → 差別化が成功の条件<br>
・手詰まり型事業 → 成功の条件がない<br><br>

<b>切り口2: 市場ライフサイクル → マトリクスの変遷（図表15）</b><br>
・導入期 → 分散型事業（プレイヤーが散在）<br>
・成長期 → 勝負軸で分岐:<br>
　　単一の勝負軸 → 規模型事業へ<br>
　　複数の勝負軸 → 特化型事業へ<br>
・成熟期 → 規模型 or 特化型が定着<br>
・衰退期 → 市場縮小<br>

<div class="example">
<b>補足</b><br>
手詰まり型は「成功の条件がない」不健全な状態であり、ライフサイクル上の正常な段階ではない。手詰まり型に陥った場合、競争軸を再定義して特化型へ移行することが脱出策となる。これが次問（Q3）の「熾烈なシェア争いからの脱却」につながる。
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第2章「なぜ『競争の戦略』を使いこなせないのか」
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

script_dir = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mm/porter23/'
output_path = f'{script_dir}mba_mm_porter23_ch2q02_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
