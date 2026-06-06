#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ankiのカードを別のデッキに移動するスクリプト（改良版）
"""

import json
import urllib.request
import sys

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

        if response_data.get('error'):
            print(f"APIエラー: {response_data['error']}")
            return None

        return response_data.get('result')
    except Exception as e:
        print(f"通信エラー: {e}")
        return None

def main():
    print("=" * 60)
    print("Ankiカード移動スクリプト（改良版）")
    print("=" * 60)

    # 1. 接続確認
    print("\nAnkiとの接続を確認中...")
    version = invoke('version')
    if not version:
        print("✗ Ankiに接続できません")
        sys.exit(1)
    print(f"✓ AnkiConnect バージョン {version} に接続成功")

    source_deck = "統計学v２"
    target_deck = "統計学v2"

    print(f"\n移動元デッキ: {source_deck}")
    print(f"移動先デッキ: {target_deck}")

    # 2. ノートを検索
    print(f"\n「{source_deck}」デッキのノートを検索中...")
    note_ids = invoke('findNotes', query=f'deck:"{source_deck}"')

    if not note_ids:
        print(f"✗ 「{source_deck}」デッキにノートが見つかりませんでした")
        sys.exit(1)

    print(f"✓ {len(note_ids)}件のノートが見つかりました")

    # 3. 各ノートのカードIDを取得
    print("\nカードIDを取得中...")
    all_card_ids = []
    for note_id in note_ids:
        cards_info = invoke('cardsInfo', cards=invoke('findCards', query=f'nid:{note_id}'))
        if cards_info:
            for card in cards_info:
                all_card_ids.append(card['cardId'])

    print(f"✓ {len(all_card_ids)}枚のカードを見つけました")

    # 4. カードを1枚ずつ移動
    print(f"\nカードを「{target_deck}」デッキに移動中...")
    success_count = 0

    for i, card_id in enumerate(all_card_ids, 1):
        result = invoke('changeDeck', cards=[card_id], deck=target_deck)
        if result is not None:
            success_count += 1
            if i % 5 == 0 or i == len(all_card_ids):
                print(f"  {i}/{len(all_card_ids)}枚移動完了")
        else:
            print(f"  ✗ カードID {card_id} の移動に失敗")

    if success_count == len(all_card_ids):
        print(f"✓ 全{success_count}枚のカードを移動しました")
    else:
        print(f"⚠ {success_count}/{len(all_card_ids)}枚を移動しました")

    # 5. 確認
    print(f"\n確認中...")
    target_cards = invoke('findCards', query=f'deck:"{target_deck}"')
    source_cards = invoke('findCards', query=f'deck:"{source_deck}"')

    print(f"「{target_deck}」デッキ: {len(target_cards) if target_cards else 0}枚")
    print(f"「{source_deck}」デッキ: {len(source_cards) if source_cards else 0}枚")

    print("\n" + "=" * 60)
    print("移動完了")
    print("=" * 60)
    print(f"「{source_deck}」→「{target_deck}」")
    print(f"移動枚数: {success_count}枚")
    print("\nAnkiで確認してください。")

if __name__ == '__main__':
    main()
