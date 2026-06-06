#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計学v2デッキへの完全移行スクリプト
1. 既存のv2デッキカードを全削除
2. 修正済みの全カードを再追加
"""

import json
import urllib.request
import subprocess
import glob


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
    print("統計学v2デッキへの完全移行")
    print("=" * 70)
    print()

    # Step 1: AnkiConnect接続確認
    print("🔌 AnkiConnectに接続中...")
    version = invoke_anki('version')
    if version is None:
        print("❌ Ankiが起動していないか、AnkiConnectがインストールされていません")
        return

    print(f"✅ AnkiConnect接続成功")
    print()

    # Step 2: 統計学v2デッキの既存カードを全削除
    print("🗑️  統計学v2デッキの既存カードを削除中...")
    note_ids = invoke_anki('findNotes', query='deck:統計学v2')

    if note_ids:
        print(f"   見つかったカード: {len(note_ids)}枚")
        delete_result = invoke_anki('deleteNotes', notes=note_ids)
        print(f"   ✅ {len(note_ids)}枚のカードを削除しました")
    else:
        print("   ℹ️  削除するカードはありませんでした")
    print()

    # Step 3: 全ての検証済みスクリプトを実行
    print("📝 修正済みカードを追加中...")
    print()

    verified_scripts = [
        'logarithm_properties_verified.py',
        'variance_standard_deviation_verified.py',
        'counting_principles_verified.py',
        'probability_events_verified.py',
        'box_plot_stem_leaf_verified.py',
        'skewness_kurtosis_verified.py',
        'measures_of_central_tendency_verified.py',
        'frequency_distribution_verified.py',
        'powers_of_two_verified.py',
        'lorenz_gini_verified.py',
        'sturges_formula_verified.py',
        'squares_11_to_20_verified.py',
        'geometric_mean_verified.py',
        'greek_letters_verified.py',
        'harmonic_mean_verified.py',
        'trimmed_mean_verified.py'
    ]

    total_added = 0
    for script_name in verified_scripts:
        script_path = f'/Users/sasaki/{script_name}'
        print(f"  🔄 実行中: {script_name}")

        try:
            result = subprocess.run(
                ['python3', script_path],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                # 出力から追加成功数を取得
                output_lines = result.stdout.split('\n')
                for line in output_lines:
                    if '追加成功:' in line:
                        # 例: "  ✅ 追加成功: 7枚"
                        parts = line.split(':')
                        if len(parts) >= 2:
                            count_str = parts[1].strip().replace('枚', '')
                            try:
                                count = int(count_str)
                                total_added += count
                            except:
                                pass
                print(f"     ✅ 完了")
            else:
                print(f"     ⚠️  エラー: {result.stderr[:100]}")
        except Exception as e:
            print(f"     ❌ 失敗: {e}")

    print()
    print("=" * 70)
    print("✨ 移行完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  🗑️  削除: {len(note_ids) if note_ids else 0}枚")
    print(f"  ✅ 追加: {total_added}枚（推定）")
    print()
    print("=" * 70)
    print("次のステップ:")
    print("=" * 70)
    print("  1. Ankiで統計学v2デッキを開く")
    print("  2. カードが正しく表示されることを確認")
    print("  3. 特に以下の点をチェック:")
    print("     - 数式が正しくレンダリングされている")
    print("     - \\text{} が表示されていない")
    print("     - 日本語が正しく表示されている")
    print("     - 表が正しく表示されている")
    print()


if __name__ == "__main__":
    main()
