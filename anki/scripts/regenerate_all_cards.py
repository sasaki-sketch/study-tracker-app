#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全カードを再生成（エラー修正版）
1. 統計学v2デッキを削除
2. 全75枚を再生成
"""

import json
import urllib.request
import subprocess
import os

def invoke_anki(action, **params):
    """AnkiConnectにリクエストを送信"""
    request_json = json.dumps({
        'action': action,
        'version': 6,
        'params': params
    }).encode('utf-8')

    try:
        response = urllib.request.urlopen(
            urllib.request.Request('http://localhost:8765', request_json)
        )
        result = json.loads(response.read().decode('utf-8'))

        if result['error']:
            raise Exception(f"AnkiConnect error: {result['error']}")

        return result['result']
    except Exception as e:
        print(f"❌ エラー: {e}")
        return None

def main():
    print("=" * 70)
    print("全カード再生成（エラー修正版）")
    print("=" * 70)
    print()

    # AnkiConnect接続確認
    print("🔌 AnkiConnectに接続中...")
    version = invoke_anki('version')
    if version is None:
        print("❌ Ankiが起動していないか、AnkiConnectがインストールされていません")
        return

    print(f"✅ AnkiConnect接続成功")
    print()

    # ステップ1: 統計学v2デッキを削除
    deck_name = "統計学v2"
    print(f"🗑️  デッキ削除中: {deck_name}")

    # デッキIDを取得
    deck_names = invoke_anki('deckNames')
    if deck_name in deck_names:
        # デッキ内の全ノートIDを取得
        note_ids = invoke_anki('findNotes', query=f'deck:"{deck_name}"')
        if note_ids:
            print(f"   削除対象: {len(note_ids)}枚")
            result = invoke_anki('deleteNotes', notes=note_ids)
            print(f"   ✅ {len(note_ids)}枚削除完了")
        else:
            print(f"   ℹ️  デッキは空です")
    else:
        print(f"   ℹ️  デッキが存在しません")

    print()

    # ステップ2: 全カード生成スクリプトを実行
    scripts = [
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

    print("📝 カード生成中...")
    print()

    total_added = 0
    for i, script in enumerate(scripts, 1):
        script_name = os.path.basename(script)
        print(f"[{i}/{len(scripts)}] {script_name}")

        result = subprocess.run(
            ['python3', script],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            # 出力から追加枚数を抽出
            output = result.stdout
            if '追加成功' in output:
                # 「✅ 追加成功: X枚」の形式から抽出
                import re
                match = re.search(r'追加成功:\s*(\d+)枚', output)
                if match:
                    count = int(match.group(1))
                    total_added += count
                    print(f"   ✅ {count}枚追加")
                else:
                    print(f"   ✅ 完了")
            else:
                print(f"   ✅ 完了")
        else:
            print(f"   ❌ エラー")
            print(result.stderr)

    print()
    print("=" * 70)
    print(f"✨ 全カード再生成完了！")
    print("=" * 70)
    print(f"📊 合計: {total_added}枚追加")
    print()

if __name__ == "__main__":
    main()
