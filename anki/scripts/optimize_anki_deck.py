#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ankiデッキ最適化スクリプト - カード削減実行
ギリシャ文字カードを79枚 → 20枚に削減
"""

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


def get_cards_by_tags(deck_name, tags):
    """指定したタグを持つカードIDを取得"""
    query = f'deck:"{deck_name}" '
    query += ' OR '.join([f'tag:{tag}' for tag in tags])

    card_ids = invoke_anki('findCards', query=query)
    return card_ids if card_ids else []


def get_card_info(card_ids):
    """カードの詳細情報を取得"""
    if not card_ids:
        return []

    cards_info = invoke_anki('cardsInfo', cards=card_ids)
    return cards_info if cards_info else []


def delete_cards(card_ids):
    """カードを削除"""
    if not card_ids:
        print("削除するカードがありません")
        return 0

    result = invoke_anki('deleteNotes', notes=card_ids)
    return len(card_ids) if result is not None else 0


def count_cards_by_tag(deck_name, tag):
    """特定タグのカード数を数える"""
    query = f'deck:"{deck_name}" tag:{tag}'
    card_ids = invoke_anki('findCards', query=query)
    return len(card_ids) if card_ids else 0


def main():
    """メイン実行"""
    print("=" * 70)
    print("Ankiデッキ最適化 - カード削減実行")
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
    print("📊 現在のカード構成:")
    print()

    priority_s = count_cards_by_tag(deck_name, "priority-S")
    priority_a = count_cards_by_tag(deck_name, "priority-A")
    priority_b = count_cards_by_tag(deck_name, "priority-B")
    priority_c = count_cards_by_tag(deck_name, "priority-C")
    order_mem = count_cards_by_tag(deck_name, "order-memorization")
    rate = count_cards_by_tag(deck_name, "rate-of-change")
    scales = count_cards_by_tag(deck_name, "measurement-scales")
    variables = count_cards_by_tag(deck_name, "variables")

    print(f"  ギリシャ文字 (Priority-S): {priority_s}枚")
    print(f"  ギリシャ文字 (Priority-A): {priority_a}枚")
    print(f"  ギリシャ文字 (Priority-B): {priority_b}枚")
    print(f"  ギリシャ文字 (Priority-C): {priority_c}枚")
    print(f"  順番記憶カード: {order_mem}枚")
    print(f"  変化率カード: {rate}枚")
    print(f"  尺度カード: {scales}枚")
    print(f"  変数カード: {variables}枚")

    total_before = priority_s + priority_a + priority_b + priority_c + order_mem + rate + scales + variables
    greek_before = priority_s + priority_a + priority_b + priority_c + order_mem

    print()
    print(f"  📈 合計: {total_before}枚")
    print(f"  📈 ギリシャ文字関連: {greek_before}枚")
    print()

    # 削除対象のカードを取得
    print("🗑️  削除対象カードを特定中...")
    print()

    # Priority-B, Priority-C, 順番記憶カードを削除
    tags_to_delete = ['priority-B', 'priority-C', 'order-memorization']

    cards_to_delete = get_cards_by_tags(deck_name, tags_to_delete)

    if not cards_to_delete:
        print("⚠️  削除対象のカードが見つかりませんでした")
        return

    print(f"  削除対象: {len(cards_to_delete)}枚")
    print(f"    - Priority-B: {priority_b}枚")
    print(f"    - Priority-C: {priority_c}枚")
    print(f"    - 順番記憶: {order_mem}枚")
    print()

    # カード情報を取得して確認
    cards_info = get_card_info(cards_to_delete)

    print("削除するカードの一部を確認:")
    for i, card_info in enumerate(cards_info[:5], 1):
        tags = ' '.join(card_info.get('tags', []))
        print(f"  {i}. Tags: {tags}")

    if len(cards_info) > 5:
        print(f"  ... 他{len(cards_info) - 5}枚")
    print()

    # 確認
    print("⚠️  上記のカードを削除します。よろしいですか？")
    print("   (このスクリプトは確認なしで削除を実行します)")
    print()

    # ノートIDを取得（カードIDではなくノートIDで削除）
    note_ids = list(set([card['note'] for card in cards_info]))

    print(f"🗑️  {len(note_ids)}個のノートを削除中...")
    print(f"   デバッグ: 最初の5個のノートID: {note_ids[:5]}")
    print()

    # AnkiConnectのdeleteNotesは notes パラメータではなく、リストを直接渡す
    result = invoke_anki('deleteNotes', notes=note_ids)

    if result is None:
        # 別の方法を試す: 1つずつ削除
        print("⚠️  一括削除に失敗。1つずつ削除を試みます...")
        deleted_count = 0
        for note_id in note_ids:
            r = invoke_anki('deleteNotes', notes=[note_id])
            if r is not None:
                deleted_count += 1
                if deleted_count % 10 == 0:
                    print(f"  ✓ {deleted_count}/{len(note_ids)}個削除完了...")

        if deleted_count > 0:
            result = True  # 成功扱い
            print(f"✅ {deleted_count}個のノートを削除しました")
        else:
            result = None

    if result is not None:
        print(f"✅ 削除完了!")
        print()
    else:
        print("❌ 削除に失敗しました")
        return

    # 削除後のカード数を確認
    print("📊 削減後のカード構成:")
    print()

    priority_s_after = count_cards_by_tag(deck_name, "priority-S")
    priority_a_after = count_cards_by_tag(deck_name, "priority-A")
    priority_b_after = count_cards_by_tag(deck_name, "priority-B")
    priority_c_after = count_cards_by_tag(deck_name, "priority-C")
    order_mem_after = count_cards_by_tag(deck_name, "order-memorization")
    rate_after = count_cards_by_tag(deck_name, "rate-of-change")
    scales_after = count_cards_by_tag(deck_name, "measurement-scales")
    variables_after = count_cards_by_tag(deck_name, "variables")

    print(f"  ギリシャ文字 (Priority-S): {priority_s_after}枚")
    print(f"  ギリシャ文字 (Priority-A): {priority_a_after}枚")
    print(f"  ギリシャ文字 (Priority-B): {priority_b_after}枚")
    print(f"  ギリシャ文字 (Priority-C): {priority_c_after}枚")
    print(f"  順番記憶カード: {order_mem_after}枚")
    print(f"  変化率カード: {rate_after}枚")
    print(f"  尺度カード: {scales_after}枚")
    print(f"  変数カード: {variables_after}枚")

    total_after = priority_s_after + priority_a_after + priority_b_after + priority_c_after + order_mem_after + rate_after + scales_after + variables_after
    greek_after = priority_s_after + priority_a_after + priority_b_after + priority_c_after + order_mem_after

    print()
    print(f"  📈 合計: {total_after}枚")
    print(f"  📈 ギリシャ文字関連: {greek_after}枚")
    print()

    # サマリー
    print("=" * 70)
    print("✨ 最適化完了!")
    print("=" * 70)
    print()
    print(f"📊 削減結果:")
    print(f"  削減前: {total_before}枚 → 削減後: {total_after}枚")
    print(f"  削減数: {total_before - total_after}枚")
    print()
    print(f"🎯 ギリシャ文字カード:")
    print(f"  削減前: {greek_before}枚 → 削減後: {greek_after}枚")
    print(f"  削減率: {(greek_before - greek_after) / greek_before * 100:.1f}%")
    print()
    print(f"📚 最終構成:")
    print(f"  ギリシャ文字: {greek_after}枚 ({greek_after / total_after * 100:.1f}%)")
    print(f"  変化率: {rate_after}枚 ({rate_after / total_after * 100:.1f}%)")
    print(f"  尺度: {scales_after}枚 ({scales_after / total_after * 100:.1f}%)")
    print(f"  変数: {variables_after}枚 ({variables_after / total_after * 100:.1f}%)")
    print()
    print(f"🚀 次のステップ:")
    print(f"  1. Ankiで '{deck_name}' デッキを確認")
    print(f"  2. tag:priority-S で重要カードを確認")
    print(f"  3. 統計WEBのStep1に沿って新規カード作成")
    print()


if __name__ == "__main__":
    main()
