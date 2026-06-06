#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
条件付き確率とベイズの定理の計算例を検証するスクリプト
"""

print("=" * 60)
print("1. 条件付き確率の計算例")
print("=" * 60)

# 例1: 色付き玉の問題
print("【例1】赤玉3個（「1」が2個、「2」が1個）と白玉3個")
print("赤色が出た条件下で「1」である確率は？")
print()

# 確率を計算
prob_red = 3/6  # 赤玉が出る確率
prob_1_and_red = 2/6  # 「1」かつ赤玉の確率
prob_1_given_red = prob_1_and_red / prob_red  # 条件付き確率

print(f"P(赤玉) = 3/6 = {prob_red:.4f}")
print(f"P(「1」∩赤玉) = 2/6 = {prob_1_and_red:.4f}")
print(f"P(「1」|赤玉) = {prob_1_and_red:.4f} ÷ {prob_red:.4f} = {prob_1_given_red:.4f} = 2/3")
print()

# 例2: サイコロ2回投げ
print("【例2】サイコロ2回投げ")
print("1回目が4の条件下で、合計が8以上となる確率は？")
print()

# 1回目が4の場合、2回目は4,5,6で合計8以上
prob_first_4 = 1/6
prob_sum_8_and_first_4 = 3/36  # (4,4), (4,5), (4,6)
prob_sum_8_given_first_4 = prob_sum_8_and_first_4 / prob_first_4

print(f"P(1回目が4) = 1/6 = {prob_first_4:.4f}")
print(f"P(合計≥8 ∩ 1回目4) = 3/36 = {prob_sum_8_and_first_4:.4f}")
print(f"P(合計≥8|1回目4) = {prob_sum_8_and_first_4:.4f} ÷ {prob_first_4:.4f} = {prob_sum_8_given_first_4:.4f} = 1/2")
print()

print("=" * 60)
print("2. ベイズの定理の計算例（工場の不良品問題）")
print("=" * 60)

# 工場XとYの電子部品生産
print("【問題】工場XとYが電子部品を生産")
print("・工場X：生産シェア60%、不良率2%")
print("・工場Y：生産シェア40%、不良率5%")
print("不良品が見つかったとき、工場Xの製品である確率は？")
print()

# 事前確率
prob_X = 0.60
prob_Y = 0.40

# 条件付き確率（尤度）
prob_defect_given_X = 0.02
prob_defect_given_Y = 0.05

# 全確率の公式：P(不良品)
prob_defect = prob_X * prob_defect_given_X + prob_Y * prob_defect_given_Y

# ベイズの定理：P(X|不良品)
prob_X_given_defect = (prob_X * prob_defect_given_X) / prob_defect

print("【ステップ1】事前確率")
print(f"P(X) = {prob_X}")
print(f"P(Y) = {prob_Y}")
print()

print("【ステップ2】条件付き確率（尤度）")
print(f"P(不良品|X) = {prob_defect_given_X}")
print(f"P(不良品|Y) = {prob_defect_given_Y}")
print()

print("【ステップ3】全確率の公式")
print(f"P(不良品) = P(X)×P(不良品|X) + P(Y)×P(不良品|Y)")
print(f"         = {prob_X}×{prob_defect_given_X} + {prob_Y}×{prob_defect_given_Y}")
print(f"         = {prob_X * prob_defect_given_X} + {prob_Y * prob_defect_given_Y}")
print(f"         = {prob_defect}")
print()

print("【ステップ4】ベイズの定理")
print(f"P(X|不良品) = P(X)×P(不良品|X) / P(不良品)")
print(f"            = {prob_X}×{prob_defect_given_X} / {prob_defect}")
print(f"            = {prob_X * prob_defect_given_X} / {prob_defect}")
print(f"            = {prob_X_given_defect:.4f} = 37.5%")
print()

print("【解釈】")
print(f"事前確率：工場Xの製品である確率 = {prob_X*100:.1f}%")
print(f"事後確率：不良品が工場Xの製品である確率 = {prob_X_given_defect*100:.1f}%")
print("→ 不良率が低い工場Xより、不良率が高い工場Yの可能性が相対的に高まった")
print()

print("=" * 60)
print("3. ベイズの定理の計算例（病気検査問題）")
print("=" * 60)

# 病気検査の問題
print("【問題】日本人の0.01%が罹患する病気の検査")
print("・感度（患者→陽性）：95%")
print("・特異度（非患者→陰性）：80%")
print("陽性判定が出たとき、実際に病気である確率は？")
print()

# 事前確率
prob_disease = 0.0001  # 0.01%
prob_healthy = 1 - prob_disease

# 条件付き確率
prob_positive_given_disease = 0.95  # 感度
prob_negative_given_healthy = 0.80  # 特異度
prob_positive_given_healthy = 1 - prob_negative_given_healthy  # 偽陽性率

# 全確率の公式：P(陽性)
prob_positive = (prob_disease * prob_positive_given_disease +
                 prob_healthy * prob_positive_given_healthy)

# ベイズの定理：P(病気|陽性)
prob_disease_given_positive = (prob_disease * prob_positive_given_disease) / prob_positive

print("【ステップ1】事前確率")
print(f"P(病気) = {prob_disease} = 0.01%")
print(f"P(健康) = {prob_healthy} = 99.99%")
print()

print("【ステップ2】条件付き確率")
print(f"P(陽性|病気) = {prob_positive_given_disease} （感度）")
print(f"P(陽性|健康) = {prob_positive_given_healthy} （偽陽性率）")
print()

print("【ステップ3】全確率の公式")
print(f"P(陽性) = P(病気)×P(陽性|病気) + P(健康)×P(陽性|健康)")
print(f"        = {prob_disease}×{prob_positive_given_disease} + {prob_healthy}×{prob_positive_given_healthy}")
print(f"        = {prob_disease * prob_positive_given_disease:.6f} + {prob_healthy * prob_positive_given_healthy:.6f}")
print(f"        = {prob_positive:.6f}")
print()

print("【ステップ4】ベイズの定理")
print(f"P(病気|陽性) = P(病気)×P(陽性|病気) / P(陽性)")
print(f"             = {prob_disease}×{prob_positive_given_disease} / {prob_positive:.6f}")
print(f"             = {prob_disease * prob_positive_given_disease:.6f} / {prob_positive:.6f}")
print(f"             = {prob_disease_given_positive:.6f} = {prob_disease_given_positive*100:.4f}%")
print()

print("【解釈】")
print("陽性判定が出ても、実際に病気である確率はわずか0.0475%")
print("→ 病気が非常に稀なため、偽陽性の影響が大きい")
print()

print("=" * 60)
print("すべての計算が検証されました")
print("=" * 60)
