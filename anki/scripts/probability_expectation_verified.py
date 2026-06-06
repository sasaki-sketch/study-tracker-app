#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級 Ankiカード - 確率と期待値（検証済み）
作成日: 2026-01-13
"""

cards = [
    # カード1: 順列と組み合わせの違い
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】順列と組み合わせの違いは何か？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
<br>

<b>1. 順列（Permutation）</b><br>
順序をつけて並べる配列のこと。<br>
異なるn個からr個を取り出して並べる場合の数を \\(_nP_r\\) で表す。<br>
<br>

<b>2. 組み合わせ（Combination）</b><br>
順序を考慮せずに選ぶこと。<br>
異なるn個からr個を取り出す場合の数を \\(_nC_r\\) で表す。<br>
<br>

<b>主な違い:</b><br>
• 順列：順序が重要（A→B と B→A は異なる）<br>
• 組み合わせ：順序は無関係（A,B の組み合わせは1通り）<br>
<br>

<hr>

<b>具体例:</b><br>
<br>

<b>【問題】5人から3人を選ぶ</b><br>
<br>

• <b>順列</b>（委員長・副委員長・書記を決める）<br>
　\\(_5P_3 = 60\\)通り<br>
　→ 役割が異なるので順序が重要<br>
<br>

• <b>組み合わせ</b>（3人の委員を選ぶだけ）<br>
　\\(_5C_3 = 10\\)通り<br>
　→ 役割がないので順序は無関係<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 役割や順番がある → 順列<br>
• 単に選ぶだけ → 組み合わせ<br>
• 関係式：\\(_nC_r = \\frac{_nP_r}{r!}\\)<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
理系ラボ「順列と組み合わせの公式とその違い」<br>
https://rikeilabo.com/formula-and-diferrence-of-permutation-combination<br>
計算例は検証スクリプトprobability_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'permutation', 'combination']
    },

    # カード2: 順列と組み合わせの公式
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】順列と組み合わせの公式は？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>公式:</b><br>
<br>

<b>1. 順列の公式</b><br>
\\[_nP_r = n(n-1)(n-2)\\cdots(n-r+1) = \\frac{n!}{(n-r)!}\\]
<br>

<b>2. 組み合わせの公式</b><br>
\\[_nC_r = \\frac{_nP_r}{r!} = \\frac{n!}{r!(n-r)!}\\]
<br>

<b>関係式:</b><br>
\\[_nC_r = \\frac{_nP_r}{r!}\\]
<br>

<hr>

<b>具体例: \\(_5P_3\\) と \\(_5C_3\\) を計算</b><br>
<br>

<b>【順列の計算】</b><br>
\\[_5P_3 = \\frac{5!}{(5-3)!} = \\frac{5!}{2!} = \\frac{120}{2} = 60\\text{通り}\\]
<br>

または、直接計算:<br>
\\[_5P_3 = 5 \\times 4 \\times 3 = 60\\text{通り}\\]
<br>

<b>【組み合わせの計算】</b><br>
\\[_5C_3 = \\frac{5!}{3! \\times 2!} = \\frac{120}{6 \\times 2} = \\frac{120}{12} = 10\\text{通り}\\]
<br>

<b>【関係式の確認】</b><br>
\\[_5C_3 = \\frac{_5P_3}{3!} = \\frac{60}{6} = 10\\text{通り}\\]
<br>

→ 組み合わせは順列をr!で割ったもの<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 順列：n個からr個を順番に並べる<br>
• 組み合わせ：n個からr個を選ぶ（順不同）<br>
• 階乗：n! = n×(n-1)×(n-2)×...×2×1<br>
• 0! = 1（定義）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
理系ラボ「順列と組み合わせの公式とその違い」<br>
計算例は検証スクリプトprobability_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'permutation', 'combination', 'formula']
    },

    # カード3: 余事象
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】余事象とは何か？どんな時に使うのか？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
余事象とは、ある事象Aが起こらない場合を指す。<br>
事象Aの余事象を \\(\\bar{A}\\) または \\(A^c\\) で表す。<br>
<br>

<b>公式:</b><br>
\\[P(\\bar{A}) = 1 - P(A)\\]
\\[P(A) + P(\\bar{A}) = 1\\]
<br>

<b>使用場面:</b><br>
「<b>少なくとも◯個〜</b>」という問題で余事象を使うと計算が簡単になる。<br>
<br>

<hr>

<b>具体例: 白玉3個、赤玉7個から3つ取り出す</b><br>
<br>

<b>【問題】赤玉が少なくとも1つ出る確率は？</b><br>
<br>

<b>方法1: 直接計算（複雑）</b><br>
赤1個 + 赤2個 + 赤3個 の場合を全て計算…（大変）<br>
<br>

<b>方法2: 余事象を使う（簡単）</b><br>
余事象：「赤玉が1つも出ない」＝「白玉が3つ出る」<br>
<br>

• 全体の組み合わせ：\\(_{10}C_3 = 120\\)通り<br>
• 白玉3つの組み合わせ：\\(_3C_3 = 1\\)通り<br>
• 赤玉が少なくとも1つ出る確率：<br>
\\[P(\\text{赤≥1}) = 1 - \\frac{1}{120} = \\frac{119}{120} \\approx 0.9917\\]
<br>

→ 余事象を使うことで、1通りだけ計算すれば良い！<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 「少なくとも〜」の問題は余事象が有効<br>
• 余事象は「起こらない」場合を考える<br>
• P(A) + P(余事象) = 1 は必ず成立<br>
• 余事象の方が単純な場合が多い<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「9-4. 確率の計算（余事象）」<br>
https://bellcurve.jp/statistics/course/6345.html<br>
計算例は検証スクリプトprobability_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'complementary-event']
    },

    # カード4: 独立事象
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】独立事象とは何か？その公式は？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
2つの事象が独立とは、一方の事象の発生結果が他方の事象の確率に影響を与えないこと。<br>
<br>

例：コイン投げとサイコロ投げは独立。<br>
　　コインの結果がサイコロの結果に影響しない。<br>
<br>

<b>公式:</b><br>
独立な事象A、事象Bについて、両方が同時に起こる確率（積事象）は：<br>
\\[P(A \\cap B) = P(A) \\times P(B)\\]
<br>

<hr>

<b>具体例1: コインとサイコロ</b><br>
<br>

<b>【問題】コインが表、かつサイコロが1の確率は？</b><br>
<br>

• \\(P(\\text{表}) = \\frac{1}{2}\\)<br>
• \\(P(\\text{1}) = \\frac{1}{6}\\)<br>
<br>

独立なので：<br>
\\[P(\\text{表} \\cap \\text{1}) = \\frac{1}{2} \\times \\frac{1}{6} = \\frac{1}{12} \\approx 0.0833\\]
<br>

<b>具体例2: サイコロ2回投げ</b><br>
<br>

<b>【問題】6の目が2回連続で出る確率は？</b><br>
<br>

1回目と2回目は独立なので：<br>
\\[P(\\text{両方6}) = \\frac{1}{6} \\times \\frac{1}{6} = \\frac{1}{36} \\approx 0.0278\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 独立 = 一方が他方に影響しない<br>
• 復元抽出（戻す）の場合は独立<br>
• 非復元抽出（戻さない）の場合は独立でない<br>
• 独立でない場合は乗法定理を使う（次のカード参照）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「9-5. 確率と独立」<br>
https://bellcurve.jp/statistics/course/6347.html<br>
計算例は検証スクリプトprobability_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'independence']
    },

    # カード5: 加法定理
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】加法定理とは何か？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
加法定理は、2つ以上の事象の和事象（AまたはB）の確率を計算する定理。<br>
<br>

<b>公式:</b><br>
<br>

<b>1. 排反事象の場合</b><br>
事象AとBが排反（同時に起こらない）とき：<br>
\\[P(A \\cup B) = P(A) + P(B)\\]
<br>

<b>2. 一般の場合</b><br>
事象AとBが排反でないとき：<br>
\\[P(A \\cup B) = P(A) + P(B) - P(A \\cap B)\\]
<br>

重複部分を引くことで、二重に数えないようにする。<br>
<br>

<hr>

<b>具体例1: 排反事象（サイコロ）</b><br>
<br>

<b>【問題】サイコロで1か2が出る確率は？</b><br>
<br>

1と2は同時に出ないので排反：<br>
\\[P(\\text{1か2}) = P(\\text{1}) + P(\\text{2}) = \\frac{1}{6} + \\frac{1}{6} = \\frac{1}{3}\\]
<br>

<b>具体例2: 一般の場合</b><br>
<br>

<b>【問題】30までの数で、2か3で割り切れる確率は？</b><br>
<br>

• 2で割り切れる数：15個 → \\(P(2) = \\frac{15}{30}\\)<br>
• 3で割り切れる数：10個 → \\(P(3) = \\frac{10}{30}\\)<br>
• 6で割り切れる数：5個 → \\(P(6) = \\frac{5}{30}\\)<br>
<br>

6で割り切れる数は2でも3でも割り切れるので重複：<br>
\\[P(\\text{2か3}) = \\frac{15}{30} + \\frac{10}{30} - \\frac{5}{30} = \\frac{20}{30} = \\frac{2}{3}\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 排反 = 同時に起こらない（AとBの共通部分が空）<br>
• 排反でない場合は共通部分を引く<br>
• 3つ以上の事象にも拡張可能<br>
• ベン図で考えると理解しやすい<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「9-6. 加法定理」<br>
https://bellcurve.jp/statistics/course/23780.html<br>
計算例は検証スクリプトprobability_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'addition-theorem']
    },

    # カード6: 乗法定理
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】乗法定理とは何か？いつ使うのか？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
乗法定理は、2つの事象が同時に起こる確率を求める定理。<br>
条件付き確率の式を変形したもの。<br>
<br>

<b>公式:</b><br>
\\[P(A \\cap B) = P(A) \\times P(B|A)\\]
または<br>
\\[P(A \\cap B) = P(B) \\times P(A|B)\\]
<br>

\\(P(B|A)\\)：「Aが起こった条件のもとでBが起こる確率」（条件付き確率）<br>
<br>

<b>使用場面:</b><br>
後の事象の確率が先の事象に依存する「従属事象」の問題で使う。<br>
<br>

<hr>

<b>具体例: 当たりくじ4本、外れくじ6本（計10本）</b><br>
<br>

<b>【問題1】くじを戻す場合、太郎と花子が両方当たる確率は？</b><br>
<br>

戻すので独立：<br>
\\[P(\\text{両方当たる}) = P(\\text{太郎}) \\times P(\\text{花子}) = \\frac{4}{10} \\times \\frac{4}{10} = \\frac{16}{100} = \\frac{4}{25}\\]
<br>

<b>【問題2】くじを戻さない場合、太郎と花子が両方当たる確率は？</b><br>
<br>

戻さないので従属（乗法定理を使う）：<br>
• 太郎が当たる確率：\\(P(A) = \\frac{4}{10}\\)<br>
• 太郎が当たった後、花子が当たる確率：\\(P(B|A) = \\frac{3}{9}\\)<br>
<br>

\\[P(A \\cap B) = \\frac{4}{10} \\times \\frac{3}{9} = \\frac{12}{90} = \\frac{2}{15}\\]
<br>

→ 戻さない場合の方が確率が低い<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 独立事象：P(A∩B) = P(A)×P(B)<br>
• 従属事象：P(A∩B) = P(A)×P(B|A) （乗法定理）<br>
• 非復元抽出（戻さない）→ 従属事象<br>
• 復元抽出（戻す）→ 独立事象<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「10-3. 乗法定理」<br>
https://bellcurve.jp/statistics/course/6442.html<br>
計算例は検証スクリプトprobability_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'multiplication-theorem']
    },

    # カード7: 期待値
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【確率】期待値とは何か？どのように計算するのか？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
期待値は「1回の試行で得られる値の平均値」。<br>
得られうるすべての値とそれが起こる確率の積を合計したもの。<br>
<br>

<b>公式:</b><br>
確率変数Xがとりうる値を \\(x_1, x_2, \\ldots, x_n\\)、<br>
それぞれの確率を \\(p_1, p_2, \\ldots, p_n\\) とするとき：<br>
\\[E(X) = \\sum_{i=1}^{n} p_i x_i = p_1 x_1 + p_2 x_2 + \\cdots + p_n x_n\\]
<br>

<hr>

<b>具体例1: サイコロの目の期待値</b><br>
<br>

各目（1〜6）が出る確率は \\(\\frac{1}{6}\\)：<br>
\\[E(X) = 1 \\times \\frac{1}{6} + 2 \\times \\frac{1}{6} + \\cdots + 6 \\times \\frac{1}{6}\\]
\\[= \\frac{1+2+3+4+5+6}{6} = \\frac{21}{6} = 3.5\\]
<br>

→ 何回か投げると1回当たりの平均が3.5になると期待できる<br>
<br>

<b>具体例2: 金銭ゲーム</b><br>
<br>

<b>【問題】サイコロの目×100円がもらえるゲーム。期待値は？</b><br>
<br>

\\[E(X) = 100 \\times \\frac{1}{6} + 200 \\times \\frac{1}{6} + \\cdots + 600 \\times \\frac{1}{6}\\]
\\[= 100 \\times 3.5 = 350\\text{円}\\]
<br>

<b>具体例3: コイントス（公平なゲーム）</b><br>
<br>

<b>【問題】表で100円獲得、裏で100円支払う。期待値は？</b><br>
<br>

\\[E(X) = 100 \\times \\frac{1}{2} + (-100) \\times \\frac{1}{2} = 0\\text{円}\\]
<br>

→ 期待値が0なので、長期的には儲けも損もないゲーム<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• 期待値 ≠ 1回で確実に得られる値<br>
• 期待値 = 長期的な平均値<br>
• 期待値は実際には出ない値になることもある（例：3.5）<br>
• 期待値の性質：E(aX+b) = aE(X) + b<br>
• 分散の公式：V(X) = E(X²) - {E(X)}²<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「9-7. 期待値」<br>
https://bellcurve.jp/statistics/course/6349.html<br>
統計WEB「12-3. 確率変数の期待値」<br>
https://bellcurve.jp/statistics/course/6712.html<br>
計算例は検証スクリプトprobability_calculation_check.pyで検算済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'probability', 'expectation', 'expected-value']
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
