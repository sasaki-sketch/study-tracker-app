"""
証券市場線（SML） - 中小企業診断士 財務会計
Security Market Line

作成日: 2026-03-03
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740927201
DECK_ID = 1740927202

# 画像ファイル設定
IMAGE_NAME = 'smec_fa_0421_security_market_line.png'
SCRIPT_DIR = '/Users/sasaki/study_app/anki/scripts/smec/fa/'
IMAGE_PATH = SCRIPT_DIR + IMAGE_NAME

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_証券市場線',
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
    '中小企業診断士_財務会計::04_ファイナンス::証券市場線'
)

# カード内容
question = """証券市場線（SML）の定義・グラフの構造・割高/割安の判定方法を答えよ"""

answer = f"""<b>Security Market Line / SML</b>（証券市場線）

<b>定義</b>: CAPMを可視化したグラフ。横軸にβ、縦軸に期待収益率をとった直線

<div style="text-align: center; margin: 15px 0;">
<img src="{IMAGE_NAME}" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">
</div>

<b>グラフの構造</b>:
<table>
<tr><th>要素</th><th>値</th></tr>
<tr><td>Y切片</td><td>リスクフリーレート（\\(R_f\\)）</td></tr>
<tr><td>β=1の点</td><td>市場ポートフォリオ（\\(E(R_m)\\)）</td></tr>
<tr><td>傾き</td><td>マーケットリスクプレミアム（\\(E(R_m) - R_f\\)）</td></tr>
</table>

<b>割高・割安の判定</b>:
<table>
<tr><th>位置</th><th>判定</th><th>意味</th><th>投資行動</th></tr>
<tr><td>SML<b>上</b></td><td><b>適正価格</b></td><td>CAPMの理論値通り</td><td>保有継続</td></tr>
<tr><td>SML<b>より上</b></td><td><b>割安</b>（過小評価）</td><td>リターンがリスク対比で高い</td><td><b>買い</b></td></tr>
<tr><td>SML<b>より下</b></td><td><b>割高</b>（過大評価）</td><td>リターンがリスク対比で低い</td><td><b>売り</b></td></tr>
</table>

<b>CML vs SML</b>:
<table>
<tr><th></th><th>CML</th><th>SML</th></tr>
<tr><td>横軸</td><td>σ（標準偏差）</td><td><b>β</b></td></tr>
<tr><td>対象</td><td>効率的ポートフォリオのみ</td><td><b>全ての個別証券・ポートフォリオ</b></td></tr>
<tr><td>リスク</td><td>トータルリスク</td><td><b>システマティックリスクのみ</b></td></tr>
</table>

<div class="important">注意:</div>
<ul>
<li>均衡状態では全ての証券がSML上に位置する</li>
<li>SMLの傾きが急 → リスク回避度が高い市場</li>
<li>βが負の証券も理論上存在（市場と逆に動く）</li>
</ul>

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、みずほ証券 ファイナンス用語集</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力（画像ファイルを同梱）
output_path = SCRIPT_DIR + 'smec_fa_0421_証券市場線_verified.apkg'
package = genanki.Package(deck)
package.media_files = [IMAGE_PATH]
package.write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Media included: {IMAGE_NAME}")
