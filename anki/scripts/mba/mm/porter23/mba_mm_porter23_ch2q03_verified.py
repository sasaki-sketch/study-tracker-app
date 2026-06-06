import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

# model_id_base(1702010100) + question_index(6) = 1702010106
MODEL_ID = 1702010106
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

question_html = """<div style="font-size:14px; color:#888; margin-bottom:8px;">porter23 Ch2 Q3</div>
熾烈なシェア争いから脱却し、「手詰まり型事業」に陥らないためには、どうすればよいのか"""

answer_html = """<b>手詰まり型事業の原因（2つ）:</b><br>
1. コモディティ商品であること<br>
2. シェア1位の覇権争いが行われること<br><br>

<b>熾烈なシェア争いの要因:</b><br>
・成熟市場であること<br>
・差別化された競争軸が見いだせないこと<br><br>

<b>脱却方法:</b><br>
・市場の見極め: コモディティ商品か？成熟市場か？ポジション把握（クープマン目標値）<br>
・陥った場合: すぐに模倣されない、しっかりとした差別化を効かせる<br><br>

<b>クープマン目標値（図表17）:</b><br>
<table style="width:100%; border-collapse:collapse; font-size:14px; margin:8px 0;">
<tr style="background:#f0f4f8;"><td style="padding:4px; border:1px solid #d0d7de;"><b>73.9%</b></td><td style="padding:4px; border:1px solid #d0d7de;">独占的市場シェア</td><td style="padding:4px; border:1px solid #d0d7de;">完全な独占。短期的にトップが逆転されることはほとんどない</td></tr>
<tr><td style="padding:4px; border:1px solid #d0d7de;"><b>41.7%</b></td><td style="padding:4px; border:1px solid #d0d7de;">相対的安定シェア</td><td style="padding:4px; border:1px solid #d0d7de;">トップの地位はほぼ安泰。逆転される可能性は少ない</td></tr>
<tr style="background:#fff3cd;"><td style="padding:4px; border:1px solid #d0d7de;"><b>26.1%</b></td><td style="padding:4px; border:1px solid #d0d7de;">市場影響シェア</td><td style="padding:4px; border:1px solid #d0d7de;">頭ひとつ抜け出した水準。2位はトップを狙える ← <b>覇権争い</b></td></tr>
<tr style="background:#fff3cd;"><td style="padding:4px; border:1px solid #d0d7de;"><b>19.3%</b></td><td style="padding:4px; border:1px solid #d0d7de;">並列的競争シェア</td><td style="padding:4px; border:1px solid #d0d7de;">横並び状態。競争が拮抗 ← <b>覇権争い</b></td></tr>
<tr style="background:#fff3cd;"><td style="padding:4px; border:1px solid #d0d7de;"><b>10.9%</b></td><td style="padding:4px; border:1px solid #d0d7de;">市場的認知シェア</td><td style="padding:4px; border:1px solid #d0d7de;">ようやく存在が認められる水準 ← <b>覇権争い</b></td></tr>
</table>
※ 26.1%以下で覇権争いが起きやすい<br>

<div class="example">
<b>補足</b><br>
牧田氏は「手詰まり型からの脱却」の核心を、既存の競争軸上で戦うのをやめ、競争軸そのものを再定義する（新しい勝負軸を見つける）ことだとしている。単なる差別化ではなく、発想の転換が必要。これがCh3「有意差」の議論につながる。
</div>

<div class="source">
出典: 牧田幸裕『ポーターの「競争の戦略」を使いこなすための23問』第2章「なぜ『競争の戦略』を使いこなせないのか」
</div>"""

my_note = genanki.Note(model=my_model, fields=[question_html, answer_html])
my_deck.add_note(my_note)

script_dir = '/Users/sasaki/02_Personal/anki/anki/scripts/mba/mm/porter23/'
output_path = f'{script_dir}mba_mm_porter23_ch2q03_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
