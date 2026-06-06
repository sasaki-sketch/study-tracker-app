#!/usr/bin/env python3
"""
相関分析（第26章）- Ankiカード作成スクリプト
統計検定2級対応

検証済み情報源:
- 統計WEB (bellcurve.jp) 26-1 ~ 26-5
- 九州大学統計学ガイド
- 高校数学の美しい物語

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
    '統計検定2級_相関分析',
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
    '統計検定2級::26_相関分析'
)

# カードデータ
cards_data = [
    # カード1: 散布図とは
    {
        'question': '''<b>散布図（Scatter Plot）とは</b>

散布図の定義と、何を確認するために使うか？''',
        'answer': '''<b>定義:</b>
2つの変数の関係を視覚的に表すグラフ。各データ点を座標平面上にプロットする。

<b>用途:</b>
<ul>
<li>2変数間の<b>関係の有無</b>を確認</li>
<li><b>関係の方向</b>（正・負）を確認</li>
<li><b>関係の強さ</b>を視覚的に把握</li>
<li><b>外れ値</b>の発見</li>
<li><b>非線形関係</b>の発見</li>
</ul>

<b>散布図から読み取れること:</b>
<ul>
<li>右上がり → 正の相関</li>
<li>右下がり → 負の相関</li>
<li>点がバラバラ → 相関なし</li>
<li>曲線的なパターン → 非線形関係</li>
</ul>

<span class="important">重要:</span> 相関係数を計算する<b>前に</b>必ず散布図を確認すべき''',
        'source': '統計WEB 26-1'
    },

    # カード2: 正の相関と負の相関
    {
        'question': '''<b>正の相関と負の相関</b>

正の相関と負の相関の定義と、具体例は？''',
        'answer': '''<b>正の相関（Positive Correlation）:</b>
<div class="formula">
一方の変数が増加すると、他方も増加する関係
相関係数: \\(0 < r \\leq 1\\)
</div>
<ul>
<li>例: 身長と体重</li>
<li>例: 勉強時間とテストの点数</li>
<li>例: 気温とアイスクリームの売上</li>
</ul>

<b>負の相関（Negative Correlation）:</b>
<div class="formula">
一方の変数が増加すると、他方が減少する関係
相関係数: \\(-1 \\leq r < 0\\)
</div>
<ul>
<li>例: 気温と暖房の使用量</li>
<li>例: 運動量と体脂肪率</li>
<li>例: 価格と需要量</li>
</ul>

<b>無相関（No Correlation）:</b>
<div class="formula">
2変数間に線形関係がない
相関係数: \\(r \\approx 0\\)
</div>

<span class="important">注意:</span> 相関係数が0でも非線形の関係がある場合がある''',
        'source': '統計WEB 26-2'
    },

    # カード3: 相関係数の公式
    {
        'question': '''<b>相関係数（ピアソンの積率相関係数）の公式</b>

相関係数 \\(r\\) を求める公式は？''',
        'answer': '''<b>公式（定義式）:</b>
<div class="formula">
\\[r = \\frac{S_{xy}}{S_x \\cdot S_y} = \\frac{\\text{共分散}}{x\\text{の標準偏差} \\times y\\text{の標準偏差}}\\]
</div>

<b>展開した形:</b>
<div class="formula">
\\[r = \\frac{\\sum_{i=1}^{n}(x_i - \\bar{x})(y_i - \\bar{y})}{\\sqrt{\\sum_{i=1}^{n}(x_i - \\bar{x})^2} \\cdot \\sqrt{\\sum_{i=1}^{n}(y_i - \\bar{y})^2}}\\]
</div>

<b>共分散の公式:</b>
<div class="formula">
\\[S_{xy} = \\frac{1}{n}\\sum_{i=1}^{n}(x_i - \\bar{x})(y_i - \\bar{y})\\]
\\[= \\overline{xy} - \\bar{x}\\bar{y}\\]
</div>

<b>別表現:</b>
<div class="formula">
\\[r = \\frac{\\overline{xy} - \\bar{x}\\bar{y}}{S_x \\cdot S_y}\\]
</div>

<span class="important">覚え方:</span> 相関係数 = 共分散 / (標準偏差の積)''',
        'source': '統計WEB 26-3'
    },

    # カード4: 相関係数の性質
    {
        'question': '''<b>相関係数の性質</b>

相関係数 \\(r\\) が持つ重要な性質は？''',
        'answer': '''<b>性質1: 範囲</b>
<div class="formula">
\\[-1 \\leq r \\leq 1\\]
</div>

<b>性質2: 特別な値の意味</b>
<ul>
<li>\\(r = 1\\): 完全な正の相関（直線上に並ぶ）</li>
<li>\\(r = -1\\): 完全な負の相関（直線上に並ぶ）</li>
<li>\\(r = 0\\): 線形相関なし</li>
</ul>

<b>性質3: 単位に依存しない</b>
<ul>
<li>変数を定数倍しても相関係数は変わらない</li>
<li>例: cmをmに変換しても \\(r\\) は同じ</li>
</ul>

<b>性質4: 線形変換に対する不変性</b>
<div class="formula">
\\(x' = ax + b\\), \\(y' = cy + d\\) (\\(a, c > 0\\)) のとき
\\[r_{x'y'} = r_{xy}\\]
</div>

<b>相関の強さの目安:</b>
<table>
<tr><th>\\(|r|\\)</th><th>相関の強さ</th></tr>
<tr><td>0.7 ~ 1.0</td><td>強い相関</td></tr>
<tr><td>0.4 ~ 0.7</td><td>中程度の相関</td></tr>
<tr><td>0.2 ~ 0.4</td><td>弱い相関</td></tr>
<tr><td>0 ~ 0.2</td><td>ほとんど相関なし</td></tr>
</table>''',
        'source': '統計WEB 26-3'
    },

    # カード5: 相関係数の計算例
    {
        'question': '''<b>【計算問題】相関係数</b>

以下のデータから相関係数を求めよ。

<table>
<tr><th>x</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>
<tr><th>y</th><td>2</td><td>4</td><td>5</td><td>4</td><td>10</td></tr>
</table>''',
        'answer': '''<b>Step 1: 平均を計算</b>
\\[\\bar{x} = \\frac{1+2+3+4+5}{5} = 3\\]
\\[\\bar{y} = \\frac{2+4+5+4+10}{5} = 5\\]

<b>Step 2: 偏差と偏差の積を計算</b>
<table>
<tr><th>\\(x_i\\)</th><th>\\(y_i\\)</th><th>\\(x_i - \\bar{x}\\)</th><th>\\(y_i - \\bar{y}\\)</th><th>積</th></tr>
<tr><td>1</td><td>2</td><td>-2</td><td>-3</td><td>6</td></tr>
<tr><td>2</td><td>4</td><td>-1</td><td>-1</td><td>1</td></tr>
<tr><td>3</td><td>5</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>4</td><td>4</td><td>1</td><td>-1</td><td>-1</td></tr>
<tr><td>5</td><td>10</td><td>2</td><td>5</td><td>10</td></tr>
</table>

<b>Step 3: 各成分を計算</b>
\\[\\sum(x_i - \\bar{x})(y_i - \\bar{y}) = 6+1+0-1+10 = 16\\]
\\[\\sum(x_i - \\bar{x})^2 = 4+1+0+1+4 = 10\\]
\\[\\sum(y_i - \\bar{y})^2 = 9+1+0+1+25 = 36\\]

<b>Step 4: 相関係数を計算</b>
<div class="formula">
\\[r = \\frac{16}{\\sqrt{10} \\times \\sqrt{36}} = \\frac{16}{\\sqrt{360}} \\approx \\frac{16}{18.97} \\approx 0.84\\]
</div>

<div class="example">
<b>答え: \\(r \\approx 0.84\\)</b>（強い正の相関）
</div>''',
        'source': '統計WEB 26-3'
    },

    # カード6: 無相関の検定
    {
        'question': '''<b>無相関の検定</b>

母相関係数 \\(\\rho\\) が0かどうかを検定する方法は？''',
        'answer': '''<b>仮説:</b>
<ul>
<li>帰無仮説: \\(H_0: \\rho = 0\\)（無相関）</li>
<li>対立仮説: \\(H_1: \\rho \\neq 0\\)（相関あり）</li>
</ul>

<b>検定統計量:</b>
<div class="formula">
\\[t = \\frac{r\\sqrt{n-2}}{\\sqrt{1-r^2}}\\]
</div>

<b>従う分布:</b> 自由度 \\(n - 2\\) の<b>t分布</b>

<b>各記号:</b>
<ul>
<li>\\(r\\): 標本相関係数</li>
<li>\\(n\\): サンプルサイズ</li>
</ul>

<b>判定:</b>
\\(|t| > t_{\\alpha/2}(n-2)\\) なら帰無仮説を棄却
→ 「相関がある」と結論

<span class="important">ポイント:</span>
<ul>
<li>サンプルサイズが小さいと、強い相関でも有意にならないことがある</li>
<li>サンプルサイズが大きいと、弱い相関でも有意になることがある</li>
</ul>''',
        'source': '統計WEB 26-3'
    },

    # カード7: 無相関の検定の計算例
    {
        'question': '''<b>【計算問題】無相関の検定</b>

12組のデータから相関係数 \\(r = 0.6\\) が得られた。
有意水準5%で相関があるといえるか？

（参考: \\(t_{0.025}(10) = 2.228\\)）''',
        'answer': '''<b>仮説:</b>
<ul>
<li>\\(H_0: \\rho = 0\\)</li>
<li>\\(H_1: \\rho \\neq 0\\)</li>
</ul>

<b>与えられた値:</b>
<ul>
<li>\\(r = 0.6\\)</li>
<li>\\(n = 12\\)</li>
<li>自由度: \\(n - 2 = 10\\)</li>
</ul>

<b>検定統計量の計算:</b>
<div class="formula">
\\[t = \\frac{r\\sqrt{n-2}}{\\sqrt{1-r^2}} = \\frac{0.6 \\times \\sqrt{10}}{\\sqrt{1-0.36}}\\]
\\[= \\frac{0.6 \\times 3.162}{\\sqrt{0.64}} = \\frac{1.897}{0.8} = 2.37\\]
</div>

<b>判定:</b>
\\(|t| = 2.37 > 2.228\\) → <b>棄却域に入る</b>

<div class="example">
<b>結論:</b> 有意水準5%で帰無仮説を棄却する。
母集団において相関が<b>ある</b>といえる。
</div>''',
        'source': '統計WEB 26-3'
    },

    # カード8: 偏相関係数の定義
    {
        'question': '''<b>偏相関係数とは</b>

偏相関係数の定義と、なぜ必要なのか？''',
        'answer': '''<b>定義:</b>
第3の変数 \\(z\\) の影響を取り除いた、\\(x\\) と \\(y\\) の純粋な相関係数

<div class="formula">
「\\(z\\) の影響を除いた \\(x\\) と \\(y\\) の相関」
</div>

<b>必要な理由:</b>
<ul>
<li><b>疑似相関（見かけ上の相関）</b>を見抜くため</li>
<li>第3の変数が両方に影響している場合、本当の関係を把握できない</li>
</ul>

<b>疑似相関の例:</b>
<div class="example">
「アイスクリームの売上」と「水難事故」に相関がある
→ 実は「気温」が両方に影響している
→ 気温の影響を除くと、相関はほぼ0になる
</div>

<b>偏相関係数と単相関係数の比較:</b>
<table>
<tr><th></th><th>単相関係数</th><th>偏相関係数</th></tr>
<tr><td>意味</td><td>2変数の相関</td><td>第3変数を除いた相関</td></tr>
<tr><td>疑似相関</td><td>検出できない</td><td>検出できる</td></tr>
</table>

<span class="important">重要:</span> 単相関と偏相関に大きな差がある → 交絡あり''',
        'source': '統計WEB 26-4'
    },

    # カード9: 偏相関係数の公式
    {
        'question': '''<b>偏相関係数の公式</b>

\\(z\\) の影響を除いた \\(x\\) と \\(y\\) の偏相関係数 \\(r_{xy \\cdot z}\\) を求める公式は？''',
        'answer': '''<div class="formula">
\\[r_{xy \\cdot z} = \\frac{r_{xy} - r_{xz} \\cdot r_{yz}}{\\sqrt{1 - r_{xz}^2} \\cdot \\sqrt{1 - r_{yz}^2}}\\]
</div>

<b>各記号:</b>
<ul>
<li>\\(r_{xy}\\): \\(x\\) と \\(y\\) の相関係数</li>
<li>\\(r_{xz}\\): \\(x\\) と \\(z\\) の相関係数</li>
<li>\\(r_{yz}\\): \\(y\\) と \\(z\\) の相関係数</li>
</ul>

<b>分子の意味:</b>
\\[r_{xy} - r_{xz} \\cdot r_{yz}\\]
= 「\\(x\\)と\\(y\\)の相関」から「\\(z\\)を経由した間接的な相関」を引く

<b>分母の意味:</b>
\\(z\\) で説明できない部分の調整

<span class="important">特殊なケース:</span>
<ul>
<li>\\(r_{xz} = 0\\) または \\(r_{yz} = 0\\) のとき: \\(r_{xy \\cdot z} = r_{xy}\\)</li>
<li>\\(r_{xy} = r_{xz} \\cdot r_{yz}\\) のとき: \\(r_{xy \\cdot z} = 0\\)（完全な疑似相関）</li>
</ul>''',
        'source': '統計WEB 26-4'
    },

    # カード10: 偏相関係数の計算例
    {
        'question': '''<b>【計算問題】偏相関係数</b>

3つの変数間の相関係数が以下のとき、\\(z\\) の影響を除いた \\(x\\) と \\(y\\) の偏相関係数を求めよ。

<ul>
<li>\\(r_{xy} = 0.8\\)（xとyの相関）</li>
<li>\\(r_{xz} = 0.9\\)（xとzの相関）</li>
<li>\\(r_{yz} = 0.85\\)（yとzの相関）</li>
</ul>''',
        'answer': '''<b>公式に代入:</b>
<div class="formula">
\\[r_{xy \\cdot z} = \\frac{r_{xy} - r_{xz} \\cdot r_{yz}}{\\sqrt{1 - r_{xz}^2} \\cdot \\sqrt{1 - r_{yz}^2}}\\]
</div>

<b>分子の計算:</b>
\\[r_{xy} - r_{xz} \\cdot r_{yz} = 0.8 - 0.9 \\times 0.85\\]
\\[= 0.8 - 0.765 = 0.035\\]

<b>分母の計算:</b>
\\[\\sqrt{1 - 0.9^2} \\cdot \\sqrt{1 - 0.85^2}\\]
\\[= \\sqrt{0.19} \\cdot \\sqrt{0.2775}\\]
\\[= 0.436 \\times 0.527 = 0.230\\]

<b>偏相関係数:</b>
<div class="formula">
\\[r_{xy \\cdot z} = \\frac{0.035}{0.230} \\approx 0.15\\]
</div>

<div class="example">
<b>答え: \\(r_{xy \\cdot z} \\approx 0.15\\)</b>

元の相関係数は0.8（強い相関）だったが、\\(z\\)の影響を除くと0.15（ほぼ無相関）
→ <b>疑似相関</b>であった
</div>''',
        'source': '統計WEB 26-4'
    },

    # カード11: 層別解析
    {
        'question': '''<b>層別解析とは</b>

層別解析の定義と目的は？''',
        'answer': '''<b>定義:</b>
データを特定の要因（層別因子）でグループ分けして、各グループごとに分析を行うこと

<b>目的:</b>
<ul>
<li><b>交絡因子</b>の影響を制御する</li>
<li>グループ間の違いを明らかにする</li>
<li><b>シンプソンのパラドックス</b>を回避する</li>
</ul>

<b>例:</b>
<div class="example">
「新薬の効果」を分析する場合
<ul>
<li>全体で見ると効果なし</li>
<li>年齢層別に分析すると各層で効果あり</li>
</ul>
→ 年齢が交絡因子になっていた
</div>

<b>層別因子の例:</b>
<ul>
<li>性別（男性/女性）</li>
<li>年齢層（若年/中年/高齢）</li>
<li>地域（都市部/地方）</li>
<li>疾患の重症度</li>
</ul>

<span class="important">ポイント:</span> 全体の結果と層別の結果が異なる場合、交絡因子の存在を疑う''',
        'source': '統計WEB 26-5'
    },

    # カード12: シンプソンのパラドックス
    {
        'question': '''<b>シンプソンのパラドックス</b>

シンプソンのパラドックスとは何か？具体例とともに説明せよ。''',
        'answer': '''<b>定義:</b>
<div class="formula">
集団を分割した各グループでは成立する傾向が、
全体を合わせると<b>逆転</b>する現象
</div>

<b>具体例（架空の治療効果）:</b>
<table>
<tr><th></th><th>治療A</th><th>治療B</th></tr>
<tr><td>軽症者</td><td>80/100 (80%)</td><td>70/80 (87.5%)</td></tr>
<tr><td>重症者</td><td>20/80 (25%)</td><td>10/20 (50%)</td></tr>
<tr><td><b>全体</b></td><td><b>100/180 (55.6%)</b></td><td><b>80/100 (80%)</b></td></tr>
</table>

<b>パラドックスの内容:</b>
<ul>
<li>軽症者: 治療B の方が効果的</li>
<li>重症者: 治療B の方が効果的</li>
<li>全体: 治療A の方が効果的<b>（逆転！）</b></li>
</ul>

<b>原因:</b>
治療Aは重症者に多く使われ、治療Bは軽症者に多く使われた
→ 重症度が<b>交絡因子</b>

<span class="important">対策:</span>
<ul>
<li>層別解析を行う</li>
<li>交絡因子を調整した分析を行う</li>
</ul>''',
        'source': '統計WEB, Wikipedia'
    },

    # カード13: 相関と因果関係
    {
        'question': '''<b>相関関係と因果関係</b>

「相関関係がある」ことと「因果関係がある」ことの違いは？''',
        'answer': '''<b>相関関係:</b>
<div class="formula">
2つの変数が<b>一緒に変化する</b>傾向がある
「AとBに関連がある」
</div>

<b>因果関係:</b>
<div class="formula">
一方の変数が他方に<b>影響を与える</b>
「AがBの原因である」
</div>

<span class="important">重要:</span>
<div class="example">
<b>相関関係 ≠ 因果関係</b>

相関があっても因果関係があるとは限らない！
</div>

<b>相関があっても因果がない例:</b>
<ul>
<li><b>疑似相関:</b> 第3の変数が両方に影響
<br>例: アイス売上 ↔ 水難事故（気温が原因）</li>
<li><b>偶然の一致:</b> 統計的に偶然相関が出た</li>
<li><b>逆の因果:</b> BがAの原因かもしれない</li>
</ul>

<b>因果関係を示すには:</b>
<ul>
<li>時間的な前後関係がある</li>
<li>メカニズムが説明できる</li>
<li>ランダム化比較試験（RCT）で確認</li>
<li>交絡因子を調整しても関係が残る</li>
</ul>''',
        'source': '統計WEB 26-4, 26-5'
    },

    # カード14: 相関分析のまとめ
    {
        'question': '''<b>相関分析のまとめ</b>

第26章で学んだ相関分析の主要な公式と概念をまとめよ。''',
        'answer': '''<b>1. 相関係数の公式:</b>
<div class="formula">
\\[r = \\frac{S_{xy}}{S_x \\cdot S_y}\\]
範囲: \\(-1 \\leq r \\leq 1\\)
</div>

<b>2. 無相関の検定:</b>
<div class="formula">
\\[t = \\frac{r\\sqrt{n-2}}{\\sqrt{1-r^2}}\\]
自由度: \\(n - 2\\) のt分布
</div>

<b>3. 偏相関係数:</b>
<div class="formula">
\\[r_{xy \\cdot z} = \\frac{r_{xy} - r_{xz} \\cdot r_{yz}}{\\sqrt{1 - r_{xz}^2} \\cdot \\sqrt{1 - r_{yz}^2}}\\]
</div>

<b>4. 重要な概念:</b>
<table>
<tr><th>用語</th><th>意味</th></tr>
<tr><td>疑似相関</td><td>第3変数が原因の見かけの相関</td></tr>
<tr><td>交絡因子</td><td>両変数に影響を与える第3変数</td></tr>
<tr><td>シンプソンのパラドックス</td><td>層別と全体で結果が逆転</td></tr>
</table>

<span class="important">注意点:</span>
<ul>
<li>相関 ≠ 因果</li>
<li>必ず散布図を確認する</li>
<li>外れ値の影響に注意</li>
</ul>''',
        'source': '統計WEB 26章'
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
output_file = '相関分析_verified.apkg'
genanki.Package(deck).write_to_file(output_file)

print(f"✅ Ankiパッケージを作成しました: {output_file}")
print(f"📊 カード枚数: {len(cards_data)}枚")
print("\n作成されたカード:")
for i, card in enumerate(cards_data, 1):
    title = card['question'].split('\n')[0].replace('<b>', '').replace('</b>', '')
    print(f"  {i}. {title}")
