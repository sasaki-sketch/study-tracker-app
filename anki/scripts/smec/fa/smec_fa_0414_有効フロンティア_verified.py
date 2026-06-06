"""
有効フロンティア（効率的フロンティア） - 中小企業診断士 財務会計
Efficient Frontier

作成日: 2026-03-03
"""

import genanki
import shutil
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740926501
DECK_ID = 1740926502

# 画像ファイルパス
IMAGE_SRC = '/Users/sasaki/Library/Application Support/CleanShot/media/media_Jt4r2xViE0/CleanShot 2026-03-03 at 20.38.31@2x.png'
IMAGE_NAME = 'smec_fa_0414_efficient_frontier.png'

# 画像をスクリプトと同じディレクトリにコピー（ファイル名を正規化）
SCRIPT_DIR = '/Users/sasaki/study_app/anki/scripts/smec/fa/'
IMAGE_DEST = SCRIPT_DIR + IMAGE_NAME
shutil.copy2(IMAGE_SRC, IMAGE_DEST)

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_有効フロンティア',
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
    '中小企業診断士_財務会計::04_ファイナンス::有効フロンティア'
)

# カード内容
question = """有効フロンティアの定義・グラフ上の特徴・資本市場線との関係を答えよ"""

answer = f"""<b>Efficient Frontier</b>（有効フロンティア / 効率的フロンティア）

<b>定義</b>: 同じリスクで最大のリターン、または同じリターンで最小のリスクとなるポートフォリオの集合
<b>提唱者</b>: Harry Markowitz（1952年、現代ポートフォリオ理論）

<div style="text-align: center; margin: 15px 0;">
<img src="{IMAGE_NAME}" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">
</div>

<table>
<tr><th>点</th><th>意味</th></tr>
<tr><td><b>B</b></td><td><b>最小分散ポートフォリオ</b>（リスク最小の点）</td></tr>
<tr><td><b>B→C→D→A</b>（太線）</td><td><b>有効フロンティア</b>（効率的な組合せ）</td></tr>
<tr><td>B以下（細線）</td><td>非効率領域（同リスクでより高リターンが存在）</td></tr>
<tr><td>曲線内側</td><td><b>投資機会集合</b>（実現可能な全ポートフォリオ）</td></tr>
</table>

<b>安全資産を含む場合</b>:
<table>
<tr><th>用語</th><th>説明</th></tr>
<tr><td>資本市場線（CML）</td><td>安全資産から有効フロンティアへの<b>接線</b></td></tr>
<tr><td>接点ポートフォリオ</td><td>CMLと有効フロンティアの接点 = <b>市場ポートフォリオ</b></td></tr>
</table>

投資家はリスク許容度に応じて、安全資産と市場ポートフォリオの<b>配分比率</b>を決定する。借入可能な場合、接点より右側（レバレッジ投資）も選択可能。

<div class="important">注意:</div>
<ul>
<li>有効フロンティアの<b>下側</b>（Bより下）は非効率 → 合理的投資家は選択しない</li>
<li>リスク回避的 ≠ 最低リスクを選ぶ（リスクに見合うリターンがあれば高リスクも選択）</li>
<li>CMLは安全資産導入で有効フロンティアが<b>直線に変わる</b>ことを示す</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、グロービス経営大学院</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力（画像ファイルを同梱）
output_path = SCRIPT_DIR + 'smec_fa_0414_有効フロンティア_verified.apkg'
package = genanki.Package(deck)
package.media_files = [IMAGE_DEST]
package.write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Media included: {IMAGE_NAME}")
