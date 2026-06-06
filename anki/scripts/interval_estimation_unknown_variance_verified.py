#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級対策：母平均の区間推定（母分散未知）
出典：統計学の時間 | 統計WEB (https://bellcurve.jp/)
     あつまれ統計の森 (https://www.hello-statisticians.com/)
"""

import genanki
import random

# デッキIDとモデルIDを生成
DECK_ID = random.randrange(1 << 30, 1 << 31)
MODEL_ID = random.randrange(1 << 30, 1 << 31)

# Ankiモデルの定義
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
            'qfmt': '<div style="font-size: 20px; text-align: center;">{{Question}}</div>',
            'afmt': '''
                <div style="font-size: 20px; text-align: center;">{{Question}}</div>
                <hr id="answer">
                <div style="font-size: 18px;">{{Answer}}</div>
            ''',
        },
    ],
    css='''
        .card {
            font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro W3", Meiryo, メイリオ, Osaka, "MS PGothic", arial, helvetica, sans-serif;
            text-align: left;
            color: black;
            background-color: white;
            padding: 20px;
        }
        .mjx-math {
            font-size: 1.2em;
        }
    '''
)

# デッキの作成
deck = genanki.Deck(DECK_ID, '統計検定2級::母平均の区間推定（母分散未知）')

# カード1: t分布とは
note1 = genanki.Note(
    model=model,
    fields=[
        't分布とは何ですか？正規分布との違いは？',
        '''<b>t分布の定義</b><br>
母分散が未知の場合に、母平均の区間推定や仮説検定に用いられる確率分布。<br>
正規分布に従う母集団からサンプルサイズnの標本を抽出したとき、次の統計量がt分布に従う：<br><br>

\\[t = \\frac{\\bar{X} - \\mu}{s/\\sqrt{n}}\\]<br><br>

ここで：<br>
・X̄ = 標本平均<br>
・μ = 母平均<br>
・s = 不偏標準偏差（√(不偏分散)）<br>
・n = サンプルサイズ<br><br>

<b>正規分布との違い</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>標準正規分布</th>
<th>t分布</th>
</tr>
<tr>
<td><b>使用条件</b></td>
<td>母分散既知</td>
<td>母分散未知</td>
</tr>
<tr>
<td><b>形状</b></td>
<td>固定</td>
<td>自由度により変化</td>
</tr>
<tr>
<td><b>裾</b></td>
<td>比較的薄い</td>
<td>正規分布より厚い</td>
</tr>
<tr>
<td><b>パラメータ</b></td>
<td>なし</td>
<td>自由度（n-1）</td>
</tr>
<tr>
<td><b>期待値</b></td>
<td>0</td>
<td>0（自由度>1）</td>
</tr>
<tr>
<td><b>分散</b></td>
<td>1</td>
<td>m/(m-2)（自由度m>2）</td>
</tr>
</table>
<br>

<b>t分布の特徴</b><br>
・自由度が大きくなるにつれて、標準正規分布に近づく<br>
・自由度が小さいほど、裾が厚く（ばらつきが大きい）なる<br>
・左右対称で平均0の分布<br>
・正規分布と同じく、中央が最も高い釣鐘型<br><br>

<b>自由度とは</b><br>
自由度 = n - 1（サンプルサイズから1を引いた値）<br><br>

サンプル平均を計算に使うため、1つの制約が生じて自由度が1減る。<br><br>

<b>発見者</b><br>
William Sealy Gosset（ゴセット）により発見され、後に「Student's t-distribution」として知られるようになった。<br><br>

<b>実用上の重要性</b><br>
現実の統計分析では母分散が未知であることがほとんどなので、<b>t分布の方が正規分布より実用的</b>である。<br><br>

<small>出典：統計WEB「標本とt分布」</small>'''
    ]
)
deck.add_note(note1)

# カード2: 母平均の信頼区間の公式（母分散未知）
note2 = genanki.Note(
    model=model,
    fields=[
        '母平均の信頼区間の計算式（母分散未知）を示してください。',
        '''<b>基本公式</b><br>
母平均 μ の信頼係数100α%の信頼区間：<br><br>

\\[\\bar{x} - t_{\\alpha/2}(n-1) \\cdot \\frac{s}{\\sqrt{n}} \\leq \\mu \\leq \\bar{x} + t_{\\alpha/2}(n-1) \\cdot \\frac{s}{\\sqrt{n}}\\]<br><br>

または：<br>
\\[\\bar{x} \\pm t_{\\alpha/2}(n-1) \\cdot \\frac{s}{\\sqrt{n}}\\]<br><br>

<b>記号の意味</b><br>
・x̄ = 標本平均<br>
・μ = 母平均（推定したい値）<br>
・s = 不偏標準偏差（不偏分散の平方根）<br>
・n = サンプルサイズ<br>
・t<sub>α/2</sub>(n-1) = 自由度n-1のt分布の上側α/2点<br><br>

<b>不偏分散と不偏標準偏差</b><br>
\\[s^2 = \\frac{1}{n-1}\\sum_{i=1}^{n}(X_i - \\bar{X})^2\\]<br><br>

\\[s = \\sqrt{s^2}\\]<br><br>

母分散が未知のため、標本から<b>不偏分散</b>を計算して母分散の推定値として使用する。<br><br>

<b>母分散既知の場合との比較</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>母分散既知</th>
<th>母分散未知</th>
</tr>
<tr>
<td><b>使用分布</b></td>
<td>標準正規分布</td>
<td>t分布</td>
</tr>
<tr>
<td><b>分散の値</b></td>
<td>母分散σ²（既知）</td>
<td>不偏分散s²（計算）</td>
</tr>
<tr>
<td><b>臨界値</b></td>
<td>z値（例：1.96）</td>
<td>t値（自由度で変化）</td>
</tr>
<tr>
<td><b>区間の幅</b></td>
<td>相対的に狭い</td>
<td>相対的に広い</td>
</tr>
<tr>
<td><b>現実性</b></td>
<td>非現実的</td>
<td>現実的</td>
</tr>
</table>
<br>

<b>重要なポイント</b><br>
・母分散が未知の場合、<b>必ずt分布を使用</b>する<br>
・不偏分散は n-1 で割る（標本分散は n で割る）<br>
・自由度が大きい（n>30程度）場合、t値はz値に近づく<br>
・サンプルサイズが小さいほど、t分布を使う重要性が高まる<br><br>

<small>出典：統計WEB「母平均の信頼区間の求め方（母分散未知）」、あつまれ統計の森</small>'''
    ]
)
deck.add_note(note2)

# カード3: 信頼区間の計算手順（母分散未知）
note3 = genanki.Note(
    model=model,
    fields=[
        '母平均の信頼区間を求める手順を説明してください（母分散未知）。',
        '''<b>4つのステップ</b><br><br>

<b>ステップ1：標本平均と不偏分散を算出</b><br>
標本データから平均値と不偏分散を計算する。<br><br>

標本平均：<br>
\\[\\bar{x} = \\frac{1}{n}\\sum_{i=1}^{n} x_i\\]<br><br>

不偏分散：<br>
\\[s^2 = \\frac{1}{n-1}\\sum_{i=1}^{n}(x_i - \\bar{x})^2\\]<br><br>

不偏標準偏差：<br>
\\[s = \\sqrt{s^2}\\]<br><br>

<b>ステップ2：自由度を決定</b><br>
自由度 = n - 1<br><br>

nはサンプルサイズ。標本平均を計算に使うため、1つの制約が生じる。<br><br>

<b>ステップ3：t分布表からt値を確認</b><br>
信頼係数に応じたt値をt分布表から求める：<br>
・自由度 n-1 の行を確認<br>
・信頼係数95%なら上側2.5%点の列を参照<br>
・該当するt値を読み取る<br><br>

例：n=10（自由度9）、95%信頼区間の場合<br>
→ t = 2.262<br><br>

<b>ステップ4：信頼区間を求める</b><br>
公式に値を代入して計算：<br>
\\[\\bar{x} - t \\cdot \\frac{s}{\\sqrt{n}} \\leq \\mu \\leq \\bar{x} + t \\cdot \\frac{s}{\\sqrt{n}}\\]<br><br>

<b>具体例</b><br>
工場の部品重量データ：<br>
・サンプルサイズ：n = 10<br>
・標本平均：x̄ = 100.03g<br>
・不偏分散：s² = 1.34g²<br>
・不偏標準偏差：s ≈ 1.16g<br>
・信頼係数：95%<br>
・自由度：9<br>
・t値（自由度9、上側2.5%点）：2.262<br><br>

計算：<br>
\\[100.03 - 2.262 \\times \\frac{1.16}{\\sqrt{10}} \\leq \\mu \\leq 100.03 + 2.262 \\times \\frac{1.16}{\\sqrt{10}}\\]<br><br>

\\[100.03 - 0.83 \\leq \\mu \\leq 100.03 + 0.83\\]<br><br>

\\[99.20 \\leq \\mu \\leq 100.86\\]<br><br>

<b>結果：95%の信頼度で、母平均は 99.20g 〜 100.86g の範囲にある</b><br><br>

<b>注意点</b><br>
・母分散既知の場合と比べて、信頼区間の幅が広くなる<br>
・サンプルサイズが小さいほど、t値が大きくなり、区間が広くなる<br>
・自由度が30を超えると、t値はz値に近づく<br><br>

<small>出典：統計WEB「母平均の信頼区間の求め方（母分散未知）」</small>'''
    ]
)
deck.add_note(note3)

# カード4: t分布表の使い方
note4 = genanki.Note(
    model=model,
    fields=[
        't分布表の使い方を説明してください。',
        '''<b>t分布表とは</b><br>
t分布において、ある確率に対応するt値を示した表。<br>
自由度と上側確率の組み合わせでt値を求める。<br><br>

<b>表の構造</b><br>
・縦軸：自由度（m = n-1）<br>
・横軸：上側確率（α/2）<br>
・セルの値：t値<br><br>

<b>使い方の手順</b><br><br>

<b>ステップ1：信頼係数から上側確率を計算</b><br>
信頼係数95%の場合：<br>
・中央に95%を含む<br>
・両側に 5% が残る<br>
・片側（上側）には 2.5% = 0.025<br><br>

<b>ステップ2：自由度を決定</b><br>
自由度 = n - 1<br>
例：サンプルサイズ10の場合、自由度 = 9<br><br>

<b>ステップ3：t値を読み取る</b><br>
t分布表で、自由度9の行と上側確率0.025の列が交わるセルの値を読み取る。<br>
→ t = 2.262<br><br>

<b>主要な信頼係数とt値の例</b><br>
自由度9の場合：<br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>信頼係数</th>
<th>上側確率</th>
<th>t値</th>
</tr>
<tr>
<td>90%</td>
<td>0.05</td>
<td>1.833</td>
</tr>
<tr>
<td>95%</td>
<td>0.025</td>
<td>2.262</td>
</tr>
<tr>
<td>99%</td>
<td>0.005</td>
<td>3.250</td>
</tr>
</table>
<br>

<b>自由度による変化</b><br>
95%信頼区間（上側2.5%点）の場合：<br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>自由度</th>
<th>t値</th>
<th>備考</th>
</tr>
<tr>
<td>1</td>
<td>12.706</td>
<td>非常に大きい</td>
</tr>
<tr>
<td>5</td>
<td>2.571</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>2.228</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>2.086</td>
<td></td>
</tr>
<tr>
<td>30</td>
<td>2.042</td>
<td>z値に近い</td>
</tr>
<tr>
<td>∞</td>
<td>1.960</td>
<td>z値と同じ</td>
</tr>
</table>
<br>

<b>観察されるパターン</b><br>
・自由度が小さいほど、t値は大きくなる<br>
・自由度が大きくなると、t値は標準正規分布のz値に近づく<br>
・自由度30以上では、t値 ≈ z値<br><br>

<b>Excelでの求め方</b><br>
=T.INV.2T(α, m)<br><br>

例：自由度9、95%信頼区間（α=0.05）<br>
=T.INV.2T(0.05, 9) = 2.262<br><br>

<b>片側検定の場合</b><br>
片側検定（上側確率α）の場合：<br>
=T.INV(1-α, m)<br><br>

<b>重要なポイント</b><br>
・信頼区間の計算では両側検定を使用する<br>
・サンプルサイズが小さい場合、t値とz値の差が大きい<br>
・統計検定2級では、自由度10〜120の上側2.5%点や5%点の値を参照することが多い<br><br>

<small>出典：統計WEB「t分布表」</small>'''
    ]
)
deck.add_note(note4)

# カード5: 不偏分散を使う理由
note5 = genanki.Note(
    model=model,
    fields=[
        '母分散未知の場合、なぜ不偏分散を使うのですか？標本分散との違いは？',
        '''<b>標本分散と不偏分散の違い</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>標本分散</th>
<th>不偏分散</th>
</tr>
<tr>
<td><b>公式</b></td>
<td>\\[\\frac{1}{n}\\sum(X_i - \\bar{X})^2\\]</td>
<td>\\[\\frac{1}{n-1}\\sum(X_i - \\bar{X})^2\\]</td>
</tr>
<tr>
<td><b>記号</b></td>
<td>V² または σ̂²</td>
<td>s² または u²</td>
</tr>
<tr>
<td><b>割る数</b></td>
<td>n</td>
<td>n-1</td>
</tr>
<tr>
<td><b>期待値</b></td>
<td>E[V²] ≠ σ²（偏る）</td>
<td>E[s²] = σ²（不偏）</td>
</tr>
<tr>
<td><b>用途</b></td>
<td>記述統計</td>
<td>推測統計（推定・検定）</td>
</tr>
</table>
<br>

<b>なぜ n-1 で割るのか</b><br>
標本から計算した標本分散は、母分散より<b>系統的に小さく</b>なる傾向がある（過小推定のバイアス）。<br><br>

理由：<br>
・標本平均 x̄ は、標本内のデータに最も近い値<br>
・標本平均からの偏差の二乗和は、真の母平均からの偏差の二乗和より小さくなる<br>
・このバイアスを補正するため、n ではなく n-1 で割る<br><br>

<b>数学的な説明</b><br>
標本平均を計算に使うことで、1つの「自由度」が失われる。<br><br>

n個のデータのうち、n-1個が決まれば、残り1個は自動的に決まる（制約条件）。<br><br>

実質的に独立な情報の数 = n - 1<br><br>

<b>不偏性の証明</b><br>
数学的に証明できる：<br>
\\[E\\left[\\frac{1}{n-1}\\sum(X_i - \\bar{X})^2\\right] = \\sigma^2\\]<br><br>

つまり、不偏分散の期待値は真の母分散に等しい。<br><br>

<b>具体例での比較</b><br>
データ：{10, 12, 14, 16, 18}（n=5）<br>
平均：14<br><br>

標本分散：<br>
\\[V^2 = \\frac{(10-14)^2 + (12-14)^2 + ... + (18-14)^2}{5} = \\frac{40}{5} = 8\\]<br><br>

不偏分散：<br>
\\[s^2 = \\frac{(10-14)^2 + (12-14)^2 + ... + (18-14)^2}{4} = \\frac{40}{4} = 10\\]<br><br>

不偏分散の方が大きい値となり、母分散の過小推定を補正している。<br><br>

<b>t分布での使用</b><br>
母分散 σ² を不偏分散 s² で推定したとき：<br>
\\[t = \\frac{\\bar{X} - \\mu}{s/\\sqrt{n}}\\]<br><br>

この統計量は、自由度 n-1 のt分布に従う。<br><br>

もし標本分散を使うと、この性質が成り立たない。<br><br>

<b>実務上の注意</b><br>
・推定・検定では<b>必ず不偏分散を使用</b><br>
・Excel：標本分散はVAR.P、不偏分散はVAR.S<br>
・Python：np.var(ddof=0)が標本分散、np.var(ddof=1)が不偏分散<br>
・n が大きい場合、両者の差は小さくなる<br><br>

<small>出典：統計WEB「標本とt分布」、あつまれ統計の森</small>'''
    ]
)
deck.add_note(note5)

# カード6: さまざまな信頼区間（母分散未知）
note6 = genanki.Note(
    model=model,
    fields=[
        '母分散未知の場合、信頼係数によって信頼区間はどう変わりますか？',
        '''<b>基本的な関係</b><br>
信頼係数が高いほど、信頼区間の幅は広くなる。<br>
母分散未知の場合も、母分散既知の場合と同じ傾向を示す。<br><br>

<b>信頼区間の幅の公式</b><br>
\\[\\text{区間の幅} = 2 \\times t_{\\alpha/2}(n-1) \\times \\frac{s}{\\sqrt{n}}\\]<br><br>

<b>主要な信頼係数とt値（自由度9）</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>信頼係数</th>
<th>上側確率</th>
<th>t値（df=9）</th>
<th>z値（参考）</th>
</tr>
<tr>
<td>90%</td>
<td>0.05</td>
<td>1.833</td>
<td>1.645</td>
</tr>
<tr>
<td>95%</td>
<td>0.025</td>
<td>2.262</td>
<td>1.960</td>
</tr>
<tr>
<td>99%</td>
<td>0.005</td>
<td>3.250</td>
<td>2.576</td>
</tr>
</table>
<br>

<b>具体例での比較</b><br>
部品重量データ（x̄=100.03g, s=1.16g, n=10, 自由度=9）の場合：<br><br>

<b>90%信頼区間（t=1.833）</b><br>
100.03 ± 1.833 × (1.16/√10) = 100.03 ± 0.67<br>
→ <b>99.36 ≤ μ ≤ 100.70</b><br><br>

<b>95%信頼区間（t=2.262）</b><br>
100.03 ± 2.262 × (1.16/√10) = 100.03 ± 0.83<br>
→ <b>99.20 ≤ μ ≤ 100.86</b><br><br>

<b>99%信頼区間（t=3.250）</b><br>
100.03 ± 3.250 × (1.16/√10) = 100.03 ± 1.19<br>
→ <b>98.84 ≤ μ ≤ 101.22</b><br><br>

<b>観察される傾向</b><br>
・信頼係数が高いほど、信頼区間の幅は広くなる<br>
・母分散既知の場合と比べて、すべての区間が広い<br>
・サンプルサイズが小さいほど、t値とz値の差が大きくなる<br><br>

<b>母分散既知との比較（同じデータで）</b><br>
仮に母標準偏差σ=1.16gが既知だった場合：<br><br>

95%信頼区間（z=1.96）：<br>
100.03 ± 1.96 × (1.16/√10) = 100.03 ± 0.72<br>
→ 99.31 ≤ μ ≤ 100.75<br><br>

母分散未知（t=2.262）：<br>
100.03 ± 2.262 × (1.16/√10) = 100.03 ± 0.83<br>
→ 99.20 ≤ μ ≤ 100.86<br><br>

<b>差：約0.11g（幅が広がる）</b><br><br>

<b>サンプルサイズの影響</b><br>
サンプルサイズを増やすと：<br>
・自由度が大きくなる<br>
・t値がz値に近づく<br>
・信頼区間の幅が狭くなる<br><br>

例：n=30（自由度29）の場合<br>
95%信頼区間のt値 = 2.045（z値1.96に近い）<br><br>

<b>実務での選択</b><br>
・<b>95%信頼区間</b>：最も一般的（推奨）<br>
・<b>99%信頼区間</b>：より慎重な判断が必要な場合<br>
・<b>90%信頼区間</b>：探索的研究<br><br>

<small>出典：統計WEB「さまざまな信頼区間（母分散未知）」</small>'''
    ]
)
deck.add_note(note6)

# カード7: 母平均の差の信頼区間（対応あり）
note7 = genanki.Note(
    model=model,
    fields=[
        '対応のあるデータの場合、母平均の差の信頼区間はどのように求めますか？',
        '''<b>対応のあるデータとは</b><br>
同じ対象に対する2つの測定値のペアデータ。<br>
例：<br>
・同じ人の治療前と治療後の血圧<br>
・同じ生徒の1学期と2学期のテスト結果<br>
・同じ製品の新旧2つの製造方法での品質<br><br>

<b>特徴</b><br>
・サンプルサイズは必ず等しい（n₁ = n₂ = n）<br>
・個体差の影響を除去できる<br>
・より精度の高い推定が可能<br><br>

<b>基本的なアプローチ</b><br>
各ペアの差 d<sub>i</sub> を計算し、差の平均について単一標本のt検定を行う。<br><br>

<b>信頼区間の公式</b><br>
\\[\\bar{x}_d \\pm t_{\\alpha/2}(n-1) \\times \\frac{s_d}{\\sqrt{n}}\\]<br><br>

ここで：<br>
・x̄<sub>d</sub> = 差の標本平均<br>
・s<sub>d</sub> = 差の不偏標準偏差<br>
・n = ペア数<br>
・t<sub>α/2</sub>(n-1) = 自由度n-1のt分布の上側α/2点<br><br>

<b>計算手順</b><br><br>

<b>ステップ1：各ペアの差を計算</b><br>
d<sub>i</sub> = X<sub>2i</sub> - X<sub>1i</sub>（後の値 - 前の値）<br><br>

<b>ステップ2：差の平均を計算</b><br>
\\[\\bar{x}_d = \\frac{1}{n}\\sum_{i=1}^{n} d_i\\]<br><br>

<b>ステップ3：差の不偏分散を計算</b><br>
\\[s_d^2 = \\frac{1}{n-1}\\sum_{i=1}^{n}(d_i - \\bar{x}_d)^2\\]<br><br>

<b>ステップ4：t値を求める</b><br>
自由度 n-1、信頼係数に対応するt値をt分布表から読み取る。<br><br>

<b>ステップ5：信頼区間を計算</b><br>
公式に代入して計算。<br><br>

<b>具体例</b><br>
5人の生徒の1学期と2学期の数学テスト結果：<br><br>

<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>生徒</th>
<th>1学期</th>
<th>2学期</th>
<th>差 d<sub>i</sub></th>
</tr>
<tr>
<td>A</td>
<td>70</td>
<td>80</td>
<td>10</td>
</tr>
<tr>
<td>B</td>
<td>60</td>
<td>55</td>
<td>-5</td>
</tr>
<tr>
<td>C</td>
<td>80</td>
<td>85</td>
<td>5</td>
</tr>
<tr>
<td>D</td>
<td>90</td>
<td>80</td>
<td>-10</td>
</tr>
<tr>
<td>E</td>
<td>75</td>
<td>80</td>
<td>5</td>
</tr>
</table>
<br>

・差の平均：x̄<sub>d</sub> = 1点<br>
・差の不偏分散：s²<sub>d</sub> = 267.5<br>
・差の不偏標準偏差：s<sub>d</sub> ≈ 16.35<br>
・サンプルサイズ：n = 5<br>
・自由度：4<br>
・t値（95%信頼区間）：2.776<br><br>

計算：<br>
\\[1 \\pm 2.776 \\times \\frac{16.35}{\\sqrt{5}} = 1 \\pm 20.30\\]<br><br>

<b>結果：-19.30 ≤ μ<sub>d</sub> ≤ 21.30</b><br><br>

95%の信頼度で、2学期と1学期の平均点の差は-19.30点〜21.30点の範囲にある。<br><br>

<b>解釈</b><br>
・信頼区間が0を含むため、統計的に有意な差があるとは言えない<br>
・2学期の方が向上したとも、低下したとも断定できない<br><br>

<small>出典：統計WEB「母平均の差の信頼区間」</small>'''
    ]
)
deck.add_note(note7)

# カード8: 母平均の差の信頼区間（対応なし）
note8 = genanki.Note(
    model=model,
    fields=[
        '対応のないデータの場合、母平均の差の信頼区間はどのように求めますか？',
        '''<b>対応のないデータとは</b><br>
無関係な異なるグループからのデータ。<br>
例：<br>
・1組と2組の生徒のテスト結果<br>
・男性と女性の身長<br>
・2つの異なる治療法の効果<br><br>

<b>特徴</b><br>
・サンプルサイズは異なる場合がある（n₁ ≠ n₂）<br>
・2つの独立した標本<br>
・個体間の相関はない<br><br>

<b>前提条件</b><br>
・2つの母集団の母分散が等しい（等分散の仮定）<br>
・各母集団が正規分布に従う<br><br>

<b>プール分散（pooled variance）の計算</b><br>
2つのグループの不偏分散を統合した推定値：<br><br>

\\[s_p^2 = \\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}\\]<br><br>

ここで：<br>
・s₁² = グループ1の不偏分散<br>
・s₂² = グループ2の不偏分散<br>
・n₁ = グループ1のサンプルサイズ<br>
・n₂ = グループ2のサンプルサイズ<br><br>

<b>信頼区間の公式</b><br>
\\[(\\bar{x}_1 - \\bar{x}_2) \\pm t_{\\alpha/2}(n_1+n_2-2) \\times \\sqrt{s_p^2\\left(\\frac{1}{n_1} + \\frac{1}{n_2}\\right)}\\]<br><br>

ここで：<br>
・x̄₁ = グループ1の標本平均<br>
・x̄₂ = グループ2の標本平均<br>
・t<sub>α/2</sub>(n₁+n₂-2) = 自由度n₁+n₂-2のt分布の上側α/2点<br><br>

<b>自由度</b><br>
自由度 = n₁ + n₂ - 2<br><br>

2つのグループそれぞれから1つずつ自由度が失われる。<br><br>

<b>計算手順</b><br><br>

<b>ステップ1：各グループの統計量を計算</b><br>
・標本平均：x̄₁, x̄₂<br>
・不偏分散：s₁², s₂²<br>
・サンプルサイズ：n₁, n₂<br><br>

<b>ステップ2：プール分散を計算</b><br>
上記の公式を使用。<br><br>

<b>ステップ3：自由度とt値を求める</b><br>
自由度 = n₁ + n₂ - 2<br>
t分布表からt値を読み取る。<br><br>

<b>ステップ4：信頼区間を計算</b><br>
公式に代入して計算。<br><br>

<b>具体例</b><br>
1組と2組の数学テスト結果：<br><br>

<b>1組（n₁=5）</b><br>
データ：{70, 60, 80, 90, 75}<br>
・平均：x̄₁ = 76点<br>
・不偏分散：s₁² = 170<br><br>

<b>2組（n₂=4）</b><br>
データ：{85, 75, 70, 85}<br>
・平均：x̄₂ = 78.75点<br>
・不偏分散：s₂² = 55.58<br><br>

<b>プール分散の計算：</b><br>
\\[s_p^2 = \\frac{(5-1) \\times 170 + (4-1) \\times 55.58}{5+4-2}\\]<br>
\\[= \\frac{680 + 166.74}{7} = \\frac{846.74}{7} \\approx 120.96\\]<br><br>

<b>t値：</b><br>
自由度7、95%信頼区間 → t = 2.365<br><br>

<b>信頼区間の計算：</b><br>
\\[(76 - 78.75) \\pm 2.365 \\times \\sqrt{120.96\\left(\\frac{1}{5} + \\frac{1}{4}\\right)}\\]<br>
\\[= -2.75 \\pm 2.365 \\times \\sqrt{120.96 \\times 0.45}\\]<br>
\\[= -2.75 \\pm 2.365 \\times 7.39\\]<br>
\\[= -2.75 \\pm 17.47\\]<br><br>

<b>結果：-20.22 ≤ μ₁-μ₂ ≤ 14.72</b><br><br>

95%の信頼度で、1組と2組の母平均の差は-20.22点〜14.72点の範囲にある。<br><br>

<b>解釈</b><br>
・信頼区間が0を含むため、統計的に有意な差があるとは言えない<br>
・1組と2組の平均点に明確な差があるとは断定できない<br><br>

<b>注意点</b><br>
・等分散の仮定が成り立たない場合、Welchのt検定を使用する<br>
・サンプルサイズが小さい場合、結果の信頼性が低下する<br><br>

<small>出典：統計WEB「母平均の差の信頼区間」</small>'''
    ]
)
deck.add_note(note8)

# カード9: 母分散既知と未知の使い分け
note9 = genanki.Note(
    model=model,
    fields=[
        '母分散既知と未知の場合で、区間推定の方法をどう使い分けますか？',
        '''<b>基本的な使い分け</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>状況</th>
<th>使用する方法</th>
</tr>
<tr>
<td>母分散が既知</td>
<td>正規分布を使用</td>
</tr>
<tr>
<td>母分散が未知</td>
<td>t分布を使用</td>
</tr>
<tr>
<td>サンプルサイズが大きい（n>30）</td>
<td>どちらでも可（結果はほぼ同じ）</td>
</tr>
<tr>
<td>サンプルサイズが小さい（n≤30）</td>
<td>適切な方法を選ぶことが重要</td>
</tr>
</table>
<br>

<b>詳細な比較</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>母分散既知</th>
<th>母分散未知</th>
</tr>
<tr>
<td><b>使用分布</b></td>
<td>標準正規分布 N(0,1)</td>
<td>t分布（自由度n-1）</td>
</tr>
<tr>
<td><b>統計量</b></td>
<td>\\[Z = \\frac{\\bar{X}-\\mu}{\\sigma/\\sqrt{n}}\\]</td>
<td>\\[t = \\frac{\\bar{X}-\\mu}{s/\\sqrt{n}}\\]</td>
</tr>
<tr>
<td><b>信頼区間</b></td>
<td>\\[\\bar{x} \\pm z_{\\alpha/2} \\frac{\\sigma}{\\sqrt{n}}\\]</td>
<td>\\[\\bar{x} \\pm t_{\\alpha/2}(n-1) \\frac{s}{\\sqrt{n}}\\]</td>
</tr>
<tr>
<td><b>分散の値</b></td>
<td>母分散σ²（既知値）</td>
<td>不偏分散s²（計算値）</td>
</tr>
<tr>
<td><b>95%臨界値</b></td>
<td>z = 1.96（固定）</td>
<td>t値（自由度で変化）</td>
</tr>
<tr>
<td><b>区間の幅</b></td>
<td>相対的に狭い</td>
<td>相対的に広い</td>
</tr>
<tr>
<td><b>現実性</b></td>
<td>非現実的</td>
<td>現実的</td>
</tr>
</table>
<br>

<b>実務での判断基準</b><br><br>

<b>ケース1：母分散が本当に既知</b><br>
・長期的な生産工程で、母分散が安定している場合<br>
・過去の大量データから母分散が正確に分かっている場合<br>
→ 正規分布を使用可能<br><br>

<b>ケース2：母分散が未知（ほとんどの場合）</b><br>
・新しい研究や調査<br>
・母集団全体のデータが入手不可能<br>
・標本データのみから推定する必要がある<br>
→ <b>t分布を使用（推奨）</b><br><br>

<b>ケース3：サンプルサイズが大きい（n>30）</b><br>
・自由度が大きいとt値≈z値<br>
・どちらの方法でも結果はほぼ同じ<br>
・母分散未知でも、正規分布の近似が使える<br><br>

<b>具体的な数値例</b><br>
95%信頼区間の臨界値：<br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>サンプルサイズ n</th>
<th>自由度</th>
<th>t値</th>
<th>z値</th>
<th>差</th>
</tr>
<tr>
<td>5</td>
<td>4</td>
<td>2.776</td>
<td>1.960</td>
<td>+42%</td>
</tr>
<tr>
<td>10</td>
<td>9</td>
<td>2.262</td>
<td>1.960</td>
<td>+15%</td>
</tr>
<tr>
<td>20</td>
<td>19</td>
<td>2.093</td>
<td>1.960</td>
<td>+7%</td>
</tr>
<tr>
<td>30</td>
<td>29</td>
<td>2.045</td>
<td>1.960</td>
<td>+4%</td>
</tr>
<tr>
<td>100</td>
<td>99</td>
<td>1.984</td>
<td>1.960</td>
<td>+1%</td>
</tr>
</table>
<br>

<b>重要なポイント</b><br>
・サンプルサイズが小さいほど、t値とz値の差が大きい<br>
・母分散未知でz値を使うと、信頼区間が<b>過小評価</b>される<br>
・統計的に誤った結論を導く可能性がある<br><br>

<b>実務上の推奨</b><br>
<b>迷ったらt分布を使う</b><br><br>

理由：<br>
・母分散が本当に既知の状況は稀<br>
・t分布を使えば、どちらの場合でも適切に対応できる<br>
・サンプルサイズが大きい場合、t分布≈正規分布になるので問題ない<br>
・より保守的（慎重）な推定となる<br><br>

<b>統計検定2級での扱い</b><br>
・問題文に「母分散が既知」と明示されている場合のみ、正規分布を使用<br>
・それ以外は、<b>t分布を使用</b>するのが標準<br><br>

<small>出典：統計WEB「母平均の信頼区間の求め方」、あつまれ統計の森</small>'''
    ]
)
deck.add_note(note9)

# カード10: サンプルサイズと信頼区間の関係（母分散未知）
note10 = genanki.Note(
    model=model,
    fields=[
        '母分散未知の場合、サンプルサイズが信頼区間に与える影響を説明してください。',
        '''<b>基本的な関係</b><br>
サンプルサイズ n が大きくなると：<br>
・自由度 n-1 が大きくなる<br>
・t値が小さくなる（z値に近づく）<br>
・標準誤差 s/√n が小さくなる<br>
・<b>信頼区間の幅が狭くなる</b><br><br>

<b>2つの効果</b><br><br>

<b>効果1：t値の減少</b><br>
自由度が大きくなると、t値が標準正規分布のz値に近づく。<br><br>

95%信頼区間のt値：<br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>n</th>
<th>自由度</th>
<th>t値</th>
<th>z値比</th>
</tr>
<tr>
<td>5</td>
<td>4</td>
<td>2.776</td>
<td>1.42倍</td>
</tr>
<tr>
<td>10</td>
<td>9</td>
<td>2.262</td>
<td>1.15倍</td>
</tr>
<tr>
<td>20</td>
<td>19</td>
<td>2.093</td>
<td>1.07倍</td>
</tr>
<tr>
<td>30</td>
<td>29</td>
<td>2.045</td>
<td>1.04倍</td>
</tr>
<tr>
<td>100</td>
<td>99</td>
<td>1.984</td>
<td>1.01倍</td>
</tr>
<tr>
<td>∞</td>
<td>∞</td>
<td>1.960</td>
<td>1.00倍</td>
</tr>
</table>
<br>

<b>効果2：標準誤差の減少</b><br>
標準誤差 = s/√n<br><br>

n が大きくなると、√n が大きくなり、標準誤差は小さくなる。<br><br>

<b>複合効果</b><br>
信頼区間の幅：<br>
\\[2 \\times t_{\\alpha/2}(n-1) \\times \\frac{s}{\\sqrt{n}}\\]<br><br>

n の増加により：<br>
・t値が減少（効果は限定的）<br>
・1/√n が減少（主要な効果）<br>
→ 幅が狭くなる<br><br>

<b>具体例</b><br>
同じ母集団から異なるサンプルサイズで標本抽出した場合（s≈10、95%信頼区間）：<br><br>

<b>n=5のとき</b><br>
・自由度：4<br>
・t値：2.776<br>
・標準誤差：10/√5 ≈ 4.47<br>
・幅：2 × 2.776 × 4.47 ≈ 24.8<br><br>

<b>n=10のとき</b><br>
・自由度：9<br>
・t値：2.262<br>
・標準誤差：10/√10 ≈ 3.16<br>
・幅：2 × 2.262 × 3.16 ≈ 14.3<br>
→ n=5の場合の58%に縮小<br><br>

<b>n=30のとき</b><br>
・自由度：29<br>
・t値：2.045<br>
・標準誤差：10/√30 ≈ 1.83<br>
・幅：2 × 2.045 × 1.83 ≈ 7.5<br>
→ n=5の場合の30%に縮小<br><br>

<b>n=100のとき</b><br>
・自由度：99<br>
・t値：1.984<br>
・標準誤差：10/√100 = 1.0<br>
・幅：2 × 1.984 × 1.0 ≈ 4.0<br>
→ n=5の場合の16%に縮小<br><br>

<b>サンプルサイズの設計</b><br>
必要な精度（幅W）が決まっている場合、必要なサンプルサイズを推定できる：<br><br>

\\[n \\approx \\left(\\frac{2ts}{W}\\right)^2\\]<br><br>

ただし、t値は n に依存するため、反復計算が必要。<br><br>

<b>実務上の目安</b><br>
・n < 10：信頼区間が非常に広い、推定精度が低い<br>
・10 ≤ n < 30：t分布の使用が重要、精度は中程度<br>
・n ≥ 30：t値≈z値、精度が向上<br>
・n ≥ 100：非常に高い精度<br><br>

<b>コストと精度のトレードオフ</b><br>
・n を2倍にすると、幅は約1/√2 ≈ 0.71倍（29%減）<br>
・n を4倍にすると、幅は約1/2（50%減）<br>
・精度を大幅に上げるには、大きなサンプルサイズが必要<br>
・サンプル収集のコストと精度のバランスを考慮<br><br>

<b>母分散既知の場合との比較</b><br>
母分散未知の場合：<br>
・サンプルサイズが小さいと、t値が大きいため幅が広い<br>
・サンプルサイズを増やす効果がより顕著<br>
・n>30になると、両者の差は小さくなる<br><br>

<small>出典：統計WEB「さまざまな信頼区間（母分散未知）」</small>'''
    ]
)
deck.add_note(note10)

# .apkgファイルとして保存
output_file = '/Users/sasaki/interval_estimation_unknown_variance_verified.apkg'
genanki.Package(deck).write_to_file(output_file)
print(f"Ankiパッケージが作成されました: {output_file}")
print(f"カード枚数: {len(deck.notes)}")
