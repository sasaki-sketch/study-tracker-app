"""
Ankiカード: MBOの実務プロセス
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-21
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703070301
deck_id = 1703070302

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_MBOプロセス',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::MBOプロセス'
)

question = '''<span class="important">MBO（Management Buy-Out）</span>の具体的な実施プロセスとスクイーズアウトの仕組みを答えよ'''

answer = '''<b>Management Buy-Out（MBO）実務プロセス</b>

<div class="formula">
<b>MBOの具体的な流れ（大正製薬の例）:</b><br><br>
① 経営陣がTOBを発表<br>
　「1株○円で買います」（市場価格より高い<b>プレミアム</b>付き）<br>
　　↓<br>
② 一般株主の大半が応じて株を売却<br>
　　↓<br>
③ 経営陣（+ファンド）が約90%以上の株式を取得<br>
　　↓<br>
④ <b>スクイーズアウト</b>（少数株主の強制排除）<br>
　　↓<br>
⑤ 株主が経営陣だけになる → <b>上場廃止</b>
</div>

<div class="formula">
<b>スクイーズアウトの2つの方法:</b>
<table>
<tr><th>方法</th><th>仕組み</th></tr>
<tr><td><b>株式等売渡請求</b></td><td>90%以上持つ株主が残りの株主に「売れ」と請求できる制度</td></tr>
<tr><td><b>株式併合</b></td><td>例:「100株→1株」に併合。1株未満の株主は強制的に現金で精算</td></tr>
</table>
</div>

<div class="example">
<b>よくある疑問:</b>
<table>
<tr><th>疑問</th><th>答え</th></tr>
<tr><td>なぜ市場価格より高く買う？</td><td>安いと株主が売ってくれない。<b>プレミアム</b>を上乗せ</td></tr>
<tr><td>お金はどこから？</td><td>自己資金＋銀行借入（LBOを併用することも多い）</td></tr>
<tr><td>なぜ上場廃止するの？</td><td>短期的な株価を気にせず<b>長期的な経営判断</b>に集中するため</td></tr>
<tr><td>再上場はできる？</td><td>できる（すかいらーく・ワールドは実際に再上場）</td></tr>
</table>
</div>

<div class="formula">
<b>日本の主なMBO事例:</b>
<table>
<tr><th>企業</th><th>年</th><th>概要</th></tr>
<tr><td>大正製薬HD</td><td>2023</td><td>創業家が約7,100億円で非公開化</td></tr>
<tr><td>ワールド</td><td>2005</td><td>上場廃止→2018年再上場</td></tr>
<tr><td>すかいらーく</td><td>2006</td><td>経営陣+ファンドでMBO→2014年再上場</td></tr>
<tr><td>ベネッセHD</td><td>2024</td><td>経営陣+EQTファンドで非公開化</td></tr>
</table>
</div>

<div class="source">出典: 会社法、中小企業診断士試験</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0307_MBOプロセス_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
