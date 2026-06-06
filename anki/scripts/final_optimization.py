#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最終最適化 - Priority-Aも削除してPriority-Sのみに
目標: ギリシャ文字カード 33枚 → 18-20枚
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


def get_cards_by_tag(deck_name, tag):
    """指定したタグを持つカードIDを取得"""
    query = f'deck:"{deck_name}" tag:{tag}'
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
    print("最終最適化 - Priority-A削除（Priority-Sのみ残す）")
    print("=" * 70)
    print()

    deck_name = "Greek Letters & Statistics"

    # 現在の状態
    priority_s = count_cards_by_tag(deck_name, "priority-S")
    priority_a = count_cards_by_tag(deck_name, "priority-A")

    print(f"📊 現在のギリシャ文字カード:")
    print(f"  Priority-S: {priority_s}枚 (保持)")
    print(f"  Priority-A: {priority_a}枚 (削除対象)")
    print()

    # Priority-Aカードを取得
    cards_to_delete = get_cards_by_tag(deck_name, "priority-A")

    if not cards_to_delete:
        print("⚠️  削除対象のカードが見つかりませんでした")
        return

    print(f"🗑️  {len(cards_to_delete)}枚のPriority-Aカードを削除します")
    print()

    # カード情報を取得
    cards_info = get_card_info(cards_to_delete)

    # ノートIDを取得
    note_ids = list(set([card['note'] for card in cards_info]))

    print(f"削除対象: {len(note_ids)}個のノート")
    print()

    # 削除実行
    result = invoke_anki('deleteNotes', notes=note_ids)

    if result is None:
        # 1つずつ削除
        print("⚠️  一括削除に失敗。1つずつ削除を試みます...")
        deleted_count = 0
        for note_id in note_ids:
            r = invoke_anki('deleteNotes', notes=[note_id])
            if r is not None:
                deleted_count += 1
                if deleted_count % 5 == 0:
                    print(f"  ✓ {deleted_count}/{len(note_ids)}個削除完了...")

        if deleted_count > 0:
            result = True
            print(f"✅ {deleted_count}個のノートを削除しました")
        else:
            print("❌ 削除に失敗しました")
            return
    else:
        print(f"✅ 削除完了!")

    print()

    # 削減後の状態
    priority_s_after = count_cards_by_tag(deck_name, "priority-S")
    priority_a_after = count_cards_by_tag(deck_name, "priority-A")
    rate = count_cards_by_tag(deck_name, "rate-of-change")
    scales = count_cards_by_tag(deck_name, "measurement-scales")
    variables = count_cards_by_tag(deck_name, "variables")

    greek_total = priority_s_after + priority_a_after
    stats_total = rate + scales + variables
    total = greek_total + stats_total

    print("=" * 70)
    print("✨ 最終最適化完了!")
    print("=" * 70)
    print()

    print(f"📊 最終カード構成:")
    print(f"  ギリシャ文字 (Priority-S): {priority_s_after}枚 ({priority_s_after / total * 100:.1f}%)")
    print(f"  変化率: {rate}枚 ({rate / total * 100:.1f}%)")
    print(f"  尺度: {scales}枚 ({scales / total * 100:.1f}%)")
    print(f"  変数: {variables}枚 ({variables / total * 100:.1f}%)")
    print()
    print(f"📈 合計: {total}枚")
    print()

    if greek_total / total <= 0.50:
        print("✅ バランス最適! ギリシャ文字が50%以下に抑えられています")
    else:
        print(f"⚠️  ギリシャ文字が{greek_total / total * 100:.1f}%（目標: 50%以下）")

    print()
    print(f"🎯 目標達成状況:")
    print(f"  目標: ギリシャ文字 20枚程度 → 実績: {greek_total}枚")
    print(f"  目標: 総カード数 120-200枚 → 現在: {total}枚 (残り{120 - total}〜{200 - total}枚追加可能)")
    print()
    print(f"🚀 次のステップ:")
    print(f"  統計WEB Step1に沿って新規カード作成:")
    print(f"  - 確率分布 (30-40枚)")
    print(f"  - 推定 (20-30枚)")
    print(f"  - 仮説検定 (30-40枚)")
    print(f"  - 回帰・相関 (10-15枚)")
    print()


if __name__ == "__main__":
    main()
