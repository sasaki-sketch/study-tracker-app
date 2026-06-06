#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正規分布と標準正規分布 - Ankiカード（検証済み）
統計検定2級対応

出典:
- 統計WEB「14-1. 正規分布」https://bellcurve.jp/statistics/course/7797.html
- 統計WEB「14-2. 正規分布の再生性と標準正規分布」https://bellcurve.jp/statistics/course/7799.html
- 統計WEB「14-4. 標準正規分布表」https://bellcurve.jp/statistics/course/7803.html
- 統計WEB「14-5. 標準正規分布表の使い方1」https://bellcurve.jp/statistics/course/7805.html
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
            font-family: arial;
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
    '統計検定2級::正規分布と標準正規分布'
)

# ============================================================
# カード1: 正規分布の定義と確率密度関数
# ============================================================
card1_front = '''
<div style="font-size:24px; padding:20px;">
    <b>【正規分布】正規分布とは何か？確率密度関数は？</b>
</div>
'''

card1_back = '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
正規分布は、平均を中心に左右対称の釣鐘型をした連続型確率分布です。<br>
多くの統計的手法がデータの正規分布を仮定しており、検定や推定などで活用されます。<br>
<br>

<b>表記法:</b><br>
確率変数Xが平均μ、分散σ²の正規分布に従うとき、<br>
\\[X \\sim N(\\mu, \\sigma^2)\\]
と表記します。<br>
<br>

