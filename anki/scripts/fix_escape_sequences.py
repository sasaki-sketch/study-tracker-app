#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全Ankiカード生成ファイルのエスケープシーケンスエラーを修正

修正内容:
1. \right → \\right (Pythonの\rを防ぐ)
2. \left → \\left (Pythonの\lを防ぐ)
3. 日本語文字の前のバックスラッシュを削除
"""

import os
import re

# 修正対象ファイル
files_to_fix = [
    '/Users/sasaki/logarithm_properties_verified.py',
    '/Users/sasaki/variance_standard_deviation_verified.py',
    '/Users/sasaki/counting_principles_verified.py',
    '/Users/sasaki/probability_events_verified.py',
    '/Users/sasaki/box_plot_stem_leaf_verified.py',
    '/Users/sasaki/skewness_kurtosis_verified.py',
    '/Users/sasaki/measures_of_central_tendency_verified.py',
    '/Users/sasaki/frequency_distribution_verified.py',
    '/Users/sasaki/powers_of_two_verified.py',
    '/Users/sasaki/lorenz_gini_verified.py',
    '/Users/sasaki/sturges_formula_verified.py',
    '/Users/sasaki/squares_11_to_20_verified.py',
    '/Users/sasaki/geometric_mean_verified.py',
    '/Users/sasaki/greek_letters_verified.py',
    '/Users/sasaki/harmonic_mean_verified.py',
    '/Users/sasaki/trimmed_mean_verified.py',
    '/Users/sasaki/additional_statistics_concepts_verified.py'
]

def fix_file(file_path):
    """ファイルのエスケープシーケンスを修正"""

    if not os.path.exists(file_path):
        print(f"⚠️  スキップ: {os.path.basename(file_path)} (存在しません)")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. \right → \\right (既に\\rightの場合は触らない)
    # 負の後読みで、直前に\がない\rightを探す
    content = re.sub(r'(?<!\\)\\right', r'\\\\right', content)

    # 2. \left → \\left (既に\\leftの場合は触らない)
    content = re.sub(r'(?<!\\)\\left', r'\\\\left', content)

    # 3. 日本語文字の前のバックスラッシュを削除
    # \白 → 白, \第 → 第 など
    content = re.sub(r'\\([ぁ-んァ-ヶー一-龠]+)', r'\1', content)

    # 変更があった場合のみ保存
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 修正完了: {os.path.basename(file_path)}")
        return True
    else:
        print(f"✓  変更なし: {os.path.basename(file_path)}")
        return False

def main():
    print("=" * 70)
    print("エスケープシーケンスエラー修正スクリプト")
    print("=" * 70)
    print()

    fixed_count = 0
    for file_path in files_to_fix:
        if fix_file(file_path):
            fixed_count += 1

    print()
    print("=" * 70)
    print(f"✨ 修正完了: {fixed_count}ファイル")
    print("=" * 70)

if __name__ == "__main__":
    main()
