"""
投資評価手法の体系 - 中小企業診断士 財務会計
Investment Evaluation Methods

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740823501
DECK_ID = 1740823502

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_投資評価手法の体系',
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
    '中小企業診断士_財務会計::03_意思決定会計::投資評価手法の体系'
)

# カード内容
question = """設備投資の意思決定における評価手法を「収益性」「安全性」「不確実性」の3視点で体系的に答えよ"""

answer = """<b>Investment Evaluation Methods</b>（投資評価手法の体系）

<b>1. 収益性評価（リターンの大きさ）</b>

<table>
<tr><th>手法</th><th>指標</th><th>評価基準</th><th>時間価値</th></tr>
<tr><td>NPV法</td><td>金額（円）</td><td>NPV &gt; 0 → 採択</td><td>○</td></tr>
<tr><td>IRR法</td><td>収益率（%）</td><td>IRR &gt; 資本コスト → 採択</td><td>○</td></tr>
<tr><td>収益性指数法（PI）</td><td>倍率</td><td>PI &gt; 1 → 採択</td><td>○</td></tr>
<tr><td>会計的投資利益率法（ARR）</td><td>利益率（%）</td><td>ARR &gt; 目標利益率 → 採択</td><td>×</td></tr>
</table>

<b>2. 安全性評価（回収の速さ）</b>

<table>
<tr><th>手法</th><th>指標</th><th>評価基準</th><th>時間価値</th></tr>
<tr><td>回収期間法（PP）</td><td>年数</td><td>PP &lt; 目標回収期間 → 採択</td><td>×</td></tr>
<tr><td>割引回収期間法（DPP）</td><td>年数</td><td>DPP &lt; 目標回収期間 → 採択</td><td>○</td></tr>
</table>

<b>3. 不確実性評価（リスクへの対処）</b>

<table>
<tr><th>手法</th><th>特徴</th></tr>
<tr><td>感度分析</td><td>個別変数を変化させNPV等への影響を測定</td></tr>
<tr><td>シナリオ分析</td><td>楽観・基本・悲観の複数シナリオで評価</td></tr>
<tr><td>デシジョンツリー</td><td>段階的意思決定を確率付きで分岐図にする</td></tr>
<tr><td>リアルオプション</td><td>将来の柔軟性（延期・拡大・撤退）に価値を認める</td></tr>
</table>

<b>横断的な分類軸</b>:
<ul>
<li><b>DCF系</b>（時間価値○）: NPV, IRR, PI, DPP</li>
<li><b>非DCF系</b>（時間価値×）: PP, ARR</li>
</ul>

<div class="important">注意:</div>
理論的にはNPV法が最も優れた指標とされるが、実務では複数手法を併用して総合的に判断する。安全性と収益性はトレードオフになることがある。

<div class="source">出典: たかぴーの中小企業診断士試験 攻略ブログ、スタディング、グロービス経営大学院</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0302_投資評価手法の体系_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
