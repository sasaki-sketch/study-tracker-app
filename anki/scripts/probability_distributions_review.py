#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級 Ankiカード: 確率分布（復習用）
学習済み範囲: 確率変数、確率分布、期待値、二項分布、ポアソン分布、幾何分布
作成日: 2026-01-16
出典: 統計WEB「統計学の時間」
"""

import genanki
import random

# デッキID（ランダム生成）
DECK_ID = random.randrange(1 << 30, 1 << 31)

# モデルID（ランダム生成）
MODEL_ID = random.randrange(1 << 30, 1 << 31)

# Ankiモデル定義
model = genanki.Model(
    MODEL_ID,
    '統計検定2級モデル',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
    css='''
        .card {
            font-family: "Hiragino Kaku Gothic ProN", "ヒラギノ角ゴ ProN", arial;
            font-size: 20px;
            text-align: left;
            color: black;
            background-color: white;
        }
    '''
)

# デッキ作成
deck = genanki.Deck(
    DECK_ID,
    '統計検定2級::確率分布（復習用）'
)

# ========================================
# カード1: 確率変数と確率分布
# ========================================
card1 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【確率変数と確率分布】確率変数とは？確率分布とは？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>確率変数（Random Variable）:</b><br>
ある変数の値をとる確率が存在する変数のこと<br>
例: サイコロの出目、コイン投げの結果<br>
<br>

<b>確率分布（Probability Distribution）:</b><br>
確率変数がとる値と、その値をとる確率の対応関係<br>
<br>

<hr>

<b>具体例:</b><br>
■ サイコロ<br>
・確率変数 X = 出目（1,2,3,4,5,6）<br>
・確率分布: P(X=1) = P(X=2) = ... = P(X=6) = 1/6<br>
<br>

■ コイン<br>
・確率変数 X = 結果（表=1, 裏=0）<br>
・確率分布: P(X=1) = P(X=0) = 1/2<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
・確率変数は「確率を持つ変数」<br>
・確率分布は「値と確率の対応表」<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計WEB「11-1. 確率変数と確率分布」<br>
https://bellcurve.jp/statistics/course/6596.html
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'probability', 'review']
)
deck.add_note(card1)

# ========================================
# カード2: 離散型と連続型確率分布
# ========================================
card2 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【確率分布の種類】離散型と連続型の違いは？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>離散型確率分布（Discrete）:</b><br>
とびとびの値をとる変数の確率分布<br>
確率を「確率質量関数」で表す<br>
<br>

<b>連続型確率分布（Continuous）:</b><br>
連続した値をとる変数の確率分布<br>
確率を「確率密度関数」で表す<br>
<br>

<hr>

<b>具体例:</b><br>

<table border="1" cellpadding="8" style="border-collapse:collapse; width:100%;">
<tr>
<th>種類</th>
<th>変数例</th>
<th>代表的分布</th>
</tr>
<tr>
<td><b>離散型</b></td>
<td>サイコロの目、人数、回数</td>
<td>二項分布、ポアソン分布、幾何分布</td>
</tr>
<tr>
<td><b>連続型</b></td>
<td>身長、体重、温度、時間</td>
<td>正規分布、指数分布</td>
</tr>
</table>
<br>

<hr>

<b>【重要ポイント】</b><br>
・離散型: 「0,1,2,3...」など数えられる<br>
・連続型: 「50kgと51kgの間に無数の値」<br>
・試験では「どちらの分布か」の判断が重要<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計WEB「11-2. 離散型確率分布」「11-3. 連続型確率分布」
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'probability', 'review']
)
deck.add_note(card2)

# ========================================
# カード3: 期待値の定義
# ========================================
card3 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【期待値】期待値E(X)の定義と計算方法は？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
確率変数がとる値と、その確率の積を全て足し合わせたもの<br>
= 確率変数の平均値<br>
<br>

<b>公式:</b><br>
<b>■ 離散型:</b><br>
\\[E(X) = \\sum_{i=1}^{n} x_i \\cdot p_i\\]
<br>

<b>■ 連続型:</b><br>
\\[E(X) = \\int_{-\\infty}^{\\infty} x f(x) dx\\]
<br>

<hr>

<b>具体例:</b><br>
<b>サイコロの期待値:</b><br>
\\[E(X) = 1 \\cdot \\frac{1}{6} + 2 \\cdot \\frac{1}{6} + 3 \\cdot \\frac{1}{6} + 4 \\cdot \\frac{1}{6} + 5 \\cdot \\frac{1}{6} + 6 \\cdot \\frac{1}{6}\\]
\\[= \\frac{1+2+3+4+5+6}{6} = \\frac{21}{6} = 3.5\\]
<br>

<hr>

<b>【重要ポイント】</b><br>
・期待値 = 平均値（確率による重み付き平均）<br>
・サイコロの期待値3.5は「実際には出ない値」<br>
・記号: E(X) または μ（ミュー）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計WEB「12-3. 確率変数の期待値」<br>
https://bellcurve.jp/statistics/course/6712.html
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'expectation', 'review']
)
deck.add_note(card3)

# ========================================
# カード4: 期待値の性質（線形性）
# ========================================
card4 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【期待値の性質】期待値の4つの重要な性質は？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>期待値の4つの性質:</b><br>
<br>

<b>1. 定数の期待値:</b><br>
\\[E(C) = C\\]
定数の期待値は定数そのもの<br>
<br>

<b>2. 加法性:</b><br>
\\[E(X + C) = E(X) + C\\]
確率変数に定数を足すと、期待値も同じだけ増える<br>
<br>

<b>3. スカラー倍:</b><br>
\\[E(kX) = k \\cdot E(X)\\]
確率変数をk倍すると、期待値もk倍になる<br>
<br>

<b>4. 線形性（和の性質）:</b><br>
\\[E(X + Y) = E(X) + E(Y)\\]
和の期待値は、期待値の和<br>
<b>※ XとYが独立でなくても成立！</b><br>
<br>

<hr>

<b>具体例:</b><br>
サイコロ2回投げる場合（X=1回目、Y=2回目）<br>
\\[E(X+Y) = E(X) + E(Y) = 3.5 + 3.5 = 7\\]
<br>

<hr>

<b>【重要ポイント】</b><br>
・性質4は「独立性不要」（超重要！）<br>
・これらの性質で計算が大幅に簡単になる<br>
・統計検定2級で頻出<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計WEB「12-4. 期待値の性質」<br>
https://bellcurve.jp/statistics/course/6714.html
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'expectation', 'review']
)
deck.add_note(card4)

# ========================================
# カード5: 二項分布
# ========================================
card5 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【二項分布】二項分布B(n, p)の定義、公式、期待値・分散は？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
成功確率pのベルヌーイ試行をn回行ったとき、<br>
成功回数Xが従う確率分布<br>
記号: \\(X \\sim B(n, p)\\)<br>
<br>

<b>確率質量関数:</b><br>
\\[P(X=k) = {}_n C_k \\cdot p^k (1-p)^{n-k}\\]
\\[(k=0,1,2,\\ldots,n)\\]
<br>

<b>期待値と分散:</b><br>
\\[E(X) = np\\]
\\[V(X) = np(1-p)\\]
<br>

<hr>

<b>具体例:</b><br>
<b>コイン10回投げて表が出る回数:</b><br>
n=10, p=0.5 → B(10, 0.5)<br>
・期待値: E(X) = 10×0.5 = 5回<br>
・分散: V(X) = 10×0.5×0.5 = 2.5<br>
<br>

<b>表が3回出る確率:</b><br>
\\[P(X=3) = {}_{10}C_3 \\cdot 0.5^3 \\cdot 0.5^7\\]
\\[= 120 \\cdot 0.125 \\cdot 0.008 \\approx 0.117\\]
<br>

<hr>

<b>【重要ポイント・使いどころ】</b><br>
・「n回中k回成功」の確率を求める<br>
・成功/失敗の2択、確率一定、独立試行<br>
・例: コイン、サイコロ、製品の良品率<br>
・統計検定2級で最頻出の分布<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計WEB「13-1. 二項分布」「13-2. 二項分布の期待値と分散」<br>
https://bellcurve.jp/statistics/course/6979.html
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'binomial', 'review']
)
deck.add_note(card5)

# ========================================
# カード6: ポアソン分布
# ========================================
card6 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【ポアソン分布】ポアソン分布Po(λ)の定義、公式、期待値・分散は？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
単位時間（単位区間）に平均λ回起こる稀な事象が、<br>
k回起こる確率を表す分布<br>
記号: \\(X \\sim Po(\\lambda)\\)<br>
<br>

<b>確率質量関数:</b><br>
\\[P(X=k) = \\frac{\\lambda^k e^{-\\lambda}}{k!}\\]
\\[(k=0,1,2,\\ldots)\\]
<br>

<b>期待値と分散:</b><br>
\\[E(X) = \\lambda\\]
\\[V(X) = \\lambda\\]
<b>※ 期待値と分散が等しい（ポアソン分布の特徴）</b><br>
<br>

<hr>

<b>具体例:</b><br>
<b>1年間（365日）に平均20日雪が降る:</b><br>
λ=20 → Po(20)<br>
・期待値: E(X) = 20日<br>
・分散: V(X) = 20<br>
<br>

<b>ちょうど25日降る確率:</b><br>
\\[P(X=25) = \\frac{20^{25} e^{-20}}{25!}\\]
（実際の計算は電卓または分布表を使用）<br>
<br>

<hr>

<b>【重要ポイント・使いどころ】</b><br>
・「稀な事象」の発生回数<br>
・例: 事故件数、不良品数、電話の着信数<br>
・二項分布B(n,p)でn大、p小の場合の近似<br>
・λ=npとして近似可能<br>
・期待値=分散（この特徴で識別可能）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計WEB「13-3. ポアソン分布」「13-4. ポアソン分布の期待値と分散」<br>
https://bellcurve.jp/statistics/course/6984.html
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'poisson', 'review']
)
deck.add_note(card6)

# ========================================
# カード7: 幾何分布
# ========================================
card7 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【幾何分布】幾何分布Ge(p)の定義、公式、期待値・分散は？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
成功確率pの独立なベルヌーイ試行を繰り返すとき、<br>
初めて成功するまでの試行回数Xが従う分布<br>
記号: \\(X \\sim Ge(p)\\)<br>
<br>

<b>確率質量関数:</b><br>
\\[P(X=k) = (1-p)^{k-1} p\\]
\\[(k=1,2,3,\\ldots)\\]
<br>

<b>期待値と分散:</b><br>
\\[E(X) = \\frac{1}{p}\\]
\\[V(X) = \\frac{1-p}{p^2}\\]
<br>

<hr>

<b>具体例:</b><br>
<b>サイコロで1が出るまでの回数:</b><br>
p = 1/6 → Ge(1/6)<br>
・期待値: E(X) = 1/(1/6) = 6回<br>
・分散: V(X) = (5/6)/(1/6)² = 30<br>
<br>

<b>3回目で初めて1が出る確率:</b><br>
\\[P(X=3) = (5/6)^2 \\cdot (1/6)\\]
\\[= \\frac{25}{36} \\cdot \\frac{1}{6} = \\frac{25}{216} \\approx 0.116\\]
<br>

<b>調査対象者の在宅確率0.2、3回目で初在宅:</b><br>
p=0.2 → Ge(0.2)<br>
\\[P(X=3) = 0.8^2 \\cdot 0.2 = 0.128\\]
期待値: E(X) = 1/0.2 = 5回<br>
<br>

<hr>

<b>【重要ポイント・使いどころ】</b><br>
・「初めて成功するまで」の試行回数<br>
・例: 初めて当たるくじ、初めて在宅、初めて故障<br>
・成功確率が小さいほど、期待値は大きい<br>
・統計検定2級で頻出（2019年6月問10など）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計WEB「13-5. 幾何分布」「13-6. 幾何分布の期待値と分散」<br>
https://bellcurve.jp/statistics/course/6990.html<br>
統計検定2級 2019年6月 問10（調査対象者在宅問題）
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'geometric', 'review']
)
deck.add_note(card7)

# ========================================
# Ankiパッケージ出力
# ========================================
if __name__ == '__main__':
    package = genanki.Package(deck)
    output_file = 'probability_distributions_review.apkg'
    package.write_to_file(output_file)
    print(f"✅ Ankiカード作成完了: {output_file}")
    print(f"📊 作成枚数: 7枚")
    print(f"📁 ファイル: /Users/sasaki/{output_file}")
    print()
    print("=" * 60)
    print("カード内容:")
    print("=" * 60)
    print("1. 確率変数と確率分布（基本概念）")
    print("2. 離散型 vs 連続型確率分布")
    print("3. 期待値の定義")
    print("4. 期待値の性質（線形性）")
    print("5. 二項分布 B(n,p)")
    print("6. ポアソン分布 Po(λ)")
    print("7. 幾何分布 Ge(p)")
    print("=" * 60)
    print()
    print("⚠️  次のステップ:")
    print("1. このスクリプトを実行してAnkiカードを生成")
    print("2. 今週中に過去問を最低1問解く（約束）")
    print("3. 推定・検定は過去問を解いてからカード作成")
    print()
    print("💡 インストール方法（genanki未インストールの場合）:")
    print("   pip3 install genanki")