<b>確率密度関数:</b><br>
\\[f(x) = \\frac{1}{\\sqrt{2\\pi\\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}\\]
<br>
ここで、μは平均、σは標準偏差です。<br>
<br>

<hr>

<b>具体例:</b><br>
テストの点数が平均60点、標準偏差10点の正規分布に従う場合：<br>
\\[X \\sim N(60, 10^2) = N(60, 100)\\]
確率密度は60点で最高となり、60点から離れるほど低くなります。<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
✓ 正規分布は平均μと分散σ²の2つのパラメータで決まる<br>
✓ E(X) = μ、V(X) = σ²<br>
✓ σが大きいほど分布が広がり、山がなだらかになる<br>
✓ μの値によってグラフが水平方向にシフトする<br>
✓ 統計検定2級では最も重要な分布の1つ<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「14-1. 正規分布」<br>
https://bellcurve.jp/statistics/course/7797.html
</div>

</div>
'''

deck.add_note(genanki.Note(
    model=model,
    fields=[card1_front, card1_back],
    tags=['statistics', 'verified', 'normal-distribution', '統計検定2級']
))

# ============================================================
# カード2: 正規分布の再生性
# ============================================================
card2_front = '''
<div style="font-size:24px; padding:20px;">
    <b>【正規分布の再生性】正規分布の再生性とは何か？</b>
</div>
'''

card2_back = '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
独立な2つの正規分布に従うデータを足すと、その和もまた正規分布に従うという性質です。<br>
これを「正規分布の再生性」といいます。<br>
<br>

<b>公式:</b><br>
XとYが独立で、<br>
\\[X \\sim N(\\mu_1, \\sigma_1^2), \\quad Y \\sim N(\\mu_2, \\sigma_2^2)\\]
のとき、<br>
\\[X + Y \\sim N(\\mu_1 + \\mu_2, \\sigma_1^2 + \\sigma_2^2)\\]
<br>

<hr>

<b>具体例:</b><br>
数学のテスト：X ~ N(60, 100)（平均60点、標準偏差10点）<br>
英語のテスト：Y ~ N(70, 144)（平均70点、標準偏差12点）<br>
<br>
2科目の合計点Zは：<br>
\\[Z = X + Y \\sim N(60+70, 100+144) = N(130, 244)\\]
平均130点、標準偏差\\(\\sqrt{244} \\approx 15.6\\)点の正規分布に従います。<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
✓ 平均は足し算：μ₁ + μ₂<br>
✓ 分散も足し算：σ₁² + σ₂²（標準偏差ではない！）<br>
✓ XとYは独立である必要がある<br>
✓ 正規分布以外（二項分布、ポアソン分布など）も再生性を持つ<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「14-2. 正規分布の再生性と標準正規分布」<br>
https://bellcurve.jp/statistics/course/7799.html<br>
統計WEB「再生性」用語集<br>
https://bellcurve.jp/statistics/glossary/1811.html
</div>

</div>
'''

deck.add_note(genanki.Note(
    model=model,
    fields=[card2_front, card2_back],
    tags=['statistics', 'verified', 'normal-distribution', 'reproducibility', '統計検定2級']
))

# ============================================================
# カード3: 標準正規分布と標準化
# ============================================================
card3_front = '''
<div style="font-size:24px; padding:20px;">
    <b>【標準正規分布】標準正規分布とは？標準化の公式は？</b>
</div>
'''

card3_back = '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
平均μ=0、分散σ²=1である正規分布を「標準正規分布」といいます。<br>
\\[Z \\sim N(0, 1)\\]
標準正規分布はすべての正規分布の基準となります。<br>
<br>

<b>確率密度関数:</b><br>
\\[f(z) = \\frac{1}{\\sqrt{2\\pi}} e^{-\\frac{z^2}{2}}\\]
<br>

<b>標準化の公式:</b><br>
任意の正規分布\\(X \\sim N(\\mu, \\sigma^2)\\)を標準正規分布に変換する公式：<br>
\\[Z = \\frac{X - \\mu}{\\sigma}\\]
このZは標準正規分布N(0, 1)に従います。<br>
<br>

<hr>

<b>具体例:</b><br>
テストの点数が X ~ N(60, 100)（平均60点、標準偏差10点）のとき、<br>
88点を標準化すると：<br>
\\[Z = \\frac{88 - 60}{10} = \\frac{28}{10} = 2.8\\]
これは「平均より標準偏差の2.8倍高い」という意味です。<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
✓ 標準化することで、異なる正規分布を比較できる<br>
✓ Z値（標準得点）は「平均からの距離が標準偏差の何倍か」を表す<br>
✓ 標準化により、標準正規分布表が使えるようになる<br>
✓ Z値の意味：Z=2なら「上位約2.5%」に相当<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「14-2. 正規分布の再生性と標準正規分布」<br>
https://bellcurve.jp/statistics/course/7799.html
</div>

</div>
'''

deck.add_note(genanki.Note(
    model=model,
    fields=[card3_front, card3_back],
    tags=['statistics', 'verified', 'standard-normal-distribution', 'standardization', '統計検定2級']
))

# ============================================================
# カード4: 標準正規分布表の使い方
# ============================================================
card4_front = '''
<div style="font-size:24px; padding:20px;">
    <b>【標準正規分布表】標準正規分布表の使い方は？</b>
</div>
'''

card4_back = '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
標準正規分布表は、標準正規分布における様々なz値以上・以下となる確率が<br>
まとめられた統計数値表です。複雑な積分計算を避けるために使用します。<br>
<br>

<b>表の見方:</b><br>
z値を小数第1位と第2位に分解して読み取ります。<br>
例：z = 1.01 → 左端の「1.0」の行と上端の「.01」の列の交点を見る<br>
<br>

<hr>

<b>具体例:</b><br>
テスト結果が平均72.8点、標準偏差15点の正規分布に従うとき、<br>
88点以上の人の割合を求める。<br>
<br>

<b>ステップ1: 標準化</b><br>
\\[Z = \\frac{88 - 72.8}{15} = \\frac{15.2}{15} = 1.01\\]
<br>

<b>ステップ2: z値を分解</b><br>
1.01 = 1.0 + 0.01<br>
<br>

<b>ステップ3: 表から確率を読み取る</b><br>
表の左端「1.0」の行、上端「.01」の列の交点 → 0.156<br>
<br>

<b>結果:</b><br>
\\[P(Z \\geq 1.01) = 0.156\\]
88点以上の人は15.6%<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
✓ まず標準化してZ値を求める<br>
✓ Z値を小数第1位と第2位に分解<br>
✓ 標準正規分布は左右対称なので、負の値は正の値で代用可能<br>
✓ 統計検定では表が提供されるので、表の読み方を練習しておく<br>
✓ 「以上」か「以下」か「間」かによって計算方法が変わる<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「14-4. 標準正規分布表」<br>
https://bellcurve.jp/statistics/course/7803.html<br>
統計WEB「14-5. 標準正規分布表の使い方1」<br>
https://bellcurve.jp/statistics/course/7805.html
</div>

</div>
'''

deck.add_note(genanki.Note(
    model=model,
    fields=[card4_front, card4_back],
    tags=['statistics', 'verified', 'standard-normal-table', '統計検定2級']
))

# ============================================================
# デッキをファイルに出力
# ============================================================
output_file = 'normal_distribution_verified.apkg'
genanki.Package(deck).write_to_file(output_file)
print(f"✅ Ankiデッキを作成しました: {output_file}")
print(f"📊 カード数: {len(deck.notes)}")
print(f"🎯 トピック: 正規分布と標準正規分布（統計検定2級対応）")
