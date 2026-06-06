"""
経営分析の5分類 - 中小企業診断士 財務会計
Financial Analysis Framework

作成日: 2026-02-28
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1709394211
DECK_ID = 1709394212

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_経営分析5分類',
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
    '中小企業診断士_財務会計::01_経営分析::経営分析5分類'
)

# カード内容
question = """経営分析の5分類とそれぞれの視点・代表指標を答えよ"""

answer = """<b>Financial Analysis Framework</b>（経営分析の5分類）

<table>
<tr><th>分類</th><th>視点</th><th>代表的指標</th></tr>
<tr><td><b>収益性</b></td><td>利益を生む力</td><td>売上高営業利益率、ROA、ROE</td></tr>
<tr><td><b>安全性</b></td><td>支払能力・財務健全性</td><td>流動比率、自己資本比率、固定長期適合率</td></tr>
<tr><td><b>効率性</b></td><td>資産活用度</td><td>総資本回転率、売上債権回転率、棚卸資産回転率</td></tr>
<tr><td><b>生産性</b></td><td>投入資源あたり成果</td><td>一人当たり売上高、労働分配率、付加価値率</td></tr>
<tr><td><b>成長性</b></td><td>将来の発展可能性</td><td>売上高成長率、経常利益成長率、総資本成長率</td></tr>
</table>

<b>構造ロジック</b>:
<ul>
<li><b>収益性・安全性・成長性</b> → 企業の健全性</li>
<li><b>効率性・生産性</b> → 経営資源の活用度</li>
</ul>

<div class="important">注意:</div>
<ul>
<li>単独指標ではなく<b>5分類を総合的に</b>分析する</li>
<li><b>同業他社比較</b>・<b>時系列比較</b>で強み弱みを特定</li>
</ul>

<div class="source">出典: ノーティカル 財務分析5分類、中小機構 経営自己診断</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0101_経営分析5分類_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
