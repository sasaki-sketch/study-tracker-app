"""
回収期間法 - 中小企業診断士 財務会計
Payback Period Method

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740823401
DECK_ID = 1740823402

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_回収期間法',
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
    '中小企業診断士_財務会計::03_意思決定会計::回収期間法'
)

# カード内容
question = """回収期間法の定義・計算式・特徴を答えよ"""

answer = """<b>Payback Period Method</b>（回収期間法）

<b>定義</b>: 投資額を回収するまでに必要な期間を求め、投資の効率性を評価する手法

<div class="formula">
① CF一定の場合:
\\[\\text{回収期間} = \\frac{\\text{初期投資額}}{\\text{年間キャッシュフロー}}\\]

② CF変動の場合:
\\[\\text{回収期間} = (n - 1) + \\frac{\\text{第}n\\text{年初の未回収残高}}{\\text{第}n\\text{年のCF}}\\]
\\(n\\) = 累積CFが初期投資額を超える年
</div>

<b>判断基準</b>: 回収期間 &lt; 目標回収期間 → 投資を実行

<b>メリット</b>:
<ul>
<li>計算が簡単で理解しやすい</li>
<li>流動性（資金回収の速さ）を重視した評価が可能</li>
</ul>

<b>デメリット</b>:
<ul>
<li><b>貨幣の時間価値を考慮しない</b></li>
<li><b>回収後のキャッシュフローを無視する</b></li>
</ul>

<div class="important">注意:</div>
NPV法やIRR法と比較して理論的正確性に劣るため、他の指標と併用して総合的に判断すべき。時間価値を考慮した改良版として<b>割引回収期間法</b>（Discounted Payback Period）がある。

<div class="source">出典: グロービス経営大学院、たかぴーの中小企業診断士試験 攻略ブログ</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0301_回収期間法_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
