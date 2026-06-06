#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分散と標準偏差（Variance and Standard Deviation） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「分散と標準偏差」https://bellcurve.jp/statistics/course/6439.html
- 統計WEB「標準偏差」https://bellcurve.jp/statistics/course/6444.html
- 統計WEB「なぜn-1で割るのか」https://bellcurve.jp/statistics/course/6448.html
"""

import json
import urllib.request


def invoke_anki(action, **params):
    """AnkiConnectにリクエストを送信"""
    request_json = json.dumps({
        'action': action,
        'version': 6,
        'params': params
    }).encode('utf-8')

    try:
        response = urllib.request.urlopen(
            urllib.request.Request('http://localhost:8765', request_json)
        )
        result = json.loads(response.read().decode('utf-8'))

        if result['error']:
            raise Exception(f"AnkiConnect error: {result['error']}")

        return result['result']
    except Exception as e:
        print(f"❌ エラー: {e}")
        return None


def create_variance_standard_deviation_cards(deck_name, model_name):
    """分散と標準偏差カードを作成（検証済み）"""

    cards = [
        # カード1: 分散の定義と3つの公式
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【分散の定義】<br>母分散・標本分散・不偏分散の<br>公式は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>分散とは:</b><br>
データの散らばり具合を表す指標<br>
平均からの偏差の2乗の平均<br>
<br>

<hr>

<b>【3種類の分散】</b><br>
<br>

<b>①母分散（Population Variance）: σ²</b><br>
\\[\\sigma^2 = \\frac{1}{N}\\sum_{i=1}^N (x_i - \\mu)^2\\]
<br>

• 母集団全体の分散<br>
• N = 母集団のサイズ<br>
• μ = 母平均<br>
• 母集団すべてのデータが分かる場合に使用<br>
<br>

<b>②標本分散（Sample Variance）: s²</b><br>
\\[s^2 = \\frac{1}{n}\\sum_{i=1}^n (x_i - \\bar{x})^2\\]
<br>

• 標本データの分散<br>
• n = 標本サイズ<br>
• x̄ = 標本平均<br>
• <b>⚠ 母分散を過小評価する（バイアスあり）</b><br>
<br>

<b>③不偏分散（Unbiased Variance）: s²または u²</b><br>
\\[s^2 = \\frac{1}{n-1}\\sum_{i=1}^n (x_i - \\bar{x})^2\\]
<br>

• <b>n-1で割る</b>（自由度補正）<br>
• 母分散の不偏推定量<br>
• <b>統計検定2級では基本的にこれを使用</b><br>
• 期待値E[s²] = σ²（不偏性）<br>
<br>

<hr>

<b>【計算用の展開公式】</b><br>
<br>

偏差の2乗和の計算が面倒な場合:<br>
\\[\\sigma^2 = \\frac{1}{N}\\sum_{i=1}^N x_i^2 - \\mu^2\\]
<br>

\\[s^2 = \\frac{1}{n-1}\\left(\\sum_{i=1}^n x_i^2 - n\\bar{x}^2\\right)\\]
<br>

「2乗の平均 - 平均の2乗」<br>
<br>

<hr>

<b>【分散の性質】</b><br>
<br>

• <b>単位: データの単位の2乗</b><br>
  例: データがcm → 分散はcm²<br>
<br>

• <b>値が大きい → 散らばりが大きい</b><br>
• <b>値が小さい → 散らばりが小さい</b><br>
• <b>最小値は0</b>（全データが同じ値の時）<br>
• <b>常に非負</b><br>
<br>

<hr>

<b>【Excel関数】</b><br>
<br>

• <b>VAR.P(範囲)</b>: 母分散（÷N）<br>
• <b>VAR.S(範囲)</b>: 不偏分散（÷n-1）<br>
• <b>VAR(範囲)</b>: VAR.Sと同じ（互換性のため残存）<br>
<br>

<b>統計分析では通常VAR.Sを使用</b><br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「分散と標準偏差」<br>
統計WEB「なぜn-1で割るのか」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'variance', 'definition', 'formula', 'unbiased']
        },

        # カード2: なぜn-1で割るのか（自由度の概念）
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【不偏分散】<br>なぜn-1で割るのか？<br>自由度の概念とは？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【結論】</b><br>
標本分散（÷n）は母分散を<b>過小評価</b>する<br>
→ n-1で割ることで<b>不偏推定量</b>になる<br>
<br>

<hr>

<b>【なぜ過小評価するのか】</b><br>
<br>

<b>理由1: 標本平均と標本データの関係</b><br>
• 標本平均x̄は標本データから計算される<br>
• 標本データは偶然x̄の近くに集まりやすい<br>
• → 標本内での偏差が母集団より小さくなる傾向<br>
<br>

<b>具体例:</b><br>
母集団: {1, 2, 3, 4, 5}（母平均μ=3, 母分散σ²=2）<br>
<br>

標本{1, 2}を取った場合:<br>
• 標本平均x̄ = 1.5<br>
• 標本分散(÷2) = 0.25<br>
• → 母分散2.0を大きく過小評価<br>
<br>

標本{1, 5}を取った場合:<br>
• 標本平均x̄ = 3<br>
• 標本分散(÷2) = 4<br>
• → 母分散2.0より大きい<br>
<br>

<b>多数の標本で平均すると:</b><br>
• E[標本分散(÷n)] = \\(\\frac{n-1}{n}\\sigma^2\\) < σ²<br>
• → 系統的に過小評価（バイアス）<br>
<br>

<hr>

<b>【自由度の概念】</b><br>
<br>

<b>自由度 = 独立に変動できるデータの個数</b><br>
<br>

<b>n個のデータで平均x̄が決まると:</b><br>
• n-1個のデータは自由に決められる<br>
• 最後の1個は自動的に決まる<br>
<br>

<b>具体例: n=3, x̄=10</b><br>
• x₁=8, x₂=12 と自由に決めると<br>
• x₃は必ず10になる（和=30にするため）<br>
• → 自由度 = 3-1 = 2<br>
<br>

<b>分散の計算では:</b><br>
• 平均を使って偏差を計算する<br>
• → 独立な情報は n-1個<br>
• → n-1で割るのが適切<br>
<br>

<hr>

<b>【不偏性の証明（概要）】</b><br>
<br>

不偏分散の期待値:<br>
\\[E\\left[\\frac{1}{n-1}\\sum(x_i - \\bar{x})^2\\right] = \\sigma^2\\]
<br>

一方、標本分散の期待値:<br>
\\[E\\left[\\frac{1}{n}\\sum(x_i - \\bar{x})^2\\right] = \\frac{n-1}{n}\\sigma^2 < \\sigma^2\\]
<br>

<b>→ n-1で割ることで不偏性を達成</b><br>
<br>

<hr>

<b>【実務上の使い分け】</b><br>
<br>

<b>n-1で割る（不偏分散）:</b><br>
• 標本から母集団の分散を推定する場合<br>
• 統計的検定・推定を行う場合<br>
• <b>統計検定2級では基本的にこちら</b><br>
• Excel: VAR.S, STDEV.S<br>
<br>

<b>nで割る（標本分散）:</b><br>
• 標本自体の散らばりを記述する場合のみ<br>
• 母集団全体のデータがある場合<br>
• Excel: VAR.P, STDEV.P<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
<br>

• 標本サイズnが大きい → n-1 ≈ n（差は小さい）<br>
• n=2の時: ÷1と÷2で2倍の差!<br>
• n=100の時: ÷99と÷100で約1%の差<br>
<br>

• <b>統計的推論では必ずn-1を使用</b><br>
• 記述統計でも不偏分散を使うのが一般的<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「なぜn-1で割るのか」<br>
統計WEB「不偏分散」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'variance', 'degrees-of-freedom', 'unbiased', 'n-1']
        },

        # カード3: 分散の計算例と解釈
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【分散の計算例】<br>具体的な計算方法と<br>結果の解釈は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【例題: 5人のテスト得点】</b><br>
<br>

<b>データ: 70, 75, 80, 85, 90点</b><br>
<br>

<hr>

<b>【計算手順】</b><br>
<br>

<b>ステップ1: 平均を計算</b><br>
\\[\\bar{x} = \\frac{70 + 75 + 80 + 85 + 90}{5} = \\frac{400}{5} = 80\\]
<br>
（単位：点）
<br>

<b>ステップ2: 各データの偏差を計算</b><br>
• x₁ - x̄ = 70 - 80 = -10<br>
• x₂ - x̄ = 75 - 80 = -5<br>
• x₃ - x̄ = 80 - 80 = 0<br>
• x₄ - x̄ = 85 - 80 = 5<br>
• x₅ - x̄ = 90 - 80 = 10<br>
<br>

<b>ステップ3: 偏差の2乗を計算</b><br>
• (-10)² = 100<br>
• (-5)² = 25<br>
• (0)² = 0<br>
• (5)² = 25<br>
• (10)² = 100<br>
<br>

<b>ステップ4: 偏差の2乗の和</b><br>
\\[\\sum(x_i - \\bar{x})^2 = 100 + 25 + 0 + 25 + 100 = 250\\]
<br>

<b>ステップ5: n-1で割る（不偏分散）</b><br>
\\[s^2 = \\frac{250}{5-1} = \\frac{250}{4} = 62.5\\]
<br>
（単位：点²）
<br>

<hr>

<b>【展開公式での計算】</b><br>
<br>

別の計算方法:<br>
\\[s^2 = \\frac{1}{n-1}\\left(\\sum_{i=1}^n x_i^2 - n\\bar{x}^2\\right)\\]
<br>

<b>ステップ1: データの2乗の和</b><br>
• 70² = 4900<br>
• 75² = 5625<br>
• 80² = 6400<br>
• 85² = 7225<br>
• 90² = 8100<br>
• 合計: 32250<br>
<br>

<b>ステップ2: 公式に代入</b><br>
\\[s^2 = \\frac{1}{4}\\left(32250 - 5 \\times 80^2\\right)\\]
\\[= \\frac{1}{4}\\left(32250 - 32000\\right)\\]
\\[= \\frac{250}{4} = 62.5\\]
<br>
（単位：点²）
<br>

→ 同じ結果! ✓<br>
<br>

<hr>

<b>【結果の解釈】</b><br>
<br>

<b>分散 = 62.5点²</b><br>
<br>

<b>意味:</b><br>
• 平均からの偏差の2乗の平均値<br>
• 値が大きい → データのばらつきが大きい<br>
• 値が小さい → データのばらつきが小さい<br>
<br>

<b>注意点:</b><br>
• <b>単位が「点²」で解釈しづらい</b><br>
• → 標準偏差（√62.5 ≈ 7.9点）の方が直感的<br>
<br>

<hr>

<b>【比較例】</b><br>
<br>

<b>データA: 70, 75, 80, 85, 90</b><br>
• 平均: 80点<br>
• 不偏分散: 62.5点²<br>
<br>

<b>データB: 78, 79, 80, 81, 82</b><br>
• 平均: 80点（同じ）<br>
• 偏差の2乗和: (-2)²+(-1)²+0²+1²+2² = 10<br>
• 不偏分散: 10÷4 = 2.5点²<br>
<br>

<b>解釈:</b><br>
• 平均は同じでも分散が異なる<br>
• データAの方がばらつきが大きい（62.5 > 2.5）<br>
• 分散はデータの散らばり具合を数値化<br>
<br>

<hr>

<b>【Excelでの計算】</b><br>
<br>

A1:A5にデータ{70, 75, 80, 85, 90}を入力<br>
<br>

<b>=VAR.S(A1:A5)</b> → 62.5<br>
<br>

<b>確認:</b><br>
• =AVERAGE(A1:A5) → 80<br>
• =VAR.P(A1:A5) → 50（母分散、÷5）<br>
• =VAR.S(A1:A5) → 62.5（不偏分散、÷4）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「分散と標準偏差」<br>
計算例を検証済み<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'variance', 'calculation', 'example', 'interpretation']
        },

        # カード4: 標準偏差の定義と公式
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【標準偏差の定義】<br>なぜ平方根をとるのか？<br>公式は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>標準偏差とは:</b><br>
分散の平方根（√分散）<br>
データの散らばり具合を<b>元の単位</b>で表す指標<br>
<br>

<hr>

<b>【公式】</b><br>
<br>

<b>①母標準偏差（Population Standard Deviation）: σ</b><br>
\\[\\sigma = \\\\sqrt{{\\frac{1}{N}\\sum_{i=1}^N (x_i - \\mu)^2}}\\]
<br>

• 母分散の平方根<br>
• 母集団の散らばり<br>
<br>

<b>②標本標準偏差（Sample Standard Deviation）: s</b><br>
\\[s = \\\\sqrt{{\\frac{1}{n-1}\\sum_{i=1}^n (x_i - \\bar{x})^2}}\\]
<br>

• 不偏分散の平方根<br>
• <b>統計検定2級ではこちらを使用</b><br>
<br>

<hr>

<b>【なぜ平方根をとるのか】</b><br>
<br>

<b>理由1: 単位を元に戻す</b><br>
<br>

• 分散: データの単位の<b>2乗</b><br>
  例: データがcm → 分散はcm²<br>
<br>

• 標準偏差: データの単位と<b>同じ</b><br>
  例: データがcm → 標準偏差もcm<br>
<br>

<b>具体例: 身長データ</b><br>
• 平均: 170cm<br>
• 分散: 25cm²（解釈しづらい）<br>
• 標準偏差: √25 = 5cm（解釈しやすい！）<br>
<br>

「平均身長170cm、標準偏差5cm」<br>
→ 「平均から±5cm程度のばらつき」と直感的<br>
<br>

<b>理由2: データのスケールに対応</b><br>
<br>

• 分散は2乗のため値が大きくなりすぎる<br>
• 平方根をとることで適切なスケールに<br>
<br>

<b>例:</b><br>
• データ: {70, 80, 90}（範囲20）<br>
• 分散: 約100（大きすぎ）<br>
• 標準偏差: √100 = 10（妥当）<br>
<br>

<b>理由3: 正規分布との対応</b><br>
<br>

正規分布N(μ, σ²)では:<br>
• 平均±1σの範囲: 約68%のデータ<br>
• 平均±2σの範囲: 約95%のデータ<br>
• 平均±3σの範囲: 約99.7%のデータ<br>
<br>

→ 標準偏差は<b>ばらつきの基準単位</b>として機能<br>
<br>

<hr>

<b>【計算例】</b><br>
<br>

<b>データ: {70, 75, 80, 85, 90}点</b><br>
<br>

<b>ステップ1: 不偏分散を計算</b><br>
s² = 62.5点²（前のカードで計算済み）<br>
<br>

<b>ステップ2: 平方根をとる</b><br>
\\[s = \\\\sqrt{62.5} \\\approx 7.9\\]
<br>
（単位：点）
<br>

<b>解釈:</b><br>
• 平均80点、標準偏差7.9点<br>
• 多くのデータは平均±8点程度に分布<br>
• 分散62.5点²より直感的!<br>
<br>

<hr>

<b>【Excel関数】</b><br>
<br>

• <b>STDEV.P(範囲)</b>: 母標準偏差（√母分散）<br>
• <b>STDEV.S(範囲)</b>: 標本標準偏差（√不偏分散）<br>
• <b>STDEV(範囲)</b>: STDEV.Sと同じ（互換性）<br>
<br>

<b>例: A1:A5に{70,75,80,85,90}</b><br>
• =STDEV.S(A1:A5) → 7.906<br>
• =SQRT(VAR.S(A1:A5)) → 7.906（同じ）<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
<br>

<b>分散 vs 標準偏差の使い分け:</b><br>
<br>

<b>分散を使う場面:</b><br>
• 理論的な計算・証明<br>
• 分散分析（ANOVA）<br>
• 数学的に扱いやすい（線形性）<br>
<br>

<b>標準偏差を使う場面:</b><br>
• データの解釈・説明<br>
• グラフの誤差範囲<br>
• 正規分布での確率計算<br>
• <b>実務では標準偏差の方が一般的</b><br>
<br>

<b>統計検定2級では:</b><br>
• 両方の計算ができること<br>
• 単位の違いを理解すること<br>
• 正規分布との関係を理解すること<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「標準偏差」<br>
統計WEB「分散と標準偏差」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'standard-deviation', 'definition', 'formula', 'square-root']
        },

        # カード5: 標準偏差の使い方と変動係数
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【標準偏差の使い方】<br>変動係数とは？<br>どう解釈する？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【標準偏差の基本的な使い方】</b><br>
<br>

<b>①ばらつきの大きさを評価</b><br>
<br>

• 標準偏差が大きい → ばらつき大<br>
• 標準偏差が小さい → ばらつき小<br>
<br>

<b>例: 2つのクラスの比較</b><br>
• クラスA: 平均80点、標準偏差15点<br>
• クラスB: 平均80点、標準偏差5点<br>
<br>

→ クラスBの方が成績が安定している<br>
<br>

<b>②正規分布での確率計算</b><br>
<br>

データが正規分布N(μ, σ²)に従うとき:<br>
<br>

• <b>μ ± 1σ</b>の範囲: 約<b>68%</b>のデータ<br>
• <b>μ ± 2σ</b>の範囲: 約<b>95%</b>のデータ<br>
• <b>μ ± 3σ</b>の範囲: 約<b>99.7%</b>のデータ<br>
<br>

<b>例: 平均170cm、標準偏差5cmの身長</b><br>
• 165〜175cm（±1σ）: 約68%の人<br>
• 160〜180cm（±2σ）: 約95%の人<br>
• 155〜185cm（±3σ）: 約99.7%の人<br>
<br>

<b>③外れ値の検出</b><br>
<br>

• 平均から±3σ以上離れた値 → 外れ値の可能性<br>
• 正規分布では0.3%しか発生しない<br>
<br>

<hr>

<b>【変動係数（Coefficient of Variation: CV）】</b><br>
<br>

<b>定義:</b><br>
\\[\\mathrm{CV} = \\frac{s}{\\bar{x}} \\times 100\%\\]
<br>

または<br>
\\[\\mathrm{CV} = \\frac{\sigma}{\mu} \\times 100\%\\]
<br>

<b>意味:</b><br>
• 標準偏差を平均で割った値<br>
• <b>相対的なばらつきの大きさ</b><br>
• 単位に依存しない<br>
<br>

<hr>

<b>【変動係数の必要性】</b><br>
<br>

<b>問題: 異なる単位・スケールのデータを比較したい</b><br>
<br>

<b>例1: 身長と体重のばらつき比較</b><br>
• 身長: 平均170cm、標準偏差5cm<br>
• 体重: 平均60kg、標準偏差4kg<br>
<br>

→ 標準偏差だけでは比較不可（単位が違う）<br>
<br>

<b>変動係数で比較:</b><br>
• 身長のCV: 5/170 × 100% ≈ 2.9%<br>
• 体重のCV: 4/60 × 100% ≈ 6.7%<br>
<br>

→ 体重の方が相対的にばらつきが大きい<br>
<br>

<b>例2: 異なる時代の株価のばらつき</b><br>
• 2000年: 平均1000円、標準偏差100円<br>
• 2020年: 平均5000円、標準偏差300円<br>
<br>

→ 標準偏差は増えているが、相対的には？<br>
<br>

<b>変動係数で比較:</b><br>
• 2000年のCV: 100/1000 × 100% = 10%<br>
• 2020年のCV: 300/5000 × 100% = 6%<br>
<br>

→ 2020年の方が相対的に安定している<br>
<br>

<hr>

<b>【変動係数の解釈】</b><br>
<br>

• <b>CVが小さい</b> → データが平均に集中（安定）<br>
• <b>CVが大きい</b> → データが平均から離れている（不安定）<br>
<br>

<b>目安（一般論）:</b><br>
• CV < 10%: 比較的安定<br>
• 10% ≤ CV < 20%: 中程度のばらつき<br>
• CV ≥ 20%: ばらつきが大きい<br>
<br>

<b>注意:</b><br>
• 分野によって基準は異なる<br>
• 平均がゼロに近いと使えない<br>
• 平均が負の値では使えない<br>
<br>

<hr>

<b>【計算例】</b><br>
<br>

<b>データ: {70, 75, 80, 85, 90}点</b><br>
• 平均: 80点<br>
• 標準偏差: 7.9点<br>
<br>

<b>変動係数:</b><br>
\\[\\mathrm{CV} = \\frac{7.9}{80} \\times 100\% \\approx 9.9\%\\]
<br>

<b>解釈:</b><br>
• 約10%のばらつき<br>
• 比較的安定したデータ<br>
<br>

<hr>

<b>【統計検定2級での注意点】</b><br>
<br>

• 標準偏差と変動係数の違いを理解<br>
• 正規分布での確率計算（±1σ, ±2σ, ±3σ）<br>
• 異なるデータの比較には変動係数<br>
• 単位に注意（標準偏差は元の単位、CVは%）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「標準偏差」<br>
統計WEB「変動係数」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'standard-deviation', 'coefficient-of-variation', 'cv', 'usage']
        },

        # カード6: 4つのばらつき指標の比較
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【ばらつきの指標】<br>分散・標準偏差・範囲・IQRの<br>比較と使い分けは？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>データのばらつきを測る4つの指標:</b><br>
<br>

<hr>

<b>【①範囲（Range）】</b><br>
<br>

<b>公式:</b><br>
\\[範囲} = 最大値} - 最小値}\\]
<br>

<b>特徴:</b><br>
• <b>最も簡単</b>に計算できる<br>
• 極端な値（外れ値）に<b>強く影響される</b><br>
• データ全体の情報を使わない（2点のみ）<br>
<br>

<b>長所:</b><br>
• 直感的で分かりやすい<br>
• 計算が簡単<br>
<br>

<b>短所:</b><br>
• 外れ値に弱い<br>
• サンプルサイズの影響を受けやすい<br>
<br>

<b>例: {70, 75, 80, 85, 90}</b><br>
範囲 = 90 - 70 = 20<br>
<br>

<hr>

<b>【②四分位範囲（IQR: Interquartile Range）】</b><br>
<br>

<b>公式:</b><br>
\\[\\\IQR} = Q3 - Q1\\]
<br>

<b>特徴:</b><br>
• 中央50%のデータの範囲<br>
• <b>外れ値に頑健</b>（robust）<br>
• 箱ひげ図の箱の高さ<br>
<br>

<b>長所:</b><br>
• 外れ値の影響を受けにくい<br>
• 歪んだ分布でも使える<br>
<br>

<b>短所:</b><br>
• データの50%しか使わない<br>
• 正規分布では標準偏差ほど効率的でない<br>
<br>

<b>例: {70, 75, 80, 85, 90}</b><br>
Q1 = 75, Q3 = 85<br>
IQR = 85 - 75 = 10<br>
<br>

<hr>

<b>【③分散（Variance）: s²またはσ²】</b><br>
<br>

<b>公式（不偏分散）:</b><br>
\\[s^2 = \\frac{1}{n-1}\\sum(x_i - \\bar{x})^2\\]
<br>

<b>特徴:</b><br>
• <b>すべてのデータを使用</b><br>
• 平均からの偏差の2乗の平均<br>
• 単位がデータの2乗<br>
<br>

<b>長所:</b><br>
• 理論的に扱いやすい（線形性）<br>
• すべての情報を使う<br>
• 統計的推論の基礎<br>
<br>

<b>短所:</b><br>
• 単位が2乗で直感的でない<br>
• 外れ値の影響を受けやすい（2乗のため）<br>
<br>

<b>例: {70, 75, 80, 85, 90}</b><br>
s² = 62.5点²<br>
<br>

<hr>

<b>【④標準偏差（Standard Deviation）: sまたはσ】</b><br>
<br>

<b>公式:</b><br>
\\[s = \\\\sqrt{s^2} = \\\\sqrt{{\\frac{1}{n-1}\\sum(x_i - \\bar{x})^2}}\\]
<br>

<b>特徴:</b><br>
• 分散の平方根<br>
• <b>元のデータと同じ単位</b><br>
• <b>最も一般的に使われる</b><br>
<br>

<b>長所:</b><br>
• 直感的に理解しやすい<br>
• すべてのデータを使う<br>
• 正規分布との対応（±1σ, ±2σ）<br>
<br>

<b>短所:</b><br>
• 外れ値の影響を受ける<br>
• 歪んだ分布では解釈が難しい<br>
<br>

<b>例: {70, 75, 80, 85, 90}</b><br>
s = √62.5 ≈ 7.9点<br>
<br>

<hr>

<b>【4つの指標の比較表】</b><br>
<br>

<table border="1" cellpadding="5" style="border-collapse:collapse; max-width:100%; font-size:16px; overflow-x:auto;">
<tr style="background-color:#e0e0e0;">
  <th>指標</th>
  <th>計算の複雑さ</th>
  <th>外れ値の影響</th>
  <th>使用するデータ</th>
</tr>
<tr>
  <td><b>範囲</b></td>
  <td>簡単</td>
  <td>非常に大きい</td>
  <td>2点のみ</td>
</tr>
<tr>
  <td><b>IQR</b></td>
  <td>やや複雑</td>
  <td>小さい</td>
  <td>中央50%</td>
</tr>
<tr>
  <td><b>分散</b></td>
  <td>複雑</td>
  <td>大きい</td>
  <td>すべて</td>
</tr>
<tr>
  <td><b>標準偏差</b></td>
  <td>複雑</td>
  <td>大きい</td>
  <td>すべて</td>
</tr>
</table>
<br>

<hr>

<b>【使い分けの指針】</b><br>
<br>

<b>範囲を使う:</b><br>
• 簡単な記述統計<br>
• データの全体的な広がりを知りたい<br>
• 品質管理（管理図）<br>
<br>

<b>IQRを使う:</b><br>
• 外れ値が含まれる可能性がある<br>
• 分布が歪んでいる<br>
• 箱ひげ図での表現<br>
• ノンパラメトリック分析<br>
<br>

<b>分散を使う:</b><br>
• 理論的な計算・証明<br>
• 分散分析（ANOVA）<br>
• 数学的な扱いが必要な場合<br>
<br>

<b>標準偏差を使う:</b><br>
• <b>一般的な記述統計</b>（最も推奨）<br>
• データの解釈・説明<br>
• 正規分布を仮定できる<br>
• 信頼区間・検定統計量の計算<br>
<br>

<hr>

<b>【外れ値がある場合の例】</b><br>
<br>

<b>データA: {70, 75, 80, 85, 90}</b><br>
• 範囲: 20<br>
• IQR: 10<br>
• 標準偏差: 7.9<br>
<br>

<b>データB: {70, 75, 80, 85, 200}（外れ値あり）</b><br>
• 範囲: 130（大幅に増加!）<br>
• IQR: 10（変わらず）<br>
• 標準偏差: 54.1（大幅に増加）<br>
<br>

→ IQRは外れ値に頑健<br>
<br>

<hr>

<b>【統計検定2級では】</b><br>
<br>

• すべての指標の計算方法を習得<br>
• それぞれの特徴と使い分けを理解<br>
• 外れ値の影響を考慮<br>
• 正規分布では標準偏差が主流<br>
• 歪んだ分布ではIQRが有用<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「散らばりの指標」<br>
統計WEB「分散と標準偏差」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'variance', 'standard-deviation', 'range', 'iqr', 'comparison']
        },

        # カード7: データ変換の影響
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【データ変換の影響】<br>平均・分散・標準偏差は<br>どう変わる？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>データに定数を加えたり掛けたりした時の変化:</b><br>
<br>

<hr>

<b>【①すべてのデータに定数aを加える】</b><br>
<br>

<b>変換: y<sub>i</sub> = x<sub>i</sub> + a</b><br>
<br>

<b>影響:</b><br>
• <b>平均</b>: ȳ = x̄ + a（aだけ増加）<br>
• <b>分散</b>: s<sub>y</sub>² = s<sub>x</sub>²（変わらない!）<br>
• <b>標準偏差</b>: s<sub>y</sub> = s<sub>x</sub>（変わらない!）<br>
<br>

<b>理由:</b><br>
すべてのデータが同じだけ平行移動<br>
→ 相対的な散らばりは変わらない<br>
<br>

<b>具体例: すべての得点に5点加算</b><br>
• 元データ: {70, 75, 80, 85, 90}<br>
  - 平均: 80点<br>
  - 分散: 62.5点²<br>
  - 標準偏差: 7.9点<br>
<br>

• 変換後: {75, 80, 85, 90, 95}<br>
  - 平均: 85点（+5）<br>
  - 分散: 62.5点²（変わらず）<br>
  - 標準偏差: 7.9点（変わらず）<br>
<br>

<b>応用: 偏差値の計算</b><br>
データから平均を引く（x<sub>i</sub> - x̄）<br>
→ 平均は0になるが、分散・標準偏差は不変<br>
<br>

<hr>

<b>【②すべてのデータに定数bを掛ける】</b><br>
<br>

<b>変換: y<sub>i</sub> = b × x<sub>i</sub></b><br>
<br>

<b>影響:</b><br>
• <b>平均</b>: ȳ = b × x̄（b倍）<br>
• <b>分散</b>: s<sub>y</sub>² = b² × s<sub>x</sub>²（<b>b²倍</b>!）<br>
• <b>標準偏差</b>: s<sub>y</sub> = |b| × s<sub>x</sub>（|b|倍）<br>
<br>

<b>理由:</b><br>
偏差が b 倍になる → 偏差の2乗は b² 倍<br>
<br>

<b>具体例: すべての得点を2倍</b><br>
• 元データ: {70, 75, 80, 85, 90}<br>
  - 平均: 80点<br>
  - 分散: 62.5点²<br>
  - 標準偏差: 7.9点<br>
<br>

• 変換後: {140, 150, 160, 170, 180}<br>
  - 平均: 160点（×2）<br>
  - 分散: 250点²（×4 = ×2²）<br>
  - 標準偏差: 15.8点（×2）<br>
<br>

<b>応用: 単位変換</b><br>
• cmからmへ: ×0.01<br>
  - 平均: 0.01倍<br>
  - 分散: 0.0001倍（0.01²）<br>
  - 標準偏差: 0.01倍<br>
<br>

<hr>

<b>【③一般的な1次変換】</b><br>
<br>

<b>変換: y<sub>i</sub> = a + b × x<sub>i</sub></b><br>
<br>

<b>影響:</b><br>
• <b>平均</b>: ȳ = a + b × x̄<br>
• <b>分散</b>: s<sub>y</sub>² = b² × s<sub>x</sub>²<br>
• <b>標準偏差</b>: s<sub>y</sub> = |b| × s<sub>x</sub><br>
<br>

<b>注意: 加算aは分散・標準偏差に影響しない</b><br>
<br>

<b>具体例: 偏差値の計算</b><br>
\\[T = 50 + 10 \\times \\frac{x - \\bar{x}}{s}\\]
<br>

これは1次変換 y = a + b × x の形<br>
• a = 50<br>
• b = 10/s<br>
<br>

→ 偏差値の平均は50、標準偏差は10<br>
<br>

<hr>

<b>【実用例: 単位変換】</b><br>
<br>

<b>身長データをcmからmに変換</b><br>
<br>

• 元データ（cm）:<br>
  - 平均: 170cm<br>
  - 標準偏差: 5cm<br>
<br>

• 変換後（m）: y = x ÷ 100 = 0.01 × x<br>
  - 平均: 1.70m（×0.01）<br>
  - 標準偏差: 0.05m（×0.01）<br>
<br>

<b>温度: 摂氏から華氏への変換</b><br>
<br>

F = 32 + 1.8 × C<br>
<br>

• 摂氏データ:<br>
  - 平均: 20°C<br>
  - 標準偏差: 5°C<br>
<br>

• 華氏データ:<br>
  - 平均: 32 + 1.8 × 20 = 68°F<br>
  - 標準偏差: 1.8 × 5 = 9°F<br>
<br>

<hr>

<b>【重要な公式まとめ】</b><br>
<br>

<table border="1" cellpadding="5" style="border-collapse:collapse; max-width:100%; font-size:16px; overflow-x:auto;">
<tr style="background-color:#e0e0e0;">
  <th>変換</th>
  <th>平均</th>
  <th>分散</th>
  <th>標準偏差</th>
</tr>
<tr>
  <td>y = x + a</td>
  <td>ȳ = x̄ + a</td>
  <td>変わらず</td>
  <td>変わらず</td>
</tr>
<tr>
  <td>y = b × x</td>
  <td>ȳ = b × x̄</td>
  <td>s<sub>y</sub>² = b² × s<sub>x</sub>²</td>
  <td>s<sub>y</sub> = |b| × s<sub>x</sub></td>
</tr>
<tr>
  <td>y = a + b × x</td>
  <td>ȳ = a + b × x̄</td>
  <td>s<sub>y</sub>² = b² × s<sub>x</sub>²</td>
  <td>s<sub>y</sub> = |b| × s<sub>x</sub></td>
</tr>
</table>
<br>

<hr>

<b>【統計検定2級での重要ポイント】</b><br>
<br>

• <b>加算</b> → 分散・標準偏差は不変<br>
• <b>乗算</b> → 分散はb²倍、標準偏差は|b|倍<br>
• 単位変換の問題で頻出<br>
• 偏差値計算の理論的背景<br>
• 標準化（z得点）の計算にも関連<br>
<br>

<b>覚え方:</b><br>
• 平均は素直に変換される<br>
• 分散は「2乗」なのでb²倍<br>
• 標準偏差は「1乗」なのでb倍<br>
• 加算aは相対的位置を変えないので分散に影響なし<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「データの変換と分散」<br>
統計WEB「1次変換」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'variance', 'standard-deviation', 'data-transformation', 'linear-transformation']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("分散と標準偏差 - 検証済みAnkiカード生成")
    print("=" * 70)
    print()

    # AnkiConnect接続確認
    print("🔌 AnkiConnectに接続中...")
    version = invoke_anki('version')
    if version is None:
        print("❌ Ankiが起動していないか、AnkiConnectがインストールされていません")
        return

    print(f"✅ AnkiConnect接続成功")
    print()

    # デッキとモデル名
    deck_name = "統計学v2"
    model_name = "Basic"

    # カード作成
    cards = create_variance_standard_deviation_cards(deck_name, model_name)
    print(f"📝 {len(cards)}枚のカードを追加中...")
    print()

    cards_added = 0
    for i, card in enumerate(cards, 1):
        result = invoke_anki(
            'addNote',
            note={
                'deckName': deck_name,
                'modelName': model_name,
                'fields': {
                    'Front': card['front'],
                    'Back': card['back']
                },
                'tags': card['tags'],
                'options': {
                    'allowDuplicate': True
                }
            }
        )

        if result or result == 0:
            cards_added += 1
            print(f"  ✓ カード{i}: 追加成功")
        else:
            print(f"  ⚠ カード{i}: スキップ（重複の可能性）")

    print()
    print("=" * 70)
    print("✨ 分散と標準偏差カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 分散の定義と3つの公式（母分散・標本分散・不偏分散）")
    print("  カード2: なぜn-1で割るのか（自由度の概念）")
    print("  カード3: 分散の計算例と解釈")
    print("  カード4: 標準偏差の定義となぜ平方根をとるのか")
    print("  カード5: 標準偏差の使い方と変動係数")
    print("  カード6: 4つのばらつき指標の比較（分散・標準偏差・範囲・IQR）")
    print("  カード7: データ変換の影響（加算・乗算）")
    print()


if __name__ == "__main__":
    main()
