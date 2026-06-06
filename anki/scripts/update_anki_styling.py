#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ankiカードのスタイルを改善して更新
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


def update_model_styling():
    """ノートタイプのスタイルを改善版に更新"""
    model_name = "Greek Letters (Enhanced)"

    # 改善版CSS - フォントサイズと可読性を大幅に向上
    improved_css = """/* ギリシャ文字学習カード用スタイル（改善版） */
.card {
    font-family: -apple-system, BlinkMacSystemFont, 'Hiragino Sans', 'Yu Gothic', 'Meiryo', sans-serif;
    text-align: center;
    padding: 30px 20px;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    font-size: 20px;
    line-height: 1.6;
    max-width: 800px;
    margin: 0 auto;
}

/* 記号表示 */
.symbol {
    font-size: 96px;
    color: #2c3e50;
    margin: 30px 0;
    font-weight: bold;
}

/* 読み方 */
.reading h2 {
    font-size: 56px;
    color: #3498db;
    margin: 20px 0;
    font-weight: bold;
}

.english {
    font-size: 28px;
    color: #7f8c8d;
    font-style: italic;
    margin-top: 10px;
}

/* 質問スタイル */
.question {
    background: white;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.question h3 {
    font-size: 32px;
    color: #2c3e50;
    font-weight: bold;
    line-height: 1.5;
}

/* 回答スタイル */
.answer {
    text-align: left;
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.meaning {
    color: #e74c3c;
    font-size: 24px;
    font-weight: bold;
    border-bottom: 3px solid #e74c3c;
    padding-bottom: 15px;
    margin-bottom: 20px;
    line-height: 1.6;
}

/* ニーモニック(記憶術) - フォント改善 */
.mnemonic {
    background: #fff9e6;
    border-left: 5px solid #ffc107;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
}

.mnemonic strong {
    color: #856404;
    font-size: 22px;
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
}

.mnemonic p {
    color: #333;
    font-size: 20px;
    line-height: 1.7;
    margin: 0;
    font-weight: 500;
}

/* 使用例 - フォント改善 */
.context {
    background: #e8f4f8;
    border-left: 5px solid #17a2b8;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
}

.context strong {
    color: #0c5460;
    font-size: 22px;
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
}

.context p {
    color: #333;
    font-size: 20px;
    line-height: 1.7;
    margin: 0;
    font-weight: 500;
}

/* 補足情報 */
.info {
    margin-top: 25px;
    padding-top: 15px;
    border-top: 2px solid #ddd;
}

.info small {
    color: #6c757d;
    font-size: 18px;
}

.note {
    font-size: 22px;
    color: #6c757d;
    margin: 15px 0;
    font-weight: 500;
}

.hint {
    font-size: 19px;
    color: #95a5a6;
    line-height: 1.6;
}

/* モバイル対応 */
@media (max-width: 600px) {
    .card {
        padding: 20px 15px;
        font-size: 18px;
    }

    .symbol {
        font-size: 72px;
    }

    .reading h2 {
        font-size: 42px;
    }

    .question h3 {
        font-size: 26px;
    }

    .meaning {
        font-size: 20px;
    }

    .mnemonic strong,
    .context strong {
        font-size: 19px;
    }

    .mnemonic p,
    .context p {
        font-size: 18px;
    }
}"""

    print(f"🎨 '{model_name}' のスタイルを更新中...")

    # モデルのスタイリングを更新
    result = invoke_anki(
        'updateModelStyling',
        model={
            "name": model_name,
            "css": improved_css
        }
    )

    if result is not None:
        print(f"✅ スタイル更新完了!")
        print()
        print("📋 改善内容:")
        print("  ✓ 記憶術のフォントサイズ: 16px → 20px")
        print("  ✓ 使用例のフォントサイズ: 16px → 20px")
        print("  ✓ フォントウェイト: 太字に変更(500)")
        print("  ✓ 行間を広げて読みやすく(1.7)")
        print("  ✓ パディングを増やしてゆったり配置")
        print("  ✓ 色のコントラストを向上")
        print("  ✓ モバイル対応を追加")
        return True
    else:
        print(f"❌ スタイル更新に失敗しました")
        return False


def main():
    """メイン実行"""
    print("=" * 70)
    print("Ankiカードスタイル改善アップデート")
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

    # スタイル更新
    success = update_model_styling()

    if success:
        print()
        print("=" * 70)
        print("✨ スタイル更新完了!")
        print("=" * 70)
        print()
        print("🎯 確認方法:")
        print("  1. Ankiで任意のカードを開く")
        print("  2. 記憶術と使用例のテキストが大きく読みやすくなっています")
        print("  3. 既存のカードにも自動適用されています")
        print()


if __name__ == "__main__":
    main()
