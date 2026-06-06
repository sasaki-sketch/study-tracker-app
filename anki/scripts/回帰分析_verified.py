#!/usr/bin/env python3
"""
回帰分析（第27章）- Ankiカード作成スクリプト
統計検定2級対応

検証済み情報源:
- 統計WEB (bellcurve.jp) 27-1 ~ 27-6
- とけたろうブログ
- 東京工業大学データ解析資料

作成日: 2026-01-26
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
    '統計検定2級_回帰分析',
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
    '統計検定2級::27_回帰分析'
)

# カードデータ
cards_data = [
    # カード1: 単回帰分析とは
    {
        'question': '''<b>単回帰分析とは</b>

単回帰分析の定義と目的は？回帰式の形は？''',
        'answer': '''<b>定義:</b>
1つの説明変数（独立変数）\\(x\\) から目的変数（従属変数）\\(y\\) を予測するための分析手法

<b>回帰式（回帰直線）:</b>
<div class="formula">
\\[\\hat{y} = a + bx\\]
</div>

<b>各記号:</b>
<ul>
<li>\\(\\hat{y}\\): 予測値（推定値）</li>
<li>\\(a\\): 切片（定数項）</li>
<li>\\(b\\): 回帰係数（傾き）</li>
<li>\\(x\\): 説明変数</li>
</ul>

<b>目的:</b>
<ul>
<li>\\(x\\) と \\(y\\) の関係を数式で表す</li>
<li>新しい \\(x\\) の値から \\(y\\) を予測する</li>
<li>\\(x\\) が1単位変化したときの \\(y\\) の変化量を知る</li>
</ul>

<span class="important">回帰係数 \\(b\\) の意味:</span> \\(x\\) が1増加すると \\(y\\) は \\(b\\) だけ変化する''',
        'source': '統計WEB 27-1'
    },

    # カード2: 最小二乗法の考え方
    {
        'question': '''<b>最小二乗法とは</b>

最小二乗法の考え方と、何を最小化するか？''',
        'answer': '''<b>定義:</b>
残差（予測値と実測値の差）の二乗和を最小にするように回帰係数を求める方法

<b>残差:</b>
<div class="formula">
\\[e_i = y_i - \\hat{y}_i = y_i - (a + bx_i)\\]
</div>

<b>最小化する量（残差平方和）:</b>
<div class="formula">
\\[S = \\sum_{i=1}^{n} e_i^2 = \\sum_{i=1}^{n} (y_i - a - bx_i)^2\\]
</div>

<b>なぜ二乗するか:</b>
<ul>
<li>正負の残差が相殺しないようにするため</li>
<li>大きな残差をより重くペナルティするため</li>
<li>微分して最小値を求めやすい</li>
</ul>

<span class="important">ポイント:</span>
<ul>
<li>残差の和 → 0になるので使えない</li>
<li>残差の絶対値の和 → 微分が難しい</li>
<li>残差の二乗和 → 計算しやすく、解が一意に決まる</li>
</ul>''',
        'source': '統計WEB 27-2'
    },

    # カード3: 回帰係数の公式
    {
        'question': '''<b>最小二乗法による回帰係数の公式</b>

単回帰分析の回帰係数 \\(a\\)（切片）と \\(b\\)（傾き）を求める公式は？''',
        'answer': '''<b>傾き \\(b\\) の公式:</b>
<div class="formula">
\\[b = \\frac{S_{xy}}{S_{xx}} = \\frac{\\sum(x_i - \\bar{x})(y_i - \\bar{y})}{\\sum(x_i - \\bar{x})^2}\\]
</div>

<b>別表現:</b>
<div class="formula">
\\[b = \\frac{\\text{共分散}(x, y)}{\\text{分散}(x)} = \\frac{S_{xy}}{S_x^2}\\]
</div>

<b>切片 \\(a\\) の公式:</b>
<div class="formula">
\\[a = \\bar{y} - b\\bar{x}\\]
</div>

<b>回帰係数と相関係数の関係:</b>
<div class="formula">
\\[b = r \\cdot \\frac{S_y}{S_x}\\]
</div>
（\\(r\\): 相関係数、\\(S_x, S_y\\): 標準偏差）

<span class="important">重要な性質:</span>
<ul>
<li>回帰直線は必ず点 \\((\\bar{x}, \\bar{y})\\) を通る</li>
<li>\\(b\\) と \\(r\\) は同じ符号を持つ</li>
</ul>''',
        'source': '統計WEB 27-2'
    },

    # カード4: 回帰係数の計算例
    {
        'question': '''<b>【計算問題】回帰係数</b>

以下の統計量が与えられているとき、回帰直線 \\(\\hat{y} = a + bx\\) を求めよ。

<ul>
<li>\\(\\bar{x} = 5\\), \\(\\bar{y} = 20\\)</li>
<li>\\(S_{xy} = 30\\)（共分散 × n）</li>
<li>\\(S_{xx} = 10\\)（xの偏差平方和）</li>
</ul>''',
        'answer': '''<b>傾き \\(b\\) の計算:</b>
<div class="formula">
\\[b = \\frac{S_{xy}}{S_{xx}} = \\frac{30}{10} = 3\\]
</div>

<b>切片 \\(a\\) の計算:</b>
<div class="formula">
\\[a = \\bar{y} - b\\bar{x} = 20 - 3 \\times 5 = 20 - 15 = 5\\]
</div>

<div class="example">
<b>答え:</b> \\(\\hat{y} = 5 + 3x\\)
</div>

<b>検算:</b>
点 \\((\\bar{x}, \\bar{y}) = (5, 20)\\) を代入:
\\[\\hat{y} = 5 + 3 \\times 5 = 20 \\checkmark\\]

<span class="important">解釈:</span>
<ul>
<li>\\(x = 0\\) のとき \\(y = 5\\)</li>
<li>\\(x\\) が1増加すると \\(y\\) は3増加する</li>
</ul>''',
        'source': '統計WEB 27-2'
    },

    # カード5: 予測値と残差
    {
        'question': '''<b>予測値と残差</b>

回帰分析における予測値、残差、残差平方和の定義は？''',
        'answer': '''<b>予測値（推定値）:</b>
<div class="formula">
\\[\\hat{y}_i = a + bx_i\\]
</div>
回帰式に \\(x_i\\) を代入して得られる \\(y\\) の推定値

<b>残差:</b>
<div class="formula">
\\[e_i = y_i - \\hat{y}_i\\]
</div>
実測値と予測値の差

<b>残差平方和（SSE）:</b>
<div class="formula">
\\[SSE = \\sum_{i=1}^{n} e_i^2 = \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2\\]
</div>

<b>残差の性質:</b>
<ul>
<li>残差の和は0: \\(\\sum e_i = 0\\)</li>
<li>残差と \\(x\\) の相関は0</li>
<li>残差と予測値の相関は0</li>
</ul>

<span class="important">残差分析:</span>
残差をプロットして、回帰モデルの妥当性を確認する
<ul>
<li>パターンがない → モデルは適切</li>
<li>曲線的パターン → 非線形関係の可能性</li>
</ul>''',
        'source': '統計WEB 27-4'
    },

    # カード6: 変動の分解
    {
        'question': '''<b>変動の分解（回帰分析）</b>

回帰分析における全変動、回帰変動、残差変動の関係は？''',
        'answer': '''<b>変動の分解:</b>
<div class="formula">
\\[\\underbrace{\\sum(y_i - \\bar{y})^2}_{\\text{全変動 (SST)}} = \\underbrace{\\sum(\\hat{y}_i - \\bar{y})^2}_{\\text{回帰変動 (SSR)}} + \\underbrace{\\sum(y_i - \\hat{y}_i)^2}_{\\text{残差変動 (SSE)}}\\]
</div>

<b>各変動の意味:</b>
<table>
<tr><th>変動</th><th>記号</th><th>意味</th></tr>
<tr><td>全変動</td><td>SST</td><td>\\(y\\) の総ばらつき</td></tr>
<tr><td>回帰変動</td><td>SSR</td><td>回帰で説明できる部分</td></tr>
<tr><td>残差変動</td><td>SSE</td><td>回帰で説明できない部分</td></tr>
</table>

<b>関係式:</b>
<div class="formula">
\\[SST = SSR + SSE\\]
</div>

<span class="important">覚え方:</span>
<ul>
<li>SST: Total（全体）</li>
<li>SSR: Regression（回帰）</li>
<li>SSE: Error（誤差/残差）</li>
</ul>''',
        'source': '統計WEB 27-5'
    },

    # カード7: 決定係数
    {
        'question': '''<b>決定係数（\\(R^2\\)）</b>

決定係数の定義、公式、解釈は？''',
        'answer': '''<b>定義:</b>
回帰モデルがデータの変動をどれだけ説明できているかを表す指標

<b>公式:</b>
<div class="formula">
\\[R^2 = \\frac{SSR}{SST} = \\frac{\\text{回帰変動}}{\\text{全変動}}\\]
</div>

<b>別表現:</b>
<div class="formula">
\\[R^2 = 1 - \\frac{SSE}{SST} = 1 - \\frac{\\text{残差変動}}{\\text{全変動}}\\]
</div>

<b>性質:</b>
<ul>
<li>範囲: \\(0 \\leq R^2 \\leq 1\\)</li>
<li>\\(R^2 = 1\\): 完全に説明できる（全ての点が直線上）</li>
<li>\\(R^2 = 0\\): 全く説明できない</li>
</ul>

<b>単回帰分析での特別な性質:</b>
<div class="formula">
\\[R^2 = r^2\\]
（決定係数 = 相関係数の二乗）
</div>

<span class="important">解釈例:</span> \\(R^2 = 0.8\\) → 「\\(y\\) の変動の80%は \\(x\\) で説明できる」''',
        'source': '統計WEB 27-5'
    },

    # カード8: 重回帰分析
    {
        'question': '''<b>重回帰分析とは</b>

重回帰分析の定義と回帰式の形は？単回帰分析との違いは？''',
        'answer': '''<b>定義:</b>
複数の説明変数 \\(x_1, x_2, \\ldots, x_p\\) から目的変数 \\(y\\) を予測する分析

<b>回帰式:</b>
<div class="formula">
\\[\\hat{y} = b_0 + b_1 x_1 + b_2 x_2 + \\cdots + b_p x_p\\]
</div>

<b>各記号:</b>
<ul>
<li>\\(b_0\\): 切片（定数項）</li>
<li>\\(b_1, b_2, \\ldots, b_p\\): 偏回帰係数</li>
<li>\\(x_1, x_2, \\ldots, x_p\\): 説明変数</li>
</ul>

<b>偏回帰係数の意味:</b>
<div class="example">
\\(b_1\\) = 「他の説明変数を固定したとき、\\(x_1\\) が1単位増加すると \\(y\\) が \\(b_1\\) だけ変化する」
</div>

<b>単回帰との違い:</b>
<table>
<tr><th></th><th>単回帰</th><th>重回帰</th></tr>
<tr><td>説明変数</td><td>1つ</td><td>複数</td></tr>
<tr><td>係数</td><td>回帰係数</td><td>偏回帰係数</td></tr>
<tr><td>\\(R^2 = r^2\\)</td><td>成立</td><td>成立しない</td></tr>
</table>''',
        'source': '統計WEB 27-3'
    },

    # カード9: 自由度調整済み決定係数
    {
        'question': '''<b>自由度調整済み決定係数</b>

なぜ自由度調整済み決定係数が必要か？公式は？''',
        'answer': '''<b>問題点:</b>
決定係数 \\(R^2\\) は説明変数を増やすと必ず大きくなる
→ 無意味な変数を追加しても \\(R^2\\) は上がってしまう

<b>解決策: 自由度調整済み決定係数</b>
<div class="formula">
\\[\\bar{R}^2 = 1 - \\frac{SSE / (n - p - 1)}{SST / (n - 1)}\\]
</div>

<b>展開した形:</b>
<div class="formula">
\\[\\bar{R}^2 = 1 - \\frac{n - 1}{n - p - 1}(1 - R^2)\\]
</div>

<b>各記号:</b>
<ul>
<li>\\(n\\): サンプルサイズ</li>
<li>\\(p\\): 説明変数の数</li>
</ul>

<b>性質:</b>
<ul>
<li>無意味な変数を追加すると \\(\\bar{R}^2\\) は下がる</li>
<li>説明変数が1つのとき: \\(\\bar{R}^2 < R^2\\)</li>
<li>\\(\\bar{R}^2\\) は負の値をとることもある</li>
</ul>

<span class="important">使い分け:</span> モデル比較には \\(\\bar{R}^2\\) を使用''',
        'source': '統計WEB 27-5'
    },

    # カード10: 回帰係数のt検定
    {
        'question': '''<b>回帰係数のt検定</b>

回帰係数が有意かどうかを検定するt検定の仮説、検定統計量、自由度は？''',
        'answer': '''<b>仮説:</b>
<ul>
<li>帰無仮説: \\(H_0: b_j = 0\\)（係数は0）</li>
<li>対立仮説: \\(H_1: b_j \\neq 0\\)（係数は0ではない）</li>
</ul>

<b>検定統計量:</b>
<div class="formula">
\\[t = \\frac{b_j}{SE(b_j)} = \\frac{\\text{回帰係数}}{\\text{標準誤差}}\\]
</div>

<b>自由度:</b>
<div class="formula">
単回帰: \\(df = n - 2\\)
重回帰: \\(df = n - p - 1\\)
</div>
（\\(n\\): サンプルサイズ、\\(p\\): 説明変数の数）

<b>判定:</b>
\\(|t| > t_{\\alpha/2}(df)\\) なら係数は有意

<span class="important">重要:</span>
<ul>
<li>\\(t\\) 値 = 係数 / 標準誤差</li>
<li>自由度 = サンプル数 − 推定するパラメータ数</li>
<li>t値が大きい → その変数は重要</li>
</ul>''',
        'source': '統計WEB 27-6, とけたろうブログ'
    },

    # カード11: t検定の計算例
    {
        'question': '''<b>【計算問題】回帰係数のt検定</b>

重回帰分析の結果:
<ul>
<li>サンプルサイズ: \\(n = 20\\)</li>
<li>説明変数: 2個</li>
<li>\\(x_1\\) の係数: \\(b_1 = 3.5\\)</li>
<li>\\(b_1\\) の標準誤差: \\(SE = 1.0\\)</li>
</ul>

有意水準5%で \\(b_1\\) は有意か？
（参考: \\(t_{0.025}(17) = 2.110\\)）''',
        'answer': '''<b>仮説:</b>
<ul>
<li>\\(H_0: b_1 = 0\\)</li>
<li>\\(H_1: b_1 \\neq 0\\)</li>
</ul>

<b>自由度の計算:</b>
\\[df = n - p - 1 = 20 - 2 - 1 = 17\\]

<b>t値の計算:</b>
<div class="formula">
\\[t = \\frac{b_1}{SE(b_1)} = \\frac{3.5}{1.0} = 3.5\\]
</div>

<b>判定:</b>
\\(|t| = 3.5 > 2.110\\) → <b>棄却域に入る</b>

<div class="example">
<b>結論:</b> 有意水準5%で帰無仮説を棄却する。
回帰係数 \\(b_1\\) は<b>有意に0と異なる</b>。
→ \\(x_1\\) は \\(y\\) の予測に有意に貢献している。
</div>''',
        'source': '統計WEB 27-6'
    },

    # カード12: F検定（回帰全体の有意性）
    {
        'question': '''<b>回帰のF検定</b>

回帰モデル全体の有意性を検定するF検定の仮説と検定統計量は？''',
        'answer': '''<b>仮説:</b>
<ul>
<li>帰無仮説: \\(H_0: b_1 = b_2 = \\cdots = b_p = 0\\)
<br>（全ての回帰係数が0）</li>
<li>対立仮説: \\(H_1\\): 少なくとも1つの \\(b_j \\neq 0\\)</li>
</ul>

<b>検定統計量:</b>
<div class="formula">
\\[F = \\frac{SSR / p}{SSE / (n - p - 1)} = \\frac{\\text{回帰の平均平方}}{\\text{残差の平均平方}}\\]
</div>

<b>自由度:</b>
<ul>
<li>第1自由度（分子）: \\(p\\)（説明変数の数）</li>
<li>第2自由度（分母）: \\(n - p - 1\\)</li>
</ul>

<b>分散分析表:</b>
<table>
<tr><th>要因</th><th>平方和</th><th>自由度</th><th>平均平方</th></tr>
<tr><td>回帰</td><td>SSR</td><td>p</td><td>SSR/p</td></tr>
<tr><td>残差</td><td>SSE</td><td>n-p-1</td><td>SSE/(n-p-1)</td></tr>
<tr><td>全体</td><td>SST</td><td>n-1</td><td></td></tr>
</table>

<span class="important">t検定との違い:</span>
<ul>
<li>t検定: 個々の係数の検定</li>
<li>F検定: モデル全体の検定</li>
</ul>''',
        'source': '統計WEB 27-6'
    },

    # カード13: 単回帰のF検定とt検定の関係
    {
        'question': '''<b>単回帰分析におけるF検定とt検定の関係</b>

単回帰分析では、F検定とt検定にどのような関係があるか？''',
        'answer': '''<b>関係:</b>
<div class="formula">
単回帰分析（説明変数が1つ）では:
\\[F = t^2\\]
</div>

<b>意味:</b>
<ul>
<li>単回帰では、回帰係数のt検定と回帰のF検定は<b>等価</b></li>
<li>どちらを使っても同じ結論になる</li>
</ul>

<b>自由度の対応:</b>
<ul>
<li>t検定: 自由度 \\(n - 2\\)</li>
<li>F検定: 自由度 \\((1, n - 2)\\)</li>
</ul>

<b>臨界値の対応:</b>
<div class="formula">
\\[F_{\\alpha}(1, df) = \\left( t_{\\alpha/2}(df) \\right)^2\\]
</div>

<b>例:</b>
\\(t_{0.025}(10) = 2.228\\) のとき
\\[F_{0.05}(1, 10) = (2.228)^2 \\approx 4.96\\]

<span class="important">重回帰では:</span> この関係は成り立たない（変数が複数あるため）''',
        'source': '統計WEB 27-6'
    },

    # カード14: 回帰分析のまとめ
    {
        'question': '''<b>回帰分析のまとめ</b>

第27章で学んだ回帰分析の主要な公式をまとめよ。''',
        'answer': '''<b>1. 回帰係数（最小二乗法）:</b>
<div class="formula">
\\[b = \\frac{S_{xy}}{S_{xx}}, \\quad a = \\bar{y} - b\\bar{x}\\]
</div>

<b>2. 決定係数:</b>
<div class="formula">
\\[R^2 = \\frac{SSR}{SST} = 1 - \\frac{SSE}{SST}\\]
単回帰: \\(R^2 = r^2\\)
</div>

<b>3. 自由度調整済み決定係数:</b>
<div class="formula">
\\[\\bar{R}^2 = 1 - \\frac{n-1}{n-p-1}(1-R^2)\\]
</div>

<b>4. t検定（係数の検定）:</b>
<div class="formula">
\\[t = \\frac{b_j}{SE(b_j)}, \\quad df = n - p - 1\\]
</div>

<b>5. F検定（回帰の検定）:</b>
<div class="formula">
\\[F = \\frac{SSR/p}{SSE/(n-p-1)}, \\quad df = (p, n-p-1)\\]
</div>

<b>自由度の覚え方:</b>
<table>
<tr><th>分析</th><th>回帰係数のt検定</th></tr>
<tr><td>単回帰</td><td>\\(n - 2\\)</td></tr>
<tr><td>重回帰(p変数)</td><td>\\(n - p - 1\\)</td></tr>
</table>''',
        'source': '統計WEB 27章'
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
output_file = '回帰分析_verified.apkg'
genanki.Package(deck).write_to_file(output_file)

print(f"✅ Ankiパッケージを作成しました: {output_file}")
print(f"📊 カード枚数: {len(cards_data)}枚")
print("\n作成されたカード:")
for i, card in enumerate(cards_data, 1):
    title = card['question'].split('\n')[0].replace('<b>', '').replace('</b>', '')
    print(f"  {i}. {title}")
