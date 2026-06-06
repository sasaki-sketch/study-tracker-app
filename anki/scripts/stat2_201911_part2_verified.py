#!/usr/bin/env python3
"""
統計検定2級 2019年11月 Part2 - Ankiカード
トピック:
1. ベイズの定理・クロス表
2. 連続型確率分布・積分
3. 歪度
4. 不偏推定量・一致推定量

作成日: 2026-01-28
検証済み: WebSearch + 複数ソース確認
"""

import genanki
import random
import sys
sys.path.append('/Users/sasaki')
from anki_card_css_template import CARD_CSS

# Generate unique IDs
MODEL_ID = random.randrange(1 << 30, 1 << 31)
DECK_ID = random.randrange(1 << 30, 1 << 31)

# Model definition
model = genanki.Model(
    MODEL_ID,
    '統計検定2級_2019年11月_Part2',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
        },
    ],
    css=CARD_CSS
)

# Deck definition
deck = genanki.Deck(
    DECK_ID,
    '統計検定2級::2019年11月_Part2'
)

# =============================================================================
# Card 1: ベイズの定理 - クロス表アプローチ
# =============================================================================
card1_q = '''
<b>ベイズの定理：クロス表で解く</b><br><br>
条件付き確率の問題を<span class="important">クロス表</span>で解く手順は？<br><br>
<b>例題：</b><br>
・対策講座受講者の合格率 70%<br>
・非受講者の合格率 30%<br>
・受講率 20%<br><br>
「合格者が受講者である確率」を求めよ
'''

card1_a = '''
<b>Step 1: 100人と仮定してクロス表を作成</b>

<table>
<tr><th></th><th>受講</th><th>非受講</th><th>合計</th></tr>
<tr><td><b>合格</b></td><td>100×0.2×0.7=<b>14</b></td><td>100×0.8×0.3=<b>24</b></td><td><b>38</b></td></tr>
<tr><td><b>不合格</b></td><td>6</td><td>56</td><td>62</td></tr>
<tr><td><b>合計</b></td><td>20</td><td>80</td><td>100</td></tr>
</table>

<br>
<b>Step 2: 表から読み取る</b>
<div class="formula">
\\( P(\\text{受講}|\\text{合格}) = \\frac{14}{38} \\approx 0.368 \\)
</div>

<div class="mnemonic">
<b>ポイント：</b>「100人仮定」で計算が楽になる！
</div>

<div class="source">出典: 統計検定2級 2019年11月 問8 / 統計WEB</div>
'''

# =============================================================================
# Card 2: ベイズの定理 - 公式
# =============================================================================
card2_q = '''
<b>ベイズの定理</b><br><br>
\\( P(A|B) \\) を \\( P(B|A) \\) を使って表す公式は？
'''

card2_a = '''
<div class="formula">
\\[ P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)} \\]
</div>

<b>分母 P(B) の展開（全確率の公式）：</b>
<div class="formula">
\\[ P(B) = P(B|A) \\cdot P(A) + P(B|A^c) \\cdot P(A^c) \\]
</div>

<div class="example">
<b>覚え方：</b><br>
・分子：「AかつB」の確率<br>
・分母：「Bが起こる全ての場合」の確率
</div>

<div class="mnemonic">
<b>用途：</b>「原因→結果」の確率から「結果→原因」の確率を求める
</div>

<div class="source">出典: 統計WEB / 統計検定2級</div>
'''

# =============================================================================
# Card 3: 連続型確率分布 - PDFの条件
# =============================================================================
card3_q = '''
<b>確率密度関数（PDF）の条件</b><br><br>
連続型確率変数の確率密度関数 \\( f(x) \\) が満たすべき条件は？
'''

card3_a = '''
<div class="formula">
<b>条件1：非負性</b><br>
\\[ f(x) \\geq 0 \\quad (\\text{すべての } x) \\]
</div>

<div class="formula">
<b>条件2：全確率 = 1</b><br>
\\[ \\int_{-\\infty}^{\\infty} f(x) \\, dx = 1 \\]
</div>

<div class="example">
<b>定数 a を求める問題の解き方：</b><br>
\\( \\int f(x) dx = 1 \\) を解いて a を求める
</div>

<div class="source">出典: 統計検定2級 2019年11月 問9 / 統計WEB</div>
'''

# =============================================================================
# Card 4: 連続型確率分布 - 期待値の積分公式
# =============================================================================
card4_q = '''
<b>連続型確率変数の期待値</b><br><br>
確率密度関数 \\( f(x) \\) を持つ連続型確率変数 \\( X \\) の期待値 \\( E[X] \\) は？
'''

card4_a = '''
<div class="formula">
\\[ E[X] = \\int_{-\\infty}^{\\infty} x \\cdot f(x) \\, dx \\]
</div>

<b>よく使う積分公式：</b>
<table>
<tr><th>積分</th><th>結果</th></tr>
<tr><td>\\( \\int x \\, dx \\)</td><td>\\( \\frac{x^2}{2} \\)</td></tr>
<tr><td>\\( \\int x^2 \\, dx \\)</td><td>\\( \\frac{x^3}{3} \\)</td></tr>
<tr><td>\\( \\int x^n \\, dx \\)</td><td>\\( \\frac{x^{n+1}}{n+1} \\)</td></tr>
</table>

<div class="example">
<b>定積分の計算：</b><br>
\\( \\int_a^b f(x) dx = [F(x)]_a^b = F(b) - F(a) \\)
</div>

<div class="source">出典: 統計検定2級 2019年11月 問9 / 高校数学II</div>
'''

