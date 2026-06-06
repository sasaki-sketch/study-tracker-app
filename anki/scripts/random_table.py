#!/usr/bin/env python3
"""
Random Number Table Generator
乱数表生成プログラム

Usage: python3 random_table.py
"""

import random

# Your specifications (あなたの仕様)
rows = 100
columns = 5
digits = 1  # 0-9

# Create random number table (sampling with replacement)
# 乱数表を作成（復元抽出）

print("=" * 30)
print("Random Number Table")
print(f"({rows} rows × {columns} columns)")
print("Sampling with replacement")
print("=" * 30)
print()

for i in range(rows):
    row = [random.randint(0, 9) for _ in range(columns)]
    print(' '.join(map(str, row)))

print()
print("=" * 30)
print("Table generation complete!")
print("=" * 30)
