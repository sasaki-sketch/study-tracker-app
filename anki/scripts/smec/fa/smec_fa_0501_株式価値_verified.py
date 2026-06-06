"""
株式価値 - 中小企業診断士 財務会計
Equity Value / Shareholder Value

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740824901
DECK_ID = 1740824902

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_株式価値',
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
    '中小企業診断士_財務会計::05_企業価値::株式価値'
)

# カード内容
question = """株式価値の定義・企業価値との関係・3つの評価アプローチを答えよ"""

answer = """<b>Equity Value / Shareholder Value</b>（株式価値）

<b>定義</b>: 企業の株主に帰属する価値。<b>企業価値から有利子負債を差し引いた</b>もの。

<div class="formula">
\\[\\text{株式価値} = \\text{企業価値} - \\text{有利子負債}\\]

\\[\\text{企業価値} = \\text{事業価値} + \\text{非事業用資産}\\]
</div>

<b>3つの評価アプローチ</b>:
<table>
<tr><th>アプローチ</th><th>手法</th><th>計算方法</th></tr>
<tr><td rowspan="2"><b>コストアプローチ</b></td><td>簿価純資産法</td><td>資産（簿価）− 負債 = 株式価値</td></tr>
<tr><td>時価純資産法（修正簿価法）</td><td>資産（<b>時価</b>）− 負債 = 株式価値</td></tr>
<tr><td rowspan="3"><b>インカムアプローチ</b></td><td>DCF法</td><td>FCFをWACCで割引 → 企業価値 → 株式価値</td></tr>
<tr><td>収益還元法</td><td>当期純利益 ÷ 期待収益率</td></tr>
<tr><td>配当還元法</td><td>配当金 ÷ 株主資本コスト</td></tr>
<tr><td rowspan="3"><b>マーケットアプローチ</b></td><td>市場株価法</td><td>上場企業の市場株価を直接使用</td></tr>
<tr><td>マルチプル法（類似会社比較法）</td><td>類似上場企業の指標を使って算出</td></tr>
<tr><td>→ PER法 / PBR法</td><td>類似企業PER × 自社EPS 等</td></tr>
</table>

<b>各アプローチの特徴</b>:
<table>
<tr><th>項目</th><th>コスト</th><th>インカム</th><th>マーケット</th></tr>
<tr><td>着目点</td><td>B/S（資産・負債）</td><td>将来の収益力</td><td>市場の評価</td></tr>
<tr><td>長所</td><td>客観的・簡便</td><td>将来性を反映</td><td>市場実勢を反映</td></tr>
<tr><td>短所</td><td>将来性を反映しない</td><td>予測に依存</td><td>類似企業の選定が困難</td></tr>
<tr><td>適用場面</td><td>清算・小規模企業</td><td>M&A・事業承継</td><td>上場類似企業がある場合</td></tr>
</table>

<div class="important">注意:</div>
中小企業診断士試験ではDCF法（インカムアプローチ）の計算問題が頻出。株式価値を求める際は、DCF法で算出した企業価値から有利子負債を忘れずに差し引くこと。

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、ナレッジ・ハブ大学、一発合格道場</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0501_株式価値_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
