#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ankiデッキの現在の状態を詳細確認
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


def count_cards_by_tag(deck_name, tag):
    """特定タグのカード数を数える"""
    query = f'deck:"{deck_name}" tag:{tag}'
    card_ids = invoke_anki('findCards', query=query)
    return len(card_ids) if card_ids else 0


def get_all_cards_in_deck(deck_name):
    """デッキ内の全カードを取得"""
    query = f'deck:"{deck_name}"'
    card_ids = invoke_anki('findCards', query=query)
    return len(card_ids) if card_ids else 0


def main():
    """メイン実行"""
    print("=" * 70)
    print("Ankiデッキ状態確認")
    print("=" * 70)
    print()

    deck_name = "Greek Letters & Statistics"

    # 全カード数
    total_cards = get_all_cards_in_deck(deck_name)

    print(f"📚 デッキ: {deck_name}")
    print(f"📊 総カード数: {total_cards}枚")
    print()

    # カテゴリ別カード数
    print("=" * 70)
    print("カテゴリ別内訳:")
    print("=" * 70)
    print()

    # ギリシャ文字（優先度別）
    priority_s = count_cards_by_tag(deck_name, "priority-S")
    priority_a = count_cards_by_tag(deck_name, "priority-A")
    priority_b = count_cards_by_tag(deck_name, "priority-B")
    priority_c = count_cards_by_tag(deck_name, "priority-C")

    print("🔤 ギリシャ文字:")
    print(f"  Priority-S (最重要): {priority_s}枚")
    print(f"  Priority-A (重要): {priority_a}枚")
    print(f"  Priority-B (中程度): {priority_b}枚")
    print(f"  Priority-C (低): {priority_c}枚")
    greek_total = priority_s + priority_a + priority_b + priority_c
    print(f"  小計: {greek_total}枚 ({greek_total / total_cards * 100:.1f}%)")
    print()

    # 順番記憶
    order_mem = count_cards_by_tag(deck_name, "order-memorization")
    print(f"🎵 順番記憶カード: {order_mem}枚")
    print()

    # 統計概念
    rate = count_cards_by_tag(deck_name, "rate-of-change")
    scales = count_cards_by_tag(deck_name, "measurement-scales")
    variables = count_cards_by_tag(deck_name, "variables")

    print("📊 統計概念:")
    print(f"  変化率: {rate}枚 ({rate / total_cards * 100:.1f}%)")
    print(f"  尺度: {scales}枚 ({scales / total_cards * 100:.1f}%)")
    print(f"  説明変数・目的変数: {variables}枚 ({variables / total_cards * 100:.1f}%)")
    stats_total = rate + scales + variables
    print(f"  小計: {stats_total}枚 ({stats_total / total_cards * 100:.1f}%)")
    print()

    # サマリー
    print("=" * 70)
    print("📈 バランス評価:")
    print("=" * 70)
    print()

    print(f"ギリシャ文字: {greek_total}枚 ({greek_total / total_cards * 100:.1f}%)")
    print(f"統計概念: {stats_total}枚 ({stats_total / total_cards * 100:.1f}%)")
    print()

    if greek_total / total_cards <= 0.50:
        print("✅ バランス良好! ギリシャ文字が50%以下に抑えられています")
    elif greek_total / total_cards <= 0.60:
        print("⚠️  ギリシャ文字がやや多め（50-60%）")
    else:
        print("❌ ギリシャ文字が多すぎます（60%以上）")

    print()
    print(f"🎯 目標:")
    print(f"  最終カード数: 120-200枚（現在: {total_cards}枚）")
    print(f"  今後の追加予定: 約{120 - total_cards}〜{200 - total_cards}枚")
    print()


if __name__ == "__main__":
    main()
