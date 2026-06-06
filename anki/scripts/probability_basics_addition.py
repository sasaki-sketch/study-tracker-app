#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級 Ankiカード: 確率の基礎・正規分布（追加）
弱点補強: 条件付き確率、ベイズの定理、正規分布、68-95-99.7ルール
作成日: 2026-01-16
出典: 統計WEB「統計学の時間」
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
            font-family: "Hiragino Kaku Gothic ProN", "ヒラギノ角ゴ ProN", arial;
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
    '統計検定2級::確率の基礎と正規分布（追加）'
)

# ========================================
# カード1: 正規分布の定義と標準化
# ========================================
card1 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【正規分布】正規分布N(μ, σ²)の定義、公式、標準化は？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
左右対称の釣鐘型の連続型確率分布<br>
記号: \\(X \\sim N(\\mu, \\sigma^2)\\)<br>
<br>

<b>確率密度関数:</b><br>
\\[f(x) = \\frac{1}{\\sqrt{2\\pi}\\sigma} \\exp\\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right)\\]
<br>

<b>期待値と分散:</b><br>
\\[E(X) = \\mu\\]
\\[V(X) = \\sigma^2\\]
<br>

<b>標準化:</b><br>
異なるパラメータの正規分布を比較するため、<br>
標準正規分布N(0,1)に変換する<br>
\\[Z = \\frac{X - \\mu}{\\sigma}\\]
\\[Z \\sim N(0, 1)\\]
<br>

<hr>

<b>具体例:</b><br>
<b>テストの点数: 平均60点、標準偏差10点</b><br>
\\(X \\sim N(60, 10^2)\\)<br>
<br>

<b>80点の標準化:</b><br>
\\[Z = \\frac{80-60}{10} = 2.0\\]
→ 平均より標準偏差2つ分高い<br>
<br>

<hr>

<b>【重要ポイント・使いどころ】</b><br>
・身長、体重、テストの点など連続値<br>
・左右対称、中央が最も高い<br>
・μが中心、σが広がり具合<br>
・標準化で異なる分布を比較可能<br>
・統計検定2級で最頻出の分布<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計WEB「14-1. 正規分布」<br>
https://bellcurve.jp/statistics/course/7797.html
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'normal-distribution', 'weakness']
)
deck.add_note(card1)

# ========================================
# カード2: 68-95-99.7ルール（経験則）
# ========================================
card2 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【正規分布の経験則】68-95-99.7ルールとは？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>68-95-99.7ルール（3σルール）:</b><br>
正規分布において、データがどの範囲に収まるかを示す経験則<br>
<br>

<table border="1" cellpadding="10" style="border-collapse:collapse; width:100%; font-size:20px;">
<tr style="background-color:#f0f0f0;">
<th>範囲</th>
<th>カバー率</th>
<th>補足</th>
</tr>
<tr>
<td><b>μ ± 1σ</b></td>
<td><b>約68%</b></td>
<td>データの約7割</td>
</tr>
<tr style="background-color:#fff3cd;">
<td><b>μ ± 2σ</b></td>
<td><b>約95%</b></td>
<td>データのほぼ全体</td>
</tr>
<tr>
<td><b>μ ± 3σ</b></td>
<td><b>約99.7%</b></td>
<td>ほぼすべてのデータ</td>
</tr>
</table>
<br>

<hr>

<b>具体例:</b><br>
<b>日本人成人男性の身長: μ=170cm, σ=6cm</b><br>
<br>

<b>■ μ±1σ（164～176cm）:</b><br>
約68%の人がこの範囲<br>
<br>

<b>■ μ±2σ（158～182cm）:</b><br>
約95%の人がこの範囲 ← <b>重要！</b><br>
<br>

<b>■ μ±3σ（152～188cm）:</b><br>
約99.7%の人がこの範囲<br>
<br>

<b>逆に言うと:</b><br>
・182cm以上は上位2.5%<br>
・158cm以下は下位2.5%<br>
<br>

<hr>

<b>【超重要ポイント】</b><br>
・<b>暗記必須：68, 95, 99.7</b><br>
・μ±2σで約95% ← 試験で最頻出<br>
・この数字がないと問題が解けない<br>
・標準正規分布表と組み合わせて使用<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計学の経験則（68-95-99.7ルール）<br>
Wikipedia「68–95–99.7則」、統計WEB
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'normal-distribution', 'empirical-rule', 'weakness', 'must-memorize']
)
deck.add_note(card2)

# ========================================
# カード3: 条件付き確率
# ========================================
card3 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【条件付き確率】P(A|B)の定義と公式は？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
事象Bが起こったという条件のもとで、<br>
事象Aが起こる確率<br>
読み方: 「B given A」または「BのもとでA」<br>
<br>

<b>公式:</b><br>
\\[P(A|B) = \\frac{P(A \\cap B)}{P(B)}\\]
<br>

ここで:<br>
・P(A∩B): AとBが同時に起こる確率<br>
・P(B): 条件となる事象Bの確率<br>
<br>

<hr>

