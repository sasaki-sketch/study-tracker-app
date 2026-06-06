"""
当座資産 - 中小企業診断士 財務会計
Quick Assets

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394231
DECK_ID = 1709394232

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_当座資産',
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
    '中小企業診断士_財務会計::01_経営分析::当座資産'
)

# カード内容
question = """当座資産の定義・構成要素・当座比率を答えよ"""

answer = """<b>Quick Assets</b>（当座資産）

<b>【定義】</b>
流動資産のうち、現金または短期間で容易に現金化できる資産。

<hr>

<b>【構成要素】</b>
<div class="formula">
\\[当座資産 = 現金預金 + 受取手形 + 売掛金 + 売買目的有価証券\\]
</div>

※売買目的有価証券：短期売買で利益を得る目的で保有する有価証券

<b>【流動資産との違い】</b>
<table>
<tr><th>項目</th><th>流動資産</th><th>当座資産</th></tr>
<tr><td>現金預金</td><td>○</td><td>○</td></tr>
<tr><td>受取手形・売掛金</td><td>○</td><td>○</td></tr>
<tr><td>売買目的有価証券</td><td>○</td><td>○</td></tr>
<tr><td>棚卸資産</td><td>○</td><td>×</td></tr>
<tr><td>その他流動資産</td><td>○</td><td>×</td></tr>
</table>

→ 当座資産は棚卸資産を含まない（換金性が低いため）

<hr>

<b>【当座比率】</b>
<div class="formula">
\\[当座比率 = \\frac{当座資産}{流動負債} \\times 100\\]
</div>

<b>【目安】</b>
100%以上が望ましい（短期債務を当座資産で賄える状態）

<div class="source">出典: 過去問.com</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0111_当座資産_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
