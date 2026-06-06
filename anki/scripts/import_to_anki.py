#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AnkiConnect経由でギリシャ文字カードをAnkiにインポート
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


def create_deck(deck_name="Greek Letters & Statistics"):
    """デッキを作成"""
    print(f"📚 デッキ '{deck_name}' を作成中...")
    result = invoke_anki('createDeck', deck=deck_name)
    if result is not None:
        print(f"✅ デッキ作成完了 (ID: {result})")
    return result


def create_model():
    """カスタムノートタイプを作成"""
    model_name = "Greek Letters (Enhanced)"

    print(f"📝 ノートタイプ '{model_name}' を作成中...")

    # CSS
    css = """/* ギリシャ文字学習カード用スタイル */
.card {
    font-family: 'Hiragino Sans', 'Yu Gothic', 'Meiryo', sans-serif;
    text-align: center;
    padding: 20px;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    font-size: 18px;
}

.symbol {
    font-size: 72px;
    color: #2c3e50;
    margin: 20px 0;
}

.reading h2 {
    font-size: 48px;
    color: #3498db;
    margin: 10px 0;
}

.english {
    font-size: 24px;
    color: #7f8c8d;
    font-style: italic;
}

.question {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.question h3 {
    font-size: 28px;
    color: #2c3e50;
}

.answer {
    text-align: left;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.meaning {
    color: #e74c3c;
    font-size: 20px;
    border-bottom: 2px solid #e74c3c;
    padding-bottom: 10px;
}

.mnemonic {
    background: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 15px;
    margin: 15px 0;
    border-radius: 5px;
}

.mnemonic strong {
    color: #856404;
}

.context {
    background: #d1ecf1;
    border-left: 4px solid #17a2b8;
    padding: 15px;
    margin: 15px 0;
    border-radius: 5px;
}

.context strong {
    color: #0c5460;
}

.info {
    margin-top: 20px;
    padding-top: 10px;
    border-top: 1px solid #ddd;
    color: #6c757d;
}

.note {
    font-size: 18px;
    color: #6c757d;
    margin: 10px 0;
}

.hint {
    font-size: 16px;
    color: #95a5a6;
}"""

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
        print(f"✅ ノートタイプ作成完了")
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
    print("ギリシャ文字カード → Anki 自動インポート")
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

    # デッキ作成
    deck_name = "Greek Letters & Statistics"
    create_deck(deck_name)
    print()

    # ノートタイプ作成
    model_name = create_model()
    print()

    # カードインポート
    csv_file = "greek_letters_anki.csv"
    cards_added, cards_failed = import_cards_from_csv(csv_file, deck_name, model_name)

    print()
    print("=" * 70)
    print("✨ インポート完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    if cards_failed > 0:
        print(f"  ⚠️  スキップ: {cards_failed}枚 (重複カード)")
    print()
    print(f"🎯 次のステップ:")
    print(f"  1. Ankiで '{deck_name}' デッキを確認")
    print(f"  2. 学習設定を調整 (新規カード10-15枚/日)")
    print(f"  3. priority-S タグでフィルタして最重要文字から学習開始!")
    print()


if __name__ == "__main__":
    main()
