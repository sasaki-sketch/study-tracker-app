"""
Ankiカード: スタイル・ファッション・ファッドの違い
科目: 中小企業診断士_企業経営理論
セクション: 08 マーケティング概論・戦略
作成日: 2026-03-14
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390803
DECK_ID = 1610390803

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_スタイルファッションファッド',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::08_マーケティング概論::スタイルファッションファッド')

# --- カード ---
question = """プロダクトライフサイクルにおけるスタイル・ファッション・ファッドの違いを答えよ"""

answer = """<b>Style, Fashion, and Fad（PLCの特殊パターン）</b>

PLCの基本4段階とは異なる売上曲線を描く3つのパターン:

<b>① スタイル（Style）</b>
<ul>
<li><b>波状に繰り返す</b>長期的なパターン</li>
<li>一度衰退しても再び人気が回復する</li>
<li>例: クラシックファッション、和食、ミッドセンチュリー家具</li>
</ul>

<b>② ファッション（Fashion）</b>
<ul>
<li><b>ある時期に広く受け入れられ、やがて衰退</b>する</li>
<li>導入→成長→成熟→衰退の一巡サイクル</li>
<li>スタイルよりも短命だが、ファッドよりは長い</li>
<li>例: ミニスカート、タピオカドリンク</li>
</ul>

<b>③ ファッド（Fad）</b>
<ul>
<li><b>急速に人気が出て、急速に消える</b>超短命パターン</li>
<li>成熟期がほとんどない（急上昇→急下降）</li>
<li>例: たまごっち、ハンドスピナー</li>
</ul>

<div class="example">
<b>試験頻出ポイント（R4第33問）:</b><br>
ファッドとスタイルの入れ替え問題に注意。<br>
スタイル=「繰り返す」、ファッド=「一瞬で消える」が区別のカギ。<br>
ファッションは両者の中間的な存在。
</div>

<div class="source">出典: Kotler『Marketing Management』, 中小企業診断士R4第33問</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0803_スタイルファッションファッド_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
