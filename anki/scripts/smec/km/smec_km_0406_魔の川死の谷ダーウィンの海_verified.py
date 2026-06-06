"""
Ankiカード: 魔の川・死の谷・ダーウィンの海
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704060001
deck_id = 1704060002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_魔の川死の谷ダーウィンの海',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::魔の川・死の谷・ダーウィンの海'
)

# カード内容
question = '''イノベーションプロセスにおける「魔の川」「死の谷」「ダーウィンの海」の<span class="important">定義・段階・乗り越え方</span>を答えよ'''

answer = '''<b>Devil's River / Valley of Death / Darwinian Sea</b>

<p>技術経営（MOT）において、研究成果が産業化に至るまでに直面する3つの障壁。</p>

<div class="formula">
基礎研究 ─[魔の川]─ 応用研究・開発 ─[死の谷]─ 事業化 ─[ダーウィンの海]─ 産業化
<br><br>
<table>
<tr><th>障壁</th><th>段階間</th><th>本質的な課題</th><th>乗り越え方</th></tr>
<tr><td><b>魔の川</b></td><td>基礎研究→応用研究</td><td>研究成果が<b>製品コンセプト</b>に結びつかない</td><td>TLO活用、産学連携</td></tr>
<tr><td><b>死の谷</b></td><td>開発→事業化</td><td>製品はあるが<b>資金・人材・体制</b>が不足</td><td>知的財産の実施権付与、外部資金調達</td></tr>
<tr><td><b>ダーウィンの海</b></td><td>事業化→産業化</td><td>市場投入後の<b>競争・淘汰</b>で生き残れない</td><td>大手とのアライアンス、ファブレス生産</td></tr>
</table>
</div>

<div class="example">
<b>具体例:</b><br>
・<b>魔の川</b>: ゴムに電気を通す技術を開発したが、商用化できる製品が見つからない<br>
・<b>死の谷</b>: 画期的なVRゴーグルを開発したが、製造工場・流通・広告費が確保できず発売に至らない<br>
・<b>ダーウィンの海</b>: 楽天モバイルが参入後、3大キャリアとの激しい競争で黒字化に苦戦
</div>

<p><b>注意</b>: 3つは順番に出現する。魔の川は「技術と市場の接続」、死の谷は「資源の壁」、ダーウィンの海は「競争の壁」と整理すると区別しやすい。ベンチャー企業だけでなく大企業の新規事業開発にも当てはまる。</p>

<div class="source">出典: JMAC 用語集、たかぴーの中小企業診断士試験攻略ブログ、三菱UFJリサーチ</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0406_魔の川死の谷ダーウィンの海_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
