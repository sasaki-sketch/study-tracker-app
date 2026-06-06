#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ankiのカードを別のデッキに移動するスクリプト
"""

import json
import urllib.request
import sys

# AnkiConnect設定
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

        if len(response_data) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in response_data:
            raise Exception('response is missing required error field')
        if 'result' not in response_data:
            raise Exception('response is missing required result field')
        if response_data['error'] is not None:
            raise Exception(response_data['error'])

        return response_data['result']
    except Exception as e:
        print(f"エラー: {e}")
        return None

def main():
    print("=" * 60)
    print("Ankiカード移動スクリプト")
    print("=" * 60)

    # 1. 接続確認
    print("\nAnkiとの接続を確認中...")
    version = invoke('version')
    if not version:
        print("✗ Ankiに接続できません")
        sys.exit(1)
    print(f"✓ AnkiConnect バージョン {version} に接続成功")

    # 2. 移動元デッキのカードを検索
    source_deck = "統計学v２"
    target_deck = "統計学v2"

    print(f"\n移動元デッキ: {source_deck}")
    print(f"移動先デッキ: {target_deck}")

    # デッキ内のカードを検索
    print(f"\n「{source_deck}」デッキのカードを検索中...")
    card_ids = invoke('findCards', query=f'deck:"{source_deck}"')

    if not card_ids:
        print(f"✗ 「{source_deck}」デッキにカードが見つかりませんでした")
        sys.exit(1)

    print(f"✓ {len(card_ids)}枚のカードが見つかりました")

    # 3. カードを移動
    print(f"\nカードを「{target_deck}」デッキに移動中...")
    result = invoke('changeDeck', cards=card_ids, deck=target_deck)

    if result is not None:
        print(f"✓ {len(card_ids)}枚のカードを移動しました")
    else:
        print("✗ カードの移動に失敗しました")
        sys.exit(1)

    # 4. 確認
    print(f"\n確認: 「{target_deck}」デッキのカード数")
    new_card_ids = invoke('findCards', query=f'deck:"{target_deck}"')
    if new_card_ids:
        print(f"✓ 「{target_deck}」デッキに{len(new_card_ids)}枚のカードがあります")

    print("\n" + "=" * 60)
    print("移動完了")
    print("=" * 60)
    print(f"「{source_deck}」→「{target_deck}」")
    print(f"移動枚数: {len(card_ids)}枚")
    print("\nAnkiで確認してください。")

if __name__ == '__main__':
    main()
