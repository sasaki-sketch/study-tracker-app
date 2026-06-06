"""
MM理論（修正版・法人税あり） - 中小企業診断士 財務会計
Modigliani-Miller Theorem (Modified)

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740824101
DECK_ID = 1740824102

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_MM理論_修正版',
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
    '中小企業診断士_財務会計::04_ファイナンス::MM理論_修正版'
)

# カード内容
question = """MM理論（修正版・法人税あり）の命題1〜2の内容と計算式を答えよ"""

answer = """<b>Modigliani-Miller Theorem（Modified）</b>（MM理論・修正版）

1963年に法人税を考慮して修正。負債の<b>節税効果（タックスシールド）</b>を組み込む。

<b>命題1（企業価値）</b>:
<div class="formula">
\\[V_L = V_U + t_c \\times D\\]
レバレッジ企業の価値 = 無借金企業の価値 + <b>節税効果の現在価値</b>
</div>

<table>
<tr><th>記号</th><th>意味</th></tr>
<tr><td>\\(t_c\\)</td><td>法人税率</td></tr>
<tr><td>\\(D\\)</td><td>負債額</td></tr>
<tr><td>\\(t_c \\times D\\)</td><td>節税効果の現在価値（タックスシールド）</td></tr>
</table>

→ 負債比率↑ → <b>企業価値↑</b>

<b>命題2（株主資本コスト）</b>:
<div class="formula">
\\[r_E = r_A + (r_A - r_D) \\times (1 - t_c) \\times \\frac{D}{E}\\]
</div>

→ 通常版の式に \\((1 - t_c)\\) が掛かるため、株主資本コストの上昇が<b>緩やかになる</b> → <b>WACCは負債比率↑で低下</b>

<b>通常版との比較</b>:
<table>
<tr><th>項目</th><th>通常版（税なし）</th><th>修正版（税あり）</th></tr>
<tr><td>企業価値</td><td>資本構成に無関連</td><td>負債↑ → 企業価値↑</td></tr>
<tr><td>WACC</td><td>一定</td><td>負債↑ → WACC↓</td></tr>
<tr><td>最適資本構成</td><td>存在しない</td><td>負債100%が最適（理論上）</td></tr>
</table>

<div class="important">注意:</div>
修正版では負債100%が最適となるが、現実には<b>倒産コスト（財務的困窮コスト）</b>が存在するため、節税効果と倒産コストのトレードオフで<b>最適資本構成</b>が決まる（トレードオフ理論）。

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、グロービス経営大学院、Wikipedia</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0407_MM理論_修正版_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
