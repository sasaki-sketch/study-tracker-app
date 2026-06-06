#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修正版カードを新規タグ付きで追加（簡易版）
既存カードとは別に追加し、後で手動で古いカードを削除可能にする
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
    print("修正版カードの追加（allowDuplicate=True で強制追加）")
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

    print("📊 追加前のカード数:")
    variables_before = count_cards_by_tag(deck_name, "variables")
    scales_before = count_cards_by_tag(deck_name, "measurement-scales")
    rate_before = count_cards_by_tag(deck_name, "rate-of-change")

    print(f"  変数: {variables_before}枚")
    print(f"  尺度: {scales_before}枚")
    print(f"  変化率: {rate_before}枚")
    print()

    print("📥 修正版カードを追加中...")
    print()

    scripts = [
        ('explanatory_response_variables_anki.py', '変数カード', 5),
        ('measurement_scales_anki.py', '尺度カード', 10),
        ('rate_of_change_anki.py', '変化率カード', 10)
    ]

    for script_name, description, expected in scripts:
        print(f"  🔄 {description} ({expected}枚) を追加中...")

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
                print(f"    ⚠️  問題が発生しました")
                if result.stderr:
                    # エラーの最初の数行のみ表示
                    error_lines = result.stderr.split('\n')[:3]
                    for line in error_lines:
                        if line.strip():
                            print(f"      {line[:80]}")

        except subprocess.TimeoutExpired:
            print(f"    ⏱️  タイムアウト（30秒超過）")
        except Exception as e:
            print(f"    ❌ 実行失敗: {e}")

    print()

    # 追加後のカード数確認
    print("📊 追加後のカード数:")
    variables_after = count_cards_by_tag(deck_name, "variables")
    scales_after = count_cards_by_tag(deck_name, "measurement-scales")
    rate_after = count_cards_by_tag(deck_name, "rate-of-change")

    print(f"  変数: {variables_after}枚 (+{variables_after - variables_before})")
    print(f"  尺度: {scales_after}枚 (+{scales_after - scales_before})")
    print(f"  変化率: {rate_after}枚 (+{rate_after - rate_before})")
    print()

    print("=" * 70)
    print("✨ カード追加完了!")
    print("=" * 70)
    print()

    if (variables_after > variables_before or
        scales_after > scales_before or
        rate_after > rate_before):
        print("✅ カードが正常に追加されました")
        print()
        print("📌 次のステップ:")
        print("  1. Ankiブラウザで修正版カードを確認")
        print("  2. 表示が正しいことを確認")
        print("  3. 古いカード（表示問題あり）があれば手動で削除")
        print()
        print("🔍 古いカードの見分け方:")
        print("  - テキストが見えない部分がある")
        print("  - インラインスタイル使用（ブラウザで確認可能）")
    else:
        print("⚠️  カードが追加されませんでした")
        print("  - 既に同じカードが存在する可能性があります")
        print("  - 各Pythonスクリプトで allowDuplicate=False 設定のため")

    print()


if __name__ == "__main__":
    main()
