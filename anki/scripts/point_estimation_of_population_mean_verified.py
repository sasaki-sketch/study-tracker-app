#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級対策：母平均の点推定
出典：統計学の時間 | 統計WEB (https://bellcurve.jp/)
      高校数学の美しい物語 (https://manabitimes.jp/)
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
deck = genanki.Deck(DECK_ID, '統計検定2級::母平均の点推定')

# カード1: 点推定とは
note1 = genanki.Note(
    model=model,
    fields=[
        '点推定とは何ですか？区間推定との違いは？',
        '''<b>点推定の定義</b><br>
平均値などを1つの値で推定すること。<br>
母集団の特性を表す母数（パラメーター）を単一の数値で推測する手法。<br><br>

<b>区間推定との違い</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>点推定</th>
<th>区間推定</th>
</tr>
<tr>
<td><b>推定方法</b></td>
<td>1つの値で推定</td>
<td>ある区間（範囲）で推定</td>
</tr>
<tr>
<td><b>結果の形式</b></td>
<td>具体的な数値1つ</td>
<td>信頼区間（下限〜上限）</td>
</tr>
<tr>
<td><b>例</b></td>
<td>平均身長は170cm</td>
<td>平均身長は168〜172cm</td>
</tr>
<tr>
<td><b>精度表現</b></td>
<td>精度は示さない</td>
<td>信頼度で精度を示す</td>
</tr>
</table>
<br>

<b>具体例</b><br>
日本人全員（母集団）から抽出した100人の身長データから、日本人全員の平均身長を推測する。<br>
・点推定：平均身長は170.5cm<br>
・区間推定：平均身長は95%の確率で168.2〜172.8cmの範囲内<br><br>

<b>推測統計学における位置づけ</b><br>
母集団全体を調査することは困難なため、標本から得られた統計量を用いて母集団の母数を推測する基本的手法。<br><br>

<small>出典：統計WEB「点推定とは」</small>'''
    ]
)
deck.add_note(note1)

# カード2: 推定量と推定値
note2 = genanki.Note(
    model=model,
    fields=[
        '推定量（Estimator）と推定値（Estimate）の違いを説明してください。',
        '''<b>推定量（Estimator）</b><br>
パラメータを推定するために利用する数値の計算方法や計算式のこと。<br><br>

<b>数式表現</b><br>
標本平均の計算式：<br>
\\[\\bar{X} = \\frac{1}{n} \\sum_{i=1}^{n} X_i\\]<br><br>

これは「方法」「公式」そのものを指す。<br>
推定量には \\[\\hat{\\theta}\\] （ハット）を付けて表記することが多い。<br><br>

<b>推定値（Estimate）</b><br>
実際に試行を行った結果から計算した具体的な数値のこと。<br><br>

<b>具体例</b><br>
映画館スクリーン数の調査：<br>
・10都道府県のデータ：95, 87, 105, 92, ...<br>
・標本平均の計算式（推定量）：X̄ = (95+87+105+...)/10<br>
・計算結果（推定値）：μ̂ = 93.8<br><br>

<b>比喩的な説明</b><br>
・<b>推定量</b> = レシピ（作り方）<br>
・<b>推定値</b> = 実際に作った料理（結果）<br><br>

<b>重要なポイント</b><br>
・推定量は「方法」であり、データによらず固定<br>
・推定値は「結果」であり、データによって変わる<br>
・同じ推定量でも、標本が異なれば推定値も異なる<br><br>

<small>出典：統計WEB「母平均の点推定と推定量・推定値」</small>'''
    ]
)
deck.add_note(note2)

# カード3: 不偏性
note3 = genanki.Note(
    model=model,
    fields=[
        '推定量の不偏性（Unbiasedness）とは何ですか？',
        '''<b>定義</b><br>
推定量の期待値がパラメータ（母数）に一致する性質のこと。<br><br>

<b>数学的表現</b><br>
推定量 θ̂ が母数 θ の不偏推定量であるとは：<br>
\\[E[\\hat{\\theta}] = \\theta\\]<br><br>

<b>意味</b><br>
・長期的に見て、推定値が系統的に真の値から上下に偏らない<br>
・推定の外れ具合が中立的である<br>
・サンプルサイズ n に関係なく成立する性質<br><br>

<b>具体例</b><br>
標本平均 X̄ は母平均 μ の不偏推定量：<br>
\\[E[\\bar{X}] = E\\left[\\frac{1}{n}\\sum_{i=1}^{n} X_i\\right] = \\frac{1}{n}\\sum_{i=1}^{n} E[X_i] = \\frac{1}{n} \\cdot n\\mu = \\mu\\]<br><br>

<b>重要なポイント</b><br>
・不偏性があれば、標本サイズが小さくても良い<br>
・個々の推定値は真の値から外れることがあるが、平均的には一致<br>
・系統的な偏りがないため、推定量として信頼できる<br><br>

<b>不偏性がない例</b><br>
標本分散（n で割るもの）は母分散の不偏推定量ではない。<br>
母分散よりも系統的に小さく推定してしまう。<br><br>

<small>出典：統計WEB「推定量の性質」</small>'''
    ]
)
deck.add_note(note3)

# カード4: 一致性
note4 = genanki.Note(
    model=model,
    fields=[
        '推定量の一致性（Consistency）とは何ですか？',
        '''<b>定義</b><br>
サンプルサイズ n が大きくなれば、推定量が真のパラメータに近づく性質のこと。<br><br>

<b>数学的表現</b><br>
任意の正の値 ε に対して：<br>
\\[\\lim_{n \\to \\infty} P(|\\hat{\\theta}_n - \\theta| \\geq \\varepsilon) = 0\\]<br><br>

または同値的に：<br>
\\[\\lim_{n \\to \\infty} P(|\\hat{\\theta}_n - \\theta| < \\varepsilon) = 1\\]<br><br>

<b>意味</b><br>
・データをたくさん集めて、標本サイズ n を十分に大きくすれば、推定値は母集団の真の値に収束していく<br>
・大数の法則に基づく性質<br>
・n が大きくなるにつれて推定精度が向上<br><br>

<b>不偏性との違い</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>不偏性</th>
<th>一致性</th>
</tr>
<tr>
<td><b>サンプルサイズ</b></td>
<td>n に関係なく成立</td>
<td>n が大きい時に成立</td>
</tr>
<tr>
<td><b>性質</b></td>
<td>期待値が一致</td>
<td>確率収束する</td>
</tr>
<tr>
<td><b>小標本での保証</b></td>
<td>あり</td>
<td>なし</td>
</tr>
</table>
<br>

<b>重要なポイント</b><br>
・一致性があっても、標本サイズが小さい場合には推定値と真の値が一致していない可能性がある<br>
・不偏性と一致性は独立した性質（片方だけ持つことも、両方持つこともある）<br>
・標本平均は不偏性と一致性の両方を持つ<br><br>

<small>出典：統計WEB「推定量の性質」</small>'''
    ]
)
deck.add_note(note4)

# カード5: 有効性
note5 = genanki.Note(
    model=model,
    fields=[
        '推定量の有効性（Efficiency）とは何ですか？',
        '''<b>定義</b><br>
同じ不偏推定量の中で、分散が最も小さい推定量を有効推定量（最良不偏推定量）という。<br>
精度の高い推定量、つまり分散が小さい推定量が「有効性が高い」と言える。<br><br>

<b>数学的表現</b><br>
2つの不偏推定量 θ̂₁ と θ̂₂ について：<br>
\\[\\text{Var}(\\hat{\\theta}_1) < \\text{Var}(\\hat{\\theta}_2)\\]<br>
の場合、θ̂₁ の方が θ̂₂ より有効性が高い。<br><br>

<b>意味</b><br>
・分散が小さい推定量ほど、推定値が真の値の周りに集中する<br>
・推定の精度が高い<br>
・ばらつきが小さいため、信頼できる推定ができる<br><br>

<b>具体例</b><br>
母平均を推定する場合：<br>
・標本平均：分散 = σ²/n<br>
・標本中央値：分散 > σ²/n（正規分布の場合、約1.57倍）<br><br>

標本平均の方が有効性が高い。<br><br>

<b>有効推定量の条件</b><br>
すべての不偏推定量の中で、最も分散が小さくなるようなものが有効推定量。<br>
クラメール・ラオの不等式により、分散の下限が定められる。<br><br>

<b>3つの性質のまとめ</b><br>
良い推定量の条件：<br>
1. <b>不偏性</b>：系統的な偏りがない<br>
2. <b>一致性</b>：標本サイズを大きくすれば真の値に近づく<br>
3. <b>有効性</b>：同じ不偏推定量の中で最も精度が高い<br><br>

<small>出典：統計用語集、統計検定対策資料</small>'''
    ]
)
deck.add_note(note5)

# カード6: 標本平均の性質
note6 = genanki.Note(
    model=model,
    fields=[
        '標本平均は母平均の推定量としてどのような性質を持ちますか？',
        '''<b>標本平均の定義</b><br>
\\[\\bar{X} = \\frac{1}{n} \\sum_{i=1}^{n} X_i\\]<br><br>

<b>標本平均が持つ3つの優れた性質</b><br><br>

<b>1. 不偏性</b><br>
\\[E[\\bar{X}] = \\mu\\]<br>
標本平均の期待値は母平均に一致する。<br><br>

<b>2. 一致性</b><br>
n が大きくなると、標本平均は母平均に確率収束する。<br>
大数の法則により保証される。<br><br>

<b>3. 有効性</b><br>
標本平均は、母平均の不偏推定量の中で最も分散が小さい（最良不偏推定量）。<br>
分散は σ²/n で、これは理論的に最小値。<br><br>

<b>標本平均の分散</b><br>
\\[\\text{Var}(\\bar{X}) = \\frac{\\sigma^2}{n}\\]<br><br>

この公式から：<br>
・n が大きくなると分散は小さくなる<br>
・推定の精度は n の平方根に比例して向上<br><br>

<b>なぜ標本平均を使うのか</b><br>
母平均を推定する方法は複数あるが（中央値、トリム平均など）、標本平均は：<br>
・不偏性、一致性、有効性のすべてを満たす<br>
・計算が簡単<br>
・理論的に最も優れた推定量<br><br>

これらの理由から、母平均の点推定には標本平均が標準的に使われる。<br><br>

<small>出典：統計WEB「推定量の性質」</small>'''
    ]
)
deck.add_note(note6)

# カード7: 標本分散
note7 = genanki.Note(
    model=model,
    fields=[
        '標本分散の定義と性質を説明してください。',
        '''<b>標本分散の定義</b><br>
標本から計算される分散で、n で割って計算する：<br>
\\[S^2 = \\frac{1}{n} \\sum_{i=1}^{n} (X_i - \\bar{X})^2\\]<br><br>

<b>標本分散の期待値</b><br>
\\[E[S^2] = \\frac{n-1}{n}\\sigma^2\\]<br><br>

つまり、標本分散の期待値は母分散 σ² よりも小さくなる。<br><br>

<b>性質</b><br>
・<b>一致推定量</b>：n が大きくなれば母分散に近づく<br>
・<b>不偏推定量ではない</b>：期待値が母分散に一致しない<br>
・母分散を系統的に過小評価する<br><br>

<b>なぜ小さく推定されるのか</b><br>
標本平均 X̄ から各データまでの距離を測っているが、X̄ は標本内のデータに最も近い点。<br>
母平均 μ から測るより距離が短くなるため、散らばりが小さく見積もられる。<br><br>

<b>具体例</b><br>
データ：2, 4, 6, 8, 10（標本平均 = 6）<br><br>

標本分散：<br>
\\[S^2 = \\frac{(2-6)^2 + (4-6)^2 + (6-6)^2 + (8-6)^2 + (10-6)^2}{5}\\]<br>
\\[= \\frac{16 + 4 + 0 + 4 + 16}{5} = \\frac{40}{5} = 8\\]<br><br>

<b>使い道</b><br>
・得られたデータそのものの散らばりを表現する場合<br>
・記述統計として使用<br>
・母分散の推定には不偏分散を使うべき<br><br>

<small>出典：統計WEB「標本分散と不偏分散」</small>'''
    ]
)
deck.add_note(note7)

# カード8: 不偏分散
note8 = genanki.Note(
    model=model,
    fields=[
        '不偏分散の定義とn-1で割る理由を説明してください。',
        '''<b>不偏分散の定義</b><br>
n-1 で割って計算する分散：<br>
\\[s^2 = \\frac{1}{n-1} \\sum_{i=1}^{n} (X_i - \\bar{X})^2\\]<br><br>

または：<br>
\\[s^2 = \\frac{n}{n-1} S^2\\]<br><br>

<b>不偏分散の期待値</b><br>
\\[E[s^2] = \\sigma^2\\]<br><br>

期待値が母分散に一致するため、<b>不偏推定量</b>である。<br><br>

<b>なぜ n-1 で割るのか</b><br><br>

<b>直感的説明</b><br>
標本分散を計算するときに使う平均は母平均ではなく標本平均なので、標本分散だと平均からの差の二乗和を小さく見積もってしまう。<br>
これを補正するために n/(n-1) 倍する必要があり、結果的に n-1 で割ることになる。<br><br>

<b>数学的理由</b><br>
標本平均 X̄ を使うことで「自由度」が1つ減る：<br>
・n 個のデータがあっても、X̄ が決まると最後の1個は自動的に決まる<br>
・独立な情報は n-1 個しかない<br>
・この「自由度 = n-1」で割る<br><br>

<b>証明のアウトライン</b><br>
母平均 μ を間にはさむ：<br>
\\[(X_i - \\bar{X})^2 = [(X_i - \\mu) - (\\bar{X} - \\mu)]^2\\]<br><br>

展開して期待値をとると：<br>
\\[E\\left[\\sum(X_i - \\bar{X})^2\\right] = (n-1)\\sigma^2\\]<br><br>

したがって、n-1 で割れば期待値が σ² になる。<br><br>

<b>性質</b><br>
・不偏性と一致性を持つ推定量<br>
・統計ソフトで「分散」として出力されるのは通常、不偏分散<br>
・母分散の推定には不偏分散を使うべき<br><br>

<small>出典：統計WEB「標本分散と不偏分散」、高校数学の美しい物語</small>'''
    ]
)
deck.add_note(note8)

# カード9: 標本分散と不偏分散の比較
note9 = genanki.Note(
    model=model,
    fields=[
        '標本分散と不偏分散を比較してください。',
        '''<b>比較表</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>標本分散 S²</th>
<th>不偏分散 s²</th>
</tr>
<tr>
<td><b>定義式</b></td>
<td>Σ(Xᵢ-X̄)²/n</td>
<td>Σ(Xᵢ-X̄)²/(n-1)</td>
</tr>
<tr>
<td><b>期待値</b></td>
<td>((n-1)/n)σ²</td>
<td>σ²</td>
</tr>
<tr>
<td><b>不偏性</b></td>
<td>なし（過小推定）</td>
<td>あり</td>
</tr>
<tr>
<td><b>一致性</b></td>
<td>あり</td>
<td>あり</td>
</tr>
<tr>
<td><b>用途</b></td>
<td>記述統計</td>
<td>推測統計（推定）</td>
</tr>
<tr>
<td><b>値の大小</b></td>
<td>小さい</td>
<td>大きい（n/(n-1)倍）</td>
</tr>
</table>
<br>

<b>具体例</b><br>
データ：2, 4, 6, 8, 10（n=5, X̄=6）<br><br>

偏差平方和：Σ(Xᵢ-X̄)² = 40<br><br>

標本分散：S² = 40/5 = 8<br>
不偏分散：s² = 40/4 = 10<br><br>

不偏分散は標本分散の 5/4 = 1.25 倍。<br><br>

<b>関係式</b><br>
\\[s^2 = \\frac{n}{n-1} S^2\\]<br><br>

<b>使い分け</b><br>
・<b>標本分散</b>：得られたデータそのものの散らばりを表現したい場合<br>
・<b>不偏分散</b>：母分散を推定したい場合（推測統計）<br><br>

<b>統計ソフトでの扱い</b><br>
ExcelのVAR.S関数、PythonのNumPy、Rなどで「分散」として出力されるのは通常、不偏分散。<br><br>

<b>重要な注意</b><br>
n が大きくなると、標本分散と不偏分散の差は小さくなる（一致性）。<br>
しかし、推測統計では原則として不偏分散を使用する。<br><br>

<small>出典：統計WEB「標本分散と不偏分散」</small>'''
    ]
)
deck.add_note(note9)

# カード10: 標準偏差
note10 = genanki.Note(
    model=model,
    fields=[
        '標準偏差とは何ですか？',
        '''<b>定義</b><br>
分散の正の平方根。データのばらつきを表す基本的な指標。<br><br>

<b>数式</b><br>
標本標準偏差（記述統計）：<br>
\\[S = \\sqrt{S^2} = \\sqrt{\\frac{1}{n} \\sum_{i=1}^{n} (X_i - \\bar{X})^2}\\]<br><br>

不偏標準偏差（推測統計）：<br>
\\[s = \\sqrt{s^2} = \\sqrt{\\frac{1}{n-1} \\sum_{i=1}^{n} (X_i - \\bar{X})^2}\\]<br><br>

<b>意味</b><br>
・個々のデータのばらつきを表す<br>
・データがどれだけ平均値から離れているかを示す<br>
・元のデータと同じ単位で表現される<br><br>

<b>なぜ平方根をとるのか</b><br>
・分散は単位が「元の単位²」となり解釈しづらい<br>
・標準偏差は元のデータと同じ単位なので直感的に理解しやすい<br>
・例：身長のデータなら、分散は「cm²」、標準偏差は「cm」<br><br>

<b>具体例</b><br>
テストの点数：70, 75, 80, 85, 90（平均 = 80）<br><br>

不偏分散：s² = 62.5<br>
標準偏差：s = √62.5 ≈ 7.9点<br><br>

「平均点から約8点程度のばらつきがある」と解釈できる。<br><br>

<b>性質</b><br>
・標準偏差が大きい → データのばらつきが大きい<br>
・標準偏差が小さい → データが平均値の周りに集中<br>
・標準偏差 = 0 → すべてのデータが同じ値<br><br>

<b>注意点</b><br>
√(不偏分散) は厳密には母標準偏差の不偏推定量ではない。<br>
しかし、実用上は不偏標準偏差として扱われることが多い。<br><br>

<small>出典：統計WEB「標準偏差と標準誤差」</small>'''
    ]
)
deck.add_note(note10)

# カード11: 標準誤差
note11 = genanki.Note(
    model=model,
    fields=[
        '標準誤差（Standard Error）とは何ですか？',
        '''<b>定義</b><br>
推定量の標準偏差のこと。標本から得られる推定量そのもののバラつき（＝精度）を表す指標。<br>
一般的には、標本平均の標準偏差を意味する。<br><br>

<b>数式</b><br>
母集団の標準偏差が既知の場合：<br>
\\[\\text{SE} = \\frac{\\sigma}{\\sqrt{n}}\\]<br><br>

母集団の標準偏差が未知の場合（推定）：<br>
\\[\\text{SE} = \\frac{s}{\\sqrt{n}}\\]<br><br>

ここで：<br>
・σ = 母標準偏差<br>
・s = 標本標準偏差（通常は不偏標準偏差）<br>
・n = サンプルサイズ<br><br>

<b>意味</b><br>
・標本平均が母平均からどれくらいズレているかの指標<br>
・推定の精度を表す<br>
・標準誤差が小さい → 推定精度が高い<br>
・標準誤差が大きい → 推定精度が低い<br><br>

<b>サンプルサイズとの関係</b><br>
・n が大きくなると、標準誤差は小さくなる（1/√n に比例）<br>
・n を4倍にすると、標準誤差は半分になる<br>
・n を100倍にすると、標準誤差は1/10になる<br><br>

<b>具体例</b><br>
ある調査で標本標準偏差 s = 15、サンプルサイズ n = 100 の場合：<br><br>

標準誤差：SE = 15/√100 = 15/10 = 1.5<br><br>

標本平均が母平均から平均的に約1.5ずれることを意味する。<br><br>

<b>応用</b><br>
・区間推定（信頼区間）の計算に使用<br>
・仮説検定の検定統計量の計算に使用<br>
・推定精度の評価<br><br>

<small>出典：統計WEB「標準偏差と標準誤差」</small>'''
    ]
)
deck.add_note(note11)

# カード12: 標準偏差と標準誤差の比較
note12 = genanki.Note(
    model=model,
    fields=[
        '標準偏差と標準誤差の違いを説明してください。',
        '''<b>比較表</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>標準偏差（SD）</th>
<th>標準誤差（SE）</th>
</tr>
<tr>
<td><b>対象</b></td>
<td>個々のデータ</td>
<td>標本平均</td>
</tr>
<tr>
<td><b>何を示すか</b></td>
<td>データのばらつき</td>
<td>推定量のばらつき</td>
</tr>
<tr>
<td><b>計算式</b></td>
<td>√[Σ(Xᵢ-X̄)²/(n-1)]</td>
<td>s/√n</td>
</tr>
<tr>
<td><b>意味</b></td>
<td>データの散らばり度</td>
<td>推定値の精度</td>
</tr>
<tr>
<td><b>サンプルサイズの影響</b></td>
<td>影響を受けない</td>
<td>n が大きいと小さくなる</td>
</tr>
<tr>
<td><b>用途</b></td>
<td>記述統計</td>
<td>推測統計</td>
</tr>
</table>
<br>

<b>詳しい説明</b><br><br>

<b>標準偏差</b><br>
・得られたデータがどのくらい散らばっているかを示す<br>
・この散らばりはデータ数、試行回数に依存しない<br>
・「個人差」「製品のばらつき」など、対象そのものの変動を表現<br><br>

<b>標準誤差</b><br>
・サンプルの平均値が母集団の平均値にどれくらい近いかを示す<br>
・標準偏差にサンプルサイズを反映させた指標<br>
・「推定の精度」を表現<br><br>

<b>関係式</b><br>
\\[\\text{SE} = \\frac{\\text{SD}}{\\sqrt{n}}\\]<br><br>

<b>使い分け</b><br><br>

<b>標準偏差を使う場面</b><br>
・サンプル一つ一つの「ばらつき」を捉えたい場合<br>
・データの変動性を記述したい場合<br>
・例：「このクラスの身長のばらつきは SD = 5cm です」<br><br>

<b>標準誤差を使う場面</b><br>
・実験の代表値（平均値）がどの程度ばらつくのかを知りたい場合<br>
・推定の精度を評価したい場合<br>
・例：「標本平均の推定誤差は SE = 0.5cm です」<br><br>

<b>エラーバーでの使い分け</b><br>
・標準偏差：データのばらつきを示したい場合<br>
・標準誤差：推定の精度を示したい場合<br>
・目的に応じて使い分けが重要<br><br>

<small>出典：統計WEB「標準偏差と標準誤差」、いちばんやさしい医療統計</small>'''
    ]
)
deck.add_note(note12)

# .apkgファイルとして保存
output_file = '/Users/sasaki/point_estimation_of_population_mean_verified.apkg'
genanki.Package(deck).write_to_file(output_file)
print(f"Ankiパッケージが作成されました: {output_file}")
print(f"カード枚数: {len(deck.notes)}")
