"""
Ankiカード: チャンドラーとポーターの戦略の定義
科目: 中小企業診断士_企業経営理論
セクション: 01 経営戦略（ドメイン・全社戦略）
作成日: 2026-03-13
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390107
DECK_ID = 1610390107

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_チャンドラーとポーターの戦略定義',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::01_経営戦略::チャンドラーとポーターの戦略定義')

# --- カード ---
question = """チャンドラーとポーターの戦略の定義を答えよ"""

answer = """<b>Chandler (1962) / Porter (1996) の戦略定義</b>

<table>
<tr><th></th><th>チャンドラー</th><th>ポーター</th></tr>
<tr><td><b>定義</b></td><td>企業の基本的な<b>長期目標</b>を決定し、目標達成のための<b>行動選択</b>と<b>資源配分</b>を行うこと</td><td>自社と他社の<b>差別化</b>（他社と異なる活動を行い、独自のポジションを築くこと）</td></tr>
<tr><td><b>視点</b></td><td>「<b>何をするか</b>」を計画する</td><td>「<b>何が違うか</b>」を選択する</td></tr>
</table>

<div class="important">チャンドラーは戦略を「目標→行動→資源配分」の<b>計画プロセス</b>として捉え、ポーターは<b>競争相手との違いを作ること</b>として捉えている。試験では両者の定義の入れ替え問題に注意。</div>

<div class="source">出典: Chandler『Strategy and Structure』(1962), Porter「What is Strategy?」HBR(1996)</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0107_チャンドラーとポーターの戦略定義_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
