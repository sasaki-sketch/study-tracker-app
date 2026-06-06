"""
エーベルの三次元枠組み - 中小企業診断士 企業戦略論
Abell's Three-Dimensional Framework

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

MODEL_ID = 1740928301
DECK_ID = 1740928302

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業戦略論_エーベルの三次元枠組み',
    fields=[{'name': 'Question'}, {'name': 'Answer'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="question">{{Question}}</div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
    }],
    css=CARD_CSS
)

deck = genanki.Deck(DECK_ID, '中小企業診断士_企業戦略論::01_ドメイン::エーベルの三次元枠組み')

question = """エーベルの三次元枠組みの3つの次元と具体例を答えよ"""

answer = """<b>Abell's Three-Dimensional Framework</b>（エーベルの三次元枠組み）

<b>事業ドメイン</b>を定義する標準的なフレームワーク。3つの次元で事業領域を特定する。

<table>
<tr><th>次元</th><th>問い</th><th>例（富士フイルム化粧品）</th></tr>
<tr><td><b>顧客層</b><br>Customer Groups</td><td>誰に？</td><td>40代女性</td></tr>
<tr><td><b>顧客機能</b><br>Customer Functions</td><td>何を？（ニーズ）</td><td>若々しい肌</td></tr>
<tr><td><b>技術</b><br>Technologies</td><td>どのように？</td><td>コラーゲン技術</td></tr>
</table>

<div class="important">注意:</div>
<ul>
<li>エーベルの枠組みは<b>事業ドメイン</b>の定義に使う（企業ドメインではない）</li>
<li>3次元のいずれかでセグメントを絞ることで、<b>差別的優位性</b>を構築できる</li>
<li>「誰に・何を・どのように」のセットで覚える</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、スタディング R1第1問</div>
"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

output_path = '/Users/sasaki/study_app/anki/scripts/smec/st/smec_st_0103_エーベルの三次元枠組み_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
