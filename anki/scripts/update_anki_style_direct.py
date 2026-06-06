#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ankiのスタイルを直接更新するスクリプト（改善版v2.0）
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


def read_css_file(filename):
    """CSSファイルを読み込む"""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def update_model_templates():
    """ノートタイプのテンプレートを直接更新"""
    model_name = "Greek Letters (Enhanced)"

    print(f"🎨 '{model_name}' のスタイルを更新中...")

    # CSSファイルを読み込み
    improved_css = read_css_file('IMPROVED_ANKI_CSS.css')

    # モデル情報を取得
    model_names = invoke_anki('modelNames')
    if model_name not in model_names:
        print(f"❌ モデル '{model_name}' が見つかりません")
        return False

    # モデルのフィールドとテンプレートを取得
    model_info = invoke_anki('modelFieldNames', modelName=model_name)

    # スタイルを更新
    # AnkiConnectのupdateModelStylingは使えないので、代替方法を使用
    print("📝 スタイル更新を試行中...")

    # 方法1: modelTemplates経由で更新を試みる
    templates_result = invoke_anki('modelTemplates', modelName=model_name)

    if templates_result:
        # テンプレート情報を取得
        card_template = templates_result.get('Card 1', {})

        # 新しいモデル情報を構築
        update_data = {
            'name': model_name,
            'templates': {
                'Card 1': {
                    'Front': card_template.get('Front', '{{Front}}'),
                    'Back': card_template.get('Back', '{{Front}}<hr id=answer>{{Back}}')
                }
            },
            'css': improved_css
        }

        # updateModelTemplates を試す
        result = invoke_anki('updateModelTemplates', model=update_data)

        if result is not None:
            print(f"✅ スタイル更新成功!")
            return True

    print("⚠️  自動更新に失敗しました。手動更新が必要です。")
    return False


def main():
    """メイン実行"""
    print("=" * 70)
    print("Ankiカードスタイル自動更新 v2.0")
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

    # スタイル更新を試行
    success = update_model_templates()

    print()
    if success:
        print("=" * 70)
        print("✨ スタイル更新完了!")
        print("=" * 70)
        print()
        print("🎯 確認方法:")
        print("  1. Ankiで任意のカードを開く")
        print("  2. ギリシャ文字が超巨大(180px)になっています")
        print("  3. 記憶術と使用例が大きく(22px)読みやすくなっています")
    else:
        print()
        print("=" * 70)
        print("📖 手動更新が必要です")
        print("=" * 70)
        print()
        print("以下の手順で更新してください:")
        print("  1. Anki → ブラウズ (⌘+B)")
        print("  2. 上部メニュー → カード...")
        print("  3. 下部 → スタイルタブ")
        print("  4. 全選択(⌘+A) → 削除")
        print("  5. IMPROVED_ANKI_CSS.css の内容をコピペ")
        print("  6. 保存")
        print()
        print("詳細は ANKI_FINAL_UPDATE_GUIDE.md を参照してください")


if __name__ == "__main__":
    main()
