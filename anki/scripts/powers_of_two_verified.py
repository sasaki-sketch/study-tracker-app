#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2の累乗（Powers of 2） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「スタージェスの公式」
- 統計学情報局「スタージェスの公式」
- 複数の数学・IT教育サイトで検証済み
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


def create_powers_of_two_cards(deck_name, model_name):
    """2の累乗カードを作成（検証済み）"""

    cards = [
        # カード1: 2の累乗一覧（2^1〜2^10）
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【2の累乗】<br>2¹ 〜 2¹⁰ は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>2の累乗（2¹〜2¹⁰）:</b><br>
<br>

\\[2^1 = 2\\]
\\[2^2 = 4\\]
\\[2^3 = 8\\]
\\[2^4 = 16\\]
\\[2^5 = 32\\]
\\[2^6 = 64\\]
\\[2^7 = 128\\]
\\[2^8 = 256\\]
\\[2^9 = 512\\]
\\[2^{10} = 1024 \  （約1000）\\]
<br>

<hr>

<b>【覚え方】</b><br>
• 2倍ずつ増える<br>
• <b>2¹⁰ = 1024</b> を基準に覚える<br>
• 1024 ≈ 1K（キロ）<br>
<br>

<b>パターン:</b><br>
• 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024<br>
• 音読すると覚えやすい<br>
<br>

<hr>

<b>【統計検定2級での使用】</b><br>
• スタージェスの公式：k = 1 + log₂ n<br>
• log₂の計算に必要<br>
• 関数電卓不可のため暗記が重要<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
複数の教育サイトで検証済み<br>
統計検定2級での使用場面を確認
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'powers-of-two', 'memorization']
        },

        # カード2: 2の累乗一覧（2^11〜2^16）+ 覚え方
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【2の累乗】<br>2¹¹ 〜 2¹⁶ は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>2の累乗（2¹¹〜2¹⁶）:</b><br>
<br>

\\[2^{11} = 2048 \  （約2000）\\]
\\[2^{12} = 4096 \  （約4000）\\]
\\[2^{13} = 8192 \  （約8000）\\]
\\[2^{14} = 16384 \  （約16000）\\]
\\[2^{15} = 32768 \  （約32000）\\]
\\[2^{16} = 65536 \  （約65000）\\]
<br>

<hr>

<b>【覚え方】</b><br>
<br>

<b>基準を使う:</b><br>
• 2¹⁰ = 1024 を基準<br>
• 2¹¹ = 1024 × 2 = 2048<br>
• 2¹² = 1024 × 4 = 4096<br>
<br>

<b>倍々計算:</b><br>
• 2¹¹ = 2048<br>
• 2¹² = 2048 × 2 = 4096<br>
• 2¹³ = 4096 × 2 = 8192<br>
• 以降同様に2倍ずつ<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>コンピュータサイエンスでの意味:</b><br>
• 2⁸ = 256（1バイトで表現できる数）<br>
• 2¹⁰ ≈ 1KB（キロバイト）<br>
• 2¹⁶ = 65536 ≈ 64K<br>
• 2²⁰ ≈ 1MB（メガバイト）<br>
• 2³⁰ ≈ 1GB（ギガバイト）<br>
<br>

<b>統計検定2級では:</b><br>
• 主に2¹⁰までを使用<br>
• スタージェスの公式で必要<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
複数の教育サイトで検証済み<br>
コンピュータサイエンスでの使用例も確認
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'powers-of-two', 'memorization']
        },

        # カード3: スタージェスの公式での使用
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【2の累乗】<br>スタージェスの公式での使い方</b><br>
    <br>
    データ数 n = 64 のとき<br>
    階級数 k は？
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>スタージェスの公式:</b><br>
\\[k = 1 + \\log_2 n\\]
<br>

k: 階級数<br>
n: データ数<br>
<br>

<hr>

<b>解答:</b><br>
<br>

<b>ステップ1: log₂ 64 を求める</b><br>
64 = 2⁶ より<br>
log₂ 64 = 6<br>
<br>

