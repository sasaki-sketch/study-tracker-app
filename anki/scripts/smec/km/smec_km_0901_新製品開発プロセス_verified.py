"""
Ankiカード: コトラーの新製品開発プロセス（8段階）
科目: 中小企業診断士_企業経営理論
セクション: 09_マーケティングミックス（4P）
作成日: 2026-03-20
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1709010101
deck_id = 1709010102

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_新製品開発プロセス',
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
    '中小企業診断士_企業経営理論::09_マーケティングミックス::新製品開発プロセス'
)

# カード内容
question = '''コトラーの新製品開発プロセスの<span class="important">8段階の順番と各段階の内容</span>を答えよ'''

answer = '''<b>New Product Development Process</b>（新製品開発プロセス）

<p>コトラー（Kotler）が提唱した8段階のプロセス:</p>

<div class="formula">
<table>
<tr><th>#</th><th>段階</th><th>英語</th><th>内容</th></tr>
<tr><td>1</td><td><b>アイデア創出</b></td><td>Idea Generation</td><td>社内外からアイデアを収集（シーズ発想/ニーズ発想）</td></tr>
<tr><td>2</td><td><b>アイデア・スクリーニング</b></td><td>Idea Screening</td><td>アイデアを評価・絞り込み。ドロップエラー/ゴーエラーを最小化</td></tr>
<tr><td>3</td><td><b>コンセプトの開発とテスト</b></td><td>Concept Dev. &amp; Testing</td><td>アイデアを消費者視点で具体化し、ターゲット消費者の反応を調査</td></tr>
<tr><td>4</td><td><b>マーケティング戦略の立案</b></td><td>Marketing Strategy Dev.</td><td>ターゲット市場、価格・流通戦略、長期目標を策定</td></tr>
<tr><td>5</td><td><b>事業性の分析</b></td><td>Business Analysis</td><td>売上・コスト・利益を予測し採算性を評価</td></tr>
<tr><td>6</td><td><b>製品開発</b></td><td>Product Development</td><td>コンセプトをプロトタイプ（試作品）に変換。ここで初めて物理的製品が存在</td></tr>
<tr><td>7</td><td><b>市場テスト</b></td><td>Market Testing</td><td>限定市場で実際に販売し反応を検証</td></tr>
<tr><td>8</td><td><b>市場導入</b></td><td>Commercialization</td><td>本格的に市場投入。When/Where/Howを決定</td></tr>
</table>
</div>

<div class="example">
<b>試験頻出の引っかけポイント:</b><br>
・「マーケティング戦略立案」→「事業性の分析」の順（<b>逆に出題されやすい</b>）<br>
・コンセプト・テストの段階ではまだ<b>物理的製品は存在しない</b><br>
・原典では<b>8段階</b>（コンセプト開発とテストは一体）。テキストによっては分割して9段階とする場合もある<br>
・スクリーニングの<b>ドロップエラー</b>（良いアイデアを落とす）と<b>ゴーエラー</b>（悪いアイデアを通す）
</div>

<div class="source">出典: Kotler &amp; Keller『Marketing Management』、中小企業診断士試験 R4第34問</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0901_新製品開発プロセス_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
