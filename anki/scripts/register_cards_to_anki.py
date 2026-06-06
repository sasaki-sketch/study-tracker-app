#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AnkiConnectを使用してカードをAnkiに登録するスクリプト
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

def check_anki_connection():
    """Ankiとの接続を確認"""
    print("Ankiとの接続を確認中...")
    result = invoke('version')
    if result:
        print(f"✓ AnkiConnect バージョン {result} に接続成功")
        return True
    else:
        print("✗ Ankiに接続できません")
        print("  - Ankiアプリが起動していることを確認してください")
        print("  - AnkiConnectアドオンがインストールされていることを確認してください")
        return False

def create_deck(deck_name):
    """デッキを作成（既存の場合は何もしない）"""
    print(f"\nデッキ「{deck_name}」を確認中...")
    result = invoke('createDeck', deck=deck_name)
    if result is not None:
        print(f"✓ デッキ「{deck_name}」準備完了")
        return True
    return False

def add_note(deck_name, front, back, tags):
    """ノートを追加"""
    note = {
        'deckName': deck_name,
        'modelName': 'Basic',
        'fields': {
            'Front': front,
            'Back': back
        },
        'tags': tags,
        'options': {
            'allowDuplicate': False
        }
    }

    result = invoke('addNote', note=note)
    return result

def register_cards_from_file(file_path, deck_name):
    """Pythonファイルからカードを読み込んでAnkiに登録"""
    print(f"\n{'='*60}")
    print(f"ファイル: {file_path}")
    print(f"{'='*60}")

    # ファイルを実行してcardsリストを取得
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # cardsリストを抽出
    local_vars = {}
    exec(code, {}, local_vars)
    cards = local_vars.get('cards', [])

    if not cards:
        print("✗ カードが見つかりませんでした")
        return 0

    print(f"カード数: {len(cards)}枚")

    success_count = 0
    duplicate_count = 0
    error_count = 0

    for i, card in enumerate(cards, 1):
        front = card['front']
        back = card['back']
        tags = card['tags']

        # タイトルを抽出（表示用）
        import re
        title_match = re.search(r'<b>(.+?)</b>', front)
        title = title_match.group(1) if title_match else f"カード{i}"

        print(f"\n{i}. {title}")

        result = add_note(deck_name, front, back, tags)

        if result:
            print(f"   ✓ 登録成功 (Note ID: {result})")
            success_count += 1
        elif result is None:
            # エラーメッセージからduplicate判定
            print(f"   ⚠ 既に登録済み（スキップ）")
            duplicate_count += 1
        else:
            print(f"   ✗ 登録失敗")
            error_count += 1

    print(f"\n【結果】")
    print(f"  成功: {success_count}枚")
    print(f"  重複: {duplicate_count}枚")
    print(f"  失敗: {error_count}枚")

    return success_count

def main():
    print("=" * 60)
    print("Ankiカード登録スクリプト")
    print("=" * 60)

    # 1. 接続確認
    if not check_anki_connection():
        print("\nAnkiを起動してから再度実行してください。")
        sys.exit(1)

    # 2. デッキ作成
    deck_name = "統計学v２"
    if not create_deck(deck_name):
        print("\nデッキの作成に失敗しました。")
        sys.exit(1)

    # 3. カードファイルのリスト
    card_files = [
        ('/Users/sasaki/kurtosis_verified.py', '尖度'),
        ('/Users/sasaki/probability_expectation_verified.py', '確率と期待値'),
        ('/Users/sasaki/bayes_theorem_verified.py', '条件付き確率とベイズの定理')
    ]

    total_success = 0

    # 4. 各ファイルからカードを登録
    for file_path, topic in card_files:
        try:
            count = register_cards_from_file(file_path, deck_name)
            total_success += count
        except FileNotFoundError:
            print(f"\n✗ ファイルが見つかりません: {file_path}")
        except Exception as e:
            print(f"\n✗ エラーが発生しました: {e}")

    # 5. 最終結果
    print("\n" + "=" * 60)
    print("登録完了")
    print("=" * 60)
    print(f"合計登録枚数: {total_success}枚")
    print(f"デッキ名: {deck_name}")
    print("\nAnkiで確認してください。")

if __name__ == '__main__':
    main()
