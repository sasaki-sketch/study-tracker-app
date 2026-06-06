"""
リスクプレミアム - 中小企業診断士 財務会計
Risk Premium

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740823901
DECK_ID = 1740823902

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_リスクプレミアム',
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

# デッキ定義
deck = genanki.Deck(
    DECK_ID,
    '中小企業診断士_財務会計::04_ファイナンス::リスクプレミアム'
)

# カード内容
question = """リスクプレミアムの定義・種類・CAPMでの使われ方を答えよ"""

answer = """<b>Risk Premium</b>（リスクプレミアム）

<b>定義</b>: リスク資産の期待収益率から無リスク利子率を差し引いた差。投資家がリスクを引き受ける対価として要求する追加的リターン。

<div class="formula">
\\[\\text{リスクプレミアム} = \\text{リスク資産の期待収益率} - R_f\\]
</div>

<b>主な種類</b>:
<table>
<tr><th>種類</th><th>意味</th><th>目安</th></tr>
<tr><td>マーケットリスクプレミアム（MRP）</td><td>市場ポートフォリオの期待収益率 − \\(R_f\\)</td><td>日本: 4〜6%、米国: 6〜8%</td></tr>
<tr><td>エクイティリスクプレミアム</td><td>株式投資に対するリスクプレミアム</td><td>MRPとほぼ同義で使われることが多い</td></tr>
<tr><td>サイズプレミアム</td><td>小型株が大型株より高いリターンを示す追加プレミアム</td><td>実務ではイボットソンデータを使用</td></tr>
</table>

<b>CAPMでの使われ方</b>:
<div class="formula">
\\[R_e = R_f + \\beta \\times \\underbrace{(R_m - R_f)}_{\\text{MRP}}\\]
</div>

<ul>
<li>\\(\\beta\\): 個別株式の市場に対する感応度（\\(\\beta = 1\\)で市場と同じリスク）</li>
<li>\\(\\beta \\times MRP\\): その株式<b>固有のリスクプレミアム</b></li>
</ul>

<div class="important">注意:</div>
MRPの推定にはヒストリカル法（過去のTOPIX利回り − 国債利回り）が一般的。試験ではMRPの値は問題文で与えられることが多い。

<div class="source">出典: グロービス経営大学院、野村證券、SMBC日興証券</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0405_リスクプレミアム_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
