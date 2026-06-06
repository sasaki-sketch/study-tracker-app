"""
会計的投資利益率法 - 中小企業診断士 財務会計
Accounting Rate of Return

作成日: 2026-03-01
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデルID（ランダム生成した固定値）
MODEL_ID = 1740823701
DECK_ID = 1740823702

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '中小企業診断士_財務会計_会計的投資利益率法',
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
    '中小企業診断士_財務会計::03_意思決定会計::会計的投資利益率法'
)

# カード内容
question = """会計的投資利益率法（ARR）の定義・計算式・特徴を答えよ"""

answer = """<b>Accounting Rate of Return</b>（会計的投資利益率法）

<b>定義</b>: 投資案から得られる平均年間利益を投資額で割り、会計的な利益率で投資を評価する手法

<div class="formula">
\\[ARR = \\frac{\\text{平均年間利益}}{\\text{平均投資額}} \\times 100 \\text{ (%)}\\]

\\[\\text{平均年間利益} = \\frac{\\text{増分CF合計（税引後）} - \\text{初期投資額}}{\\text{耐用年数}}\\]

\\[\\text{平均投資額} = \\frac{\\text{初期投資額} + \\text{残存価値}}{2}\\]
</div>

<b>分子の「利益」</b>: 投資案が生み出す<b>税引後の増分利益</b>（= 税引後増分CF − 減価償却費）。P/L上の特定科目ではなく、当該投資による追加的な利益。

<b>判断基準</b>: ARR &gt; 目標利益率 → 採択

<b>2つのバリエーション</b>:
<table>
<tr><th>種類</th><th>分母</th></tr>
<tr><td>総投資利益率</td><td>初期投資額（総額）</td></tr>
<tr><td>平均投資利益率</td><td>平均投資額（÷2）</td></tr>
</table>

<b>メリット</b>:
<ul>
<li>計算が容易で、会計上の利益率として直感的に理解しやすい</li>
<li>投資期間全体を通じた包括的な評価が可能</li>
</ul>

<b>デメリット</b>:
<ul>
<li><b>貨幣の時間価値を考慮しない</b></li>
<li>CFではなく<b>会計的利益</b>に基づくため、減価償却方法により結果が変わる</li>
<li>CFの発生タイミングを無視する</li>
</ul>

<div class="important">注意:</div>
非DCF系の手法であり、理論的にはNPV法に劣る。試験では「平均投資額 = 初期投資額 ÷ 2」（残存価値ゼロ・定額法前提）の計算がよく問われる。

<div class="source">出典: 知っとく会計学、プロフェッショナル簿記、スタディング</div>
"""

# カード追加
note = genanki.Note(
    model=model,
    fields=[question, answer]
)
deck.add_note(note)

# パッケージ出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/fa/smec_fa_0304_会計的投資利益率法_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"Generated: {output_path}")