<b>ステップ2: 公式に代入</b><br>
k = 1 + 6 = <b>7</b><br>
<br>

<b>答え:</b> 階級数は <b>7</b><br>
<br>

<hr>

<b>他の例:</b><br>
<br>

<b>n = 128 の場合:</b><br>
128 = 2⁷ より log₂ 128 = 7<br>
k = 1 + 7 = <b>8</b><br>
<br>

<b>n = 256 の場合:</b><br>
256 = 2⁸ より log₂ 256 = 8<br>
k = 1 + 8 = <b>9</b><br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>2の累乗なら簡単:</b><br>
n が2の累乗 (2^m) なら、log₂ n = m<br>
暗算で計算可能<br>
<br>

<b>2の累乗でない場合:</b><br>
• 2の累乗で挟む<br>
• 例: n = 100 の場合<br>
  64 < 100 < 128<br>
  2⁶ < 100 < 2⁷<br>
  → log₂ 100 は 6 と 7 の間<br>
  → k ≈ 7〜8<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「スタージェスの公式」<br>
統計学情報局で計算例を検証
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'powers-of-two', 'sturges', 'application']
        },

        # カード4: log₂の計算テクニック
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【2の累乗】<br>log₂ n の計算方法</b><br>
    <br>
    統計検定2級では<br>
    関数電卓が使えない！<br>
    <br>
    どうやって計算する？
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>方法1: 2で割り続ける</b><br>
<br>

n を2で割り続けて、何回割れるか数える<br>
<br>

<b>例: n = 64</b><br>
64 ÷ 2 = 32<br>
32 ÷ 2 = 16<br>
16 ÷ 2 = 8<br>
8 ÷ 2 = 4<br>
4 ÷ 2 = 2<br>
2 ÷ 2 = 1<br>
<br>
→ 6回割れた<br>
→ log₂ 64 = <b>6</b><br>
<br>

<hr>

<b>方法2: 2の累乗を使う</b><br>
<br>

2の累乗を暗記しておき、該当する値を探す<br>
<br>

<b>例: n = 128</b><br>
2⁷ = 128<br>
→ log₂ 128 = <b>7</b><br>
<br>

<hr>

<b>方法3: 範囲で推定（2の累乗でない場合）</b><br>
<br>

<b>例: n = 100</b><br>
2⁶ = 64 < 100 < 128 = 2⁷<br>
→ log₂ 100 は 6 と 7 の間<br>
→ より正確には 6.64...<br>
<br>

スタージェスの公式では:<br>
k = 1 + log₂ 100<br>
k ≈ 1 + 6.64 ≈ 7.64<br>
→ 四捨五入して k = <b>8</b><br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>統計検定2級での実践:</b><br>
• 2の累乗を暗記しておく（2¹〜2¹⁰）<br>
• 2の累乗で挟んで概算<br>
• 小数点以下は四捨五入<br>
<br>

<b>常用対数から計算（参考）:</b><br>
\\[\\log_2 n = \\frac{\\log_{10} n}{\\log_{10} 2} = \\frac{\\log_{10} n}{0.301}\\]
<br>

ただし、試験では関数電卓不可のため、<br>
上記の方法1〜3を使う<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計検定2級の受験体験談・Q&Aサイト<br>
計算方法を複数のソースで検証
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'powers-of-two', 'log2', 'calculation', 'technique']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("2の累乗 - 検証済みAnkiカード生成")
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
    deck_name = "統計学v2"
    model_name = "Basic"

    # カード作成
    cards = create_powers_of_two_cards(deck_name, model_name)
    print(f"📝 {len(cards)}枚のカードを追加中...")
    print()

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
                    'allowDuplicate': True
                }
            }
        )

        if result or result == 0:
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
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 2の累乗一覧（2¹〜2¹⁰）")
    print("  カード2: 2の累乗一覧（2¹¹〜2¹⁶）+ 覚え方")
    print("  カード3: スタージェスの公式での使用")
    print("  カード4: log₂の計算テクニック")
    print()


if __name__ == "__main__":
    main()
