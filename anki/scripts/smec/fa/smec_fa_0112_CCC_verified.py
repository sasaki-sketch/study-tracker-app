"""
CCC（キャッシュコンバージョンサイクル） - 中小企業診断士 財務会計
Cash Conversion Cycle

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394233
DECK_ID = 1709394234

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_CCC',
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
    '中小企業診断士_財務会計::01_経営分析::CCC'
)

# カード内容
question = """CCC（キャッシュコンバージョンサイクル）の定義・計算式を答えよ"""

answer = """<b>Cash Conversion Cycle</b>（キャッシュコンバージョンサイクル）

<b>【定義】</b>
仕入代金の支払いから売上代金の回収までに要する日数。資金繰りの効率性を示す指標。

<hr>

<b>【計算式】</b>
<div class="formula">
\\[CCC = 売上債権回転日数 + 棚卸資産回転日数 - 仕入債務回転日数\\]
</div>

<b>【各要素の計算】</b>
<table>
<tr><th>指標</th><th>計算式</th></tr>
<tr><td>売上債権回転日数</td><td>売上債権 ÷ 売上高 × 365</td></tr>
<tr><td>棚卸資産回転日数</td><td>棚卸資産 ÷ 売上原価 × 365</td></tr>
<tr><td>仕入債務回転日数</td><td>仕入債務 ÷ 仕入高 × 365</td></tr>
</table>

<hr>

<b>【解釈】</b>
<ul>
<li>CCCが<b>短い</b> → 資金繰りが良好</li>
<li>CCCが<b>長い</b> → 運転資金が多く必要</li>
<li>CCCが<b>マイナス</b> → 支払い前に回収完了（理想的）</li>
</ul>

<b>【目安】</b>
90日以内が目安（業種により異なる）

<b>【改善方法】</b>
<ul>
<li>売上債権回転日数↓（早期回収）</li>
<li>棚卸資産回転日数↓（在庫削減）</li>
<li>仕入債務回転日数↑（支払猶予延長）</li>
</ul>

<div class="source">出典: 過去問.com</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0112_CCC_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
