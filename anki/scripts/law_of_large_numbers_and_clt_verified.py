#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級対策：大数の法則と中心極限定理
出典：統計学の時間 | 統計WEB (https://bellcurve.jp/)
      高校数学の美しい物語 (https://manabitimes.jp/)
      高校物理の備忘録 (https://physnotes.jp/)
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
deck = genanki.Deck(DECK_ID, '統計検定2級::大数の法則と中心極限定理')

# カード1: 大数の法則の基本定義
note1 = genanki.Note(
    model=model,
    fields=[
        '大数の法則とは何ですか？',
        '''<b>定義</b><br>
たくさん実験すればデータの平均は真の平均（母平均）に近づくという法則。<br>
試行回数を増やすにつれ、標本平均が母平均へと収束していく性質を指す。<br><br>

<b>数学的表現</b><br>
任意の正の数 ε に対して、<br>
\\[\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| < \\varepsilon) = 1\\]<br><br>

<b>意味</b><br>
試行回数 n を増やすと、標本平均 X̄ₙ が母平均 μ から大きく外れてしまう確率は限りなくゼロに近づく。<br><br>

<b>発見者</b><br>
ヤコブ・ベルヌーイによって提唱された。<br><br>

<b>重要なポイント</b><br>
・大量のデータから計算した平均値は、母集団の真の平均値の信頼できる推定値となる<br>
・試行回数が少ないと結果は大きく変動するが、試行回数を増やすと安定する<br><br>

<small>出典：統計WEB、高校数学の美しい物語</small>'''
    ]
)
deck.add_note(note1)

# カード2: 大数の弱法則
note2 = genanki.Note(
    model=model,
    fields=[
        '大数の弱法則（Weak Law of Large Numbers）とは何ですか？',
        '''<b>定義</b><br>
標本サイズ n が大きくなるにつれ、標本平均が母平均から外れる確率が限りなく小さくなる法則。<br><br>

<b>数学的表現</b><br>
任意の正の数 ε に対して、<br>
\\[\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| \\geq \\varepsilon) = 0\\]<br><br>

<b>特徴</b><br>
・<b>確率収束</b>を示す<br>
・「ズレが生じる確率が限りなく小さくなる」という主張<br>
・チェビシェフの不等式から導出される<br><br>

<b>証明の方針</b><br>
標本平均の分散が 1/n に比例して減少することを利用する：<br>
\\[\\text{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n}\\]<br><br>

n が大きくなると分散が小さくなるため、標本平均は母平均の周りに集中する。<br><br>

<b>統計検定2級での重要度</b><br>
弱法則の概念と意味を理解していれば十分。証明の詳細は不要。<br><br>

<small>出典：高校物理の備忘録、Wikipedia</small>'''
    ]
)
deck.add_note(note2)

# カード3: 大数の強法則
note3 = genanki.Note(
    model=model,
    fields=[
        '大数の強法則（Strong Law of Large Numbers）とは何ですか？弱法則との違いは？',
        '''<b>定義</b><br>
各試行において、標本平均は確率1で母平均に収束する法則。<br><br>

<b>数学的表現</b><br>
\\[P\\left(\\lim_{n \\to \\infty} \\bar{X}_n = \\mu\\right) = 1\\]<br><br>

<b>特徴</b><br>
・<b>概収束</b>を示す<br>
・弱法則よりも強い主張<br>
・強法則が成立するならば弱法則も成立する<br><br>

<b>弱法則との違い</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>弱法則</th>
<th>強法則</th>
</tr>
<tr>
<td><b>収束の種類</b></td>
<td>確率収束</td>
<td>概収束</td>
</tr>
<tr>
<td><b>主張</b></td>
<td>ズレる確率が0に近づく</td>
<td>確率1で収束する</td>
</tr>
<tr>
<td><b>証明</b></td>
<td>比較的簡単</td>
<td>高度</td>
</tr>
<tr>
<td><b>関係</b></td>
<td>強法則から導かれる</td>
<td>弱法則を含む</td>
</tr>
</table>
<br>

<b>統計検定2級での重要度</b><br>
2つの違いがあることを知っていれば十分。詳細な証明は範囲外。<br><br>

<small>出典：Wikipedia、高校物理の備忘録</small>'''
    ]
)
deck.add_note(note3)

# カード4: 大数の法則の具体例
note4 = genanki.Note(
    model=model,
    fields=[
        '大数の法則の具体例を挙げてください。',
        '''<b>例1: サイコロ</b><br>
通常のサイコロを1回振ると、出目の期待値は 3.5 です。<br><br>

・10回振った場合：標本平均は 2.8 や 4.2 など、3.5 から大きくずれることがある<br>
・100回振った場合：標本平均は 3.4 や 3.6 など、3.5 に近づく<br>
・10,000回振った場合：標本平均は 3.5 に非常に近くなる<br><br>

<b>例2: コイン投げ</b><br>
表が出る確率が 1/2 のコインを繰り返し投げた場合：<br><br>

・100回投げ：表の割合が 0.49（真の値 0.5 との差 0.01）<br>
・10,000回投げ：表の割合が 0.5010（真の値との差 0.001）<br><br>

試行回数を増やすほど、理論値に近づいていく。<br><br>

<b>例3: サイコロで1の目が出る確率</b><br>
・10回振る：1の目が出る回数は 0回〜5回など変動が大きい<br>
・1000回振る：1の目が出る割合は 1/6 ≈ 0.167 に近づく<br><br>

<b>実用例</b><br>
・保険会社が大量の契約から平均的な損失を予測<br>
・工場で大量生産品の品質管理<br>
・視聴率調査などの標本調査<br><br>

<small>出典：高校数学の美しい物語、統計WEB</small>'''
    ]
)
deck.add_note(note4)

# カード5: 中心極限定理の基本定義
note5 = genanki.Note(
    model=model,
    fields=[
        '中心極限定理（Central Limit Theorem）とは何ですか？',
        '''<b>定義</b><br>
標本を抽出する母集団が平均 μ、分散 σ² の正規分布に従う場合においても、従わない場合においても、抽出するサンプルサイズ n が大きくなるにつれて標本平均の分布は「平均 μ、分散 σ²/n」の正規分布 N(μ, σ²/n) に近づく。<br><br>

<b>数学的表現</b><br>
母集団の平均を μ、分散を σ² とすると、サンプルサイズ n の標本平均 X̄ の分布は：<br>
\\[\\bar{X} \\sim N\\left(\\mu, \\frac{\\sigma^2}{n}\\right)\\]<br><br>

または標準化すると：<br>
\\[Z = \\frac{\\bar{X} - \\mu}{\\sigma/\\sqrt{n}} \\sim N(0, 1)\\]<br><br>

<b>重要なポイント</b><br>
・<b>母集団の分布によらず成立する</b>（これが非常に重要！）<br>
・母集団が正規分布でなくても、標本平均は正規分布に従う<br>
・サンプルサイズが大きいほど正規分布に近づく<br><br>

<b>実用的な意義</b><br>
・標本平均を使った推測統計の理論的基礎<br>
・区間推定や仮説検定で正規分布を使える根拠<br>
・母集団の分布が不明でも、標本平均については正規分布を仮定できる<br><br>

<small>出典：統計WEB「中心極限定理」</small>'''
    ]
)
deck.add_note(note5)

# カード6: 標本平均の分布
note6 = genanki.Note(
    model=model,
    fields=[
        '標本平均の分布について説明してください。',
        '''<b>基本性質</b><br>
母集団の平均を μ、分散を σ² とすると、サンプルサイズ n の標本平均 X̄ について：<br><br>

<b>1. 期待値（平均）</b><br>
\\[E[\\bar{X}] = \\mu\\]<br>
標本平均の期待値は母平均に等しい。<br><br>

<b>2. 分散</b><br>
\\[\\text{Var}(\\bar{X}) = \\frac{\\sigma^2}{n}\\]<br>
標本平均の分散は母分散の 1/n 倍。<br><br>

<b>3. 標準偏差（標準誤差）</b><br>
\\[\\text{SE}(\\bar{X}) = \\frac{\\sigma}{\\sqrt{n}}\\]<br>
標本平均の標準偏差を「標準誤差」と呼ぶ。<br><br>

<b>サンプルサイズの影響</b><br>
・n が大きいほど、標本平均の分散は小さくなる<br>
・n が大きいほど、標本平均は母平均に集中する<br>
・n が大きいほど、推定精度が向上する<br><br>

<b>具体例</b><br>
サイコロを投げる実験：<br>
・5回投げ：標本平均のばらつきが大きい<br>
・200回投げ：標本平均のばらつきが明らかに小さい<br><br>

これは分散が 1/n に比例するため。<br><br>

<small>出典：統計WEB「中心極限定理2」</small>'''
    ]
)
deck.add_note(note6)

# カード7: 標準誤差
note7 = genanki.Note(
    model=model,
    fields=[
        '標準誤差（Standard Error）とは何ですか？標準偏差との違いは？',
        '''<b>定義</b><br>
標本平均の標準偏差のこと。標本平均がどれくらいばらつくかを示す指標。<br><br>

<b>公式</b><br>
\\[\\text{SE} = \\frac{\\sigma}{\\sqrt{n}}\\]<br><br>

ここで：<br>
・σ = 母集団の標準偏差<br>
・n = サンプルサイズ<br><br>

<b>標準偏差との違い</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>標準偏差（SD）</th>
<th>標準誤差（SE）</th>
</tr>
<tr>
<td><b>何を示すか</b></td>
<td>個々のデータのばらつき</td>
<td>標本平均のばらつき</td>
</tr>
<tr>
<td><b>公式</b></td>
<td>σ</td>
<td>σ/√n</td>
</tr>
<tr>
<td><b>用途</b></td>
<td>データの変動を表す</td>
<td>推定の精度を表す</td>
</tr>
<tr>
<td><b>サンプルサイズの影響</b></td>
<td>影響を受けない</td>
<td>n が大きいと小さくなる</td>
</tr>
</table>
<br>

<b>意味</b><br>
標準誤差は、標本平均がどれだけ信頼できるかを示す指標。<br>
・標準誤差が小さい → 推定精度が高い<br>
・標準誤差が大きい → 推定精度が低い<br><br>

<b>具体例</b><br>
母集団の標準偏差 σ = 10 の場合：<br>
・n = 25 のとき：SE = 10/√25 = 2<br>
・n = 100 のとき：SE = 10/√100 = 1<br><br>

サンプルサイズを4倍にすると、標準誤差は半分になる。<br><br>

<small>出典：統計WEB「中心極限定理」</small>'''
    ]
)
deck.add_note(note7)

# カード8: 中心極限定理の標準化
note8 = genanki.Note(
    model=model,
    fields=[
        '中心極限定理における標準化の式を示してください。',
        '''<b>標準化の式</b><br>
標本平均 X̄ を標準化した値 Z は：<br><br>

\\[Z = \\frac{\\bar{X} - \\mu}{\\sigma/\\sqrt{n}}\\]<br><br>

ここで：<br>
・X̄ = 標本平均<br>
・μ = 母平均<br>
・σ = 母標準偏差<br>
・n = サンプルサイズ<br><br>

<b>意味</b><br>
n が大きくなると、Z は標準正規分布 N(0, 1) に収束する。<br><br>

<b>分母の意味</b><br>
σ/√n は標準誤差であり、標本平均のばらつきを表す。<br><br>

<b>応用</b><br>
この標準化により：<br>
・標本平均から母平均を推定できる（区間推定）<br>
・仮説検定が可能になる<br>
・正規分布表（z表）を使った確率計算ができる<br><br>

<b>具体例</b><br>
母平均 μ = 50、母標準偏差 σ = 10、サンプルサイズ n = 100 の場合：<br><br>

標本平均が 52 だったとき：<br>
\\[Z = \\frac{52 - 50}{10/\\sqrt{100}} = \\frac{2}{1} = 2\\]<br><br>

この Z 値を使って、標本平均が 52 以上になる確率などを計算できる。<br><br>

<small>出典：統計WEB「中心極限定理2」</small>'''
    ]
)
deck.add_note(note8)

# カード9: サンプルサイズの目安
note9 = genanki.Note(
    model=model,
    fields=[
        '中心極限定理を適用する際のサンプルサイズの目安は？',
        '''<b>一般的な目安</b><br>
n ≥ 30<br><br>

サンプルサイズが 30 以上あれば、標本平均の分布は正規分布とみなして統計解析を行うことが多い。<br><br>

<b>注意点</b><br>
この「30」という数字は絶対的な基準ではない：<br><br>

<b>母集団が正規分布に従う場合</b><br>
・n が小さくても（n < 30）、標本平均は正規分布に従う<br>
・t分布を使った推定・検定を行う<br><br>

<b>母集団が正規分布から大きく外れる場合</b><br>
・n = 30 でも不十分な場合がある<br>
・より大きなサンプルサイズが必要<br>
・特に歪度が大きい分布や裾の重い分布<br><br>

<b>母集団の分布による違い</b><br>
・対称な分布：n = 20〜30 で十分<br>
・やや歪んだ分布：n = 30〜50 が望ましい<br>
・大きく歪んだ分布：n ≥ 100 が必要な場合も<br><br>

<b>実務上の判断</b><br>
・母集団の分布が不明な場合：n ≥ 30 を目安とする<br>
・母集団が正規分布に近いと考えられる場合：より小さな n でも可<br>
・ヒストグラムやQ-Qプロットで正規性を確認することが望ましい<br><br>

<small>出典：統計WEB、Qiita（統計検定対策記事）</small>'''
    ]
)
deck.add_note(note9)

# カード10: 大数の法則と中心極限定理の違い
note10 = genanki.Note(
    model=model,
    fields=[
        '大数の法則と中心極限定理の違いを説明してください。',
        '''<b>比較表</b><br>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>項目</th>
<th>大数の法則</th>
<th>中心極限定理</th>
</tr>
<tr>
<td><b>主張</b></td>
<td>標本平均が母平均に近づく</td>
<td>標本平均の分布が正規分布に近づく</td>
</tr>
<tr>
<td><b>焦点</b></td>
<td>値の収束</td>
<td>分布の形</td>
</tr>
<tr>
<td><b>結論</b></td>
<td>X̄ → μ</td>
<td>X̄ ∼ N(μ, σ²/n)</td>
</tr>
<tr>
<td><b>応用</b></td>
<td>点推定の正当化</td>
<td>区間推定・仮説検定の基礎</td>
</tr>
</table>
<br>

<b>詳細な説明</b><br><br>

<b>大数の法則</b><br>
・試行回数を増やすと、標本平均が母平均に近づくことを保証<br>
・「どこに収束するか」に焦点<br>
・例：サイコロを1万回振ると、平均は 3.5 に近づく<br><br>

<b>中心極限定理</b><br>
・標本平均の<u>分布</u>が正規分布になることを保証<br>
・「分布の形がどうなるか」に焦点<br>
・例：サイコロを10回振る実験を1000回繰り返すと、得られた1000個の標本平均は正規分布に従う<br><br>

<b>関係性</b><br>
・両者は独立した定理だが、補完的な関係<br>
・大数の法則：標本平均が母平均に収束することを示す<br>
・中心極限定理：その収束の「速さ」や「ばらつき」を正規分布で記述<br><br>

<b>統計的推測における役割</b><br>
・大数の法則：標本平均を使って母平均を推定することが妥当であることを保証<br>
・中心極限定理：その推定の精度（信頼区間）を計算できることを保証<br><br>

<small>出典：Wikipedia、統計WEB、いちばんやさしい医療統計</small>'''
    ]
)
deck.add_note(note10)

# カード11: 中心極限定理の応用例
note11 = genanki.Note(
    model=model,
    fields=[
        '中心極限定理の実用的な応用例を挙げてください。',
        '''<b>1. 区間推定</b><br>
標本平均から母平均の信頼区間を計算：<br><br>

95%信頼区間：<br>
\\[\\bar{X} \\pm 1.96 \\times \\frac{\\sigma}{\\sqrt{n}}\\]<br><br>

中心極限定理により、母集団の分布によらず、この区間が正しく計算できる。<br><br>

<b>2. 仮説検定</b><br>
t検定やz検定の理論的基礎：<br>
・標本平均が正規分布に従うことを前提<br>
・中心極限定理がこの前提を正当化<br><br>

<b>3. 品質管理</b><br>
工場で製品を抜き取り検査する場合：<br>
・標本平均から全体の品質を推定<br>
・管理図（X̄管理図）で工程管理<br><br>

<b>4. 世論調査・視聴率調査</b><br>
・全体の一部を調査して全体を推定<br>
・標本サイズから誤差範囲を計算<br>
・例：視聴率±2.5%という表現の根拠<br><br>

<b>5. 医学研究</b><br>
・臨床試験での治療効果の評価<br>
・標本から母集団の平均的な効果を推定<br><br>

<b>6. A/Bテスト</b><br>
・Webサイトのデザインや機能の比較<br>
・2つのグループの平均値の差を検定<br><br>

<b>7. 金融リスク管理</b><br>
・ポートフォリオのリターンの分布を推定<br>
・VaR（Value at Risk）の計算<br><br>

<b>共通点</b><br>
すべて「標本から母集団を推測する」場面で、中心極限定理が理論的基礎を提供している。<br><br>

<small>出典：統計WEB、AVILEN（中心極限定理の解説）</small>'''
    ]
)
deck.add_note(note11)

# カード12: 中心極限定理の実験例
note12 = genanki.Note(
    model=model,
    fields=[
        '中心極限定理を確認する実験例を説明してください。',
        '''<b>サイコロの実験</b><br><br>

<b>実験1：サイコロを2回投げる</b><br>
・この操作を1000回繰り返す<br>
・各回の標本平均（2個の出目の平均）を記録<br>
・結果：ヒストグラムは正規分布の形が明確でない<br><br>

<b>実験2：サイコロを5回投げる</b><br>
・この操作を1000回繰り返す<br>
・各回の標本平均（5個の出目の平均）を記録<br>
・結果：ヒストグラムが正規分布に近づき始める<br><br>

<b>実験3：サイコロを10回投げる</b><br>
・この操作を1000回繰り返す<br>
・各回の標本平均（10個の出目の平均）を記録<br>
・結果：ヒストグラムは明らかに正規分布の形になる<br><br>

<b>実験4：サイコロを200回投げる</b><br>
・この操作を1000回繰り返す<br>
・各回の標本平均を記録<br>
・結果：<br>
  - 非常にきれいな正規分布の形<br>
  - ばらつきが5回の場合より明らかに小さい<br>
  - 平均は 3.5 に集中<br><br>

<b>観察される現象</b><br>
1. サンプルサイズが大きいほど、標本平均の分布が正規分布に近づく<br>
2. サンプルサイズが大きいほど、標本平均のばらつきが小さくなる（分散 = σ²/n）<br>
3. どのサンプルサイズでも、標本平均の平均は母平均（3.5）に一致<br><br>

<b>重要な気づき</b><br>
元のサイコロの分布は<u>一様分布</u>（正規分布ではない）だが、標本平均の分布は正規分布になる。<br>
これが中心極限定理の威力！<br><br>

<small>出典：統計WEB「中心極限定理」</small>'''
    ]
)
deck.add_note(note12)

# .apkgファイルとして保存
output_file = '/Users/sasaki/law_of_large_numbers_and_clt_verified.apkg'
genanki.Package(deck).write_to_file(output_file)
print(f"Ankiパッケージが作成されました: {output_file}")
print(f"カード枚数: {len(deck.notes)}")
