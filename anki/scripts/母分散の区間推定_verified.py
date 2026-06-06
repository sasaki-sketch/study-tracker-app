#!/usr/bin/env python3
"""
母分散の区間推定 - Ankiカード作成スクリプト
統計検定2級対応

検証済み情報源:
- 統計WEB (bellcurve.jp)
- Wikipedia カイ二乗分布

作成日: 2026-01-25
"""

import genanki
import random
from anki_card_css_template import CARD_CSS

# 一意のモデルIDとデッキID
MODEL_ID = random.randrange(1 << 30, 1 << 31)
DECK_ID = random.randrange(1 << 30, 1 << 31)

# カードモデル（MathJax対応）
model = genanki.Model(
    MODEL_ID,
    '統計検定2級_母分散の区間推定',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Source'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '''
<div class="question">{{Question}}</div>
''',
            'afmt': '''
<div class="question">{{Question}}</div>
<hr id="answer">
<div class="answer">{{Answer}}</div>
<div class="source">出典: {{Source}}</div>
''',
        },
    ],
    css=CARD_CSS
)

# デッキ作成
deck = genanki.Deck(
    DECK_ID,
    '統計検定2級::22_母分散の区間推定'
)

# カードデータ
cards_data = [
    # カード1: カイ二乗分布の定義
    {
        'question': '''<b>カイ二乗分布の定義</b>

カイ二乗分布（\\(\\chi^2\\) 分布）はどのように定義されるか？''',
        'answer': '''<b>定義:</b>

\\(Z_1, Z_2, \\ldots, Z_k\\) が互いに<b>独立</b>で<b>標準正規分布 \\(N(0,1)\\)</b> に従うとき、

<div class="formula">
\\[\\chi^2 = Z_1^2 + Z_2^2 + \\cdots + Z_k^2 = \\sum_{i=1}^{k} Z_i^2\\]
</div>

が従う確率分布を<b>自由度 \\(k\\) のカイ二乗分布</b>という。

記号: \\(\\chi^2(k)\\) または \\(\\chi^2_k\\)

<b>ポイント:</b>
<ul>
<li>標準正規分布に従う確率変数の<b>二乗和</b></li>
<li>自由度 = 足し合わせる変数の個数</li>
<li>常に \\(\\chi^2 \\geq 0\\)（二乗和なので非負）</li>
</ul>''',
        'source': '統計WEB 22-1'
    },

    # カード2: カイ二乗分布の期待値と分散
    {
        'question': '''<b>カイ二乗分布の期待値と分散</b>

自由度 \\(k\\) のカイ二乗分布 \\(\\chi^2(k)\\) に従う確率変数 \\(X\\) の期待値と分散は？''',
        'answer': '''<div class="formula">
<b>期待値:</b>
\\[E(X) = k\\]

<b>分散:</b>
\\[V(X) = 2k\\]
</div>

<b>覚え方:</b>
<ul>
<li>期待値 = 自由度そのもの</li>
<li>分散 = 自由度の2倍</li>
</ul>

<b>例: 自由度10のカイ二乗分布</b>
<ul>
<li>期待値: \\(E(X) = 10\\)</li>
<li>分散: \\(V(X) = 20\\)</li>
<li>標準偏差: \\(\\sigma = \\sqrt{20} \\approx 4.47\\)</li>
</ul>

<span class="important">注意:</span> 自由度が大きくなると、期待値も分散も大きくなる''',
        'source': '統計WEB 22-1'
    },

    # カード3: カイ二乗分布の再生性
    {
        'question': '''<b>カイ二乗分布の再生性</b>

\\(X_1 \\sim \\chi^2(k_1)\\) と \\(X_2 \\sim \\chi^2(k_2)\\) が独立のとき、\\(X_1 + X_2\\) はどのような分布に従うか？''',
        'answer': '''<b>再生性（加法性）:</b>

<div class="formula">
\\(X_1\\) と \\(X_2\\) が独立で、それぞれ \\(\\chi^2(k_1)\\)、\\(\\chi^2(k_2)\\) に従うとき、

\\[X_1 + X_2 \\sim \\chi^2(k_1 + k_2)\\]
</div>

<b>意味:</b>
<ul>
<li>カイ二乗分布に従う独立な確率変数の和も、カイ二乗分布に従う</li>
<li>和の自由度 = 各自由度の和</li>
</ul>

<b>例:</b>
\\(X_1 \\sim \\chi^2(3)\\) と \\(X_2 \\sim \\chi^2(5)\\) が独立なら

\\[X_1 + X_2 \\sim \\chi^2(8)\\]

<span class="important">注意:</span> 独立性が必要条件''',
        'source': '統計WEB 22-1'
    },

    # カード4: カイ二乗分布の形状
    {
        'question': '''<b>カイ二乗分布の形状の特徴</b>

カイ二乗分布のグラフはどのような形状か？自由度によってどう変化するか？''',
        'answer': '''<b>形状の特徴:</b>
<ul>
<li><b>非対称</b>（正規分布・t分布と異なり左右対称ではない）</li>
<li><b>右に裾が長い</b>（右に歪んだ分布）</li>
<li>\\(x \\geq 0\\) の範囲のみ（負の値をとらない）</li>
</ul>

<b>自由度による変化:</b>
<ul>
<li>自由度が小さい → 左に偏った形状</li>
<li>自由度が大きい → より対称に近づく（正規分布に近似）</li>
<li>自由度 \\(k \\to \\infty\\) で正規分布 \\(N(k, 2k)\\) に近づく</li>
</ul>

<span class="important">重要:</span> 左右非対称のため、信頼区間を求める際は上側・下側それぞれの臨界値が必要''',
        'source': '統計WEB 22-1, 22-2'
    },

    # カード5: カイ二乗分布表の読み方
    {
        'question': '''<b>カイ二乗分布表の読み方</b>

カイ二乗分布表で \\(\\chi^2_{0.025}(9) = 19.02\\) とはどういう意味か？''',
        'answer': '''<b>記号の意味:</b>

\\(\\chi^2_{\\alpha}(k)\\) = 自由度 \\(k\\) のカイ二乗分布において、<b>上側確率が \\(\\alpha\\)</b> となる点

<div class="formula">
\\[P(X > \\chi^2_{\\alpha}(k)) = \\alpha\\]
</div>

<b>例: \\(\\chi^2_{0.025}(9) = 19.02\\)</b>
<ul>
<li>自由度9のカイ二乗分布において</li>
<li>「\\(X > 19.02\\)」となる確率が 2.5%（= 0.025）</li>
<li>これは95%信頼区間の<b>上側臨界値</b></li>
</ul>

<b>95%信頼区間で必要な値（自由度9）:</b>
<ul>
<li>上側2.5%点: \\(\\chi^2_{0.025}(9) = 19.02\\)</li>
<li>下側2.5%点: \\(\\chi^2_{0.975}(9) = 2.70\\)</li>
</ul>

<span class="important">注意:</span> 下側の点は「上側97.5%点」として表から読む''',
        'source': '統計WEB 22-2'
    },

    # カード6: 不偏分散とカイ二乗分布の関係
    {
        'question': '''<b>不偏分散とカイ二乗分布の関係</b>

正規母集団から抽出した標本の不偏分散 \\(s^2\\) とカイ二乗分布の関係は？''',
        'answer': '''<b>重要な定理:</b>

母集団が正規分布 \\(N(\\mu, \\sigma^2)\\) に従うとき、サンプルサイズ \\(n\\) の標本から計算した不偏分散 \\(s^2\\) について、

<div class="formula">
\\[\\frac{(n-1)s^2}{\\sigma^2} \\sim \\chi^2(n-1)\\]
</div>

<b>意味:</b>
<ul>
<li>不偏分散を母分散で割り、(n-1)倍したものは自由度(n-1)のカイ二乗分布に従う</li>
<li>この関係を利用して母分散の区間推定ができる</li>
</ul>

<b>自由度が (n-1) になる理由:</b>
不偏分散の計算で標本平均 \\(\\bar{X}\\) を使うため、1つの自由度が失われる

<span class="important">前提条件:</span> 母集団が正規分布に従うこと''',
        'source': '統計WEB 22-3'
    },

    # カード7: 母分散の信頼区間の公式
    {
        'question': '''<b>母分散の信頼区間の公式</b>

正規母集団の母分散 \\(\\sigma^2\\) の信頼係数 \\((1-\\alpha)\\) の信頼区間を求める公式は？''',
        'answer': '''<div class="formula">
\\[\\frac{(n-1)s^2}{\\chi^2_{\\alpha/2}(n-1)} \\leq \\sigma^2 \\leq \\frac{(n-1)s^2}{\\chi^2_{1-\\alpha/2}(n-1)}\\]
</div>

<b>各記号:</b>
<ul>
<li>\\(n\\): サンプルサイズ</li>
<li>\\(s^2\\): 不偏分散</li>
<li>\\(\\chi^2_{\\alpha/2}(n-1)\\): 上側 \\(\\alpha/2\\) 点</li>
<li>\\(\\chi^2_{1-\\alpha/2}(n-1)\\): 下側 \\(\\alpha/2\\) 点（= 上側 \\((1-\\alpha/2)\\) 点）</li>
</ul>

<b>95%信頼区間の場合 (\\(\\alpha = 0.05\\)):</b>
<div class="formula">
\\[\\frac{(n-1)s^2}{\\chi^2_{0.025}(n-1)} \\leq \\sigma^2 \\leq \\frac{(n-1)s^2}{\\chi^2_{0.975}(n-1)}\\]
</div>

<span class="important">注意:</span> 分母の位置に注意！大きい臨界値が下限、小さい臨界値が上限''',
        'source': '統計WEB 22-3'
    },

    # カード8: 母分散の信頼区間 計算例
    {
        'question': '''<b>【計算問題】母分散の信頼区間</b>

正規母集団から10個の標本を抽出したところ、不偏分散は \\(s^2 = 2.5\\) であった。

母分散 \\(\\sigma^2\\) の<b>95%信頼区間</b>を求めよ。

（参考）自由度9のカイ二乗分布:
\\(\\chi^2_{0.025}(9) = 19.02\\)、\\(\\chi^2_{0.975}(9) = 2.70\\)''',
        'answer': '''<b>与えられた値:</b>
<ul>
<li>サンプルサイズ: \\(n = 10\\)</li>
<li>不偏分散: \\(s^2 = 2.5\\)</li>
<li>自由度: \\(n - 1 = 9\\)</li>
</ul>

<b>公式に代入:</b>
<div class="formula">
\\[\\frac{(n-1)s^2}{\\chi^2_{0.025}(9)} \\leq \\sigma^2 \\leq \\frac{(n-1)s^2}{\\chi^2_{0.975}(9)}\\]
</div>

<b>計算:</b>
\\[\\frac{9 \\times 2.5}{19.02} \\leq \\sigma^2 \\leq \\frac{9 \\times 2.5}{2.70}\\]
\\[\\frac{22.5}{19.02} \\leq \\sigma^2 \\leq \\frac{22.5}{2.70}\\]

<div class="example">
<b>答え: \\(1.18 \\leq \\sigma^2 \\leq 8.33\\)</b>
</div>

<span class="important">ポイント:</span> 分母が大きい方（19.02）で割ると下限、小さい方（2.70）で割ると上限になる''',
        'source': '統計WEB 22-4'
    },

    # カード9: 母標準偏差の信頼区間
    {
        'question': '''<b>母標準偏差の信頼区間</b>

母分散の95%信頼区間が \\(1.18 \\leq \\sigma^2 \\leq 8.33\\) のとき、母標準偏差 \\(\\sigma\\) の95%信頼区間は？''',
        'answer': '''<b>方法:</b> 母分散の信頼区間の両端の平方根をとる

<div class="formula">
\\[\\sqrt{1.18} \\leq \\sigma \\leq \\sqrt{8.33}\\]
</div>

<b>計算:</b>
\\[1.09 \\leq \\sigma \\leq 2.89\\]

<div class="example">
<b>答え: \\(1.09 \\leq \\sigma \\leq 2.89\\)</b>
</div>

<b>一般公式:</b>
<div class="formula">
\\[\\sqrt{\\frac{(n-1)s^2}{\\chi^2_{\\alpha/2}(n-1)}} \\leq \\sigma \\leq \\sqrt{\\frac{(n-1)s^2}{\\chi^2_{1-\\alpha/2}(n-1)}}\\]
</div>

<span class="important">注意:</span> 平方根をとるため、\\(\\sigma > 0\\) の範囲で考える''',
        'source': '統計WEB 22-4'
    },

    # カード10: 母平均の推定との違い
    {
        'question': '''<b>母分散の区間推定と母平均の区間推定の違い</b>

母分散の区間推定で使う分布は？母平均の区間推定との違いは？''',
        'answer': '''<b>使用する分布の違い:</b>

<table>
<tr><th>推定対象</th><th>使用する分布</th></tr>
<tr><td>母平均（母分散既知）</td><td>正規分布</td></tr>
<tr><td>母平均（母分散未知）</td><td>t分布</td></tr>
<tr><td><b>母分散</b></td><td><b>カイ二乗分布</b></td></tr>
</table>

<b>信頼区間の形の違い:</b>
<ul>
<li><b>母平均:</b> \\(\\bar{X} \\pm\\) （誤差の幅）→ <b>対称</b></li>
<li><b>母分散:</b> 分数の形 → <b>非対称</b></li>
</ul>

<b>臨界値の違い:</b>
<ul>
<li>正規分布・t分布: 1つの臨界値で両側（対称なので）</li>
<li>カイ二乗分布: 上側・下側の2つの臨界値が必要（非対称）</li>
</ul>

<span class="important">重要:</span> 母分散の推定では母集団の正規性が必要''',
        'source': '統計WEB 22-3'
    },
]

# カードをデッキに追加
for card_data in cards_data:
    note = genanki.Note(
        model=model,
        fields=[
            card_data['question'],
            card_data['answer'],
            card_data['source']
        ]
    )
    deck.add_note(note)

# パッケージとして保存
output_file = '母分散の区間推定_verified.apkg'
genanki.Package(deck).write_to_file(output_file)

print(f"✅ Ankiパッケージを作成しました: {output_file}")
print(f"📊 カード枚数: {len(cards_data)}枚")
print("\n作成されたカード:")
for i, card in enumerate(cards_data, 1):
    title = card['question'].split('\n')[0].replace('<b>', '').replace('</b>', '')
    print(f"  {i}. {title}")
