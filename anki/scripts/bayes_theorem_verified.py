#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級 Ankiカード - 条件付き確率とベイズの定理（検証済み）
作成日: 2026-01-13
"""

cards = [
    # カード1: 条件付き確率の定義
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】条件付き確率とは何か？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
ある事象が起こるという条件のもとで、別のある事象が起こる確率のこと。<br>
事象Bが起こったときに事象Aが起こる確率を \\(P(A|B)\\) と表す。<br>
<br>

<b>公式:</b><br>
\\[P(A|B) = \\frac{P(A \\cap B)}{P(B)}\\]
<br>

<b>記号の意味:</b><br>
• \\(P(A|B)\\)：「事象Bが起こったときの事象Aの条件付き確率」<br>
• \\(P(A \\cap B)\\)：事象AとBが同時に起こる確率<br>
• \\(P(B)\\)：事象Bが起こる確率（\\(P(B) > 0\\)）<br>
<br>

<hr>

<b>具体例: 色付き玉の問題</b><br>
<br>

<b>【問題】</b><br>
赤玉3個（「1」が2個、「2」が1個）と白玉3個が入った袋から1個取り出す。<br>
赤色が出た条件下で「1」である確率は？<br>
<br>

<b>【解答】</b><br>
• \\(P(\\text{赤玉}) = \\frac{3}{6} = \\frac{1}{2}\\)<br>
• \\(P(\\text{「1」} \\cap \\text{赤玉}) = \\frac{2}{6} = \\frac{1}{3}\\)<br>
<br>

\\[P(\\text{「1」}|\\text{赤玉}) = \\frac{P(\\text{「1」} \\cap \\text{赤玉})}{P(\\text{赤玉})} = \\frac{1/3}{1/2} = \\frac{2}{3}\\]
<br>

→ 赤玉が出た条件下では、「1」である確率は2/3<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• P(A|B) ≠ P(B|A)（一般に異なる）<br>
• P(B) = 0 の場合は定義されない<br>
• 独立事象の場合：P(A|B) = P(A)<br>
• 条件付き確率は乗法定理の導出に使われる<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「10-1. 条件付き確率とは」<br>
https://bellcurve.jp/statistics/course/6438.html<br>
計算例は検証スクリプトbayes_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'conditional-probability']
    },

    # カード2: ベイズの定理の定義
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】ベイズの定理とは何か？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
観測された結果から原因を推定するための確率理論。<br>
結果事象Aが起こったときに、特定の原因Biが起こった確率を求める定理。<br>
<br>

<b>公式:</b><br>
\\[P(B_i|A) = \\frac{P(B_i) \\cdot P(A|B_i)}{P(A)}\\]
<br>

さらに、分母を展開すると：<br>
\\[P(B_i|A) = \\frac{P(B_i) \\cdot P(A|B_i)}{\\sum_{j} P(B_j) \\cdot P(A|B_j)}\\]
<br>

<b>各項の意味:</b><br>
• \\(P(B_i|A)\\)：<b>事後確率</b>（結果Aから推定される原因Biの確率）<br>
• \\(P(B_i)\\)：<b>事前確率</b>（原因Biの初期確率）<br>
• \\(P(A|B_i)\\)：<b>尤度</b>（原因Biのもとで結果Aが起こる確率）<br>
• \\(P(A)\\)：<b>周辺尤度</b>（全体での結果Aの確率、全確率の公式で計算）<br>
<br>

<hr>

<b>全確率の公式:</b><br>
\\[P(A) = \\sum_{i} P(B_i) \\cdot P(A|B_i)\\]
<br>

複数の原因における結果の確率を、各原因の確率で加重平均したもの。<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 「結果から原因を推定」する問題で使う<br>
• 統計検定2級ではほぼ毎回出題される重要トピック<br>
• 原因Biは互いに排反（同時に起こらない）である必要がある<br>
• 事前確率を新しい情報で更新→事後確率を得る<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「10-4. ベイズの定理」<br>
https://bellcurve.jp/statistics/course/6444.html<br>
Qiita「ベイズの定理_統計検定2級対策」<br>
https://qiita.com/Mrs_P/items/326a5deffaa452cd522e
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'bayes-theorem', 'definition']
    },

    # カード3: 事前確率と事後確率
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】事前確率と事後確率の違いは何か？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
<br>

<b>1. 事前確率（Prior Probability）</b><br>
情報を得る前の確率。初期状態での確率。<br>
ベイズの定理では \\(P(B_i)\\) で表される。<br>
<br>

<b>2. 事後確率（Posterior Probability）</b><br>
新しい情報を得た後に更新された確率。<br>
ベイズの定理では \\(P(B_i|A)\\) で表される。<br>
<br>

<b>関係式（ベイズの定理）:</b><br>
\\[\\text{事後確率} = \\frac{\\text{事前確率} \\times \\text{尤度}}{\\text{周辺尤度}}\\]
<br>

<hr>

<b>具体例: USB製品の返品問題</b><br>
<br>

<b>【問題設定】</b><br>
• 市場シェア：A社80%、B社10%、C社10%<br>
• 返品率：A社2%、B社2%、C社10%<br>
• ある返品USB製品が届いた。C社製である確率は？<br>
<br>

<b>【事前確率】</b><br>
情報を得る前（返品される前）の確率：<br>
\\(P(C) = 0.1\\)（10%）<br>
<br>

<b>【事後確率の計算】</b><br>
返品されたという情報を得た後の確率：<br>
<br>

全確率の公式：<br>
\\[P(\\text{返品}) = 0.8 \\times 0.02 + 0.1 \\times 0.02 + 0.1 \\times 0.10 = 0.028\\]
<br>

ベイズの定理：<br>
\\[P(C|\\text{返品}) = \\frac{0.1 \\times 0.10}{0.028} = \\frac{0.01}{0.028} \\approx 0.357\\]
<br>

<b>【解釈】</b><br>
• 事前確率：10%（市場シェアから）<br>
• 事後確率：35.7%（返品という情報で更新）<br>
→ 返品率が高いC社の可能性が大きく上昇<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 事前確率：初期情報のみに基づく<br>
• 事後確率：新しい証拠・観測結果を組み込む<br>
• ベイズの定理は確率を更新する枠組み<br>
• 統計検定2級では必ず出題される重要概念<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「10-5. 事前確率と事後確率」<br>
https://bellcurve.jp/statistics/course/6446.html
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'bayes-theorem', 'prior-posterior']
    },

    # カード4: ベイズの定理の計算例（工場問題）
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】ベイズの定理の計算例：工場の不良品問題</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>問題:</b><br>
工場XとYが電子部品を生産している。<br>
• 工場X：生産シェア60%、不良率2%<br>
• 工場Y：生産シェア40%、不良率5%<br>
<br>

市場から不良品が見つかった。工場Xの製品である確率は？<br>
<br>

<hr>

<b>解答:</b><br>
<br>

<b>ステップ1: 事前確率</b><br>
\\(P(X) = 0.60\\)、\\(P(Y) = 0.40\\)<br>
<br>

<b>ステップ2: 尤度（条件付き確率）</b><br>
\\(P(\\text{不良品}|X) = 0.02\\)<br>
\\(P(\\text{不良品}|Y) = 0.05\\)<br>
<br>

<b>ステップ3: 全確率の公式</b><br>
\\[P(\\text{不良品}) = P(X) \\cdot P(\\text{不良品}|X) + P(Y) \\cdot P(\\text{不良品}|Y)\\]
\\[= 0.60 \\times 0.02 + 0.40 \\times 0.05\\]
\\[= 0.012 + 0.020 = 0.032\\]
<br>

<b>ステップ4: ベイズの定理</b><br>
\\[P(X|\\text{不良品}) = \\frac{P(X) \\cdot P(\\text{不良品}|X)}{P(\\text{不良品})}\\]
\\[= \\frac{0.60 \\times 0.02}{0.032} = \\frac{0.012}{0.032} = 0.375 = 37.5\\%\\]
<br>

<hr>

<b>【解釈】</b><br>
• <b>事前確率</b>：工場Xの製品である確率 = 60%<br>
• <b>事後確率</b>：不良品が工場Xの製品である確率 = 37.5%<br>
<br>

確率が60%→37.5%に<b>低下</b>した理由：<br>
工場Yの不良率（5%）が工場X（2%）より高いため、<br>
不良品が見つかると工場Yの可能性が相対的に高まった。<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
• 結果から原因を推定する典型問題<br>
• 全確率の公式で分母を計算するのを忘れずに<br>
• 事後確率は必ずしも事前確率より大きくならない<br>
• 尤度の大小が事後確率に影響する<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
Qiita「ベイズの定理_統計検定2級対策」<br>
https://qiita.com/Mrs_P/items/326a5deffaa452cd522e<br>
計算例は検証スクリプトbayes_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'bayes-theorem', 'example']
    },

    # カード5: ベイズの定理の計算例（病気検査問題）
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】ベイズの定理の計算例：病気検査問題</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>問題:</b><br>
日本人の0.01%が罹患する稀な病気の検査がある。<br>
• 感度（患者→陽性）：95%<br>
• 特異度（非患者→陰性）：80%<br>
<br>

陽性判定が出たとき、実際に病気である確率は？<br>
<br>

<hr>

<b>解答:</b><br>
<br>

<b>ステップ1: 事前確率</b><br>
\\(P(\\text{病気}) = 0.0001\\)（0.01%）<br>
\\(P(\\text{健康}) = 0.9999\\)（99.99%）<br>
<br>

<b>ステップ2: 尤度（条件付き確率）</b><br>
\\(P(\\text{陽性}|\\text{病気}) = 0.95\\)（感度）<br>
\\(P(\\text{陽性}|\\text{健康}) = 1 - 0.80 = 0.20\\)（偽陽性率）<br>
<br>

<b>ステップ3: 全確率の公式</b><br>
\\[P(\\text{陽性}) = P(\\text{病気}) \\cdot P(\\text{陽性}|\\text{病気}) + P(\\text{健康}) \\cdot P(\\text{陽性}|\\text{健康})\\]
\\[= 0.0001 \\times 0.95 + 0.9999 \\times 0.20\\]
\\[= 0.000095 + 0.19998 = 0.200075\\]
<br>

<b>ステップ4: ベイズの定理</b><br>
\\[P(\\text{病気}|\\text{陽性}) = \\frac{P(\\text{病気}) \\cdot P(\\text{陽性}|\\text{病気})}{P(\\text{陽性})}\\]
\\[= \\frac{0.0001 \\times 0.95}{0.200075} = \\frac{0.000095}{0.200075} \\approx 0.000475 = 0.0475\\%\\]
<br>

<hr>

<b>【解釈】</b><br>
陽性判定が出ても、実際に病気である確率は<b>わずか0.0475%</b>。<br>
<br>

<b>なぜこんなに低いのか？</b><br>
• 病気が非常に稀（0.01%）<br>
• 偽陽性率が20%と高い<br>
• 健康な人の数が圧倒的に多いため、偽陽性の絶対数が多い<br>
<br>

\\(\\text{偽陽性} = 0.9999 \\times 0.20 = 0.19998\\)<br>
\\(\\text{真陽性} = 0.0001 \\times 0.95 = 0.000095\\)<br>
<br>

→ 偽陽性が真陽性の2000倍以上！<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 稀な病気では陽性でも実際の確率は低い<br>
• 事前確率（有病率）が事後確率に大きく影響<br>
• 感度・特異度だけで判断してはいけない<br>
• 医療統計で頻出の重要問題<br>
• 統計検定2級でも類似問題が出題される<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「10-6. ベイズの定理の使い方」<br>
https://bellcurve.jp/statistics/course/6448.html<br>
計算例は検証スクリプトbayes_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'bayes-theorem', 'medical-test']
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
