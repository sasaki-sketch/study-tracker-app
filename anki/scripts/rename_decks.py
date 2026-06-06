#!/usr/bin/env python3
"""
統計検定2級 Ankiデッキリネームスクリプト

既存のデッキを新しい階層構造にリネームします。
実行前にAnkiが起動していてAnkiConnectが有効になっている必要があります。
"""

import json
import urllib.request


def invoke(action, **params):
    """AnkiConnect APIを呼び出す"""
    request_json = json.dumps({
        'action': action,
        'version': 6,
        'params': params
    }).encode('utf-8')

    req = urllib.request.Request('http://localhost:8765', request_json)
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))

    if result.get('error'):
        raise Exception(result['error'])
    return result.get('result')


# リネームマッピング（現在の名前 → 新しい名前）
RENAME_MAP = {
    # 確率分布
    "統計検定2級::確率分布（復習用）": "統計検定2級::04_確率分布::01_離散型分布",
    "統計検定2級::正規分布と標準正規分布": "統計検定2級::04_確率分布::02_正規分布",
    "統計検定2級::確率の基礎と正規分布（追加）": "統計検定2級::03_確率::01_確率の基礎",

    # 標本分布
    "統計検定2級::大数の法則と中心極限定理": "統計検定2級::05_標本分布::01_大数の法則",
    "統計検定2級::標本と抽出法": "統計検定2級::05_標本分布::02_標本と抽出法",

    # 推定
    "統計検定2級::母平均の点推定": "統計検定2級::06_推定::01_点推定",
    "統計検定2級::母平均の区間推定（母分散既知）": "統計検定2級::06_推定::02_母平均区間推定_分散既知",
    "統計検定2級::母平均の区間推定（母分散未知）": "統計検定2級::06_推定::03_母平均区間推定_分散未知",
    "統計検定2級::21_母比率の区間推定": "統計検定2級::06_推定::04_母比率区間推定",
    "統計検定2級::22_母分散の区間推定": "統計検定2級::06_推定::05_母分散区間推定",

    # 検定
    "統計検定2級::23_検定の前に": "統計検定2級::07_検定::01_検定の基礎",
    "統計検定2級::24_平均値の検定": "統計検定2級::07_検定::02_母平均の検定",
    "統計検定2級::25_さまざまな検定": "統計検定2級::07_検定::03_各種検定",

    # 回帰分析
    "統計検定2級::26_相関分析": "統計検定2級::08_回帰分析::01_相関分析",
    "統計検定2級::27_回帰分析": "統計検定2級::08_回帰分析::02_回帰分析",

    # 過去問
    "統計検定2級::2019年11月": "統計検定2級::99_過去問::2019年11月",
    "統計検定2級::2019年11月_Part2": "統計検定2級::99_過去問::2019年11月_Part2",
    "統計検定2級::過去問復習_20260128": "統計検定2級::99_過去問::復習_20260128",
}


def main():
    print("=" * 60)
    print("統計検定2級 デッキリネームスクリプト")
    print("=" * 60)

    # 現在のデッキ一覧を取得
    current_decks = invoke('deckNames')
    print(f"\n現在のデッキ数: {len(current_decks)}")

    # 統計検定2級デッキのみフィルタ
    stat_decks = [d for d in current_decks if d.startswith('統計検定2級')]
    print(f"統計検定2級関連デッキ: {len(stat_decks)}")

    # リネーム前のカード数を確認
    cards_before = invoke('findCards', query='deck:統計検定2級')
    print(f"総カード数（リネーム前）: {len(cards_before)}")

    print("\n" + "-" * 60)
    print("リネーム処理を開始します...")
    print("-" * 60)

    renamed_count = 0
    skipped_count = 0

    for old_name, new_name in RENAME_MAP.items():
        if old_name in current_decks:
            print(f"\n[リネーム] {old_name}")
            print(f"       → {new_name}")
            try:
                # changeDeck は使えないので、デッキを新規作成してカードを移動
                # まず新しいデッキを作成
                invoke('createDeck', deck=new_name)

                # 旧デッキのカードを取得
                cards = invoke('findCards', query=f'deck:"{old_name}"')

                if cards:
                    # カードを新デッキに移動
                    invoke('changeDeck', cards=cards, deck=new_name)
                    print(f"       {len(cards)}枚のカードを移動")

                # 旧デッキを削除（空になったら）
                remaining = invoke('findCards', query=f'deck:"{old_name}"')
                if not remaining:
                    invoke('deleteDecks', decks=[old_name], cardsToo=False)
                    print(f"       旧デッキを削除")

                renamed_count += 1
            except Exception as e:
                print(f"       エラー: {e}")
        else:
            print(f"\n[スキップ] {old_name} (存在しません)")
            skipped_count += 1

    print("\n" + "=" * 60)
    print("リネーム完了")
    print("=" * 60)

    # リネーム後のカード数を確認
    cards_after = invoke('findCards', query='deck:統計検定2級')
    print(f"\n総カード数（リネーム後）: {len(cards_after)}")

    if len(cards_before) == len(cards_after):
        print("カード数の検証: OK（変化なし）")
    else:
        print(f"警告: カード数が変化しました（{len(cards_before)} → {len(cards_after)}）")

    print(f"\nリネーム成功: {renamed_count}")
    print(f"スキップ: {skipped_count}")

    # 新しいデッキ構造を表示
    print("\n" + "-" * 60)
    print("新しいデッキ構造:")
    print("-" * 60)
    new_decks = invoke('deckNames')
    stat_decks_new = sorted([d for d in new_decks if d.startswith('統計検定2級')])
    for deck in stat_decks_new:
        # インデントを付けて表示
        depth = deck.count('::')
        indent = "  " * depth
        name = deck.split('::')[-1]
        print(f"{indent}{name}")


if __name__ == '__main__':
    main()
