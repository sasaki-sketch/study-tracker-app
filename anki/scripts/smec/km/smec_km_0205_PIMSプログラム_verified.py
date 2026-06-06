"""
Ankiカード: PIMSプログラム
科目: 中小企業診断士_企業経営理論
セクション: 02 競争戦略
作成日: 2026-03-14
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# --- モデル定義 ---
MODEL_ID = 1710390205
DECK_ID = 1610390205

model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_企業経営理論_PIMSプログラム',
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
deck = genanki.Deck(DECK_ID, '中小企業診断士_企業経営理論::02_競争戦略::PIMSプログラム')

# --- カード ---
question = """PIMSプログラムの概要と主要な研究結果を答えよ"""

answer = """<b>PIMS: Profit Impact of Market Strategy</b>（市場戦略の利益効果）

1960年代にGE（ゼネラル・エレクトリック）社内で開始、1970年代にハーバード・ビジネススクールに引き継がれた<b>実証研究プロジェクト</b>。多様な業界の約600のSBU（戦略事業単位）のデータを分析し、事業の収益性を左右する要因を特定した。

<b>主要な研究結果:</b>

<b>① 市場シェアとROIの正の相関</b>
<ul>
<li>市場シェアに<b>10%の差</b>があると、税引前ROIに平均<b>5%の差</b>が生じる</li>
<li>シェアが高いほど収益性が高い傾向</li>
</ul>

<b>② 業績を規定する主要因（重要度順）</b>
<ul>
<li>投資集中度、生産性、<b>市場地位</b>、対象市場の成長性、<b>製品・サービスの質</b>など9つ</li>
</ul>

<b>③ 市場シェアと知覚品質は連動する</b>
<ul>
<li>両者は対立するものではなく、<b>双方が収益性向上に貢献</b>する</li>
</ul>

<b>④ ビルド戦略のジレンマ</b>
<ul>
<li>シェアを伸ばす局面は短期的にコスト増 → 同じシェア帯で「維持」する場合よりROIが低い傾向</li>
</ul>

<div class="important">試験頻出ポイント（R2第4問）:<br>「市場シェアと品質の追求は両立できない」→ <b>誤り</b>。PIMSではシェアと知覚品質は連動し、両立する。<br>PIMSは<b>実証研究</b>に基づく点がポーターの理論的フレームワークとの違い。</div>

<div class="source">出典: Buzzell & Gale『The PIMS Principles』, DHBR「PIMS: ROIは市場シェアに従う」, 中小企業診断士R2第4問</div>"""

note = genanki.Note(model=model, fields=[question, answer])
deck.add_note(note)

# --- パッケージ出力 ---
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0205_PIMSプログラム_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
