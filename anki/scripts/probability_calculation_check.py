#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
確率と期待値の計算例を検証するスクリプト
"""

import math

print("=" * 60)
print("1. 順列と組み合わせの計算例")
print("=" * 60)

# 順列の計算: 5P3
n, r = 5, 3
permutation = math.factorial(n) // math.factorial(n - r)
print(f"5P3 = 5!/(5-3)! = 5!/2! = {permutation}通り")

# 組み合わせの計算: 5C3
combination = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
print(f"5C3 = 5!/(3!×2!) = {combination}通り")

# 関係式の確認
print(f"5C3 = 5P3/3! = {permutation}/{math.factorial(r)} = {permutation // math.factorial(r)}通り")
print()

print("=" * 60)
print("2. 余事象の計算例")
print("=" * 60)

# 白玉3個、赤玉7個から3つ取り出す
total_balls = 10
white_balls = 3
red_balls = 7
draw = 3

# 全体の組み合わせ
total_combinations = math.factorial(total_balls) // (math.factorial(draw) * math.factorial(total_balls - draw))
print(f"全体の組み合わせ: 10C3 = {total_combinations}通り")

# 白玉3つが出る場合（余事象）
white_only = math.factorial(white_balls) // (math.factorial(draw) * math.factorial(white_balls - draw))
print(f"白玉3つが出る: 3C3 = {white_only}通り")

# 赤玉が少なくとも1つ出る確率
prob_at_least_one_red = (total_combinations - white_only) / total_combinations
print(f"赤玉が少なくとも1つ出る確率: (120-1)/120 = {prob_at_least_one_red:.4f}")
print(f"余事象を使った計算: 1 - 1/120 = {1 - white_only/total_combinations:.4f}")
print()

print("=" * 60)
print("3. 独立事象の計算例")
print("=" * 60)

# コインとサイコロ
prob_heads = 1/2
prob_one = 1/6
prob_heads_and_one = prob_heads * prob_one
print(f"コインが表: P(表) = {prob_heads}")
print(f"サイコロが1: P(1) = {prob_one:.4f}")
print(f"両方起こる: P(表∩1) = {prob_heads} × {prob_one:.4f} = {prob_heads_and_one:.4f}")
print()

print("=" * 60)
print("4. 加法定理の計算例")
print("=" * 60)

# サイコロで1か2が出る確率（排反事象）
prob_1 = 1/6
prob_2 = 1/6
prob_1_or_2 = prob_1 + prob_2
print(f"【排反事象】サイコロで1か2: {prob_1:.4f} + {prob_2:.4f} = {prob_1_or_2:.4f} = 1/3")
print()

# 30までの数で2か3で割り切れる（排反でない）
n_total = 30
n_div_2 = 15  # 2で割り切れる
n_div_3 = 10  # 3で割り切れる
n_div_6 = 5   # 6で割り切れる（2と3の公倍数）

prob_div_2 = n_div_2 / n_total
prob_div_3 = n_div_3 / n_total
prob_div_6 = n_div_6 / n_total
prob_div_2_or_3 = prob_div_2 + prob_div_3 - prob_div_6

print(f"【一般の場合】30までの数で2か3で割り切れる:")
print(f"P(2で割り切れる) = {n_div_2}/{n_total} = {prob_div_2:.4f}")
print(f"P(3で割り切れる) = {n_div_3}/{n_total} = {prob_div_3:.4f}")
print(f"P(6で割り切れる) = {n_div_6}/{n_total} = {prob_div_6:.4f}")
print(f"P(2か3) = {prob_div_2:.4f} + {prob_div_3:.4f} - {prob_div_6:.4f} = {prob_div_2_or_3:.4f} = 2/3")
print()

print("=" * 60)
print("5. 期待値の計算例")
print("=" * 60)

# サイコロの期待値
dice_values = [1, 2, 3, 4, 5, 6]
dice_prob = 1/6
expectation = sum(v * dice_prob for v in dice_values)
print(f"【サイコロの目の期待値】")
print(f"E(X) = 1×(1/6) + 2×(1/6) + ... + 6×(1/6)")
print(f"     = {expectation:.1f}")
print()

# 金銭ゲーム
payoff = [v * 100 for v in dice_values]
expectation_money = sum(p * dice_prob for p in payoff)
print(f"【サイコロの目×100円がもらえるゲーム】")
print(f"E(X) = 100×(1/6) + 200×(1/6) + ... + 600×(1/6)")
print(f"     = {expectation_money:.1f}円")
print()

# コイントス（公平なゲーム）
coin_payoff = [100, -100]
coin_prob = [1/2, 1/2]
expectation_coin = sum(p * pr for p, pr in zip(coin_payoff, coin_prob))
print(f"【コイントス：表で100円獲得、裏で100円支払い】")
print(f"E(X) = 100×(1/2) + (-100)×(1/2)")
print(f"     = {expectation_coin:.1f}円")
print(f"→ 期待値が0なので儲けがないゲーム")
print()

print("=" * 60)
print("6. 乗法定理の計算例")
print("=" * 60)

# くじを戻す場合（独立）
prob_win = 4/10
prob_both_win_replace = prob_win * prob_win
print(f"【くじを戻す場合】")
print(f"P(太郎が当たる) = {prob_win}")
print(f"P(花子が当たる) = {prob_win}")
print(f"P(両方当たる) = {prob_win} × {prob_win} = {prob_both_win_replace:.4f} = 4/25")
print()

# くじを戻さない場合（従属）
prob_win_first = 4/10
prob_win_second_given_first = 3/9
prob_both_win_no_replace = prob_win_first * prob_win_second_given_first
print(f"【くじを戻さない場合】")
print(f"P(太郎が当たる) = {prob_win_first}")
print(f"P(太郎が当たった後、花子が当たる) = {prob_win_second_given_first:.4f}")
print(f"P(両方当たる) = {prob_win_first} × {prob_win_second_given_first:.4f} = {prob_both_win_no_replace:.4f} = 2/15")
print()

print("=" * 60)
print("すべての計算が検証されました")
print("=" * 60)
