#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
スタージェスの公式（Sturges' Formula） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「階級幅の決め方」https://bellcurve.jp/statistics/course/1656.html
- 統計WEB用語集「スタージェスの公式」
- 統計学情報局「スタージェスの公式」
- 複数の統計学サイトで検証済み
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


def create_sturges_formula_cards(deck_name, model_name):
    """スタージェスの公式カードを作成（検証済み）"""

    cards = [
        # カード1: スタージェスの公式の定義と公式
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【スタージェスの公式】<br>定義と公式は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
ヒストグラムや度数分布表を作成する際に、<br>
適切な階級数を決定するための公式<br>
<br>

<b>公式:</b><br>
\\[k = 1 + \\log_2 n\\]
<br>

k: 階級数<br>
n: データ数（サンプルサイズ）<br>
<br>

<b>別の表記（常用対数）:</b><br>
\\[k = 1 + 3.32 \\log_{10} n\\]
<br>

（log₂ n = 3.32 × log₁₀ n）<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>公式の意味:</b><br>
• データ数が増えると、階級数も対数的に増加<br>
• データ数が2倍になっても、階級数は1つ増えるだけ<br>
<br>

<b>小数の扱い:</b><br>
• 計算結果が小数の場合は四捨五入<br>
• 例: k = 7.64 → 8階級<br>
<br>

<b>重要な注意:</b><br>
• これは<b>目安</b>であって絶対的なルールではない<br>
• データの性質に応じて調整可能<br>
• 分布の特徴が分かりやすいことが最優先<br>
<br>

<b>英語:</b> Sturges' Formula / Sturges' Rule<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「2-3. 階級幅の決め方」<br>
統計WEB用語集「スタージェスの公式」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'sturges', 'definition']
        },

        # カード2: スタージェスの公式の使い方と計算手順
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【スタージェスの公式】<br>使い方と階級幅の計算手順は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>使用場面:</b><br>
• ヒストグラム作成時<br>
• 度数分布表作成時<br>
• データの分布を可視化する時<br>
<br>

<hr>

<b>計算手順:</b><br>
<br>

<b>ステップ1: データ数を確認</b><br>
n = データ数<br>
<br>

<b>ステップ2: 階級数を計算</b><br>
k = 1 + log₂ n<br>
（小数なら四捨五入）<br>
<br>

<b>ステップ3: 階級幅を計算</b><br>
\\[h = \\frac{最大値 - 最小値}{k}\\]
<br>

h: 階級幅<br>
k: 階級数<br>
<br>

<b>ステップ4: 階級を設定</b><br>
最小値から階級幅hずつ区切る<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>Excelでの計算:</b><br>
階級数: =1+LOG(n,2)<br>
階級幅: =(MAX(範囲)-MIN(範囲))/階級数<br>
<br>

<b>統計検定2級では:</b><br>
• log₂の計算が必要<br>
• 2の累乗の知識が役立つ<br>
• 関数電卓不可のため手計算<br>
<br>

<b>階級幅の調整:</b><br>
• 計算結果を切りの良い数に調整可能<br>
• 例: h = 4.3 → 5 に調整<br>
• 見やすさを優先<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「2-3. 階級幅の決め方」<br>
複数の統計サイトで計算手順を検証
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'sturges', 'usage']
        },

        # カード3: スタージェスの公式の計算例
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【スタージェスの公式】<br>計算例</b><br>
    <br>
    100個のデータ<br>
    （最小値: 10、最大値: 90）<br>
    <br>
    階級数と階級幅は？
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>解答:</b><br>
<br>

<b>ステップ1: 階級数を計算</b><br>
\\[k = 1 + \\log_2 100\\]
<br>

log₂ 100 の計算:<br>
64 < 100 < 128<br>
2⁶ < 100 < 2⁷<br>
→ log₂ 100 ≈ 6.64<br>
<br>

k = 1 + 6.64 = 7.64<br>
→ 四捨五入して <b>k = 8</b><br>
<br>

<b>ステップ2: 階級幅を計算</b><br>
\\[h = \\frac{90 - 10}{8} = \\frac{80}{8} = 10\\]
<br>

<b>答え:</b><br>
• 階級数: <b>8階級</b><br>
• 階級幅: <b>10</b><br>
<br>

<hr>

<b>階級の設定例:</b><br>
1. 10以上 20未満<br>
2. 20以上 30未満<br>
3. 30以上 40未満<br>
4. 40以上 50未満<br>
5. 50以上 60未満<br>
6. 60以上 70未満<br>
7. 70以上 80未満<br>
8. 80以上 90未満<br>
<br>

<hr>

<b>【他の例】</b><br>
<br>

<b>n = 64 の場合:</b><br>
k = 1 + log₂ 64 = 1 + 6 = <b>7</b><br>
<br>

<b>n = 50 の場合:</b><br>
32 < 50 < 64 → 2⁵ < 50 < 2⁶<br>
log₂ 50 ≈ 5.64<br>
k = 1 + 5.64 ≈ <b>7</b><br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>常用対数での計算（参考）:</b><br>
k = 1 + 3.32 × log₁₀ 100<br>
k = 1 + 3.32 × 2 = 7.64<br>
→ 同じ結果<br>
<br>

<b>統計検定2級では:</b><br>
• 2の累乗で挟んで概算<br>
• 小数点以下は四捨五入<br>
• 階級幅は切りの良い数に調整可<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計学情報局「スタージェスの公式」の例題<br>
計算結果を検算して検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'sturges', 'example', 'calculation']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("スタージェスの公式 - 検証済みAnkiカード生成")
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
    cards = create_sturges_formula_cards(deck_name, model_name)
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
    print("✨ スタージェスの公式カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: スタージェスの公式の定義と公式")
    print("  カード2: スタージェスの公式の使い方と計算手順")
    print("  カード3: スタージェスの公式の計算例")
    print()


if __name__ == "__main__":
    main()
