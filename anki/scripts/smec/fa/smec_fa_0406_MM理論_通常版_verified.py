"""
MM理論（通常版・法人税なし） - 中小企業診断士 財務会計
Modigliani-Miller Theorem (Original)

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740824001
DECK_ID = 1740824002

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_MM理論_通常版',
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
    '中小企業診断士_財務会計::04_ファイナンス::MM理論_通常版'
)

# カード内容
question = """MM理論（通常版・法人税なし）の命題1〜3の内容と計算式を答えよ"""

answer = """<b>Modigliani-Miller Theorem（Original）</b>（MM理論・通常版）

1958年、モジリアーニとミラーが提唱。<b>完全資本市場</b>（法人税なし・取引コストなし・情報の対称性）を前提とする。

<b>命題1（企業価値の無関連命題）</b>:
<div class="formula">
\\[V_L = V_U\\]
資本構成が変わっても<b>企業価値は変化しない</b>
</div>

\\(V_L\\): レバレッジ企業の価値、\\(V_U\\): 無借金企業の価値

<b>命題2（株主資本コスト）</b>:
<div class="formula">
\\[r_E = r_A + (r_A - r_D) \\times \\frac{D}{E}\\]
</div>

<table>
<tr><th>記号</th><th>意味</th></tr>
<tr><td>\\(r_E\\)</td><td>株主資本コスト</td></tr>
<tr><td>\\(r_A\\)</td><td>総資本コスト（WACC、一定）</td></tr>
<tr><td>\\(r_D\\)</td><td>負債コスト</td></tr>
<tr><td>\\(D/E\\)</td><td>負債比率</td></tr>
</table>

→ 負債比率↑ → 株主資本コスト↑ だが、安い負債で調達するため<b>WACCは一定</b>

<b>命題3（投資のカットオフレート）</b>:

投資判断のハードルレートは資本構成に依存せず、<b>WACCで一意に決まる</b>（命題1・2の帰結）

<div class="important">注意:</div>
現実には法人税・倒産コスト等が存在するため、そのままでは適用できない。修正MM理論の出発点（ベンチマーク）として重要。

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、グロービス経営大学院、みずほ証券</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0406_MM理論_通常版_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
