#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2の累乗暗記カード - シンプル版
太字・括弧・記号だけで見やすく
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


def create_powers_cards(deck_name, model_name):
    """2の累乗カードを作成（シンプル版）"""

    cards = [
        # カード1: 2の累乗一覧（2^1〜2^10）
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>2の累乗<br>2¹ 〜 2¹⁰ は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>2¹ = 2</b><br>
<b>2² = 4</b><br>
<b>2³ = 8</b><br>
<b>2⁴ = 16</b><br>
<b>2⁵ = 32</b><br>
<b>2⁶ = 64</b><br>
<b>2⁷ = 128</b><br>
<b>2⁸ = 256</b><br>
<b>2⁹ = 512</b><br>
<b>2¹⁰ = 1024</b> （約1000）<br>
<br>
<hr>
<b>覚え方:</b><br>
• 2倍ずつ増える<br>
• 2¹⁰ = 1024 ≈ 1K（キロ）
</div>''',
            'tags': ['powers', 'memorization']
        },

        # カード2: 2の累乗一覧（2^11〜2^16）
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>2の累乗<br>2¹¹ 〜 2¹⁶ は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>2¹¹ = 2048</b> （約2000）<br>
<b>2¹² = 4096</b> （約4000）<br>
<b>2¹³ = 8192</b> （約8000）<br>
<b>2¹⁴ = 16384</b> （約16000）<br>
<b>2¹⁵ = 32768</b> （約32000）<br>
<b>2¹⁶ = 65536</b> （約65000）<br>
<br>
<hr>
<b>覚え方:</b><br>
• 2¹⁰ = 1024から2倍ずつ<br>
• 2¹⁶ = 65536 ≈ 64K
</div>''',
            'tags': ['powers', 'memorization']
        },

        # カード3: 重要な2の累乗（コンピュータサイエンス）
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>コンピュータでよく使う<br>2の累乗は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【バイト単位】</b><br>
• 2⁸ = 256（1バイトで表現できる数）<br>
• 2¹⁰ = 1024 ≈ 1KB<br>
• 2²⁰ = 1,048,576 ≈ 1MB<br>
• 2³⁰ = 1,073,741,824 ≈ 1GB<br>
<br>
<hr>
<b>【ビット数】</b><br>
• 2⁸ = 256（8ビット整数）<br>
• 2¹⁶ = 65,536（16ビット整数）<br>
• 2³² = 4,294,967,296（32ビット整数）<br>
<br>
<hr>
<b>【覚え方】</b><br>
• 10乗ごとに約1000倍<br>
• 2¹⁰ ≈ 1K（キロ）<br>
• 2²⁰ ≈ 1M（メガ）<br>
• 2³⁰ ≈ 1G（ギガ）
</div>''',
            'tags': ['powers', 'computer']
        },

        # カード4: 2の累乗の計算テクニック
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>2の累乗を<br>素早く計算するテクニックは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【基準を覚える】</b><br>
• 2¹⁰ = 1024<br>
• 2²⁰ = 1,048,576<br>
<br>
<hr>
<b>【加算を利用】</b><br>
2ᵃ × 2ᵇ = 2⁽ᵃ⁺ᵇ⁾<br>
<br>
<b>例:</b><br>
2¹⁵ = 2¹⁰ × 2⁵<br>
    = 1024 × 32<br>
    = 32,768<br>
<br>
<hr>
<b>【半分を利用】</b><br>
2ⁿ = 2ⁿ⁻¹ × 2<br>
<br>
<b>例:</b><br>
2⁹ = 2⁸ × 2<br>
   = 256 × 2<br>
   = 512<br>
<br>
<hr>
<b>【統計検定での使用】</b><br>
スタージェスの公式で階級数を計算する時
</div>''',
            'tags': ['powers', 'technique']
        },

        # カード5: スタージェスの公式での使用
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>スタージェスの公式で<br>2の累乗を使う場面は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【スタージェスの公式】</b><br>
k = 1 + log₂ n<br>
<br>
k = 階級数<br>
n = データ数<br>
<br>
<hr>
<b>【2の累乗を利用した逆算】</b><br>
<br>
もしnが2の累乗なら簡単！<br>
<br>
<b>例1: n = 64 = 2⁶</b><br>
k = 1 + log₂ 64<br>
  = 1 + 6<br>
  = 7<br>
<br>
<b>例2: n = 128 = 2⁷</b><br>
k = 1 + log₂ 128<br>
  = 1 + 7<br>
  = 8<br>
<br>
<hr>
<b>【近似値で推定】</b><br>
n = 50の場合<br>
32 < 50 < 64<br>
2⁵ < 50 < 2⁶<br>
<br>
→ log₂ 50 は 5と6の間<br>
→ k ≈ 6〜7
</div>''',
            'tags': ['powers', 'sturges', 'application']
        },

        # カード6: 2の累乗クイズ形式
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>次の数は2の何乗?<br><br>64<br>256<br>1024<br>4096</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>答え:</b><br>
<br>
<b>64 = 2⁶</b><br>
（2 × 2 × 2 × 2 × 2 × 2）<br>
<br>
<b>256 = 2⁸</b><br>
（64 × 4 = 2⁶ × 2²）<br>
<br>
<b>1024 = 2¹⁰</b><br>
（約1K、キロバイト）<br>
<br>
<b>4096 = 2¹²</b><br>
（1024 × 4 = 2¹⁰ × 2²）<br>
<br>
<hr>
<b>覚え方:</b><br>
• 64 → ロクヨン → 2⁶<br>
• 256 → ニーゴーロク → 2⁸<br>
• 1024 → せん → 2¹⁰
</div>''',
            'tags': ['powers', 'quiz']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("2の累乗暗記カード - シンプル版カード生成")
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

    # デッキとモデル名
    deck_name = "統計学"
    model_name = "Basic"

    # カード作成
    cards = create_powers_cards(deck_name, model_name)
    print(f"📝 {len(cards)}枚のカードを追加中...")

    cards_added = 0
    for i, card in enumerate(cards, 1):
        result = invoke_anki(
            'addNote',
            note={
                'deckName': deck_name,
                'modelName': model_name,
                'fields': {
                    'Front': card['front'],
                    'Back': card['back']
                },
                'tags': card['tags'],
                'options': {
                    'allowDuplicate': False
                }
            }
        )

        if result:
            cards_added += 1
            print(f"  ✓ カード{i}: 追加成功")
        else:
            print(f"  ⚠ カード{i}: スキップ（重複の可能性）")

    print()
    print("=" * 70)
    print("✨ 2の累乗カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()


if __name__ == "__main__":
    main()
