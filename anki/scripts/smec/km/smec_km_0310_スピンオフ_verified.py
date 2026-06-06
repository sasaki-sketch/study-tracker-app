"""
Ankiカード: スピンオフ・スピンアウト・カーブアウト
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703100301
deck_id = 1703100302

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_スピンオフ',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::スピンオフ'
)

question = '''<span class="important">スピンオフ・スピンアウト・カーブアウト</span>の定義と違いを答えよ'''

answer = '''<b>Spin-off, Spin-out &amp; Carve-out</b>（事業の切り出し手法）

<div class="formula">
<b>3つの違い:</b>
<table>
<tr><th></th><th>スピンオフ</th><th>スピンアウト</th><th>カーブアウト</th></tr>
<tr><td><b>英語</b></td><td>Spin-off</td><td>Spin-out</td><td>Carve-out</td></tr>
<tr><td><b>親会社との資本関係</b></td><td><b>維持する</b></td><td><b>断つ（完全独立）</b></td><td><b>外部資本を入れる</b></td></tr>
<tr><td><b>イメージ</b></td><td>子が独立するが<b>実家と繋がったまま</b></td><td>子が<b>完全に家を出る</b></td><td>子を独立させつつ<b>外部の支援者をつける</b></td></tr>
<tr><td><b>例</b></td><td>ソニー→ソニーFG（金融事業を分離、株式保有継続）</td><td>元社員が退職して技術を活かして起業</td><td>事業部を切り出してVCの出資を受けて新会社化</td></tr>
</table>
</div>

<div class="mnemonic">
<b>覚え方:</b><br><br>
親会社<br>
　├─ <b>スピンオフ</b>（紐付き）→ 親会社と資本関係<b>維持</b><br>
　├─ <b>スピンアウト</b>（紐を切る）→ <b>完全独立</b><br>
　└─ <b>カーブアウト</b>（紐＋外部の紐）→ 親会社＋<b>外部資本</b><br><br>
・Spin-<b>off</b> = offだけど<b>繋がったまま</b>離れる<br>
・Spin-<b>out</b> = outで<b>完全に外</b>に出る<br>
・<b>Carve</b>-out = Carve（彫り出す）＝事業を<b>削り出して</b>外部資本を入れる
</div>

<div class="example">
<b>試験での引っかけ:</b><br>
・「スピンオフは親会社と資本関係を断つ」→ <b>×</b> 断つのは<b>スピンアウト</b><br>
・「スピンアウトは親会社の子会社として独立」→ <b>×</b> <b>完全独立</b>（資本関係なし）<br>
・「カーブアウトは親会社だけで行う」→ <b>×</b> <b>外部資本（VC等）</b>を入れるのが特徴
</div>

<div class="source">出典: 中小企業診断士試験</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0310_スピンオフ_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
