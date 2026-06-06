#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
11²から20²までの2乗（Squares from 11² to 20²） - 検証済みAnkiカード
統計検定2級対策・数学基礎

情報源：
- 天才村木の勉強道場「二乗の数の覚え方(11から19)」
- 秀英予備校「一の位が5である自然数の2乗 一瞬で暗算しよう」
- 複数の数学教育サイトで検証済み
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


def create_squares_11_to_20_cards(deck_name, model_name):
    """11²から20²までの2乗カードを作成（検証済み）"""

    cards = [
        # カード1: 11²から15²（語呂合わせ + 5で終わる数の法則）
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【2乗の暗記】<br>11² から 15² は？<br>語呂合わせで覚えよう！</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>11² から 15² の値:</b><br>
<br>

<table border="1" style="border-collapse:collapse; width:100%;">
<tr style="background-color:#f0f0f0;">
  <th>計算</th>
  <th>答え</th>
  <th>語呂合わせ</th>
</tr>
<tr>
  <td style="font-size:22px;">\\(11^2\\)</td>
  <td style="font-size:22px; font-weight:bold;">121</td>
  <td>いい<b>いい</b>、<b>人に人</b></td>
</tr>
<tr>
  <td style="font-size:22px;">\\(12^2\\)</td>
  <td style="font-size:22px; font-weight:bold;">144</td>
  <td><b>胃に胃に</b>、<b>石</b>よ</td>
</tr>
<tr>
  <td style="font-size:22px;">\\(13^2\\)</td>
  <td style="font-size:22px; font-weight:bold;">169</td>
  <td><b>いざいざ</b>、<b>イチロー</b>君</td>
</tr>
<tr>
  <td style="font-size:22px;">\\(14^2\\)</td>
  <td style="font-size:22px; font-weight:bold;">196</td>
  <td><b>ドシドシ</b>、<b>一苦労</b></td>
</tr>
<tr style="background-color:#fff9e6;">
  <td style="font-size:22px;">\\(15^2\\)</td>
  <td style="font-size:22px; font-weight:bold;">225</td>
  <td><b>イチゴイチゴ</b>に<b>ニコッ</b></td>
</tr>
</table>
<br>

<hr>

<b>【5で終わる数の特別な計算法】</b><br>
<br>

<b>公式:</b><br>
一の位が5の2乗 = <b>十の位 × (十の位 + 1)</b> の後ろに <b>25</b><br>
<br>

<b>15²の計算:</b><br>
• 十の位 = 1<br>
• 1 × (1 + 1) = 1 × 2 = 2<br>
• 2の後ろに25 → <b>225</b> ✓<br>
<br>

<b>25²の計算:</b><br>
• 十の位 = 2<br>
• 2 × (2 + 1) = 2 × 3 = 6<br>
• 6の後ろに25 → <b>625</b> ✓<br>
<br>

<b>35²の計算:</b><br>
• 十の位 = 3<br>
• 3 × (3 + 1) = 3 × 4 = 12<br>
• 12の後ろに25 → <b>1225</b> ✓<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>なぜ覚える必要があるのか:</b><br>
• 平方根の計算（\\(\\sqrt{144} = 12\\)）<br>
• 三平方の定理（\\(3^2 + 4^2 = 5^2\\)）<br>
• 円の面積計算<br>
• 統計検定での時短<br>
<br>

<b>覚え方のコツ:</b><br>
• 語呂合わせを声に出す<br>
• 5で終わる数は公式で計算<br>
• 毎日1回復習する<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
天才村木の勉強道場「二乗の数の覚え方(11から19)」<br>
秀英予備校「一の位が5である自然数の2乗」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['mathematics', 'verified', 'squares', 'memorization', '11-15']
        },

        # カード2: 16²から19²（語呂合わせ）
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【2乗の暗記】<br>16² から 19² は？<br>語呂合わせで覚えよう！</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>16² から 19² の値:</b><br>
<br>

