"""
内部留保 - 中小企業診断士 財務会計
Retained Earnings / Internal Reserves

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740825501
DECK_ID = 1740825502

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_内部留保',
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
    '中小企業診断士_財務会計::01_経営分析::内部留保'
)

# カード内容
question = """内部留保の定義・計算式・利益剰余金との関係を答えよ"""

answer = """<b>Retained Earnings / Internal Reserves</b>（内部留保）

<b>定義</b>: 当期純利益のうち、配当として社外に流出せず<b>社内に蓄積された利益</b>。B/S上では<b>利益剰余金</b>として計上される。

<div class="formula">
\\[\\text{内部留保} = \\text{当期純利益} - \\text{配当金}\\]

\\[\\text{内部留保率} = \\frac{\\text{内部留保}}{\\text{当期純利益}} = 1 - \\text{配当性向}\\]

例: 純利益100万、配当40万 → 内部留保 = 60万、内部留保率 = 60%
</div>

<b>内部留保と利益剰余金の関係</b>:
<table>
<tr><th>項目</th><th>内部留保</th><th>利益剰余金</th></tr>
<tr><td>性質</td><td>1期間のフロー</td><td>B/Sに蓄積されたストック</td></tr>
<tr><td>意味</td><td>今期残した利益</td><td>過去から積み上がった利益の累計</td></tr>
<tr><td>関係</td><td colspan="2">毎期の内部留保が積み上がって → 利益剰余金になる</td></tr>
</table>

<b>利益剰余金の内訳</b>:
<table>
<tr><th>区分</th><th>内容</th></tr>
<tr><td>利益準備金</td><td>会社法で積立が義務付けられた準備金</td></tr>
<tr><td>任意積立金</td><td>企業が自主的に積み立てた金額</td></tr>
<tr><td>繰越利益剰余金</td><td>上記以外の未処分利益</td></tr>
</table>

<div class="important">注意:</div>
「内部留保」は正式な会計用語ではなく決算書には登場しない。また内部留保＝現金ではない。利益を設備投資や在庫に充てている場合、利益剰余金が多くても手元現金が少ないケースは多い。

<div class="source">出典: マネーフォワード、弥生会計、カオナビ人事用語集</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0119_内部留保_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
