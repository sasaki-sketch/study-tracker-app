#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
尖度の計算例を検証するスクリプト
"""

import numpy as np

# 例1: 簡単なデータ（5個のデータ）
data1 = np.array([1, 2, 3, 4, 5])
n1 = len(data1)
mean1 = np.mean(data1)
std1 = np.std(data1, ddof=0)  # nで割る標準偏差（統計検定2級の定義）

# 手計算での尖度（過剰尖度）
numerator1 = np.sum((data1 - mean1)**4) / n1
denominator1 = std1**4
kurtosis1_manual = numerator1 / denominator1 - 3

# numpyでの検証
kurtosis1_fisher = np.sum((data1 - mean1)**4) / (n1 * std1**4) - 3

print("=" * 60)
print("例1: データ = [1, 2, 3, 4, 5]")
print("=" * 60)
print(f"平均: {mean1:.4f}")
print(f"標準偏差（nで割る）: {std1:.4f}")
print(f"手計算での尖度: {kurtosis1_manual:.4f}")
print(f"Fisher定義での尖度: {kurtosis1_fisher:.4f}")
print()

# 中間計算を表示
print("【詳細計算過程】")
print(f"各データ - 平均: {data1 - mean1}")
print(f"(データ - 平均)^4: {(data1 - mean1)**4}")
print(f"分子 Σ(xi-x̄)^4 / n: {numerator1:.4f}")
print(f"分母 s^4: {denominator1:.4f}")
print(f"μ4/σ4: {numerator1/denominator1:.4f}")
print(f"μ4/σ4 - 3 = {numerator1/denominator1 - 3:.4f}")
print()

# 例2: 正規分布に近いデータ
np.random.seed(42)
data2 = np.random.normal(0, 1, 1000)
n2 = len(data2)
mean2 = np.mean(data2)
std2 = np.std(data2, ddof=0)  # nで割る標準偏差
kurtosis2 = np.sum((data2 - mean2)**4) / (n2 * std2**4) - 3

print("=" * 60)
print("例2: 正規分布（N=1000）")
print("=" * 60)
print(f"平均: {mean2:.4f}")
print(f"標準偏差（nで割る）: {std2:.4f}")
print(f"尖度: {kurtosis2:.4f}")
print("→ 正規分布なので尖度≈0となるはず")
print()

# 例3: 一様分布（平坦な分布）
np.random.seed(42)
data3 = np.random.uniform(0, 1, 1000)
n3 = len(data3)
mean3 = np.mean(data3)
std3 = np.std(data3, ddof=0)  # nで割る標準偏差
kurtosis3 = np.sum((data3 - mean3)**4) / (n3 * std3**4) - 3

print("=" * 60)
print("例3: 一様分布（N=1000）")
print("=" * 60)
print(f"平均: {mean3:.4f}")
print(f"標準偏差（nで割る）: {std3:.4f}")
print(f"尖度: {kurtosis3:.4f}")
print("→ 一様分布なので尖度<0（平坦）となるはず")
print()

# 理論値との比較
print("=" * 60)
print("理論値との比較")
print("=" * 60)
print("一様分布U(0,1)の理論的尖度: -1.2")
print(f"計算結果: {kurtosis3:.4f}")
print()
