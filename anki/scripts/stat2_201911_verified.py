#!/usr/bin/env python3
"""
統計検定2級 2019年11月 - Ankiカード
トピック:
1. 幾何平均（平均変化率）
2. 指数法則（分数指数・負の指数）
3. コレログラム

作成日: 2026-01-27
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
    '統計検定2級_2019年11月',
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
    '統計検定2級::2019年11月'
)

# =============================================================================
# Card 1: 幾何平均（平均変化率）の公式
# =============================================================================
card1_q = '''
<b>平均変化率（幾何平均）</b><br><br>
時点0の値 \\(x_0\\) から時点 \\(n\\) の値 \\(x_n\\) まで、<br>
<span class="important">一定の変化率 \\(r\\)</span> で変化したとき、<br><br>
平均変化率 \\(r\\) を求める公式は？
'''

card1_a = '''
<div class="formula">
\\[ r = \\left( \\frac{x_n}{x_0} \\right)^{\\frac{1}{n}} - 1 \\]
</div>

<b>導出:</b><br>
\\( x_0 \\times (1+r)^n = x_n \\) を \\(r\\) について解く

<div class="example">
<b>例:</b> 1月の指数102.6 → 4月の指数105.6（3ヶ月間）<br>
\\[ r = \\left( \\frac{105.6}{102.6} \\right)^{\\frac{1}{3}} - 1 \\approx 0.0096 \\]
パーセント表示: \\( r \\times 100 \\approx 0.96\\% \\)
</div>

<div class="mnemonic">
<b>注意:</b> 期間数 = 終点 - 始点（1月→4月は<b>3</b>回の変化）
</div>

<div class="source">出典: 統計検定2級 2019年11月 問3[7] / 統計WEB</div>
'''

# =============================================================================
# Card 2: 指数法則 - 負の指数
# =============================================================================
card2_q = '''
<b>指数法則：負の指数</b><br><br>
\\( a \\neq 0 \\) のとき、<br><br>
\\( a^{-n} \\) はどのように表せるか？
'''

card2_a = '''
<div class="formula">
\\[ a^{-n} = \\frac{1}{a^n} \\]
</div>

<b>意味:</b> マイナス乗は「逆数」を表す

<div class="example">
<b>例:</b><br>
• \\( 2^{-3} = \\frac{1}{2^3} = \\frac{1}{8} \\)<br>
• \\( 10^{-2} = \\frac{1}{100} = 0.01 \\)<br>
• \\( x^{-1} = \\frac{1}{x} \\)
</div>

<div class="source">出典: 高校数学II 指数関数</div>
'''

# =============================================================================
# Card 3: 指数法則 - 分数指数
# =============================================================================
card3_q = '''
<b>指数法則：分数指数</b><br><br>
\\( a > 0 \\) のとき、<br><br>
\\( a^{\\frac{m}{n}} \\) はどのように表せるか？
'''

card3_a = '''
<div class="formula">
\\[ a^{\\frac{m}{n}} = \\sqrt[n]{a^m} = \\left( \\sqrt[n]{a} \\right)^m \\]
</div>

<b>特に:</b>
<div class="formula">
\\[ a^{\\frac{1}{n}} = \\sqrt[n]{a} \\]
（n乗根）
</div>

<div class="example">
<b>例:</b><br>
• \\( 8^{\\frac{1}{3}} = \\sqrt[3]{8} = 2 \\)<br>
• \\( 16^{\\frac{3}{4}} = \\sqrt[4]{16^3} = (\\sqrt[4]{16})^3 = 2^3 = 8 \\)<br>
• \\( 27^{\\frac{2}{3}} = \\sqrt[3]{27^2} = 3^2 = 9 \\)
</div>

<div class="mnemonic">
<b>覚え方:</b> 分母がルートの次数、分子が累乗
</div>

<div class="source">出典: 高校数学II 指数関数</div>
'''

# =============================================================================
# Card 4: コレログラムの定義
# =============================================================================
card4_q = '''
<b>コレログラム（Correlogram）とは？</b><br><br>
時系列分析で使われるグラフの一種。<br>
何を表すグラフか？
'''

card4_a = '''
<div class="formula">
<b>コレログラム</b> = 自己相関関数（ACF）のグラフ
</div>

<b>軸の意味:</b>
<table>
<tr><th>軸</th><th>内容</th></tr>
<tr><td>横軸</td><td>ラグ（時間のずれ）</td></tr>
<tr><td>縦軸</td><td>自己相関係数（-1〜1）</td></tr>
</table>

<br>
<b>自己相関係数:</b><br>
元のデータと、時間をずらしたデータとの相関

<div class="example">
<b>用途:</b><br>
• データの周期性（季節変動など）を検出<br>
• 時系列モデルの選択
</div>

<div class="source">出典: 統計検定2級 2019年11月 問5[9] / 統計WEB</div>
'''

# =============================================================================
# Card 5: コレログラムの読み方（季節性）
# =============================================================================
card5_q = '''
<b>コレログラムの読み方：季節性の検出</b><br><br>
月次データで <span class="important">12ヶ月周期の季節性</span> がある場合、<br>
コレログラムにはどのような特徴が現れるか？
'''

card5_a = '''
<div class="formula">
<b>ラグ12, 24, 36... で正の強いピーク</b>が現れる
</div>

<b>理由:</b><br>
1年前（12ヶ月前）のデータと強い正の相関があるため

<div class="example">
<b>パターン別の特徴:</b>
<table>
<tr><th>データの性質</th><th>コレログラムの特徴</th></tr>
<tr><td>12ヶ月周期</td><td>ラグ12, 24で正のピーク</td></tr>
<tr><td>6ヶ月周期</td><td>ラグ6, 12, 18で正のピーク</td></tr>
<tr><td>トレンドのみ</td><td>徐々に減衰</td></tr>
<tr><td>ランダム（無相関）</td><td>すべて点線内</td></tr>
</table>
</div>

<div class="mnemonic">
<b>点線:</b> 5%有意水準の棄却限界値<br>
→ 点線を超えれば有意な自己相関あり
</div>

<div class="source">出典: 統計検定2級 2019年11月 問5[9] / 統計WEB / data-viz-lab.com</div>
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
output_file = '/Users/sasaki/stat2_201911_verified.apkg'
genanki.Package(deck).write_to_file(output_file)
print(f"✅ Generated: {output_file}")
print(f"📚 Cards created: {len(cards)}")
