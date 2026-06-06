"""
資金調達の分類（4つの軸） - 中小企業診断士 財務会計
Classification of Corporate Financing

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740926301
DECK_ID = 1740926302

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_資金調達の分類',
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
    '中小企業診断士_財務会計::04_ファイナンス::資金調達の分類'
)

# カード内容
question = """資金調達の分類（4つの軸）について、各調達手段の分類を答えよ"""

answer = """<b>Classification of Corporate Financing</b>（資金調達の分類）

4つの分類軸:
<table>
<tr><th>軸</th><th>英語</th><th>区分</th></tr>
<tr><td>①</td><td>Equity vs Debt Capital</td><td>自己資本 vs 他人資本</td></tr>
<tr><td>②</td><td>External vs Internal Financing</td><td>外部金融 vs 内部金融</td></tr>
<tr><td>③</td><td>Direct vs Indirect Financing</td><td>直接金融 vs 間接金融</td></tr>
<tr><td>④</td><td>Short-term vs Long-term</td><td>短期 vs 長期</td></tr>
</table>

<b>各調達手段の分類一覧</b>:
<table>
<tr><th>調達手段</th><th>①自己/他人</th><th>②内部/外部</th><th>③直接/間接</th><th>④短期/長期</th></tr>
<tr><td>企業間信用<br>（買掛金・支払手形）</td><td>他人</td><td>外部</td><td>間接</td><td>短期</td></tr>
<tr><td>短期借入金</td><td>他人</td><td>外部</td><td>間接</td><td>短期</td></tr>
<tr><td>長期借入金</td><td>他人</td><td>外部</td><td>間接</td><td>長期</td></tr>
<tr><td>社債</td><td>他人</td><td>外部</td><td><b>直接</b></td><td>長期</td></tr>
<tr><td>株式発行</td><td><b>自己</b></td><td>外部</td><td><b>直接</b></td><td>長期</td></tr>
<tr><td>内部留保<br>（減価償却含む）</td><td><b>自己</b></td><td><b>内部</b></td><td>−</td><td>−</td></tr>
</table>

<div class="important">注意:</div>
<ul>
<li><b>内部金融</b>は「内部留保」のみ（減価償却による資金留保も含む）</li>
<li><b>直接金融</b> = 投資家から直接調達（株式・社債）、<b>間接金融</b> = 金融機関経由（借入）</li>
<li>社債は「他人資本」だが「直接金融」→ 混同しやすいので注意</li>
<li>企業間信用は「外部金融」かつ「間接金融」かつ「短期」に分類</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、野村證券 証券用語集、東海東京証券 証券用語集</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0412_資金調達の分類_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
