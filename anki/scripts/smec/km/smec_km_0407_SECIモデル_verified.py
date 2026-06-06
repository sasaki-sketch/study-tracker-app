"""
Ankiカード: SECIモデル
科目: 中小企業診断士_企業経営理論
セクション: 04_技術経営・イノベーション
作成日: 2026-03-16
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1704070001
deck_id = 1704070002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_SECIモデル',
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
    '中小企業診断士_企業経営理論::04_技術経営・イノベーション::SECIモデル'
)

# カード内容
question = '''野中郁次郎が提唱したSECIモデルの<span class="important">4つのプロセス</span>（暗黙知・形式知の変換）の定義と具体例を答えよ'''

answer = '''<b>SECI Model</b>（セキモデル／知識創造モデル）

<p>野中郁次郎（1990）が提唱。暗黙知と形式知の相互変換を通じて、組織的に新たな知識を創造するプロセスモデル。</p>

<div class="formula">
<table>
<tr><th>プロセス</th><th>変換</th><th>定義</th><th>具体例</th></tr>
<tr><td><b>S: 共同化</b>（Socialization）</td><td>暗黙知→暗黙知</td><td>共体験を通じて暗黙知を共有</td><td>熟練技術者の技を見て学ぶ、OJT</td></tr>
<tr><td><b>E: 表出化</b>（Externalization）</td><td>暗黙知→形式知</td><td>暗黙知を言語・図式で表現</td><td>経験則をマニュアル化、比喩で説明</td></tr>
<tr><td><b>C: 連結化</b>（Combination）</td><td>形式知→形式知</td><td>形式知を組み合わせて新知識を創造</td><td>データ分析、報告書の統合、DB構築</td></tr>
<tr><td><b>I: 内面化</b>（Internalization）</td><td>形式知→暗黙知</td><td>形式知を実践し自分のものにする</td><td>マニュアルを読んで実践、ロールプレイ</td></tr>
</table>
</div>

<div class="example">
<b>サイクルの流れ:</b><br>
共同化（体験で共有）→ 表出化（言語化）→ 連結化（体系化）→ 内面化（実践で体得）→ 再び共同化へ…<br><br>
このスパイラルが個人→グループ→組織→組織間へと拡大することで、<b>組織的知識創造</b>が実現する。<br><br>

<b>哲学的背景（ヘーゲル弁証法）:</b><br>
野中自身が『知識創造企業』第2章でヘーゲル弁証法を理論的基盤として位置づけている。暗黙知（テーゼ）と形式知（アンチテーゼ）という対立する知の相互変換を通じて、より高次の知識を生み出す構造はアウフヘーベン（止揚）に通じる。Nonaka et al. (2000) でも「知識創造の鍵は<b>弁証法的思考（dialectical thinking）</b>」と明記。
</div>

<p><b>注意</b>: 表出化（暗黙知→形式知）が最も困難かつ重要なプロセス。暗黙知は「言葉にできない知」なので、比喩・モデル・コンセプトなどを駆使して形式知に変換する必要がある。ナレッジマネジメントの基礎理論。</p>

<div class="source">出典: 野中郁次郎・竹内弘高『知識創造企業』、Nonaka et al. (2000) "SECI, Ba and Leadership"、富士フイルム SECIモデル解説</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0407_SECIモデル_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