<table border="1" style="border-collapse:collapse; width:100%;">
<tr style="background-color:#f0f0f0;">
  <th>計算</th>
  <th>答え</th>
  <th>語呂合わせ</th>
</tr>
<tr>
  <td style="font-size:22px;">\\(16^2\\)</td>
  <td style="font-size:22px; font-weight:bold;">256</td>
  <td><b>イロイロ煮込む</b></td>
</tr>
<tr>
  <td style="font-size:22px;">\\(17^2\\)</td>
  <td style="font-size:22px; font-weight:bold;">289</td>
  <td><b>ドナドナ二拍</b>、いーないーな二泊</td>
</tr>
<tr>
  <td style="font-size:22px;">\\(18^2\\)</td>
  <td style="font-size:22px; font-weight:bold;">324</td>
  <td><b>イヤイヤ、ミニ</b>よ</td>
</tr>
<tr>
  <td style="font-size:22px;">\\(19^2\\)</td>
  <td style="font-size:22px; font-weight:bold;">361</td>
  <td><b>イクイク、寒い</b>とこ</td>
</tr>
</table>
<br>

<hr>

<b>【別の覚え方: パターン認識】</b><br>
<br>

<b>11-19の2乗の計算パターン:</b><br>
\\[(10 + a)^2 = 100 + 20a + a^2\\]
<br>

<b>例: 16²の計算</b><br>
\\(16^2 = (10 + 6)^2 = 100 + 20 \\times 6 + 6^2\\)<br>
\\(= 100 + 120 + 36 = 256\\) ✓<br>
<br>

<b>例: 18²の計算</b><br>
\\(18^2 = (10 + 8)^2 = 100 + 20 \\times 8 + 8^2\\)<br>
\\(= 100 + 160 + 64 = 324\\) ✓<br>
<br>

<b>手順:</b><br>
1. 100を基準にする<br>
2. 一の位を20倍して足す<br>
3. 一の位の2乗を足す<br>
<br>

<hr>

<b>【数値の特徴】</b><br>
<br>

<b>16² = 256:</b><br>
• 2⁸ = 256（2の8乗と同じ！）<br>
• コンピュータで重要な数<br>
<br>

<b>17² = 289:</b><br>
• 素数17の2乗<br>
<br>

<b>18² = 324:</b><br>
• 324 = 18 × 18<br>
• 3で割り切れる（3² = 9の倍数）<br>
<br>

<b>19² = 361:</b><br>
• 素数19の2乗<br>
• 400に近い（20² = 400）<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>覚えるべき理由:</b><br>
• 平方根の逆算（\\(\\sqrt{256} = 16\\)）<br>
• 因数分解の高速化<br>
• 概算の精度向上<br>
<br>

<b>覚え方のコツ:</b><br>
• 語呂合わせを繰り返す<br>
• パターン計算で確認<br>
• 毎日復習する<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
天才村木の勉強道場「二乗の数の覚え方(11から19)」<br>
複数の数学教育サイトで検証済み
</div>

