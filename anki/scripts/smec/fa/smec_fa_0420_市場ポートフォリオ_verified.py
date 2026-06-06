"""
市場ポートフォリオ - 中小企業診断士 財務会計
Market Portfolio

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740927101
DECK_ID = 1740927102

# 画像ファイル設定
IMAGE_NAME = 'smec_fa_0420_market_portfolio.png'
SCRIPT_DIR = '/Users/sasaki/study_app/anki/scripts/smec/fa/'
IMAGE_PATH = SCRIPT_DIR + IMAGE_NAME

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_市場ポートフォリオ',
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
    '中小企業診断士_財務会計::04_ファイナンス::市場ポートフォリオ'
)

# カード内容
question = """市場ポートフォリオの定義・特徴・関連理論との関係を答えよ"""

answer = f"""<b>Market Portfolio</b>（市場ポートフォリオ / マーケットポートフォリオ）

<b>定義</b>: 世の中の全てのリスク資産を<b>時価総額比率</b>で組み入れたポートフォリオ

<div style="text-align: center; margin: 15px 0;">
<img src="{IMAGE_NAME}" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">
</div>

<b>他の理論との関係</b>:
<table>
<tr><th>理論</th><th>市場ポートフォリオの位置づけ</th></tr>
<tr><td>効率的フロンティア</td><td>CMLとの<b>接点</b>（= 接点ポートフォリオ）</td></tr>
<tr><td>分離定理</td><td>全投資家が保有する<b>共通の</b>リスク資産構成</td></tr>
<tr><td>CAPM</td><td>期待収益率算出の<b>基準</b>（β=1）</td></tr>
<tr><td>CML</td><td>安全資産と市場ポートフォリオを結ぶ直線上</td></tr>
</table>

<b>β値との関係</b>:
<table>
<tr><th>資産</th><th>β値</th></tr>
<tr><td>安全資産（国債）</td><td>β = <b>0</b></td></tr>
<tr><td>市場ポートフォリオ</td><td>β = <b>1</b></td></tr>
<tr><td>β &gt; 1 の個別証券</td><td>市場より高感応度</td></tr>
<tr><td>β &lt; 1 の個別証券</td><td>市場より低感応度</td></tr>
</table>

<b>実務での代理変数</b>:
<table>
<tr><th>市場</th><th>代理指標</th></tr>
<tr><td>日本</td><td>TOPIX</td></tr>
<tr><td>米国</td><td>S&P 500</td></tr>
</table>

<div class="important">注意:</div>
<ul>
<li>理論上は全資産（株式・債券・不動産・人的資本等）を含むが、実際には<b>計測不可能</b></li>
<li>この問題点は<b>ロールの批判</b>（Roll's Critique）と呼ばれる</li>
<li>市場ポートフォリオは投資家のリスク回避度と<b>無関係</b>に決まる（分離定理）</li>
<li>試験では「最適なリスク資産ポートフォリオはリスク回避度に依存しない」が頻出</li>
</ul>

<div class="source">出典: みずほ証券 ファイナンス用語集、スタディング R3第20問</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力（画像ファイルを同梱）
output_path = SCRIPT_DIR + 'smec_fa_0420_市場ポートフォリオ_verified.apkg'
package = genanki.Package(deck)
package.media_files = [IMAGE_PATH]
package.write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Media included: {IMAGE_NAME}")
