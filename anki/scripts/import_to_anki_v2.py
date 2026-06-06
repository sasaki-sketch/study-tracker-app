#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AnkiConnect経由でギリシャ文字カードをAnkiにインポート（改善版v2.0）
- 超大型フォント
- 高コントラスト
- 読みやすいデザイン
"""

import json
import urllib.request
import csv


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


def delete_old_deck(deck_name):
    """既存のデッキを削除"""
    print(f"🗑️  既存デッキ '{deck_name}' を削除中...")
    decks = invoke_anki('deckNames')

    if deck_name in decks:
        result = invoke_anki('deleteDecks', decks=[deck_name], cardsToo=True)
        if result is not None:
            print(f"✅ 既存デッキを削除しました")
            return True
    else:
        print(f"ℹ️  既存デッキは存在しません（スキップ）")
        return True


def create_deck(deck_name="Greek Letters & Statistics"):
    """デッキを作成"""
    print(f"📚 デッキ '{deck_name}' を作成中...")
    result = invoke_anki('createDeck', deck=deck_name)
    if result is not None:
        print(f"✅ デッキ作成完了 (ID: {result})")
    return result


def create_model_v2():
    """改善版カスタムノートタイプを作成"""
    model_name = "Greek Letters v2 (Super Readable)"

    print(f"📝 ノートタイプ '{model_name}' を作成中...")

    # 改善版CSS v2.0 - 読み込み
    with open('IMPROVED_ANKI_CSS.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # モデル作成
    result = invoke_anki(
        'createModel',
        modelName=model_name,
        inOrderFields=['Front', 'Back'],
        css=css,
        isCloze=False,
        cardTemplates=[
            {
                'Name': 'Card 1',
                'Front': '{{Front}}',
                'Back': '{{Front}}<hr id=answer>{{Back}}'
            }
        ]
    )

    if result is not None:
        print(f"✅ ノートタイプ作成完了（改善版v2.0）")
    else:
        print(f"ℹ️  既存のノートタイプを使用します")

    return model_name


def import_cards_from_csv(csv_file, deck_name, model_name):
    """CSVファイルからカードをインポート"""
    print(f"📥 {csv_file} からカードを読み込み中...")

    cards_added = 0
    cards_failed = 0

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')

        for row in reader:
            front = row['Front']
            back = row['Back']
            tags = row['Tags'].split()

            # カードを追加
            result = invoke_anki(
                'addNote',
                note={
                    'deckName': deck_name,
                    'modelName': model_name,
                    'fields': {
                        'Front': front,
                        'Back': back
                    },
                    'tags': tags,
                    'options': {
                        'allowDuplicate': False
                    }
                }
            )

            if result:
                cards_added += 1
                if cards_added % 10 == 0:
                    print(f"  ✓ {cards_added}枚インポート完了...")
            else:
                cards_failed += 1

    return cards_added, cards_failed


def main():
    """メイン実行"""
    print("=" * 70)
    print("ギリシャ文字カード → Anki 再インポート（改善版v2.0）")
    print("=" * 70)
    print()

    # AnkiConnect接続確認
    print("🔌 AnkiConnectに接続中...")
    version = invoke_anki('version')
    if version is None:
        print("❌ Ankiが起動していないか、AnkiConnectがインストールされていません")
        print("   Ankiを起動してから再度実行してください")
        return

    print(f"✅ AnkiConnect接続成功 (version {version})")
    print()

    # 既存デッキを削除
    deck_name = "Greek Letters & Statistics"
    delete_old_deck(deck_name)
    print()

    # デッキ作成
    create_deck(deck_name)
    print()

    # ノートタイプ作成（改善版）
    model_name = create_model_v2()
    print()

    # カードインポート
    csv_file = "greek_letters_anki.csv"
    cards_added, cards_failed = import_cards_from_csv(csv_file, deck_name, model_name)

    print()
    print("=" * 70)
    print("✨ 再インポート完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    if cards_failed > 0:
        print(f"  ⚠️  スキップ: {cards_failed}枚")
    print()
    print(f"🎯 改善内容:")
    print(f"  ✓ ギリシャ文字: 180px（超巨大!）")
    print(f"  ✓ カタカナ読み: 72px（鮮やかな青）")
    print(f"  ✓ 英語読み: 36px（濃いグレー）")
    print(f"  ✓ 記憶術: 22px（ほぼ黒、読みやすい）")
    print(f"  ✓ 使用例: 22px（ほぼ黒、読みやすい）")
    print()
    print(f"🚀 次のステップ:")
    print(f"  1. Ankiで '{deck_name}' デッキを確認")
    print(f"  2. カードを開いて改善を確認!")
    print()


if __name__ == "__main__":
    main()
