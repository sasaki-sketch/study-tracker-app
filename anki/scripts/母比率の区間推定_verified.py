#!/usr/bin/env python3
"""
母比率の区間推定 - Ankiカード作成スクリプト
統計検定2級対応

検証済み情報源:
- 統計WEB (bellcurve.jp)
- 統計検定公式問題集

作成日: 2026-01-25
"""

import genanki
import random
from anki_card_css_template import CARD_CSS_NO_TABLE

# 一意のモデルIDとデッキID
MODEL_ID = random.randrange(1 << 30, 1 << 31)
DECK_ID = random.randrange(1 << 30, 1 << 31)

# カードモデル（MathJax対応）
model = genanki.Model(
    MODEL_ID,
    '統計検定2級_母比率の区間推定',
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
    css=CARD_CSS_NO_TABLE
)

# デッキ作成
deck = genanki.Deck(
    DECK_ID,
    '統計検定2級::21_母比率の区間推定'
)

# カードデータ
cards_data = [
    # カード1: 母比率の信頼区間の公式
    {
        'question': '''<b>母比率の信頼区間の公式</b>

標本比率 \\(\\hat{p}\\)、標本サイズ \\(n\\) のとき、母比率 \\(p\\) の信頼区間を求める公式は？''',
        'answer': '''<div class="formula">
\\[\\hat{p} - z_{\\frac{\\alpha}{2}} \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}} \\leq p \\leq \\hat{p} + z_{\\frac{\\alpha}{2}} \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}\\]
</div>

<b>z値（臨界値）:</b>
<ul>
<li>信頼度95%: \\(z = 1.96\\)</li>
<li>信頼度99%: \\(z = 2.58\\)</li>
</ul>

<b>95%信頼区間の場合:</b>
<div class="formula">
\\[\\hat{p} \\pm 1.96 \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}\\]
</div>

<span class="important">注意:</span> \\(n\\) が十分大きいとき（目安: \\(n\\hat{p} \\geq 5\\) かつ \\(n(1-\\hat{p}) \\geq 5\\)）に使用可能''',
        'source': '統計WEB 21-1, 21-2'
    },

    # カード2: 公式の導出（理論的背景）
    {
        'question': '''<b>母比率の信頼区間の導出</b>

なぜ母比率の区間推定で正規分布を使うことができるのか？
導出の流れを説明せよ。''',
        'answer': '''<b>導出の流れ:</b>

<b>Step 1: 二項分布</b>
成功回数 \\(X\\) は二項分布に従う:
\\[X \\sim B(n, p)\\]

<b>Step 2: 正規近似（中心極限定理）</b>
\\(n\\) が大きいとき、標本比率 \\(\\hat{p} = X/n\\) は近似的に正規分布に従う:
\\[\\hat{p} \\sim N\\left(p, \\frac{p(1-p)}{n}\\right)\\]

<b>Step 3: 標準化</b>
\\[Z = \\frac{\\hat{p} - p}{\\sqrt{\\frac{p(1-p)}{n}}} \\sim N(0, 1)\\]

<b>Step 4: 母比率の置換</b>
分母の \\(p\\) を標本比率 \\(\\hat{p}\\) で置き換える（大標本では一致推定量）

<span class="important">ポイント:</span> 二項分布 → 正規近似 → 標準化 → 母比率を標本比率で置換''',
        'source': '統計WEB 21-1'
    },

    # カード3: 計算例1
    {
        'question': '''<b>【計算問題】母比率の信頼区間</b>

テレビ番組の視聴率調査で、100人中10人がA番組を視聴していた。

A番組の視聴率の<b>95%信頼区間</b>を求めよ。''',
        'answer': '''<b>与えられた値:</b>
<ul>
<li>標本サイズ: \\(n = 100\\)</li>
<li>視聴者数: 10人</li>
<li>標本比率: \\(\\hat{p} = 10/100 = 0.1\\)</li>
</ul>

<b>計算:</b>
<div class="formula">
\\[\\hat{p} \\pm 1.96 \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}\\]
\\[= 0.1 \\pm 1.96 \\sqrt{\\frac{0.1 \\times 0.9}{100}}\\]
\\[= 0.1 \\pm 1.96 \\times 0.03\\]
\\[= 0.1 \\pm 0.059\\]
</div>

<div class="example">
<b>答え: 4.1% ～ 15.9%</b>

または \\(0.041 \\leq p \\leq 0.159\\)
</div>''',
        'source': '統計WEB 21-2'
    },

    # カード4: 計算例2
    {
        'question': '''<b>【計算問題】母比率の信頼区間</b>

新商品の試食調査で、400人中100人が「おいしい」と回答した。

「おいしい」と感じる人の母比率の<b>95%信頼区間</b>を求めよ。''',
        'answer': '''<b>与えられた値:</b>
<ul>
<li>標本サイズ: \\(n = 400\\)</li>
<li>「おいしい」回答者: 100人</li>
<li>標本比率: \\(\\hat{p} = 100/400 = 0.25\\)</li>
</ul>

<b>計算:</b>
<div class="formula">
\\[\\hat{p} \\pm 1.96 \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}\\]
\\[= 0.25 \\pm 1.96 \\sqrt{\\frac{0.25 \\times 0.75}{400}}\\]
\\[= 0.25 \\pm 1.96 \\times 0.0217\\]
\\[= 0.25 \\pm 0.042\\]
</div>

<div class="example">
<b>答え: 20.8% ～ 29.2%</b>

または \\(0.208 \\leq p \\leq 0.292\\)
</div>

<span class="important">補足:</span> 肯定回答と否定回答の信頼区間の幅は等しい''',
        'source': '統計WEB 21-2'
    },

    # カード5: 必要なサンプルサイズの公式
    {
        'question': '''<b>必要なサンプルサイズの公式</b>

母比率の区間推定で、信頼区間の幅を一定以下に抑えるために必要なサンプルサイズ \\(n\\) を求める公式は？''',
        'answer': '''<b>信頼区間の幅の条件:</b>
\\[2 \\times z_{\\frac{\\alpha}{2}} \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}} \\leq d\\]

ここで \\(d\\) は許容する信頼区間の幅

<b>サンプルサイズの公式:</b>
<div class="formula">
\\[n \\geq \\left( \\frac{2 \\times z_{\\frac{\\alpha}{2}} \\times \\sqrt{\\hat{p}(1-\\hat{p})}}{d} \\right)^2\\]
</div>

<b>95%信頼区間の場合:</b>
<div class="formula">
\\[n \\geq \\left( \\frac{2 \\times 1.96 \\times \\sqrt{\\hat{p}(1-\\hat{p})}}{d} \\right)^2\\]
</div>

<span class="important">ポイント:</span> 信頼区間の幅は \\(\\sqrt{n}\\) に反比例するため、幅を半分にするには \\(n\\) を4倍にする必要がある''',
        'source': '統計WEB 21-4'
    },

    # カード6: 母比率不明時のサンプルサイズ
    {
        'question': '''<b>母比率が不明な場合のサンプルサイズ</b>

事前に母比率の予測が困難な場合、必要なサンプルサイズを求めるにはどうすればよいか？''',
        'answer': '''<b>方法:</b> \\(\\hat{p} = 0.5\\) を使用する

<b>理由:</b>
<ul>
<li>\\(\\hat{p}(1-\\hat{p})\\) は \\(\\hat{p} = 0.5\\) のとき最大値 \\(0.25\\) をとる</li>
<li>これにより信頼区間の幅が最大になる</li>
<li>最大の幅に対応するサンプルサイズを確保すれば、実際の \\(\\hat{p}\\) がどのような値でも条件を満たす</li>
</ul>

<div class="formula">
<b>95%信頼区間、幅4%以下の場合:</b>
\\[n \\geq \\left( \\frac{2 \\times 1.96 \\times \\sqrt{0.5 \\times 0.5}}{0.04} \\right)^2\\]
\\[n \\geq \\left( \\frac{1.96}{0.04} \\right)^2 = 49^2 = 2401\\]
</div>

<span class="important">結論:</span> 母比率不明なら \\(\\hat{p} = 0.5\\) で計算（最も保守的）''',
        'source': '統計WEB 21-5'
    },

    # カード7: サンプルサイズ計算例
    {
        'question': '''<b>【計算問題】必要なサンプルサイズ</b>

視聴率調査を行う。事前調査で視聴率は10%以下と推測されている。

95%信頼区間の幅を<b>5%以下</b>にするには、何人以上に調査する必要があるか？''',
        'answer': '''<b>与えられた条件:</b>
<ul>
<li>信頼度: 95%（\\(z = 1.96\\)）</li>
<li>推定視聴率: \\(\\hat{p} = 0.1\\)（最大値を使用）</li>
<li>許容幅: \\(d = 0.05\\)</li>
</ul>

<b>計算:</b>
<div class="formula">
\\[n \\geq \\left( \\frac{2 \\times 1.96 \\times \\sqrt{0.1 \\times 0.9}}{0.05} \\right)^2\\]
\\[= \\left( \\frac{3.92 \\times 0.3}{0.05} \\right)^2\\]
\\[= \\left( \\frac{1.176}{0.05} \\right)^2\\]
\\[= 23.52^2 = 553.2\\]
</div>

<div class="example">
<b>答え: 554人以上</b>
</div>

<span class="important">注意:</span> サンプルサイズは切り上げる''',
        'source': '統計WEB 21-4'
    },

    # カード8: 母比率の差の信頼区間の公式
    {
        'question': '''<b>母比率の差の信頼区間の公式</b>

2つの母集団から得た標本比率 \\(\\hat{p}_1, \\hat{p}_2\\) を用いて、母比率の差 \\(p_1 - p_2\\) の信頼区間を求める公式は？''',
        'answer': '''<div class="formula">
\\[(\\hat{p}_1 - \\hat{p}_2) \\pm z_{\\frac{\\alpha}{2}} \\sqrt{\\frac{\\hat{p}_1(1-\\hat{p}_1)}{n_1} + \\frac{\\hat{p}_2(1-\\hat{p}_2)}{n_2}}\\]
</div>

<b>95%信頼区間の場合:</b>
<div class="formula">
\\[(\\hat{p}_1 - \\hat{p}_2) \\pm 1.96 \\sqrt{\\frac{\\hat{p}_1(1-\\hat{p}_1)}{n_1} + \\frac{\\hat{p}_2(1-\\hat{p}_2)}{n_2}}\\]
</div>

<b>導出の背景:</b>
<ul>
<li>正規分布の再生性により、標本比率の差も正規分布に従う</li>
<li>分散は各標本の分散の和となる（独立性）</li>
</ul>

<span class="important">検定への応用:</span> 信頼区間に0が含まれなければ、母比率の差は有意''',
        'source': '統計WEB 21-6'
    },

    # カード9: 母比率の差の計算例
    {
        'question': '''<b>【計算問題】母比率の差の信頼区間</b>

野菜ジュースの購買意欲調査:
<ul>
<li>女性: 200人中80人が「買いたい」</li>
<li>男性: 300人中60人が「買いたい」</li>
</ul>

女性と男性の購買意欲の差の<b>95%信頼区間</b>を求めよ。''',
        'answer': '''<b>与えられた値:</b>
<ul>
<li>女性: \\(n_1 = 200\\), \\(\\hat{p}_1 = 80/200 = 0.4\\)</li>
<li>男性: \\(n_2 = 300\\), \\(\\hat{p}_2 = 60/300 = 0.2\\)</li>
</ul>

<b>標本比率の差:</b>
\\[\\hat{p}_1 - \\hat{p}_2 = 0.4 - 0.2 = 0.2\\]

<b>標準誤差の計算:</b>
<div class="formula">
\\[SE = \\sqrt{\\frac{0.4 \\times 0.6}{200} + \\frac{0.2 \\times 0.8}{300}}\\]
\\[= \\sqrt{0.0012 + 0.000533} = \\sqrt{0.001733}\\]
\\[= 0.0416\\]
</div>

<b>95%信頼区間:</b>
\\[0.2 \\pm 1.96 \\times 0.0416 = 0.2 \\pm 0.082\\]

<div class="example">
<b>答え: 0.118 ～ 0.282（11.8% ～ 28.2%）</b>
</div>

<span class="important">解釈:</span> 0を含まないので、女性の方が有意に購買意欲が高い''',
        'source': '統計WEB 21-6'
    },

    # カード10: 正規近似の条件
    {
        'question': '''<b>母比率の区間推定で正規近似が使える条件</b>

二項分布を正規分布で近似するための条件は何か？''',
        'answer': '''<b>正規近似の条件（目安）:</b>

<div class="formula">
\\[n\\hat{p} \\geq 5 \\quad \\text{かつ} \\quad n(1-\\hat{p}) \\geq 5\\]
</div>

<b>意味:</b>
<ul>
<li>成功の期待回数が5以上</li>
<li>失敗の期待回数が5以上</li>
</ul>

<b>例:</b>
<ul>
<li>\\(n = 100, \\hat{p} = 0.1\\) → \\(n\\hat{p} = 10 \\geq 5\\), \\(n(1-\\hat{p}) = 90 \\geq 5\\) ✓</li>
<li>\\(n = 20, \\hat{p} = 0.1\\) → \\(n\\hat{p} = 2 < 5\\) ✗</li>
</ul>

<span class="important">条件を満たさない場合:</span>
<ul>
<li>二項分布の正確な確率計算を使用</li>
<li>または、より大きなサンプルサイズが必要</li>
</ul>''',
        'source': '統計WEB 21-1'
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
output_file = '母比率の区間推定_verified.apkg'
genanki.Package(deck).write_to_file(output_file)

print(f"✅ Ankiパッケージを作成しました: {output_file}")
print(f"📊 カード枚数: {len(cards_data)}枚")
print("\n作成されたカード:")
for i, card in enumerate(cards_data, 1):
    # 最初の行だけ表示
    title = card['question'].split('\n')[0].replace('<b>', '').replace('</b>', '')
    print(f"  {i}. {title}")
