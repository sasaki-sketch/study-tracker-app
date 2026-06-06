"""
Ankiカード: PPM（プロダクトポートフォリオマネジメント）
科目: 中小企業診断士_企業経営理論
セクション: 01_経営戦略
作成日: 2026-03-07
検証済み: Yes
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1709010103
model = genanki.Model(
    model_id,
    'SMEC_KM_PPM',
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
    css=CARD_CSS,
)

# デッキ定義
deck_id = 2709010103
deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::01_経営戦略::PPM',
)

# カード作成
question = 'PPM（プロダクトポートフォリオマネジメント）の定義・2軸・4象限の特徴と資源配分の方向性を答えよ'

answer = '''<b>Product Portfolio Management（PPM）</b>

<ul>
<li><b>定義</b>: BCG（ボストン・コンサルティング・グループ）が提唱した、<b>市場成長率</b>と<b>相対的市場シェア</b>の2軸で事業を4分類し、経営資源の最適配分を図るフレームワーク</li>
</ul>

<div class="formula">
<b>2軸と4象限</b>
<table>
<tr><th></th><th>市場シェア <b>高</b></th><th>市場シェア <b>低</b></th></tr>
<tr><td>成長率 <b>高</b></td><td><b>花形（Star）</b></td><td><b>問題児（Question Mark）</b></td></tr>
<tr><td>成長率 <b>低</b></td><td><b>金のなる木（Cash Cow）</b></td><td><b>負け犬（Dog）</b></td></tr>
</table>
</div>

<div class="example">
<b>各象限の特徴と戦略</b>
<ul>
<li><b>花形</b>: 売上大・投資も大 → 資金収支は均衡。シェア維持が重要</li>
<li><b>金のなる木</b>: 売上大・投資小 → <b>最大の資金源</b>。ここで得た資金を問題児へ投入</li>
<li><b>問題児</b>: 売上小・投資大 → 花形に育てるか撤退か選択が必要</li>
<li><b>負け犬</b>: 売上小・投資小 → 原則<b>撤退・縮小</b></li>
</ul>
</div>

<div class="mnemonic">
<b>PLC（プロダクトライフサイクル）との対応</b><br>
問題児（導入期）→ 花形（成長期）→ 金のなる木（成熟期）→ 負け犬（衰退期）<br><br>
新規事業は<b>問題児</b>からスタートし、シェア獲得に成功すれば<b>花形</b>へ。市場成長が鈍化すると<b>金のなる木</b>となり、さらに衰退すると<b>負け犬</b>へ移行する。
</div>

<b>注意</b>: PPMの限界として、①事業間の<b>シナジー</b>を考慮しない、②市場成長率とシェアの2軸のみで判断する<b>単純化</b>、③<b>負け犬の即撤退は短絡的</b>（他事業への貢献がありうる）が頻出。GEのビジネススクリーンはPPMの限界を補う多軸評価モデル。

<div class="source">出典: たかぴーブログ、大和総研、dyzo</div>'''

note = genanki.Note(
    model=model,
    fields=[question, answer],
)

deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0103_PPM_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f'Generated: {output_path}')
