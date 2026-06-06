"""
共分散（Covariance） - 中小企業診断士 財務会計
Covariance, Correlation Coefficient, Portfolio Variance

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740926701
DECK_ID = 1740926702

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_共分散',
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
    '中小企業診断士_財務会計::04_ファイナンス::共分散'
)

# カード内容
question = """共分散の定義・計算式・相関係数およびポートフォリオ分散との関係を答えよ"""

answer = """<b>Covariance</b>（共分散）

<b>定義</b>: 2つの資産の収益率が<b>どの程度同じ方向に変動するか</b>を示す指標

<b>共分散の計算式</b>:
<div class="formula">
\\[Cov(A,B) = \\sum_{i=1}^{n} p_i \\times (r_{Ai} - E(r_A)) \\times (r_{Bi} - E(r_B))\\]
</div>

<b>計算例</b>:
<table>
<tr><th>経済状態</th><th>確率</th><th>資産A収益率</th><th>資産B収益率</th></tr>
<tr><td>好況</td><td>0.5</td><td>20%</td><td>-5%</td></tr>
<tr><td>不況</td><td>0.5</td><td>0%</td><td>15%</td></tr>
</table>

\\(E(r_A) = 0.5 \\times 20 + 0.5 \\times 0 = 10\\%\\)
\\(E(r_B) = 0.5 \\times (-5) + 0.5 \\times 15 = 5\\%\\)

<div class="formula">
\\[Cov = 0.5(20-10)(-5-5) + 0.5(0-10)(15-5)\\]
\\[= 0.5 \\times 10 \\times (-10) + 0.5 \\times (-10) \\times 10 = -50 - 50 = -100\\]
</div>

→ 負の共分散 = <b>逆方向に変動</b>（分散投資効果あり）

<b>相関係数</b>:
<div class="formula">
\\[\\rho_{AB} = \\frac{Cov(A,B)}{\\sigma_A \\times \\sigma_B}\\]
</div>

<table>
<tr><th>値</th><th>意味</th></tr>
<tr><td>+1</td><td>完全に同方向（分散効果なし）</td></tr>
<tr><td>0</td><td>無相関</td></tr>
<tr><td>-1</td><td>完全に逆方向（分散効果最大）</td></tr>
</table>

<b>2資産ポートフォリオの分散</b>:
<div class="formula">
\\[\\sigma_p^2 = w_A^2 \\sigma_A^2 + w_B^2 \\sigma_B^2 + 2 w_A w_B Cov(A,B)\\]
</div>

<div class="important">注意:</div>
<ul>
<li>共分散の符号 = 相関係数の符号（標準偏差は常に正のため）</li>
<li>\\(\\beta = \\frac{Cov(R_i, R_m)}{\\sigma_m^2}\\)（ベータ値は共分散を市場分散で割る）</li>
<li>相関係数が1未満なら、ポートフォリオを組むことでリスク低減が可能</li>
</ul>

<div class="source">出典: 一発合格まとめシート H28第15問、資格とるなら.tokyo</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0416_共分散_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
