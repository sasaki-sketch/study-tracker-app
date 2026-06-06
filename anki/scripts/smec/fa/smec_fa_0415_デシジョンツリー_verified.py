"""
デシジョンツリー（意思決定樹形図） - 中小企業診断士 財務会計
Decision Tree Analysis

作成日: 2026-03-03
"""

import genanki
import shutil
import os
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740926601
DECK_ID = 1740926602

# 画像ファイル設定
IMAGE_SRC = '/tmp/decision_tree_kaizen.png'
IMAGE_NAME = 'smec_fa_0415_decision_tree.png'
SCRIPT_DIR = '/Users/sasaki/study_app/anki/scripts/smec/fa/'
IMAGE_DEST = os.path.join(SCRIPT_DIR, IMAGE_NAME)

# 画像をコピー
shutil.copy2(IMAGE_SRC, IMAGE_DEST)

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_デシジョンツリー',
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
    '中小企業診断士_財務会計::04_ファイナンス::デシジョンツリー'
)

# カード内容
question = """デシジョンツリーの定義・構成要素・期待値の計算方法を答えよ"""

answer = f"""<b>Decision Tree Analysis</b>（デシジョンツリー / 意思決定樹形図）

<b>定義</b>: 不確実性下の意思決定を樹形図で視覚化し、<b>期待値（EMV）</b>を比較して最適な選択肢を決定する手法

<div style="text-align: center; margin: 15px 0;">
<img src="{IMAGE_NAME}" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px;">
</div>

<b>構成要素</b>:
<table>
<tr><th>記号</th><th>名称</th><th>意味</th></tr>
<tr><td><b>□</b></td><td>決定ノード</td><td>意思決定者が<b>コントロール可能</b>な選択肢</td></tr>
<tr><td><b>○</b></td><td>確率ノード</td><td><b>コントロール不可能</b>な不確実事象（確率で分岐）</td></tr>
<tr><td>△</td><td>終点ノード</td><td>結果（利益・損失）</td></tr>
</table>

<b>計算方法</b>（ロールバック法）:
<div class="formula">
\\[EMV = \\sum_{{i=1}}^{{n}} p_i \\times V_i\\]
</div>

<ol>
<li><b>右から左へ</b>逆算する（ロールバック）</li>
<li>確率ノード○: 各結果の<b>期待値</b>（確率 × 金額）を合計</li>
<li>決定ノード□: 期待値が<b>最大の選択肢</b>を採用</li>
<li>初期投資を控除して最終的な期待利益を算出</li>
</ol>

<div class="important">注意:</div>
<ul>
<li>投資と結果に時間差がある場合、期待値を<b>NPV（現在価値）</b>で表現する</li>
<li>□と○の区別が試験の頻出ポイント（コントロール可能 vs 不可能）</li>
<li>2次試験（事例IV）でも出題される重要論点</li>
</ul>

<div class="source">出典: Kaizen Penguin、木暮 Web教材（オペレーションズ・リサーチ）</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力（画像ファイルを同梱）
output_path = os.path.join(SCRIPT_DIR, 'smec_fa_0415_デシジョンツリー_verified.apkg')
package = genanki.Package(deck)
package.media_files = [IMAGE_DEST]
package.write_to_file(output_path)
print(f"Generated: {output_path}")
print(f"Media included: {IMAGE_NAME}")
