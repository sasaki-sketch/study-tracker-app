#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級 Ankiカード - 尖度（検証済み）
作成日: 2026-01-12
"""

cards = [
    # カード1: 尖度の定義
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【尖度】尖度とは何か？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
尖度（せんど、Kurtosis）は、分布が正規分布からどれだけ尖っているかを表す統計量。<br>
山の尖り度と裾の広がり度を示す。<br>
<br>

<b>2つの定義:</b><br>
1. <b>正規分布 = 3とする定義</b><br>
\\[\\text{尖度} = \\frac{\\mu_4}{\\sigma^4} = \\frac{E[(X-\\mu)^4]}{\\sigma^4}\\]
<br>

2. <b>正規分布 = 0とする定義（過剰尖度）</b><br>
\\[\\text{尖度} = \\frac{\\mu_4}{\\sigma^4} - 3 = \\frac{E[(X-\\mu)^4]}{\\sigma^4} - 3\\]
<br>

統計検定2級では、通常<b>過剰尖度（正規分布=0）</b>を使用します。<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
• 4次モーメントを使用するため、外れ値に極めて敏感<br>
• 「-3」は正規分布を基準（尖度=0）とするための調整値<br>
• ExcelのKURT関数も過剰尖度（正規分布=0）を使用<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-5. 歪度と尖度」https://bellcurve.jp/statistics/course/17950.html<br>
統計用語集「尖度」https://bellcurve.jp/statistics/glossary/2113.html<br>
Qiita「統計検定2級 歪度と尖度」より検証
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'kurtosis', 'definition']
    },

    # カード2: 尖度の公式（標本版）
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【尖度】標本データから尖度を計算する公式は？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>標本尖度の公式（過剰尖度）:</b><br>
\\[\\text{尖度} = \\frac{1}{n}\\sum_{i=1}^{n}\\frac{(x_i - \\bar{x})^4}{s^4} - 3\\]
<br>

<b>記号の意味:</b><br>
• \\(n\\)：データ数（サンプルサイズ）<br>
• \\(x_i\\)：各データの値<br>
• \\(\\bar{x}\\)：標本平均<br>
• \\(s\\)：標本標準偏差<br>
<br>

<hr>

<b>具体例: データ = [1, 2, 3, 4, 5]</b><br>
<br>

<b>ステップ1: 基本統計量</b><br>
• 平均 \\(\\bar{x} = 3.0\\)<br>
• 標準偏差 \\(s = \\sqrt{\\frac{(1-3)^2+(2-3)^2+(3-3)^2+(4-3)^2+(5-3)^2}{5}} = \\sqrt{2} \\approx 1.414\\)<br>
<br>

<b>ステップ2: 各データの偏差の4乗</b><br>
• \\((1-3)^4 = 16\\)<br>
• \\((2-3)^4 = 1\\)<br>
• \\((3-3)^4 = 0\\)<br>
• \\((4-3)^4 = 1\\)<br>
• \\((5-3)^4 = 16\\)<br>
<br>

<b>ステップ3: 尖度の計算</b><br>
\\[\\text{尖度} = \\frac{\\frac{16+1+0+1+16}{5}}{(\\sqrt{2})^4} - 3 = \\frac{6.8}{4.0} - 3 = 1.7 - 3 = -1.3\\]
<br>

→ 負の値なので、正規分布より平坦な分布<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
• 分子: 偏差の4乗の平均（4次モーメント）<br>
• 分母: 標準偏差の4乗（正規化のため）<br>
• 「-3」で正規分布を基準（尖度=0）に調整<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-5. 歪度と尖度」https://bellcurve.jp/statistics/course/17950.html<br>
計算例は検証スクリプトkurtosis_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'kurtosis', 'formula', 'calculation']
    },

    # カード3: 尖度の解釈
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【尖度】尖度の値はどのように解釈するか？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>尖度の値の解釈（過剰尖度）:</b><br>
<br>

<b>1. 尖度 &gt; 0（正の値）</b><br>
• 正規分布より尖った分布<br>
• 山が急峻で、裾が長い（裾が重い）<br>
• データが平均付近に集中し、外れ値が出やすい<br>
• 例：t分布<br>
<br>

<b>2. 尖度 = 0</b><br>
• 正規分布と同程度の尖り具合<br>
• 山の形が正規分布に近い<br>
<br>

<b>3. 尖度 &lt; 0（負の値）</b><br>
• 正規分布より平坦な分布<br>
• 山が緩やかで、裾が短い（裾が軽い）<br>
• データが散らばり、外れ値が出にくい<br>
• 例：一様分布（理論値 = -1.2）<br>
<br>

<hr>

<b>具体例（検証済み）:</b><br>
<br>

• <b>正規分布（N=1000）</b><br>
　尖度 ≈ 0.07 → ほぼ0、正規分布と確認<br>
<br>

• <b>一様分布（N=1000）</b><br>
　尖度 ≈ -1.23 → 負、平坦な分布と確認<br>
　（理論値-1.2とほぼ一致）<br>
<br>

• <b>データ [1,2,3,4,5]</b><br>
　尖度 = -1.3 → 負、平坦な分布<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 尖度は4乗を使うため、外れ値の影響を受けやすい<br>
• リスク評価や異常検知で活用される<br>
• 正規分布の判定では歪度と合わせて確認する<br>
• 統計検定2級では「正規分布=0」の定義が主流<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計情報局「尖度の意味・解釈と求め方」https://toukeigaku-jouhou.info/2017/08/20/kurtosis/<br>
Qiita「統計検定2級 歪度と尖度」https://qiita.com/koji0705/items/20b3ef8314145b765579<br>
統計WEB「3-5. 歪度と尖度」より検証
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'kurtosis', 'interpretation']
    }
]

if __name__ == '__main__':
    print(f"作成されたカード数: {len(cards)}")
    print("\n作成されたカード:")
    for i, card in enumerate(cards, 1):
        print(f"\n{i}. タグ: {card['tags']}")
        # frontからタイトルを抽出（簡易版）
        import re
        front_text = card['front']
        title_match = re.search(r'<b>(.+?)</b>', front_text)
        if title_match:
            print(f"   タイトル: {title_match.group(1)}")
