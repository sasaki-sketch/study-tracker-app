#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
日本語の前のバックスラッシュを削除
"""

import re

files_to_fix = [
    '/Users/sasaki/box_plot_stem_leaf_verified.py',
    '/Users/sasaki/probability_events_verified.py',
    '/Users/sasaki/variance_standard_deviation_verified.py'
]

def fix_japanese_backslash(file_path):
    """ファイル内の日本語前のバックスラッシュを削除"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 日本語文字（ひらがな、カタカナ、漢字）の前のバックスラッシュを削除
    # \\範囲 → 範囲, \\最大値 → 最大値 など
    content = re.sub(r'\\([ぁ-んァ-ヶー一-龠])', r'\1', content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # どの文字列が修正されたかを表示
        import os
        print(f"✅ 修正: {os.path.basename(file_path)}")

        # 修正箇所を抽出
        original_lines = original_content.split('\n')
        new_lines = content.split('\n')

        changes = []
        for i, (old, new) in enumerate(zip(original_lines, new_lines), 1):
            if old != new:
                # 変更部分を抽出
                old_matches = re.findall(r'\\([ぁ-んァ-ヶー一-龠]+)', old)
                if old_matches:
                    changes.extend(old_matches)

        if changes:
            unique_changes = list(set(changes))
            print(f"   修正した日本語: {', '.join(unique_changes[:10])}")
            if len(unique_changes) > 10:
                print(f"   (他 {len(unique_changes) - 10}件)")

        return True
    else:
        import os
        print(f"✓  変更なし: {os.path.basename(file_path)}")
        return False

def main():
    print("=" * 70)
    print("日本語バックスラッシュ修正")
    print("=" * 70)
    print()

    fixed = 0
    for file_path in files_to_fix:
        if fix_japanese_backslash(file_path):
            fixed += 1

    print()
    print("=" * 70)
    print(f"✨ 修正完了: {fixed}ファイル")
    print("=" * 70)

if __name__ == "__main__":
    main()
