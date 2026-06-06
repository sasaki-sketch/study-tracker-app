#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計学デッキから統計学v2デッキへカードを移動
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

    response = urllib.request.urlopen(
        urllib.request.Request('http://localhost:8765', request_json)
    )
    result = json.loads(response.read().decode('utf-8'))

    if result['error']:
        raise Exception(f"AnkiConnect error: {result['error']}")

    return result['result']


def main():
    print("=" * 70)
    print("統計学デッキから統計学v2デッキへカード移動")
    print("=" * 70)
    print()

    # 統計学デッキのカードを取得
    old_deck_ids = invoke_anki('findNotes', query='deck:統計学')

    if len(old_deck_ids) == 0:
        print("❌ 統計学デッキにカードがありません")
        print()
        print("手順:")
        print("1. Ankiで「ツール」→「削除したノートを復元」を実行")
        print("2. 復元したいカードを選択して復元")
        print("3. このスクリプトを再度実行")
        return

    print(f"📋 統計学デッキに {len(old_deck_ids)} 枚のカードが見つかりました")
    print()

    # カードの内容を表示
    print("移動するカード:")
    for i, note_id in enumerate(old_deck_ids, 1):
        note_info = invoke_anki('notesInfo', notes=[note_id])
        if note_info and len(note_info) > 0:
            fields = note_info[0].get('fields', {})
            front = fields.get('Front', {}).get('value', '')
            # HTMLタグを削除
            import re
            front_text = re.sub(r'<[^>]+>', '', front).strip()[:60]
            print(f"  {i}. {front_text}...")

    print()
    input("Enterキーを押すと統計学v2デッキに移動します...")
    print()

    # カードを統計学v2デッキに移動
    invoke_anki('changeDeck', cards=old_deck_ids, deck='統計学v2')

    print(f"✅ {len(old_deck_ids)} 枚のカードを統計学v2デッキに移動しました")
    print()

    # 確認
    v2_deck_ids = invoke_anki('findNotes', query='deck:統計学v2')
    print(f"📊 統計学v2デッキの現在のカード数: {len(v2_deck_ids)} 枚")
    print()


if __name__ == "__main__":
    main()
