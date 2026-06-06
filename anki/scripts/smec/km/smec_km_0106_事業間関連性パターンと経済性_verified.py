"""
Ankiカード: 事業間関連性パターン（集約型・拡散型）と経済性
科目: 中小企業診断士_企業経営理論
セクション: 01 経営戦略（ドメイン・全社戦略）
作成日: 2026-03-13
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390106
DECK_ID = 1610390106

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_事業間関連性パターン',
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

# --- デッキ定義 ---
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::01_経営戦略::事業間関連性パターンと経済性')

# --- カード ---
question = """企業ドメインにおける事業間関連性パターン（集約型・拡散型）の特徴・対応する経済性・具体例を答えよ"""

answer = """<b>Concentrated Domain / Diffuse Domain</b>（集約型ドメイン / 拡散型ドメイン）

<table>
<tr><th></th><th>集約型</th><th>拡散型</th></tr>
<tr><td><b>事業間の関連性</b></td><td>強い</td><td>弱い</td></tr>
<tr><td><b>経営資源の利用密度</b></td><td>高い</td><td>低い</td></tr>
<tr><td><b>重視する経済性</b></td><td>範囲の経済<br>(Economies of Scope)</td><td>成長の経済<br>(Economies of Growth)</td></tr>
<tr><td><b>メリット</b></td><td>収益性が高い</td><td>リスク分散</td></tr>
<tr><td><b>具体例</b></td><td><b>キヤノン</b>: 光学技術を軸にカメラ→複合機→医療機器<br><b>富士フイルム</b>: フィルム技術を化粧品・医薬品に展開</td><td><b>ソフトバンク</b>: 通信・Yahoo・投資ファンド・プロ野球<br><b>GE</b>: 航空エンジン・発電・金融・医療</td></tr>
</table>

<ul>
<li><b>範囲の経済</b>: 複数事業で経営資源（技術・ブランド・流通網等）を<b>共有</b>→コスト削減。集約型の経済的根拠</li>
<li><b>成長の経済</b>: 事業間の関連が低くても<b>成長機会の拡大</b>とリスク分散を追求。拡散型の経済的根拠</li>
<li><b>規模の経済（Economies of Scale）</b>: 同一事業内で<b>生産量を拡大</b>→単位コスト低下（←事業ドメインレベルの概念）</li>
</ul>

<div class="important">試験では集約型＝範囲の経済、拡散型＝成長の経済の対応が頻出。「規模の経済」は多角化ではなく単一事業の量的拡大の話であり混同に注意。</div>

<div class="source">出典: 榊原清則『企業ドメインの戦略論』（中公新書, 1992）/ M&Aキャピタルパートナーズ / スタディング過去問解説</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0106_事業間関連性パターンと経済性_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
