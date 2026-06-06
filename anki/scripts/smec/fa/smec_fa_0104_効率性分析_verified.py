"""
効率性分析の指標 - 中小企業診断士 財務会計
Efficiency Analysis

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394217
DECK_ID = 1709394218

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_効率性分析',
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
    '中小企業診断士_財務会計::01_経営分析::効率性分析'
)

# カード内容
question = """効率性分析の主要指標・計算式・目安を答えよ"""

answer = """<b>Efficiency Analysis</b>（効率性分析）

<table>
<tr><th>指標</th><th>計算式</th><th>解釈</th></tr>
<tr><td><b>総資本回転率</b></td><td>売上高 ÷ 総資本</td><td>資本全体の活用効率</td></tr>
<tr><td><b>売上債権回転率</b></td><td>売上高 ÷ 売上債権</td><td>債権回収の速さ</td></tr>
<tr><td><b>棚卸資産回転率</b></td><td>売上高 ÷ 棚卸資産</td><td>在庫消化の速さ</td></tr>
<tr><td><b>仕入債務回転率</b></td><td>売上原価 ÷ 仕入債務</td><td>支払いサイクル</td></tr>
<tr><td><b>有形固定資産回転率</b></td><td>売上高 ÷ 有形固定資産</td><td>設備活用の効率</td></tr>
</table>

<b>回転期間への変換</b>:
<div class="formula">
\\[回転期間(日) = \\frac{365}{回転率}\\]
</div>

<b>目安</b>:
<ul>
<li>総資本回転率: <b>1回以上</b></li>
<li>仕入債務回転期間: <b>40〜50日以内</b>が健全</li>
</ul>

<b>解釈</b>:
<ul>
<li>売上債権・棚卸資産 → 回転率<b>高い</b>ほど良い</li>
<li>仕入債務 → 回転率<b>低い</b>（期間長い）ほど資金繰り有利</li>
</ul>

<div class="important">注意:</div>
<ul>
<li>仕入債務回転期間が<b>長すぎる</b> → 支払い遅延の懸念</li>
<li><b>CCC（キャッシュコンバージョンサイクル）</b>との関連も重要</li>
</ul>

<div class="source">出典: グロービス経営大学院、マネーフォワード</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0104_効率性分析_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
