#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ankiのデッキ一覧を確認するスクリプト
"""

import json
import urllib.request

ANKI_CONNECT_URL = 'http://localhost:8765'

def invoke(action, **params):
    """AnkiConnect APIを呼び出す"""
    request_data = json.dumps({
        'action': action,
        'version': 6,
        'params': params
    }).encode('utf-8')

    try:
        response = urllib.request.urlopen(
            urllib.request.Request(ANKI_CONNECT_URL, request_data)
        )
        response_data = json.loads(response.read().decode('utf-8'))
        return response_data.get('result')
    except Exception as e:
        print(f"エラー: {e}")
        return None

# デッキ一覧を取得
print("Ankiのデッキ一覧:")
print("=" * 60)
decks = invoke('deckNames')
if decks:
    for deck in sorted(decks):
        # 各デッキのカード数を取得
        card_count = len(invoke('findCards', query=f'deck:"{deck}"') or [])
        print(f"{deck}: {card_count}枚")
else:
    print("デッキが見つかりません")