</div>
''',
            'tags': ['mathematics', 'verified', 'squares', 'memorization', '16-19']
        },

        # カード3: 20²と全体のまとめ
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【2乗の暗記】<br>20² と 11²〜20² の<br>一覧まとめ</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>20²:</b><br>
\\[20^2 = (2 \\times 10)^2 = 4 \\times 100 = \\mathbf{400}\\]
<br>

簡単！覚える必要なし。<br>
<br>

<hr>

<b>【11²〜20² 完全一覧】</b><br>
<br>

<table border="1" style="border-collapse:collapse; width:100%;">
<tr style="background-color:#f0f0f0;">
  <th>計算</th>
  <th>答え</th>
  <th>計算</th>
  <th>答え</th>
</tr>
<tr>
  <td>\\(11^2\\)</td>
  <td><b>121</b></td>
  <td>\\(16^2\\)</td>
  <td><b>256</b></td>
</tr>
<tr>
  <td>\\(12^2\\)</td>
  <td><b>144</b></td>
  <td>\\(17^2\\)</td>
  <td><b>289</b></td>
</tr>
<tr>
  <td>\\(13^2\\)</td>
  <td><b>169</b></td>
  <td>\\(18^2\\)</td>
  <td><b>324</b></td>
</tr>
<tr>
  <td>\\(14^2\\)</td>
  <td><b>196</b></td>
  <td>\\(19^2\\)</td>
  <td><b>361</b></td>
</tr>
<tr style="background-color:#fff9e6;">
  <td>\\(15^2\\)</td>
  <td><b>225</b></td>
  <td>\\(20^2\\)</td>
  <td><b>400</b></td>
</tr>
</table>
<br>

<hr>

<b>【効率的な覚え方まとめ】</b><br>
<br>

<b>方法1: 語呂合わせ（11²〜19²）</b><br>
• いいいい、人に人（121）<br>
• 胃に胃に石よ（144）<br>
• いざいざ、イチロー君（169）<br>
• ドシドシ、一苦労（196）<br>
• イチゴイチゴにニコッ（225）<br>
• イロイロ煮込む（256）<br>
• ドナドナ二拍（289）<br>
• イヤイヤ、ミニよ（324）<br>
• イクイク、寒いとこ（361）<br>
<br>

<b>方法2: 5で終わる数の公式</b><br>
\\(n5^2 = n \\times (n+1) の後ろに 25\\)<br>
• 15² = 1×2 = 2 → 225<br>
• 25² = 2×3 = 6 → 625<br>
<br>

<b>方法3: パターン計算（11〜19）</b><br>
\\((10+a)^2 = 100 + 20a + a^2\\)<br>
<br>

<hr>

<b>【平方根との関係】</b><br>
<br>

2乗を覚えれば、平方根の逆算が即座にできる:<br>
<br>

• \\(\\sqrt{121} = 11\\)<br>
• \\(\\sqrt{144} = 12\\)<br>
• \\(\\sqrt{169} = 13\\)<br>
• \\(\\sqrt{196} = 14\\)<br>
• \\(\\sqrt{225} = 15\\)<br>
• \\(\\sqrt{256} = 16\\)<br>
• \\(\\sqrt{289} = 17\\)<br>
• \\(\\sqrt{324} = 18\\)<br>
• \\(\\sqrt{361} = 19\\)<br>
• \\(\\sqrt{400} = 20\\)<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>活用場面:</b><br>
• 三平方の定理（\\(a^2 + b^2 = c^2\\)）<br>
• 平方根の計算<br>
• 因数分解（\\(x^2 - 169 = (x-13)(x+13)\\)）<br>
• 統計検定での分散計算<br>
• 円の面積（\\(\\\pi r^2\\)）<br>
<br>

<b>暗記のコツ:</b><br>
• 毎日少しずつ復習<br>
• 語呂合わせを声に出す<br>
• 平方根とセットで覚える<br>
• 実際の計算で使ってみる<br>
<br>

<b>統計検定2級では:</b><br>
• 分散・標準偏差の計算で必要<br>
• カイ二乗分布の理解<br>
• 時間短縮に役立つ<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
天才村木の勉強道場「二乗の数の覚え方(11から19)」<br>
複数の数学教育サイトで検証済み
</div>

</div>
''',
            'tags': ['mathematics', 'verified', 'squares', 'summary', '20', 'square-root']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("11²から20²までの2乗 - 検証済みAnkiカード生成")
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
    cards = create_squares_11_to_20_cards(deck_name, model_name)
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
    print("✨ 11²から20²までの2乗カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 11²から15²（語呂合わせ + 5で終わる数の法則）")
    print("  カード2: 16²から19²（語呂合わせ + パターン計算）")
    print("  カード3: 20²と全体のまとめ（一覧 + 平方根との関係）")
    print()


if __name__ == "__main__":
    main()
