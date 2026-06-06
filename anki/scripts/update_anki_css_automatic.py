#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AnkiノートタイプのCSSを自動更新
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


def main():
    """メイン実行"""
    print("=" * 70)
    print("AnkiノートタイプのCSS自動更新")
    print("=" * 70)
    print()

    # AnkiConnect接続確認
    print("🔌 AnkiConnectに接続中...")
    version = invoke_anki('version')
    if version is None:
        print("❌ Ankiが起動していないか、AnkiConnectがインストールされていません")
        return

    print(f"✅ AnkiConnect接続成功 (version {version})")
    print()

    # CSSファイルを読み込み
    print("📄 改善版CSSを読み込み中...")
    try:
        with open('/Users/sasaki/IMPROVED_ANKI_CSS.css', 'r', encoding='utf-8') as f:
            new_css = f.read()
        print(f"✅ CSS読み込み完了 ({len(new_css)}文字)")
        print()
    except Exception as e:
        print(f"❌ CSSファイルの読み込みに失敗: {e}")
        return

    # ノートタイプ名
    model_name = "Greek Letters v2 (Super Readable)"

    # 既存のノートタイプを確認
    print(f"🔍 ノートタイプ '{model_name}' を確認中...")
    model_names = invoke_anki('modelNames')

    if model_names is None:
        print("❌ ノートタイプの取得に失敗しました")
        return

    if model_name not in model_names:
        print(f"❌ ノートタイプ '{model_name}' が見つかりません")
        print(f"📋 利用可能なノートタイプ:")
        for name in model_names:
            print(f"  - {name}")
        return

    print(f"✅ ノートタイプが見つかりました")
    print()

    # CSSを更新
    print(f"🎨 CSSを更新中...")

    # AnkiConnectのupdateModelStyling APIを使用
    result = invoke_anki(
        'updateModelStyling',
        model={
            'name': model_name,
            'css': new_css
        }
    )

    if result is not None:
        print(f"✅ CSS更新成功!")
        print()

        print("=" * 70)
        print("✨ CSS更新完了!")
        print("=" * 70)
        print()

        print("🎨 更新内容:")
        print("  ✅ 色付きテキスト用クラス (.text-blue, .text-red, .text-green, .text-gray)")
        print("  ✅ ダークモード対応")
        print("  ✅ コントラスト改善 (#666 → #4b5563)")
        print("  ✅ ネストタグの色継承保証")
        print()

        print("🔍 確認方法:")
        print("  1. Ankiブラウザを開く (Cmd+B)")
        print("  2. 検索: tag:variables")
        print("  3. カード「説明変数と目的変数の違いは?」を開く")
        print()

        print("✅ 確認ポイント:")
        print("  - 「目的変数(Y)」が赤色で表示")
        print("  - 「説明変数(X)」が青色で表示")
        print("  - すべてのテキストが読みやすい")
        print()

    else:
        print(f"❌ CSS更新に失敗しました")
        print()
        print("📝 代替方法（手動更新）:")
        print("  1. Anki → ツール → ノートタイプを管理")
        print("  2. 'Greek Letters v2 (Super Readable)' を選択")
        print("  3. 「カード」ボタン → 「スタイル」タブ")
        print("  4. /Users/sasaki/IMPROVED_ANKI_CSS.css の内容を貼り付け")
        print("  5. 保存")
        print()


if __name__ == "__main__":
    main()
