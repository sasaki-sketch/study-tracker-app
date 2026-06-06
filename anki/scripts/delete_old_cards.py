#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
既存の統計学Ankiカードを削除するスクリプト
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


def delete_cards_by_tags(tags_to_delete):
    """指定されたタグのカードをすべて削除"""
    print("=" * 70)
    print("既存Ankiカード削除スクリプト")
    print("=" * 70)
    print()

    # AnkiConnect接続確認
    print("🔌 AnkiConnectに接続中...")
    version = invoke_anki('version')
    if version is None:
        print("❌ Ankiが起動していないか、AnkiConnectがインストールされていません")
        return

    print(f"✅ AnkiConnect接続成功")
    print()

    total_deleted = 0

    for tag in tags_to_delete:
        print(f"📝 タグ '{tag}' のカードを検索中...")

        # タグでノートIDを検索
        note_ids = invoke_anki('findNotes', query=f'tag:{tag}')

        if note_ids is None:
            print(f"  ⚠ タグ '{tag}' の検索に失敗")
            continue

        if len(note_ids) == 0:
            print(f"  ℹ タグ '{tag}' のカードは見つかりませんでした")
            continue

        print(f"  ✓ {len(note_ids)}枚のカードを発見")

        # ノートを削除（deleteNotesは成功時もNoneを返すことがある）
        try:
            invoke_anki('deleteNotes', notes=note_ids)
            print(f"  ✅ {len(note_ids)}枚のカードを削除しました")
            total_deleted += len(note_ids)
        except Exception as e:
            print(f"  ❌ 削除に失敗しました: {e}")

    print()
    print("=" * 70)
    print("✨ カード削除完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 削除成功: {total_deleted}枚")
    print()


def main():
    """メイン実行"""
    # 削除対象のタグリスト
    tags_to_delete = [
        'powers',       # 2の累乗カード
        'math',         # 数学公式カード
        'inequality',   # ローレンツ曲線・ジニ係数カード
        'shape',        # 歪度・尖度カード
        'memorization', # 暗記カード
        'sturges',      # スタージェス関連
        'technique',    # テクニックカード
        'computer',     # コンピュータサイエンス関連
        'logarithm',    # 対数関連
        'exponential',  # 指数関連
        'differentiation', # 微分関連
        'integration',  # 積分関連
        'lorenz',       # ローレンツ曲線
        'gini',         # ジニ係数
        'skewness',     # 歪度
        'kurtosis',     # 尖度
        'quiz',         # クイズ形式
        'exam',         # 試験関連
        'application',  # 応用
        'calculation',  # 計算
        'practice',     # 練習
        'conversion',   # 変換
        'summary',      # まとめ
        'comparison',   # 比較
        'interpretation', # 解釈
        'exam-tips'     # 試験のコツ
    ]

    print("以下のタグのカードを削除します:")
    for tag in tags_to_delete:
        print(f"  - {tag}")
    print()

    # 確認
    response = input("本当に削除しますか？ (yes/no): ")
    if response.lower() != 'yes':
        print("キャンセルしました。")
        return

    delete_cards_by_tags(tags_to_delete)


if __name__ == "__main__":
    main()
