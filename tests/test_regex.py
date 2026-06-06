#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正規表現パターンのテスト
"""

import re

# 正しいケース（エラーでない）
correct = r'\[s^2 = \frac{1}{n-1}\left(\sum_{i=1}^n x_i^2 - n\bar{x}^2\right)\]'

# 間違ったケース（エラー）
broken = r'\[s^2 = \frac{1}{n-1} eft(\sum_{i=1}^n x_i^2 - n\bar{x}^2 ight)\]'

print("=" * 70)
print("正規表現テスト")
print("=" * 70)
print()

print("正しい文字列:")
print(correct)
print()

# パターン1: [^\\]ight\)
pattern1 = r'[^\\]ight\)'
match1 = re.search(pattern1, correct)
print(f"パターン1 r'[^\\\\]ight\\)': {match1 is not None}")
if match1:
    print(f"  マッチ: {match1.group()}")
print()

# パターン2: ' ight'
match2 = ' ight)' in correct
print(f"パターン2 ' ight)' in string: {match2}")
print()

print("-" * 70)
print()

print("間違った文字列:")
print(broken)
print()

match3 = re.search(pattern1, broken)
print(f"パターン1 r'[^\\\\]ight\\)': {match3 is not None}")
if match3:
    print(f"  マッチ: {match3.group()}")
print()

match4 = ' ight)' in broken
print(f"パターン2 ' ight)' in string: {match4}")
print()

print("=" * 70)
print("Actual card content check:")
print("=" * 70)

# これは実際にAnkiから取得した内容
actual_card = '\\[s^2 = \\frac{1}{n-1}\\left(\\sum_{i=1}^n x_i^2 - n\\bar{x}^2\\right)\\]'
print(f"Actual card: {actual_card}")
print()

match5 = re.search(r'[^\\]ight\)', actual_card)
print(f"Pattern match: {match5 is not None}")
if match5:
    print(f"  Matched: {repr(match5.group())}")
    print(f"  Position: {match5.span()}")
    print(f"  Context: ...{actual_card[match5.start()-5:match5.end()+5]}...")
