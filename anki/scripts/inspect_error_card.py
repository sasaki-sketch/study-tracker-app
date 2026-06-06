#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
エラーカードの内容を詳細表示
"""

import json
import urllib.request
import re

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
    # 統計学v2デッキの全カードを取得
    deck_name = "統計学v2"
    note_ids = invoke_anki('findNotes', query=f'deck:"{deck_name}"')

    # カード4（分散の定義）を取得
    note_id = note_ids[3]  # 0-indexed, so 3 = card 4

    note_info = invoke_anki('notesInfo', notes=[note_id])
    note = note_info[0]

    back = note['fields']['Back']['value']

    print("=" * 70)
    print("カード4（分散の定義）の裏面内容")
    print("=" * 70)
    print()

    # \leftと\rightの周辺を抽出
    lines = back.split('\n')
    for i, line in enumerate(lines, 1):
        if 'left' in line.lower() or 'right' in line.lower():
            print(f"行{i}: {line}")

    print()
    print("=" * 70)
    print("raw repr:")
    print("=" * 70)
    for i, line in enumerate(lines, 1):
        if 'left' in line.lower() or 'right' in line.lower():
            print(f"行{i}: {repr(line)}")

if __name__ == "__main__":
    main()
