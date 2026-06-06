"""
CAPM（資本資産価格モデル） - 中小企業診断士 財務会計
Capital Asset Pricing Model

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740926801
DECK_ID = 1740926802

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_CAPM',
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
    '中小企業診断士_財務会計::04_ファイナンス::CAPM'
)

# カード内容
question = """CAPM（資本資産価格モデル）の定義・計算式・構成要素・WACCとの関係を答えよ"""

answer = """<b>Capital Asset Pricing Model / CAPM</b>（資本資産価格モデル）

<b>定義</b>: 個別証券のβ値から、投資家が期待する収益率（＝株主資本コスト）を算出するモデル

<b>計算式</b>:
<div class="formula">
\\[E(r_i) = r_f + \\beta_i \\times (E(r_m) - r_f)\\]
</div>

<table>
<tr><th>記号</th><th>意味</th><th>例</th></tr>
<tr><td>\\(r_f\\)</td><td>リスクフリーレート（10年国債等）</td><td>2%</td></tr>
<tr><td>\\(\\beta_i\\)</td><td>個別証券のシステマティックリスク</td><td>1.2</td></tr>
<tr><td>\\(E(r_m) - r_f\\)</td><td>マーケットリスクプレミアム</td><td>6%</td></tr>
</table>

<b>計算例</b>:
<div class="formula">
\\[E(r) = 2\\% + 1.2 \\times 6\\% = 2\\% + 7.2\\% = 9.2\\%\\]
</div>

<b>β（ベータ）の意味</b>:
<div class="formula">
\\[\\beta = \\frac{Cov(R_i, R_m)}{\\sigma_m^2}\\]
</div>

<table>
<tr><th>β値</th><th>意味</th></tr>
<tr><td>β = 1</td><td>市場と同じ変動性</td></tr>
<tr><td>β &gt; 1</td><td>市場より<b>ハイリスク</b></td></tr>
<tr><td>β &lt; 1</td><td>市場より<b>ローリスク</b></td></tr>
</table>

<b>CML vs SML</b>:
<table>
<tr><th></th><th>資本市場線（CML）</th><th>証券市場線（SML）</th></tr>
<tr><td>横軸</td><td>標準偏差（σ）</td><td><b>β</b></td></tr>
<tr><td>対象</td><td><b>効率的ポートフォリオ</b>のみ</td><td><b>全ての個別証券</b></td></tr>
<tr><td>用途</td><td>ポートフォリオ選択</td><td>個別証券の期待収益率算出</td></tr>
</table>

<b>WACCとの関係</b>:
CAPMで求めた期待収益率 = <b>株主資本コスト</b>(\\(r_e\\))
<div class="formula">
\\[WACC = r_e \\times \\frac{E}{V} + r_d(1-t) \\times \\frac{D}{V}\\]
</div>

<div class="important">注意:</div>
<ul>
<li>「マーケットリスクプレミアム」と「市場ポートフォリオの期待収益率」は別物（前者 = 後者 − \\(r_f\\)）</li>
<li>CAPMが扱うのは<b>システマティックリスク</b>（分散不能）のみ。非システマティックリスクは分散投資で消去可能</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、グロービス経営大学院</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0417_CAPM_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
