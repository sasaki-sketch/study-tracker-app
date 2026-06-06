#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
表示問題修正版カードの再インポート
- 既存の変数・尺度・変化率カードを削除
- 修正版カードを再インポート
"""

import json
import urllib.request
import subprocess
import sys


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


def get_cards_by_tags(deck_name, tags):
    """指定したタグを持つカードIDを取得"""
    query = f'deck:"{deck_name}" ('
    query += ' OR '.join([f'tag:{tag}' for tag in tags])
    query += ')'

    card_ids = invoke_anki('findCards', query=query)
    return card_ids if card_ids else []


def get_card_info(card_ids):
    """カードの詳細情報を取得"""
    if not card_ids:
        return []

    cards_info = invoke_anki('cardsInfo', cards=card_ids)
    return cards_info if cards_info else []


def count_cards_by_tag(deck_name, tag):
    """特定タグのカード数を数える"""
    query = f'deck:"{deck_name}" tag:{tag}'
    card_ids = invoke_anki('findCards', query=query)
    return len(card_ids) if card_ids else 0


def main():
    """メイン実行"""
    print("=" * 70)
    print("表示問題修正版カードの再インポート")
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

    # 現在のカード数を確認
    print("📊 削除前のカード構成:")
    print()

    variables_count = count_cards_by_tag(deck_name, "variables")
    scales_count = count_cards_by_tag(deck_name, "measurement-scales")
    rate_count = count_cards_by_tag(deck_name, "rate-of-change")
    greek_count = count_cards_by_tag(deck_name, "priority-S")

    print(f"  変数カード: {variables_count}枚")
    print(f"  尺度カード: {scales_count}枚")
    print(f"  変化率カード: {rate_count}枚")
    print(f"  ギリシャ文字 (Priority-S): {greek_count}枚")
    print()

    total_before = variables_count + scales_count + rate_count + greek_count

    # 削除対象のカードを取得
    print("🗑️  修正対象カードを削除中...")
    print()

    # 変数・尺度・変化率カードを削除
    tags_to_delete = ['variables', 'measurement-scales', 'rate-of-change']

    cards_to_delete = get_cards_by_tags(deck_name, tags_to_delete)

    if not cards_to_delete:
        print("⚠️  削除対象のカードが見つかりませんでした")
    else:
        print(f"  削除対象: {len(cards_to_delete)}枚")

        # カード情報を取得
        cards_info = get_card_info(cards_to_delete)

        # ノートIDを取得
        note_ids = list(set([card['note'] for card in cards_info]))

        print(f"  {len(note_ids)}個のノートを削除中...")

        result = invoke_anki('deleteNotes', notes=note_ids)

        if result is None:
            # 1つずつ削除を試みる
            print("  ⚠️  一括削除に失敗。1つずつ削除を試みます...")
            deleted_count = 0
            for note_id in note_ids:
                r = invoke_anki('deleteNotes', notes=[note_id])
                if r is not None:
                    deleted_count += 1
                    if deleted_count % 5 == 0:
                        print(f"    ✓ {deleted_count}/{len(note_ids)}個削除完了...")

            if deleted_count > 0:
                print(f"  ✅ {deleted_count}個のノートを削除しました")
            else:
                print("  ❌ 削除に失敗しました")
                return
        else:
            print(f"  ✅ 削除完了!")

    print()

    # 修正版カードをインポート
    print("📥 修正版カードをインポート中...")
    print()

    scripts = [
        ('explanatory_response_variables_anki.py', '変数カード', 5),
        ('measurement_scales_anki.py', '尺度カード', 10),
        ('rate_of_change_anki.py', '変化率カード', 10)
    ]

    total_added = 0

    for script_name, description, expected_count in scripts:
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
                total_added += expected_count
            else:
                print(f"    ⚠️  {description}の追加に問題がありました")
                print(f"    エラー: {result.stderr[:200]}")

        except Exception as e:
            print(f"    ❌ {description}の実行に失敗: {e}")

    print()

    # 最終確認
    print("📊 再インポート後のカード構成:")
    print()

    variables_after = count_cards_by_tag(deck_name, "variables")
    scales_after = count_cards_by_tag(deck_name, "measurement-scales")
    rate_after = count_cards_by_tag(deck_name, "rate-of-change")
    greek_after = count_cards_by_tag(deck_name, "priority-S")

    print(f"  変数カード: {variables_after}枚")
    print(f"  尺度カード: {scales_after}枚")
    print(f"  変化率カード: {rate_after}枚")
    print(f"  ギリシャ文字 (Priority-S): {greek_after}枚")
    print()

    total_after = variables_after + scales_after + rate_after + greek_after

    print("=" * 70)
    print("✨ 再インポート完了!")
    print("=" * 70)
    print()

    print(f"📊 結果:")
    print(f"  削除: {variables_count + scales_count + rate_count}枚")
    print(f"  追加: {variables_after + scales_after + rate_after}枚")
    print(f"  総カード数: {total_before}枚 → {total_after}枚")
    print()

    print(f"🎨 修正内容:")
    print(f"  ✅ インラインカラースタイル → CSSクラスに変更")
    print(f"  ✅ グレーテキスト (#666 → #4b5563) でコントラスト改善")
    print(f"  ✅ 色付きテキストのダークモード対応")
    print(f"  ✅ ネストされたタグの色継承問題を解決")
    print()

    print(f"🔍 Ankiで確認:")
    print(f"  deck:\"{deck_name}\" で全カードを確認")
    print(f"  tag:variables で変数カードのみ")
    print(f"  tag:measurement-scales で尺度カードのみ")
    print(f"  tag:rate-of-change で変化率カードのみ")
    print()

    print(f"💡 注意:")
    print(f"  学習履歴はリセットされています")
    print(f"  ギリシャ文字カード ({greek_after}枚) は影響を受けていません")
    print()


if __name__ == "__main__":
    main()
