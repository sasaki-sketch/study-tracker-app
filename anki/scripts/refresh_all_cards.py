#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
シンプルなカード再インポート（インラインスタイル版）
"""

import subprocess
import json
import urllib.request


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


def count_cards_by_tag(deck_name, tag):
    """特定タグのカード数を数える"""
    query = f'deck:"{deck_name}" tag:{tag}'
    card_ids = invoke_anki('findCards', query=query)
    return len(card_ids) if card_ids else 0


def main():
    """メイン実行"""
    print("=" * 70)
    print("シンプルなカード再インポート（インラインスタイル版）")
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

    deck_name = "Greek Letters & Statistics"

    # 現在のカード数
    print("📊 現在のカード数:")
    variables = count_cards_by_tag(deck_name, "variables")
    scales = count_cards_by_tag(deck_name, "measurement-scales")
    rate = count_cards_by_tag(deck_name, "rate-of-change")

    print(f"  変数: {variables}枚")
    print(f"  尺度: {scales}枚")
    print(f"  変化率: {rate}枚")
    print()

    if variables + scales + rate == 0:
        print("⚠️  既存カードが見つかりません。新規追加のみ実行します。")
    else:
        print("⚠️  既存カードを手動で削除してください:")
        print()
        print("  Ankiブラウザで以下のクエリを実行:")
        print(f'  deck:"{deck_name}" (tag:variables OR tag:measurement-scales OR tag:rate-of-change)')
        print()
        print("  全選択 (Cmd+A) → Delete キー")
        print()

        response = input("削除完了しましたか? (y/n): ")
        if response.lower() != 'y':
            print("削除完了後に再度実行してください")
            return

    print()
    print("📥 修正版カード（インラインスタイル版）を追加中...")
    print()

    scripts = [
        ('explanatory_response_variables_anki.py', '変数', 5),
        ('measurement_scales_anki.py', '尺度', 10),
        ('rate_of_change_anki.py', '変化率', 10)
    ]

    for script_name, description, expected in scripts:
        print(f"  🔄 {description}カード ({expected}枚) 追加中...")

        try:
            result = subprocess.run(
                ['python3', script_name],
                capture_output=True,
                text=True,
                timeout=30,
                cwd='/Users/sasaki'
            )

            if result.returncode == 0:
                print(f"    ✅ 完了")
            else:
                print(f"    ⚠️  問題発生")

        except Exception as e:
            print(f"    ❌ エラー: {e}")

    print()

    # 最終確認
    print("📊 追加後のカード数:")
    variables_after = count_cards_by_tag(deck_name, "variables")
    scales_after = count_cards_by_tag(deck_name, "measurement-scales")
    rate_after = count_cards_by_tag(deck_name, "rate-of-change")

    print(f"  変数: {variables_after}枚")
    print(f"  尺度: {scales_after}枚")
    print(f"  変化率: {rate_after}枚")
    print()

    print("=" * 70)
    print("✨ 完了!")
    print("=" * 70)
    print()

    print("🎨 修正内容:")
    print("  ✅ CSSクラス廃止 → インラインスタイルに統一")
    print("  ✅ シンプルで確実な方法に変更")
    print("  ✅ CSS不要（HTMLだけで完結）")
    print()

    print("🔍 確認方法:")
    print("  Ankiブラウザで tag:variables を検索")
    print("  「説明変数と目的変数の違いは?」カードを開く")
    print()

    print("✅ 確認ポイント:")
    print("  - 「目的変数(Y)」が赤色")
    print("  - 「説明変数(X)」が青色")
    print("  - すべての色付きテキストが表示される")
    print()


if __name__ == "__main__":
    main()
