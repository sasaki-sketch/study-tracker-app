#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Priority-Aカードをリスト表示（手動削除用）
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


def main():
    """メイン実行"""
    print("=" * 70)
    print("Priority-Aカードリスト")
    print("=" * 70)
    print()

    deck_name = "Greek Letters & Statistics"

    # Priority-Aカードを取得
    query = f'deck:"{deck_name}" tag:priority-A'
    card_ids = invoke_anki('findCards', query=query)

    if not card_ids:
        print("⚠️  Priority-Aカードが見つかりませんでした")
        return

    print(f"📋 Priority-Aカード: {len(card_ids)}枚")
    print()

    # カード情報を取得
    cards_info = invoke_anki('cardsInfo', cards=card_ids)

    if not cards_info:
        print("❌ カード情報の取得に失敗しました")
        return

    # カード一覧を表示
    print("以下のカードが削除対象です:")
    print()

    note_ids_seen = set()
    for i, card in enumerate(cards_info, 1):
        note_id = card.get('note', 'N/A')

        if note_id in note_ids_seen:
            continue
        note_ids_seen.add(note_id)

        fields = card.get('fields', {})
        front = fields.get('Front', {}).get('value', 'N/A')
        tags = ' '.join(card.get('tags', []))

        # HTMLタグを削除して表示
        import re
        front_text = re.sub('<[^<]+?>', '', front)
        front_text = front_text.strip()[:50]  # 最初の50文字

        print(f"{i}. Note ID: {note_id}")
        print(f"   Front: {front_text}...")
        print(f"   Tags: {tags}")
        print()

    print("=" * 70)
    print("手動削除の方法:")
    print("=" * 70)
    print()
    print("Ankiで以下のクエリを使用してカードを検索し、手動で削除してください:")
    print()
    print(f'  deck:"{deck_name}" tag:priority-A')
    print()
    print("または:")
    print()
    print("  1. Ankiブラウザを開く")
    print("  2. 左側で 'Greek Letters & Statistics' デッキを選択")
    print("  3. 上部の検索ボックスに 'tag:priority-A' と入力")
    print("  4. 全カードを選択 (Ctrl+A / Cmd+A)")
    print("  5. Delete キーで削除")
    print()


if __name__ == "__main__":
    main()
