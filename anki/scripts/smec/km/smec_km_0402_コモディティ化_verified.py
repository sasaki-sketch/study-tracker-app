"""
Ankiカード: コモディティ化とモジュール型アーキテクチャ
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-20
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704020401
deck_id = 1704020402

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_コモディティ化',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::コモディティ化'
)

# カード内容
question = '''<span class="important">コモディティ化</span>の定義・発生メカニズムと、モジュール型・インテグラル型アーキテクチャとの関係を答えよ'''

answer = '''<b>Commoditization</b>（コモディティ化）

<p>製品間の差別化が失われ、<b>価格競争</b>に陥る現象。</p>

<div class="formula">
<b>製品アーキテクチャと競争の関係:</b>
<table>
<tr><th></th><th>モジュール型</th><th>インテグラル型（擦り合わせ型）</th></tr>
<tr><td><b>構造</b></td><td>部品間のインターフェースが<b>標準化</b></td><td>部品間が<b>相互依存</b>、微調整が必要</td></tr>
<tr><td><b>例</b></td><td>PC、自転車</td><td>自動車、精密機器</td></tr>
<tr><td><b>参入障壁</b></td><td><b>低い</b>（部品を組み合わせれば作れる）</td><td><b>高い</b>（擦り合わせノウハウが必要）</td></tr>
<tr><td><b>差別化</b></td><td><b>困難</b> → コモディティ化しやすい</td><td><b>容易</b> → 差別化を維持しやすい</td></tr>
<tr><td><b>競争軸</b></td><td><b>価格</b></td><td><b>品質・性能</b></td></tr>
</table>
</div>

<div class="example">
<b>コモディティ化の進行メカニズム:</b><br><br>
技術の成熟 → ドミナントデザイン確立<br>
　→ インターフェースの標準化<br>
　　→ モジュール化の進行<br>
　　　→ 新規参入増加・差別化困難<br>
　　　　→ <b>コモディティ化（価格競争）</b>
</div>

<p><b>対抗戦略:</b></p>
<ul>
<li><b>インテグラル化</b>: 擦り合わせで差別化を維持（例: トヨタ）</li>
<li><b>オープン&amp;クローズ戦略</b>: 一部をオープン（普及促進）、コアをクローズ（利益確保）</li>
<li><b>サービス化</b>: 製品に付加サービスを組み合わせ</li>
</ul>

<div class="source">出典: 中小企業診断士試験、藤本隆宏『製品アーキテクチャ論』</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0402_コモディティ化_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