<b>具体例1: サイコロ2回</b><br>
2回投げて、1回目が4だった。<br>
この条件で、目の和が8以上になる確率は？<br>
<br>

<b>解:</b><br>
・1回目=4の場合: 2回目は1,2,3,4,5,6<br>
・和が8以上: 4+4=8, 4+5=9, 4+6=10 (3通り)<br>
・P(和≧8|1回目=4) = 3/6 = <b>1/2</b><br>
<br>

<b>具体例2: 玉の色と数字</b><br>
袋に赤玉3個（「1」が2個、「2」が1個）と白玉3個<br>
赤玉が引かれたという条件で「1」の確率は？<br>
<br>

<b>解:</b><br>
・赤玉3個のうち「1」は2個<br>
・P(「1」|赤) = 2/3<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
・「〇〇という条件のもとで」がキーワード<br>
・分母はP(B)（条件側）<br>
・分子はP(A∩B)（両方起こる確率）<br>
・統計検定2級でほぼ毎回出題<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計WEB「10-1. 条件付き確率とは」<br>
https://bellcurve.jp/statistics/course/6438.html
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'conditional-probability', 'weakness']
)
deck.add_note(card3)

# ========================================
# カード4: ベイズの定理
# ========================================
card4 = genanki.Note(
    model=model,
    fields=[
        # Front
        '''
<div style="font-size:24px; padding:20px;">
    <b>【ベイズの定理】定義と公式は？</b>
</div>
''',
        # Back
        '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
観察された結果（事象A）から、<br>
原因（事象Bᵢ）を推定する確率的手法<br>
「結果から原因を逆算する」<br>
<br>

<b>公式:</b><br>
互いに排反な事象B₁, B₂, ..., Bₖについて:<br>
\\[P(B_i|A) = \\frac{P(B_i) \\cdot P(A|B_i)}{\\sum_{j=1}^{k} P(B_j) \\cdot P(A|B_j)}\\]
<br>

<b>別の表現（2事象の場合）:</b><br>
\\[P(B|A) = \\frac{P(A|B) \\cdot P(B)}{P(A)}\\]
<br>

<hr>

<b>具体例: 3つの袋問題</b><br>

<b>状況:</b><br>
・袋1: 赤玉2個、白玉1個<br>
・袋2: 赤玉1個、白玉2個<br>
・袋3: 赤玉1個、白玉1個<br>
無作為に袋を選び、白玉が出た。<br>
これが袋2から出た確率は？<br>
<br>

<b>解:</b><br>
P(袋2|白) = P(袋2)×P(白|袋2) / [全袋の確率和]<br>
= (1/3)×(2/3) / [(1/3)×(1/3)+(1/3)×(2/3)+(1/3)×(1/2)]<br>
= (2/9) / (11/18)<br>
= <b>4/11 ≈ 0.364</b><br>
<br>

<b>考え方:</b><br>
白玉が出たという「結果」から、<br>
「どの袋か」という「原因」を推定している<br>
<br>

<hr>

<b>【重要ポイント・使いどころ】</b><br>
・「結果→原因」の推定<br>
・医療検査（陽性→実際の病気の確率）<br>
・不良品の原因特定<br>
・「事後確率」を求める<br>
・統計検定2級でほぼ毎回出題<br>
・公式を覚えるより、考え方を理解<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b> 統計WEB「10-4. ベイズの定理」<br>
https://bellcurve.jp/statistics/course/6444.html<br>
とけたろうブログ「条件付き確率とベイズの定理」<br>
https://toketarou.com/bayes/
</div>

</div>
'''
    ],
    tags=['statistics', 'verified', 'bayes-theorem', 'weakness']
)
deck.add_note(card4)

# ========================================
# Ankiパッケージ出力
# ========================================
if __name__ == '__main__':
    package = genanki.Package(deck)
    output_file = 'probability_basics_addition.apkg'
    package.write_to_file(output_file)
    print(f"✅ 追加Ankiカード作成完了: {output_file}")
    print(f"📊 追加枚数: 4枚")
    print(f"📁 ファイル: /Users/sasaki/{output_file}")
    print()
    print("=" * 60)
    print("追加カード内容:")
    print("=" * 60)
    print("1. 正規分布の定義と標準化")
    print("2. 68-95-99.7ルール（経験則）← 超重要！")
    print("3. 条件付き確率 P(A|B)")
    print("4. ベイズの定理")
    print("=" * 60)
    print()
    print("⚠️  弱点補強カード:")
    print("過去問で解けなかった範囲をピンポイントでカバー")
    print()
    print("📚 合計Ankiカード数:")
    print("・基本カード: 7枚（確率変数、期待値、二項分布など）")
    print("・追加カード: 4枚（正規分布、条件付き確率など）")
    print("・合計: 11枚")
    print()
    print("🎯 次のステップ:")
    print("1. このスクリプトを実行してカードを生成")
    print("2. 68-95-99.7ルールを最優先で暗記")
    print("3. 過去問2問目に挑戦")
    print("4. また解けない問題があれば報告")
