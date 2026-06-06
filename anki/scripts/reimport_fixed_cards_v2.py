#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
表示問題修正版カードの再インポート v2
- 既存カードは手動削除してもらう方式に変更
- 修正版カードを追加するのみ
"""

import subprocess
import sys


def main():
    """メイン実行"""
    print("=" * 70)
    print("表示問題修正版カードの追加")
    print("=" * 70)
    print()

    print("⚠️  実行前の準備:")
    print()
    print("Ankiブラウザで以下のクエリを使用して、既存カードを手動で削除してください:")
    print()
    print("  deck:\"Greek Letters & Statistics\" (tag:variables OR tag:measurement-scales OR tag:rate-of-change)")
    print()
    print("削除手順:")
    print("  1. Ankiブラウザを開く")
    print("  2. 上記のクエリを検索ボックスに貼り付け")
    print("  3. 表示された25枚を全選択 (Cmd+A)")
    print("  4. Delete キーで削除")
    print()

    response = input("既存カードの削除は完了しましたか? (y/n): ")

    if response.lower() != 'y':
        print()
        print("削除完了後に再度このスクリプトを実行してください")
        return

    print()
    print("📥 修正版カードをインポート中...")
    print()

    scripts = [
        ('explanatory_response_variables_anki.py', '変数カード (5枚)'),
        ('measurement_scales_anki.py', '尺度カード (10枚)'),
        ('rate_of_change_anki.py', '変化率カード (10枚)')
    ]

    for script_name, description in scripts:
        print(f"  🔄 {description}を追加中...")

        try:
            result = subprocess.run(
                ['python3', script_name],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                print(f"    ✅ {description}追加完了")
            else:
                print(f"    ⚠️  {description}の追加に問題がありました")
                if result.stderr:
                    print(f"    エラー: {result.stderr[:300]}")

        except Exception as e:
            print(f"    ❌ {description}の実行に失敗: {e}")

    print()
    print("=" * 70)
    print("✨ 修正版カードの追加完了!")
    print("=" * 70)
    print()

    print(f"🎨 修正内容:")
    print(f"  ✅ インラインカラースタイル → CSSクラスに変更")
    print(f"  ✅ グレーテキスト (#666 → #4b5563) でコントラスト改善")
    print(f"  ✅ 色付きテキストのダークモード対応")
    print(f"  ✅ ネストされたタグの色継承問題を解決")
    print()

    print(f"🔍 Ankiで確認:")
    print(f"  deck:\"Greek Letters & Statistics\" で全カードを確認")
    print(f"  総カード数: 43枚 (ギリシャ文字18枚 + 統計概念25枚)")
    print()

    print(f"📌 注意:")
    print(f"  修正されたカードの学習履歴はリセットされています")
    print(f"  ギリシャ文字カードは影響を受けていません")
    print()


if __name__ == "__main__":
    main()