# =============================================================================
# Card 5: 歪度（Skewness）
# =============================================================================
card5_q = '''
<b>歪度（Skewness）</b><br><br>
分布の歪度が<span class="important">正</span>になるのはどんな分布？
'''

card5_a = '''
<div class="formula">
<b>右に裾が長い分布</b> → 歪度は<span class="important">正</span>
</div>

<div class="formula">
<b>左に裾が長い分布</b> → 歪度は<span class="important">負</span>
</div>

<div class="mnemonic">
<b>覚え方：「うっせいわい」</b><br>
<b>右</b>（う）→ <b>正</b>（せい）→ <b>歪</b>（わい）<br><br>
右に裾が長い = 正の歪度
</div>

<div class="example">
<b>注意：</b><br>
・平均の符号と歪度は<b>無関係</b><br>
・多峰（峰が2個以上）と歪度は<b>無関係</b>
</div>

<div class="source">出典: 統計検定2級 2019年11月 問11 / 統計WEB</div>
'''

# =============================================================================
# Card 6: 不偏推定量
# =============================================================================
card6_q = '''
<b>不偏推定量（Unbiased Estimator）</b><br><br>
推定量 \\( \\hat{\\theta} \\) が母数 \\( \\theta \\) の<span class="important">不偏推定量</span>であるとは？
'''

card6_a = '''
<div class="formula">
\\[ E[\\hat{\\theta}] = \\theta \\]
<br>
推定量の<b>期待値</b>が真の母数に等しい
</div>

<div class="example">
<b>具体例：</b>
<table>
<tr><th>推定量</th><th>不偏？</th></tr>
<tr><td>標本平均 \\( \\bar{X} \\)</td><td>✅ \\( E[\\bar{X}] = \\mu \\)</td></tr>
<tr><td>標本分散 \\( S_n^2 = \\frac{1}{n}\\sum(X_i-\\bar{X})^2 \\)</td><td>❌</td></tr>
<tr><td>不偏分散 \\( S^2 = \\frac{1}{n-1}\\sum(X_i-\\bar{X})^2 \\)</td><td>✅</td></tr>
</table>
</div>

<div class="mnemonic">
<b>イメージ：</b>「平均的に当たる」（偏りがない）
</div>

<div class="source">出典: 統計検定2級 2019年11月 問12 / 統計WEB</div>
'''

# =============================================================================
# Card 7: 一致推定量
# =============================================================================
card7_q = '''
<b>一致推定量（Consistent Estimator）</b><br><br>
推定量 \\( \\hat{\\theta} \\) が母数 \\( \\theta \\) の<span class="important">一致推定量</span>であるとは？<br><br>
また、一致推定量かどうかの<b>判定法</b>は？
'''

card7_a = '''
<div class="formula">
\\[ n \\to \\infty \\text{ のとき } \\hat{\\theta} \\to \\theta \\]
<br>
サンプルサイズが大きくなると真の値に<b>収束</b>する
</div>

<b>判定法：分散が 0 に収束するか？</b>
<div class="formula">
\\[ \\lim_{n \\to \\infty} Var(\\hat{\\theta}) = 0 \\text{ なら一致推定量} \\]
</div>

<div class="example">
<b>例：</b>
<table>
<tr><th>推定量</th><th>分散</th><th>n→∞</th><th>一致？</th></tr>
<tr><td>\\( \\bar{X} = \\frac{1}{n}\\sum X_i \\)</td><td>\\( \\frac{\\sigma^2}{n} \\)</td><td>→ 0</td><td>✅</td></tr>
<tr><td>\\( \\frac{1}{2}(X_1 + X_n) \\)</td><td>\\( \\frac{\\sigma^2}{2} \\)</td><td>→ \\( \\frac{\\sigma^2}{2} \\)</td><td>❌</td></tr>
</table>
</div>

<div class="mnemonic">
<b>イメージ：</b>「データ増やせば当たる」
</div>

<div class="source">出典: 統計検定2級 2019年11月 問12 / 統計WEB</div>
'''

# =============================================================================
# Add cards to deck
# =============================================================================
cards = [
    (card1_q, card1_a),
    (card2_q, card2_a),
    (card3_q, card3_a),
    (card4_q, card4_a),
    (card5_q, card5_a),
    (card6_q, card6_a),
    (card7_q, card7_a),
]

for q, a in cards:
    note = genanki.Note(
        model=model,
        fields=[q, a]
    )
    deck.add_note(note)

# =============================================================================
# Generate .apkg file
# =============================================================================
output_file = '/Users/sasaki/stat2_201911_part2_verified.apkg'
genanki.Package(deck).write_to_file(output_file)
print(f"✅ Generated: {output_file}")
print(f"📚 Cards created: {len(cards)}")
