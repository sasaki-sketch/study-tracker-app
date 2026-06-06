#!/usr/bin/env python3
"""
統計検定2級 過去問復習カード
作成日: 2026-01-28
トピック: 母比率の信頼区間、対応あるt検定、一元配置分散分析、重回帰分析

検証済みソース:
- 統計WEB (https://bellcurve.jp/statistics/)
- JMP統計ナレッジポータル (https://www.jmp.com/ja/statistics-knowledge-portal/)
- とけたろうブログ (https://toketarou.com/)
"""

import genanki
import random
import sys
sys.path.append('/Users/sasaki')
from anki_card_css_template import CARD_CSS

# デッキとモデルのID
DECK_ID = random.randrange(1 << 30, 1 << 31)
MODEL_ID = random.randrange(1 << 30, 1 << 31)

# カードモデル
model = genanki.Model(
    MODEL_ID,
    '統計検定2級_過去問復習',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Source'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div><div class="source">{{Source}}</div>',
        },
    ],
    css=CARD_CSS
)

# デッキ作成
deck = genanki.Deck(DECK_ID, '統計検定2級::過去問復習_20260128')

# カードデータ
cards_data = [
    # ===== 母比率の信頼区間 =====
    {
        'question': '''母比率の標準誤差（SE）の公式は？
<div class="mnemonic">※ p̂ は標本比率、n は標本サイズ</div>''',
        'answer': '''<div class="formula">
\\[SE = \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}\\]
</div>
<b>ポイント:</b>
<ul>
<li>分子は p̂(1-p̂) で、p̂=0.5 のとき最大</li>
<li>n が大きいほど SE は小さくなる</li>
<li>母比率 p の代わりに標本比率 p̂ を使う</li>
</ul>''',
        'source': '統計WEB 21-1. 母比率の信頼区間の求め方'
    },
    {
        'question': '''母比率の95%信頼区間の公式は？''',
        'answer': '''<div class="formula">
\\[\\hat{p} \\pm 1.96 \\times \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}\\]
</div>
<b>信頼係数と z 値:</b>
<table>
<tr><th>信頼係数</th><th>z 値</th></tr>
<tr><td>90%</td><td>1.645</td></tr>
<tr><td>95%</td><td><span class="important">1.96</span></td></tr>
<tr><td>99%</td><td>2.576</td></tr>
</table>
<div class="mnemonic">95%の1.96は必ず覚える！</div>''',
        'source': '統計WEB 21-1. 母比率の信頼区間の求め方'
    },
    {
        'question': '''<div class="example">
<b>例題:</b> n=100人中54人がA候補に投票。<br>
A候補の得票率の95%信頼区間を求めよ。
</div>''',
        'answer': '''<b>解法:</b>
<ol>
<li>標本比率: \\(\\hat{p} = 54/100 = 0.54\\)</li>
<li>標準誤差: \\(SE = \\sqrt{\\frac{0.54 \\times 0.46}{100}} = \\sqrt{0.002484} \\approx 0.0498\\)</li>
<li>95%信頼区間: \\(0.54 \\pm 1.96 \\times 0.0498 = 0.54 \\pm 0.098\\)</li>
</ol>
<div class="formula">
<b>答え:</b> \\(0.54 \\pm 0.098\\) すなわち \\([0.442, 0.638]\\)
</div>''',
        'source': '統計検定2級 2019年11月 問13'
    },

    # ===== 対応のあるt検定 =====
    {
        'question': '''対応のあるt検定の検定統計量 T の公式は？
<div class="mnemonic">※ 差のデータ d₁, d₂, ..., dₙ について</div>''',
        'answer': '''<div class="formula">
\\[T = \\frac{\\bar{d} - \\mu_0}{\\sqrt{S_d^2/n}} = \\frac{\\bar{d} - \\mu_0}{S_d/\\sqrt{n}}\\]
</div>
<b>各記号の意味:</b>
<ul>
<li>d̄: 差の平均（例: 前-後）</li>
<li>μ₀: 帰無仮説での差の期待値（通常0）</li>
<li>S_d: 差の標本標準偏差</li>
<li>n: 対のデータ数</li>
</ul>''',
        'source': 'JMP統計ナレッジポータル - 対応のあるt検定'
    },
    {
        'question': '''対応のあるt検定の自由度は？
<div class="mnemonic">n = 標本サイズ（対の数）</div>''',
        'answer': '''<div class="formula">
\\[\\text{自由度} = n - 1\\]
</div>
<b>例:</b>
<ul>
<li>16人の前後比較 → 自由度 = 16 - 1 = <span class="important">15</span></li>
<li>40人の前後比較 → 自由度 = 40 - 1 = 39</li>
</ul>
<div class="mnemonic">
<b>覚え方:</b> 「対応あり」は1標本扱い → 自由度 n-1<br>
「対応なし」は2標本 → 自由度 n₁+n₂-2
</div>''',
        'source': 'JMP統計ナレッジポータル - 対応のあるt検定'
    },
    {
        'question': '''不偏分散 S² の定義式で、分母が n ではなく n-1 になる理由は？''',
        'answer': '''<b>理由: 自由度が n-1 だから</b>

<div class="formula">
\\[S^2 = \\frac{1}{n-1}\\sum_{i=1}^{n}(X_i - \\bar{X})^2\\]
</div>

<b>なぜ自由度が n-1 か:</b>
<ul>
<li>n個のデータがあるが、X̄ を計算に使う</li>
<li>X̄ が決まると、最後の1つのデータは他から決まる</li>
<li>よって「自由に決められる」データは n-1 個</li>
</ul>
<div class="important">分母が n-1 の場合、t分布の自由度も n-1 になる</div>''',
        'source': '統計学における自由度について - スタビジ'
    },

    # ===== 一元配置分散分析 =====
    {
        'question': '''一元配置分散分析（ANOVA）の基本的な分解式は？''',
        'answer': '''<div class="formula">
\\[S_T = S_A + S_e\\]
<b>（全変動 = 要因変動 + 残差変動）</b>
</div>
<table>
<tr><th>記号</th><th>名称</th><th>意味</th></tr>
<tr><td>S_T</td><td>全平方和</td><td>データ全体のばらつき</td></tr>
<tr><td>S_A</td><td>水準間平方和</td><td>要因（グループ間）の効果</td></tr>
<tr><td>S_e</td><td>残差平方和</td><td>グループ内のばらつき（誤差）</td></tr>
</table>''',
        'source': '統計WEB 29-3. 一元配置分散分析の流れ'
    },
    {
        'question': '''一元配置分散分析の水準間平方和 S_A の公式は？
<div class="mnemonic">※ k水準、各水準 nᵢ 個のデータ</div>''',
        'answer': '''<div class="formula">
\\[S_A = \\sum_{i=1}^{k} n_i (\\bar{y}_{i\\cdot} - \\bar{y}_{\\cdot\\cdot})^2\\]
</div>
<b>各記号の意味:</b>
<ul>
<li>k: 水準数（グループ数）</li>
<li>nᵢ: 水準 i のデータ数</li>
<li>ȳᵢ.: 水準 i の平均</li>
<li>ȳ..: 全体平均</li>
</ul>
<div class="example">
<b>例:</b> 月別売上（12水準、各11年分）<br>
→ S_A = Σ 11×(月平均 - 全体平均)²
</div>''',
        'source': '統計WEB 29-3. 一元配置分散分析の流れ'
    },
    {
        'question': '''一元配置分散分析の自由度の公式は？
<div class="mnemonic">※ k = 水準数、N = 総データ数</div>''',
        'answer': '''<div class="formula">
<table>
<tr><th>要素</th><th>自由度</th></tr>
<tr><td>水準間（要因）</td><td>\\(k - 1\\)</td></tr>
<tr><td>残差（誤差）</td><td>\\(N - k\\)</td></tr>
<tr><td>全体</td><td>\\(N - 1\\)</td></tr>
</table>
</div>
<div class="example">
<b>例:</b> 12ヶ月 × 11年 = 132データ<br>
・水準間: 12 - 1 = <span class="important">11</span><br>
・残差: 132 - 12 = <span class="important">120</span>
</div>''',
        'source': 'とけたろうブログ - 一元配置分散分析'
    },
    {
        'question': '''一元配置分散分析の対立仮説 H₁ の正しい表現は？
<div class="mnemonic">※ μᵢ は各水準の母平均</div>''',
        'answer': '''<div class="formula">
<b>正しい:</b> H₁: μᵢ のうち<span class="important">少なくとも1つ</span>が異なる
</div>
<b>間違い:</b> H₁: μᵢ の<u>すべて</u>が異なる

<div class="mnemonic">
<b>重要:</b> ANOVAのF検定は「どこかに差がある」ことしか検出できない。<br>
「すべて異なる」かどうかは判定できない。
</div>

<b>帰無仮説:</b>
\\[H_0: \\mu_1 = \\mu_2 = \\cdots = \\mu_k\\]''',
        'source': '統計WEB 29-4. 一元配置分散分析の流れ'
    },

    # ===== 重回帰分析 =====
    {
        'question': '''重回帰分析の係数を解釈するときの重要なキーワードは？''',
        'answer': '''<div class="formula">
<span class="important">「他の変数を一定として」</span><br>
（ceteris paribus / その他条件一定）
</div>

<b>例:</b> 消費支出 = α₀ + α₁×定期収入 + α₂×賞与

<table>
<tr><th>係数</th><th>正しい解釈</th></tr>
<tr><td>α₁ = 0.39</td><td><b>賞与を一定として</b>、定期収入が1万円増えると消費支出が約0.39万円増える</td></tr>
<tr><td>α₂ = 0.47</td><td><b>定期収入を一定として</b>、賞与が1万円増えると消費支出が約0.47万円増える</td></tr>
</table>''',
        'source': '高知工科大学 計量経済学講義資料'
    },
    {
        'question': '''重回帰分析で係数 β₁ = 0.39 のとき、以下の解釈は正しいか？
<div class="example">
「定期収入が1%増えると消費支出が0.39%増える」
</div>''',
        'answer': '''<div class="formula">
<span class="important">誤り</span>
</div>

<b>理由:</b>
<ul>
<li>「%」の解釈は<b>対数モデル</b>（log-log model）の場合のみ有効</li>
<li>通常の線形モデルでは係数は<b>単位あたりの変化</b>を表す</li>
</ul>

<table>
<tr><th>モデル</th><th>係数の解釈</th></tr>
<tr><td>y = α + βx</td><td>xが1単位増 → yがβ単位増</td></tr>
<tr><td>log(y) = α + βlog(x)</td><td>xが1%増 → yがβ%増</td></tr>
</table>''',
        'source': '計量経済学入門 - 重回帰モデルの解釈'
    },
    {
        'question': '''単回帰分析において、予測値の平均 ȳ̂ と実測値の平均 ȳ の関係は？''',
        'answer': '''<div class="formula">
\\[\\bar{\\hat{y}} = \\bar{y}\\]
<b>予測値の平均 = 実測値の平均</b>
</div>

<b>理由:</b> 最小二乗法（OLS）の性質により、回帰直線は必ず点 (x̄, ȳ) を通る。

<div class="example">
<b>確認方法:</b><br>
ŷ = β̂₀ + β̂₁x より<br>
ȳ̂ = β̂₀ + β̂₁x̄ = ȳ
</div>

また、<b>残差の合計は常に0</b>: \\(\\sum(y_i - \\hat{y}_i) = 0\\)''',
        'source': '統計WEB - 最小二乗法の性質'
    },
    {
        'question': '''調整済み決定係数（Adjusted R²）は何のために使う？''',
        'answer': '''<div class="formula">
<b>説明変数の数が異なるモデルを比較するため</b>
</div>

<b>通常のR²の問題:</b>
<ul>
<li>変数を増やすと必ず上がる（過学習の危険）</li>
</ul>

<b>調整済みR²の特徴:</b>
<ul>
<li>変数を増やすとペナルティがかかる</li>
<li>無駄な変数を追加すると<span class="important">下がることもある</span></li>
</ul>

<div class="example">
<b>例:</b><br>
・重回帰（2変数）: Adj R² = 0.5161<br>
・単回帰（1変数）: Adj R² = 0.5261<br>
→ 単回帰の方が良いモデルの可能性
</div>''',
        'source': '統計WEB - 自由度調整済み決定係数'
    },
]

# カード追加
for card in cards_data:
    note = genanki.Note(
        model=model,
        fields=[card['question'], card['answer'], card['source']]
    )
    deck.add_note(note)

# パッケージ保存
output_path = '/Users/sasaki/statistics_review_20260128_verified.apkg'
genanki.Package(deck).write_to_file(output_path)
print(f"✅ {len(cards_data)}枚のカードを作成しました")
print(f"📁 出力: {output_path}")
