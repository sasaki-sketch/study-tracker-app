#!/usr/bin/env python3
"""
さまざまな検定（第25章）- Ankiカード作成スクリプト
統計検定2級対応

検証済み情報源:
- 統計WEB (bellcurve.jp) 25-1 ~ 25-7
- とけたろうブログ
- 千葉大学統計学資料

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
    '統計検定2級_さまざまな検定',
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
    '統計検定2級::25_さまざまな検定'
)

# カードデータ
cards_data = [
    # カード1: 母比率の検定の公式
    {
        'question': '''<b>母比率の検定（1標本）の公式</b>

母比率 \\(p\\) に関する検定で、標本比率 \\(\\hat{p}\\)、標本サイズ \\(n\\) のとき、検定統計量の公式は？''',
        'answer': '''<div class="formula">
\\[z = \\frac{\\hat{p} - p_0}{\\sqrt{\\frac{p_0(1-p_0)}{n}}}\\]
</div>

<b>各記号:</b>
<ul>
<li>\\(\\hat{p}\\): 標本比率</li>
<li>\\(p_0\\): 帰無仮説での母比率</li>
<li>\\(n\\): 標本サイズ</li>
</ul>

<b>従う分布:</b> 標準正規分布 \\(N(0, 1)\\)

<b>仮説:</b>
<ul>
<li>帰無仮説: \\(H_0: p = p_0\\)</li>
<li>対立仮説: \\(H_1: p \\neq p_0\\)（両側）または \\(p > p_0\\), \\(p < p_0\\)（片側）</li>
</ul>

<span class="important">適用条件:</span> \\(np_0 \\geq 5\\) かつ \\(n(1-p_0) \\geq 5\\)''',
        'source': '統計WEB 25-1'
    },

    # カード2: 母比率の検定と母平均の検定の違い
    {
        'question': '''<b>母比率の検定と母平均の検定の違い</b>

検定統計量の分母（標準誤差）の計算で、母比率の検定と母平均の検定はどう異なるか？''',
        'answer': '''<b>母比率の検定:</b>
<div class="formula">
標準誤差 = \\(\\sqrt{\\frac{p_0(1-p_0)}{n}}\\)

分母に<b>帰無仮説の値 \\(p_0\\)</b> を使う
</div>

<b>母平均の検定:</b>
<div class="formula">
標準誤差 = \\(\\sqrt{\\frac{s^2}{n}}\\) または \\(\\sqrt{\\frac{\\sigma^2}{n}}\\)

分母に<b>標本から計算した値</b>（不偏分散 or 母分散）を使う
</div>

<span class="important">重要な違い:</span>
<ul>
<li>母比率の検定: 帰無仮説の \\(p_0\\) から標準誤差を計算</li>
<li>母平均の検定: 標本データから標準誤差を計算</li>
</ul>

<b>理由:</b> 母比率の場合、\\(p\\) が分かれば分散 \\(p(1-p)\\) も決まるため''',
        'source': '統計WEB 25-1'
    },

    # カード3: 母比率の検定の計算例
    {
        'question': '''<b>【計算問題】母比率の検定</b>

あるコインを100回投げたところ、60回表が出た。
このコインは公正（表が出る確率が50%）といえるか？

有意水準5%で両側検定を行え。
（参考: \\(z_{0.025} = 1.96\\)）''',
        'answer': '''<b>仮説:</b>
<ul>
<li>\\(H_0: p = 0.5\\)</li>
<li>\\(H_1: p \\neq 0.5\\)</li>
</ul>

<b>与えられた値:</b>
<ul>
<li>\\(n = 100\\), \\(\\hat{p} = 60/100 = 0.6\\), \\(p_0 = 0.5\\)</li>
</ul>

<b>検定統計量の計算:</b>
<div class="formula">
\\[z = \\frac{0.6 - 0.5}{\\sqrt{\\frac{0.5 \\times 0.5}{100}}} = \\frac{0.1}{\\sqrt{0.0025}} = \\frac{0.1}{0.05} = 2.0\\]
</div>

<b>判定:</b>
\\(|z| = 2.0 > 1.96\\) → <b>棄却域に入る</b>

<div class="example">
<b>結論:</b> 有意水準5%で帰無仮説を棄却する。
このコインは公正とはいえない（表が出やすい）。
</div>''',
        'source': '統計WEB 25-1'
    },

    # カード4: 二項分布を用いた検定
    {
        'question': '''<b>二項分布を用いた検定</b>

正規近似ができない（\\(np < 5\\) など）場合、母比率の検定はどのように行うか？''',
        'answer': '''<b>方法:</b> 二項分布の確率を直接計算してP値を求める

<b>考え方:</b>
成功回数 \\(X\\) は二項分布 \\(B(n, p_0)\\) に従う
→ 観測値以上に極端な値が出る確率（P値）を計算

<b>P値の計算:</b>
<ul>
<li>右片側検定: \\(P(X \\geq x)\\)</li>
<li>左片側検定: \\(P(X \\leq x)\\)</li>
<li>両側検定: 小さい方の確率 × 2</li>
</ul>

<div class="example">
<b>例:</b> 10回中8回成功、\\(p_0 = 0.5\\) の両側検定
\\[P(X \\geq 8) = P(8) + P(9) + P(10)\\]
\\[= \\binom{10}{8}(0.5)^{10} + \\binom{10}{9}(0.5)^{10} + \\binom{10}{10}(0.5)^{10}\\]
\\[= (45 + 10 + 1) \\times \\frac{1}{1024} = \\frac{56}{1024} \\approx 0.055\\]
両側P値 ≈ 0.11 > 0.05 → 棄却しない
</div>

<span class="important">使用場面:</span> 標本サイズが小さく正規近似が不適切な場合''',
        'source': '統計WEB 25-2'
    },

    # カード5: ポアソン分布を用いた検定
    {
        'question': '''<b>ポアソン分布を用いた検定</b>

ポアソン分布に従う事象の発生率に関する検定はどのように行うか？''',
        'answer': '''<b>ポアソン分布の特徴:</b>
<ul>
<li>稀な事象の発生回数をモデル化</li>
<li>期待値 = 分散 = \\(\\lambda\\)</li>
<li>例: 事故件数、不良品数、来客数</li>
</ul>

<b>検定方法（大標本）:</b>
<div class="formula">
\\[z = \\frac{\\bar{X} - \\lambda_0}{\\sqrt{\\lambda_0 / n}}\\]
</div>

<b>ポアソン分布の再生性:</b>
\\(X_1, X_2, \\ldots, X_n\\) が独立に \\(Po(\\lambda)\\) に従うとき
\\[\\sum_{i=1}^{n} X_i \\sim Po(n\\lambda)\\]

<div class="example">
<b>例:</b> 月平均20件の事故が起こる交差点で、対策後1年間で180件に減少。効果はあるか？

帰無仮説: \\(\\lambda = 20\\)（月平均）
期待値: \\(12 \\times 20 = 240\\)件/年
検定統計量: \\(z = \\frac{180 - 240}{\\sqrt{240}} \\approx -3.87\\)
→ 有意に減少
</div>''',
        'source': '統計WEB 25-3'
    },

    # カード6: 適合度の検定の公式
    {
        'question': '''<b>適合度の検定（カイ二乗検定）の公式</b>

観測度数が理論分布に適合するかを検定するカイ二乗統計量の公式と自由度は？''',
        'answer': '''<div class="formula">
\\[\\chi^2 = \\sum_{i=1}^{k} \\frac{(O_i - E_i)^2}{E_i}\\]
</div>

<b>各記号:</b>
<ul>
<li>\\(O_i\\): 観測度数（実測値）</li>
<li>\\(E_i\\): 期待度数（理論値）</li>
<li>\\(k\\): カテゴリ数</li>
</ul>

<b>自由度:</b>
<div class="formula">
\\[df = k - 1 - c\\]
</div>
<ul>
<li>\\(k\\): カテゴリ数</li>
<li>\\(c\\): 推定した母数の数（通常は0）</li>
</ul>

<b>仮説:</b>
<ul>
<li>\\(H_0\\): 観測度数は理論分布に適合する</li>
<li>\\(H_1\\): 観測度数は理論分布に適合しない</li>
</ul>

<span class="important">注意:</span>
<ul>
<li>期待度数は全て5以上が望ましい</li>
<li>片側検定（上側）のみ使用</li>
</ul>''',
        'source': '統計WEB 25-4'
    },

    # カード7: 適合度の検定の計算例
    {
        'question': '''<b>【計算問題】適合度の検定</b>

サイコロを60回投げた結果:
<table>
<tr><th>目</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr>
<tr><td>回数</td><td>8</td><td>12</td><td>7</td><td>15</td><td>9</td><td>9</td></tr>
</table>

このサイコロは公正（各目が等確率）といえるか？
有意水準5%で検定せよ。（参考: \\(\\chi^2_{0.05}(5) = 11.07\\)）''',
        'answer': '''<b>仮説:</b>
<ul>
<li>\\(H_0\\): 各目の出る確率は1/6で等しい</li>
<li>\\(H_1\\): 各目の出る確率は等しくない</li>
</ul>

<b>期待度数:</b> 各目 \\(E_i = 60 \\times \\frac{1}{6} = 10\\)

<b>カイ二乗値の計算:</b>
<div class="formula">
\\[\\chi^2 = \\frac{(8-10)^2}{10} + \\frac{(12-10)^2}{10} + \\frac{(7-10)^2}{10}\\]
\\[+ \\frac{(15-10)^2}{10} + \\frac{(9-10)^2}{10} + \\frac{(9-10)^2}{10}\\]
\\[= \\frac{4+4+9+25+1+1}{10} = \\frac{44}{10} = 4.4\\]
</div>

<b>自由度:</b> \\(df = 6 - 1 = 5\\)

<b>判定:</b>
\\(\\chi^2 = 4.4 < 11.07\\) → <b>棄却域に入らない</b>

<div class="example">
<b>結論:</b> 有意水準5%で帰無仮説を棄却できない。
このサイコロは公正であると考えてよい。
</div>''',
        'source': '統計WEB 25-4'
    },

    # カード8: 独立性の検定の公式
    {
        'question': '''<b>独立性の検定（カイ二乗検定）の公式</b>

分割表（クロス集計表）における独立性の検定で、検定統計量と自由度の公式は？''',
        'answer': '''<b>検定統計量:</b>
<div class="formula">
\\[\\chi^2 = \\sum_{i} \\sum_{j} \\frac{(O_{ij} - E_{ij})^2}{E_{ij}}\\]
</div>

<b>期待度数の計算:</b>
<div class="formula">
\\[E_{ij} = \\frac{(\\text{行}i\\text{の合計}) \\times (\\text{列}j\\text{の合計})}{\\text{総計}}\\]
</div>

<b>自由度:</b>
<div class="formula">
\\[df = (r - 1) \\times (c - 1)\\]
</div>
<ul>
<li>\\(r\\): 行数</li>
<li>\\(c\\): 列数</li>
</ul>

<b>仮説:</b>
<ul>
<li>\\(H_0\\): 2つの分類基準は独立である（関連がない）</li>
<li>\\(H_1\\): 2つの分類基準は独立でない（関連がある）</li>
</ul>

<span class="important">ポイント:</span> 期待度数 = (行計 × 列計) / 総計''',
        'source': '統計WEB 25-5'
    },

    # カード9: 独立性の検定の計算例
    {
        'question': '''<b>【計算問題】独立性の検定</b>

喫煙習慣と肺がんの関係:
<table>
<tr><th></th><th>肺がんあり</th><th>肺がんなし</th><th>計</th></tr>
<tr><td>喫煙者</td><td>40</td><td>60</td><td>100</td></tr>
<tr><td>非喫煙者</td><td>10</td><td>90</td><td>100</td></tr>
<tr><td>計</td><td>50</td><td>150</td><td>200</td></tr>
</table>

喫煙と肺がんに関連はあるか？有意水準5%で検定せよ。
（参考: \\(\\chi^2_{0.05}(1) = 3.84\\)）''',
        'answer': '''<b>期待度数の計算:</b>
<table>
<tr><th></th><th>肺がんあり</th><th>肺がんなし</th></tr>
<tr><td>喫煙者</td><td>\\(\\frac{100 \\times 50}{200} = 25\\)</td><td>\\(\\frac{100 \\times 150}{200} = 75\\)</td></tr>
<tr><td>非喫煙者</td><td>\\(\\frac{100 \\times 50}{200} = 25\\)</td><td>\\(\\frac{100 \\times 150}{200} = 75\\)</td></tr>
</table>

<b>カイ二乗値の計算:</b>
<div class="formula">
\\[\\chi^2 = \\frac{(40-25)^2}{25} + \\frac{(60-75)^2}{75} + \\frac{(10-25)^2}{25} + \\frac{(90-75)^2}{75}\\]
\\[= \\frac{225}{25} + \\frac{225}{75} + \\frac{225}{25} + \\frac{225}{75}\\]
\\[= 9 + 3 + 9 + 3 = 24\\]
</div>

<b>自由度:</b> \\(df = (2-1) \\times (2-1) = 1\\)

<b>判定:</b> \\(\\chi^2 = 24 > 3.84\\) → <b>棄却域に入る</b>

<div class="example">
<b>結論:</b> 喫煙と肺がんには<b>有意な関連がある</b>。
</div>''',
        'source': '統計WEB 25-5'
    },

    # カード10: 2×2分割表の簡便公式
    {
        'question': '''<b>2×2分割表のカイ二乗統計量の簡便公式</b>

2×2分割表でカイ二乗統計量を素早く計算する公式は？''',
        'answer': '''<b>2×2分割表:</b>
<table>
<tr><th></th><th>列1</th><th>列2</th><th>計</th></tr>
<tr><td>行1</td><td>a</td><td>b</td><td>a+b</td></tr>
<tr><td>行2</td><td>c</td><td>d</td><td>c+d</td></tr>
<tr><td>計</td><td>a+c</td><td>b+d</td><td>N</td></tr>
</table>

<b>簡便公式:</b>
<div class="formula">
\\[\\chi^2 = \\frac{N(ad - bc)^2}{(a+b)(c+d)(a+c)(b+d)}\\]
</div>

<b>イェーツの補正（連続修正）:</b>
<div class="formula">
\\[\\chi^2 = \\frac{N(|ad - bc| - \\frac{N}{2})^2}{(a+b)(c+d)(a+c)(b+d)}\\]
</div>

<span class="important">イェーツの補正を使う場合:</span>
<ul>
<li>期待度数が小さい場合（5未満のセルがある）</li>
<li>より保守的な検定が必要な場合</li>
</ul>

<b>自由度:</b> \\(df = 1\\)（2×2分割表では常に1）''',
        'source': '統計WEB 25-5'
    },

    # カード11: 母比率の差の検定
    {
        'question': '''<b>母比率の差の検定（2標本）の公式</b>

2つの母集団の母比率に差があるかを検定する統計量の公式は？''',
        'answer': '''<b>検定統計量:</b>
<div class="formula">
\\[z = \\frac{\\hat{p}_1 - \\hat{p}_2}{\\sqrt{\\hat{p}(1-\\hat{p})\\left(\\frac{1}{n_1} + \\frac{1}{n_2}\\right)}}\\]
</div>

<b>プールした標本比率:</b>
<div class="formula">
\\[\\hat{p} = \\frac{x_1 + x_2}{n_1 + n_2}\\]
</div>

<b>各記号:</b>
<ul>
<li>\\(\\hat{p}_1, \\hat{p}_2\\): 各群の標本比率</li>
<li>\\(x_1, x_2\\): 各群の成功数</li>
<li>\\(n_1, n_2\\): 各群のサンプルサイズ</li>
<li>\\(\\hat{p}\\): プールした標本比率</li>
</ul>

<b>従う分布:</b> 標準正規分布 \\(N(0, 1)\\)

<b>仮説:</b>
<ul>
<li>\\(H_0: p_1 = p_2\\)（差がない）</li>
<li>\\(H_1: p_1 \\neq p_2\\)（差がある）</li>
</ul>

<span class="important">重要:</span> 帰無仮説のもとでは \\(p_1 = p_2\\) なので、プールした比率を使う''',
        'source': '統計WEB 25-7'
    },

    # カード12: 母比率の差の検定と独立性の検定の関係
    {
        'question': '''<b>母比率の差の検定と独立性の検定の関係</b>

2×2分割表における「独立性の検定」と「母比率の差の検定」はどのような関係にあるか？''',
        'answer': '''<b>関係:</b>
<div class="formula">
2×2分割表では、<b>独立性の検定</b>と<b>母比率の差の検定</b>は<b>等価</b>である
</div>

<b>数学的な関係:</b>
\\[\\chi^2 = z^2\\]

<ul>
<li>独立性の検定: カイ二乗統計量を使用</li>
<li>母比率の差の検定: z統計量を使用</li>
<li>z値を二乗するとカイ二乗値になる</li>
</ul>

<b>例:</b>
z = 2.0 のとき、\\(\\chi^2 = 4.0\\)
<ul>
<li>\\(z_{0.025} = 1.96\\) → \\((1.96)^2 = 3.84 = \\chi^2_{0.05}(1)\\)</li>
</ul>

<b>使い分け:</b>
<table>
<tr><th>検定</th><th>使用場面</th></tr>
<tr><td>母比率の差の検定</td><td>2群の比率の差に興味がある</td></tr>
<tr><td>独立性の検定</td><td>2変数の関連に興味がある</td></tr>
</table>

<span class="important">結論:</span> どちらを使っても結果は同じ''',
        'source': '統計WEB 25-7'
    },

    # カード13: 検定の種類まとめ
    {
        'question': '''<b>さまざまな検定のまとめ</b>

第25章で学んだ検定の種類と、それぞれの検定統計量・自由度をまとめよ。''',
        'answer': '''<table>
<tr><th>検定</th><th>統計量</th><th>分布</th><th>自由度</th></tr>
<tr><td>母比率の検定</td><td>z</td><td>\\(N(0,1)\\)</td><td>—</td></tr>
<tr><td>母比率の差の検定</td><td>z</td><td>\\(N(0,1)\\)</td><td>—</td></tr>
<tr><td>適合度の検定</td><td>\\(\\chi^2\\)</td><td>\\(\\chi^2\\)</td><td>\\(k-1\\)</td></tr>
<tr><td>独立性の検定</td><td>\\(\\chi^2\\)</td><td>\\(\\chi^2\\)</td><td>\\((r-1)(c-1)\\)</td></tr>
</table>

<b>カイ二乗検定の共通公式:</b>
<div class="formula">
\\[\\chi^2 = \\sum \\frac{(O - E)^2}{E}\\]
（観測値 − 期待値）²/ 期待値 の総和
</div>

<b>主な臨界値:</b>
<ul>
<li>\\(z_{0.025} = 1.96\\)（両側5%）</li>
<li>\\(z_{0.05} = 1.645\\)（片側5%）</li>
<li>\\(\\chi^2_{0.05}(1) = 3.84\\)</li>
<li>\\(\\chi^2_{0.05}(2) = 5.99\\)</li>
</ul>

<span class="important">共通点:</span> すべて大標本を前提とした近似検定''',
        'source': '統計WEB 25章'
    },

    # カード14: フィッシャーの正確確率検定
    {
        'question': '''<b>フィッシャーの正確確率検定</b>

カイ二乗検定が適切でない場合に使う「フィッシャーの正確確率検定」とは？''',
        'answer': '''<b>定義:</b>
期待度数が小さい場合に用いる、分割表の正確な確率計算に基づく検定

<b>使用条件:</b>
<ul>
<li>期待度数が5未満のセルがある場合</li>
<li>サンプルサイズが小さい場合</li>
<li>2×2分割表で特に有効</li>
</ul>

<b>特徴:</b>
<ul>
<li>超幾何分布を用いて正確なP値を計算</li>
<li>近似ではなく正確な検定</li>
<li>保守的（Type I errorを抑える）</li>
</ul>

<b>カイ二乗検定との比較:</b>
<table>
<tr><th>カイ二乗検定</th><th>フィッシャーの検定</th></tr>
<tr><td>近似検定</td><td>正確検定</td></tr>
<tr><td>大標本向け</td><td>小標本でも可</td></tr>
<tr><td>計算が簡単</td><td>計算が複雑</td></tr>
</table>

<span class="important">統計検定2級では:</span> 計算方法より「いつ使うか」の判断が重要''',
        'source': '統計WEB 25-5, 千葉大学資料'
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
output_file = 'さまざまな検定_verified.apkg'
genanki.Package(deck).write_to_file(output_file)

print(f"✅ Ankiパッケージを作成しました: {output_file}")
print(f"📊 カード枚数: {len(cards_data)}枚")
print("\n作成されたカード:")
for i, card in enumerate(cards_data, 1):
    title = card['question'].split('\n')[0].replace('<b>', '').replace('</b>', '')
    print(f"  {i}. {title}")
