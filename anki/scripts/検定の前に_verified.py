#!/usr/bin/env python3
"""
検定の前に（仮説検定の基礎）- Ankiカード作成スクリプト
統計検定2級対応

検証済み情報源:
- 統計WEB (bellcurve.jp)
- 総務省統計局
- Wikipedia

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
    '統計検定2級_検定の前に',
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
    '統計検定2級::23_検定の前に'
)

# カードデータ
cards_data = [
    # カード1: 仮説検定とは
    {
        'question': '''<b>仮説検定（統計的仮説検定）とは</b>

仮説検定の基本的な考え方を説明せよ。''',
        'answer': '''<b>定義:</b>
母集団に関する仮説を立て、標本データに基づいてその仮説が正しいかどうかを統計的に判断する方法

<b>基本的な流れ:</b>
<ol>
<li><b>仮説を立てる</b>（帰無仮説と対立仮説）</li>
<li><b>有意水準を決める</b>（通常5%または1%）</li>
<li><b>検定統計量を計算</b></li>
<li><b>P値を求める</b>または<b>棄却域と比較</b></li>
<li><b>結論を出す</b>（棄却するか、しないか）</li>
</ol>

<b>背理法との類似点:</b>
<ul>
<li>「正しくない」と思われる仮説をまず仮定する</li>
<li>その仮定のもとで矛盾（確率的に起こりにくいこと）を導く</li>
<li>仮説を棄却して、対立する仮説を採択する</li>
</ul>

<span class="important">注意:</span> 背理法と違い、「完全な矛盾」ではなく「確率的に起こりにくい」という判断''',
        'source': '統計WEB 23-1, 総務省統計局'
    },

    # カード2: 帰無仮説と対立仮説
    {
        'question': '''<b>帰無仮説と対立仮説</b>

帰無仮説（\\(H_0\\)）と対立仮説（\\(H_1\\)）の定義と特徴は？''',
        'answer': '''<b>帰無仮説（\\(H_0\\)）:</b>
<ul>
<li>「差がない」「効果がない」という仮説</li>
<li>検定で<b>棄却したい</b>仮説</li>
<li>「無に帰したい仮説」が語源</li>
<li>例: \\(H_0: \\mu = 100\\)（母平均は100である）</li>
</ul>

<b>対立仮説（\\(H_1\\)）:</b>
<ul>
<li>「差がある」「効果がある」という仮説</li>
<li>本来<b>証明したい</b>仮説</li>
<li>帰無仮説が棄却されたとき採択される</li>
<li>例: \\(H_1: \\mu \\neq 100\\)（母平均は100ではない）</li>
</ul>

<div class="mnemonic">
<b>覚え方:</b>
<ul>
<li>帰無仮説 → 「無」に「帰」したい → 棄却したい仮説</li>
<li>対立仮説 → 本当に示したい仮説</li>
</ul>
</div>''',
        'source': '統計WEB 23-2'
    },

    # カード3: 有意水準
    {
        'question': '''<b>有意水準（\\(\\alpha\\)）とは</b>

有意水準の定義と一般的に使われる値は？''',
        'answer': '''<b>定義:</b>
帰無仮説を棄却するかどうかの基準となる確率

<div class="formula">
有意水準 \\(\\alpha\\) = 第1種の過誤を犯す確率の上限
</div>

<b>一般的な値:</b>
<ul>
<li><b>5%（0.05）</b> — 最もよく使われる</li>
<li><b>1%（0.01）</b> — より厳しい基準</li>
<li>10%（0.10）— 緩い基準（探索的研究など）</li>
</ul>

<b>意味:</b>
<ul>
<li>有意水準5% → P値が5%未満なら帰無仮説を棄却</li>
<li>「本当は帰無仮説が正しいのに、誤って棄却してしまう確率」を5%以下に抑える</li>
</ul>

<span class="important">重要:</span> 有意水準は検定を行う<b>前に</b>決めておく必要がある''',
        'source': '統計WEB 23-3'
    },

    # カード4: P値
    {
        'question': '''<b>P値（有意確率）とは</b>

P値の定義と解釈の仕方は？''',
        'answer': '''<b>定義:</b>
帰無仮説が正しいと仮定したとき、観測されたデータ以上に極端な結果が得られる確率

<div class="formula">
P値 = \\(P(\\text{観測値以上に極端な値} | H_0 \\text{が真})\\)
</div>

<b>解釈:</b>
<ul>
<li>P値が<b>小さい</b> → 帰無仮説のもとでは起こりにくいことが起きた → 帰無仮説は怪しい</li>
<li>P値が<b>大きい</b> → 帰無仮説のもとでも十分起こりうる → 帰無仮説を棄却できない</li>
</ul>

<b>判定基準:</b>
<ul>
<li>P値 &lt; 有意水準 → <b>帰無仮説を棄却</b></li>
<li>P値 ≥ 有意水準 → <b>帰無仮説を棄却しない</b></li>
</ul>

<span class="important">注意:</span> P値は「帰無仮説が正しい確率」ではない！''',
        'source': '統計WEB 23-2'
    },

    # カード5: 第1種の過誤
    {
        'question': '''<b>第1種の過誤（Type I Error）</b>

第1種の過誤（αエラー）とは何か？別名と具体例は？''',
        'answer': '''<b>定義:</b>
<div class="formula">
帰無仮説が<b>正しい</b>のに、誤って<b>棄却</b>してしまう誤り
</div>

<b>別名:</b>
<ul>
<li>αエラー（アルファエラー）</li>
<li>偽陽性（False Positive）</li>
<li><b>「あわてものの誤り」</b></li>
</ul>

<b>確率:</b>
\\[P(\\text{第1種の過誤}) = \\alpha = \\text{有意水準}\\]

<b>具体例（裁判に例えると）:</b>
<div class="example">
<b>無実の人を有罪にしてしまう</b>（冤罪）

帰無仮説: 被告は無罪である
→ 実際は無罪なのに、有罪と判断してしまう
</div>

<div class="mnemonic">
<b>覚え方:</b> 「あわてて」棄却 → あわてものの誤り
</div>''',
        'source': '統計WEB 23-4'
    },

    # カード6: 第2種の過誤
    {
        'question': '''<b>第2種の過誤（Type II Error）</b>

第2種の過誤（βエラー）とは何か？別名と具体例は？''',
        'answer': '''<b>定義:</b>
<div class="formula">
帰無仮説が<b>誤り</b>なのに、<b>棄却しない</b>（見逃す）誤り
</div>

<b>別名:</b>
<ul>
<li>βエラー（ベータエラー）</li>
<li>偽陰性（False Negative）</li>
<li><b>「ぼんやりものの誤り」</b></li>
</ul>

<b>確率:</b>
\\[P(\\text{第2種の過誤}) = \\beta\\]

<b>具体例（裁判に例えると）:</b>
<div class="example">
<b>真犯人を無罪にしてしまう</b>（取り逃がし）

帰無仮説: 被告は無罪である
→ 実際は有罪なのに、無罪と判断してしまう
</div>

<div class="mnemonic">
<b>覚え方:</b> 「ぼんやり」して見逃す → ぼんやりものの誤り
</div>''',
        'source': '統計WEB 23-4'
    },

    # カード7: 過誤のまとめ表
    {
        'question': '''<b>第1種・第2種の過誤のまとめ</b>

検定の結果と真実の関係を表にまとめよ。''',
        'answer': '''<table>
<tr>
<th></th>
<th>\\(H_0\\)が真<br>（差がない）</th>
<th>\\(H_1\\)が真<br>（差がある）</th>
</tr>
<tr>
<th>\\(H_0\\)を棄却<br>（差ありと判断）</th>
<td><span class="important">第1種の過誤</span><br>確率 = \\(\\alpha\\)</td>
<td>正しい判断<br>確率 = \\(1-\\beta\\)<br>（検出力）</td>
</tr>
<tr>
<th>\\(H_0\\)を棄却しない<br>（差なしと判断）</th>
<td>正しい判断<br>確率 = \\(1-\\alpha\\)</td>
<td><span class="important">第2種の過誤</span><br>確率 = \\(\\beta\\)</td>
</tr>
</table>

<b>トレードオフ関係:</b>
<ul>
<li>\\(\\alpha\\) を小さくすると → \\(\\beta\\) が大きくなる</li>
<li>両方を同時に小さくすることはできない</li>
<li>サンプルサイズを増やせば両方を小さくできる</li>
</ul>''',
        'source': '統計WEB 23-4'
    },

    # カード8: 検出力
    {
        'question': '''<b>検出力（Power）とは</b>

検出力の定義と、検出力を高める方法は？''',
        'answer': '''<b>定義:</b>
<div class="formula">
検出力 = \\(1 - \\beta\\)

= 対立仮説が真のとき、正しく帰無仮説を棄却できる確率
</div>

<b>意味:</b>
<ul>
<li>「本当に差があるとき、それを検出できる能力」</li>
<li>検出力が高い → 見逃しが少ない</li>
<li>一般的に80%（0.8）以上が望ましい</li>
</ul>

<b>検出力を高める方法:</b>
<ol>
<li><b>サンプルサイズを大きくする</b>（最も効果的）</li>
<li>有意水準を大きくする（ただしαエラー増加）</li>
<li>効果量が大きい（差が大きい）</li>
<li>ばらつきが小さい</li>
</ol>

<span class="important">実務での手順:</span> 有意水準αを先に決め、その範囲内で検出力が最大になる検定方法を選ぶ''',
        'source': '統計WEB 23-3, 23-4'
    },

    # カード9: 検定統計量
    {
        'question': '''<b>検定統計量とは</b>

検定統計量の定義と代表的な種類は？''',
        'answer': '''<b>定義:</b>
標本データを「検定するための値」に変換した統計量

<b>代表的な検定統計量:</b>

<b>1. z値（z統計量）:</b>
<div class="formula">
\\[z = \\frac{\\bar{x} - \\mu_0}{\\sqrt{\\sigma^2/n}}\\]
母分散既知の場合。標準正規分布 \\(N(0,1)\\) に従う。
</div>

<b>2. t値（t統計量）:</b>
<div class="formula">
\\[t = \\frac{\\bar{x} - \\mu_0}{\\sqrt{s^2/n}}\\]
母分散未知の場合。自由度 \\(n-1\\) のt分布に従う。
</div>

<b>3. カイ二乗値（\\(\\chi^2\\)統計量）:</b>
母分散の検定や適合度検定で使用

<span class="important">ポイント:</span> 検定統計量が棄却域に入れば帰無仮説を棄却''',
        'source': '統計WEB 23-5'
    },

    # カード10: 棄却域と採択域
    {
        'question': '''<b>棄却域と採択域</b>

棄却域と採択域の定義は？有意水準との関係は？''',
        'answer': '''<b>棄却域（Rejection Region）:</b>
<ul>
<li>検定統計量がこの領域に入ると、帰無仮説を<b>棄却</b>する</li>
<li>分布の端（裾）に位置する</li>
<li>面積 = 有意水準 \\(\\alpha\\)</li>
</ul>

<b>採択域（Acceptance Region）:</b>
<ul>
<li>検定統計量がこの領域に入ると、帰無仮説を<b>棄却しない</b></li>
<li>分布の中央に位置する</li>
<li>面積 = \\(1 - \\alpha\\)</li>
</ul>

<b>臨界値（Critical Value）:</b>
棄却域と採択域の境界となる値

<div class="example">
<b>例: 有意水準5%の両側検定（正規分布）</b>
<ul>
<li>臨界値: \\(\\pm 1.96\\)</li>
<li>棄却域: \\(z < -1.96\\) または \\(z > 1.96\\)</li>
<li>採択域: \\(-1.96 \\leq z \\leq 1.96\\)</li>
</ul>
</div>''',
        'source': '統計WEB 23-5'
    },

    # カード11: 両側検定と片側検定
    {
        'question': '''<b>両側検定と片側検定の違い</b>

両側検定と片側検定の違いと使い分けは？''',
        'answer': '''<b>両側検定:</b>
<ul>
<li>対立仮説: \\(H_1: \\mu \\neq \\mu_0\\)（異なるかどうか）</li>
<li>棄却域: 分布の<b>両端</b>に配置</li>
<li>有意水準5%なら、両端に2.5%ずつ</li>
</ul>

<b>片側検定:</b>
<ul>
<li>対立仮説: \\(H_1: \\mu > \\mu_0\\) または \\(H_1: \\mu < \\mu_0\\)</li>
<li>棄却域: 分布の<b>片側</b>のみに配置</li>
<li>有意水準5%なら、片側に5%</li>
</ul>

<b>使い分け:</b>
<table>
<tr><th>状況</th><th>検定</th></tr>
<tr><td>大きいか小さいか、どちらも知りたい</td><td>両側検定</td></tr>
<tr><td>一方向の違いのみに興味がある</td><td>片側検定</td></tr>
<tr><td>迷ったとき</td><td>両側検定（保守的）</td></tr>
</table>

<span class="important">注意:</span> 検定方法は<b>事前に</b>決める。結果を見てから変更は不可！''',
        'source': '統計WEB 23-6'
    },

    # カード12: 検定の結論の述べ方
    {
        'question': '''<b>検定の結論の述べ方</b>

帰無仮説が「棄却された場合」と「棄却されなかった場合」、それぞれどのように結論を述べるべきか？''',
        'answer': '''<b>帰無仮説が棄却された場合:</b>
<div class="example">
「有意水準5%で、帰無仮説は<b>棄却される</b>」
「母平均は100と<b>有意に異なる</b>」
「<b>統計的に有意な差がある</b>」
</div>

<b>帰無仮説が棄却されなかった場合:</b>
<div class="example">
「有意水準5%で、帰無仮説は<b>棄却されない</b>」
「母平均が100であるとは<b>否定できない</b>」
「<b>有意な差は認められなかった</b>」
</div>

<span class="important">絶対に言ってはいけないこと:</span>
<ul>
<li>× 「帰無仮説が<b>正しい</b>ことが証明された」</li>
<li>× 「差が<b>ない</b>ことが示された」</li>
<li>× 「帰無仮説を<b>採択</b>する」（避けるべき表現）</li>
</ul>

<b>理由:</b> 棄却されない = 「差がないとは言えない」であり、「差がない」の証明ではない''',
        'source': '統計WEB 23-2'
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
output_file = '検定の前に_verified.apkg'
genanki.Package(deck).write_to_file(output_file)

print(f"✅ Ankiパッケージを作成しました: {output_file}")
print(f"📊 カード枚数: {len(cards_data)}枚")
print("\n作成されたカード:")
for i, card in enumerate(cards_data, 1):
    title = card['question'].split('\n')[0].replace('<b>', '').replace('</b>', '')
    print(f"  {i}. {title}")
