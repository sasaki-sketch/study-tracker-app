#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
トリム平均（Trimmed Mean） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「いろいろな平均」https://bellcurve.jp/statistics/course/4324.html
- 統計学情報局「トリム平均の意味と計算の方法」
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


def create_trimmed_mean_cards(deck_name, model_name):
    """トリム平均カードを作成（検証済み）"""

    cards = [
        # カード1: トリム平均の定義と公式
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【トリム平均】<br>定義と公式は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
データを小さい順に並べたとき、<br>
小さい側と大きい側からそれぞれ指定した個数の値を除き、<br>
残ったデータのみから求める平均<br>
<br>

<b>別名:</b><br>
• 調整平均（ちょうせいへいきん）<br>
• 刈込み平均（かりこみへいきん）<br>
<br>

<b>公式:</b><br>
大小k個ずつ除いた場合:<br>
\\[\\bar{x}_k = \\frac{1}{n-2k} \\sum_{i=k+1}^{n-k} x_i\\]
<br>

n: データ総数<br>
k: 片側から除外する個数<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>○○％トリム平均の意味:</b><br>
• 「10％トリム平均」= 片側10％ずつ除外<br>
• つまり、両側合わせて20％を除外<br>
<br>

<b>特殊なケース:</b><br>
• 0％トリム平均 = 通常の算術平均<br>
• 25％トリム平均 = 中央平均（真ん中50％のみ使用）<br>
• さらに極端な場合 → 中央値<br>
<br>

<b>英語:</b> Trimmed Mean<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-4. いろいろな平均」<br>
統計学情報局「トリム平均の意味と計算の方法」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'trimmed-mean', 'definition']
        },

        # カード2: トリム平均の使い方と使用場面
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【トリム平均】<br>いつ使う？<br>なぜ使う？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>トリム平均を使う理由:</b><br>
<b>外れ値や異常値の影響を軽減</b>するため<br>
<br>

通常の算術平均は、極端な値の影響を大きく受けるため、<br>
データの代表値として適切でない場合がある<br>
<br>

<hr>

<b>トリム平均を使う場面:</b><br>
<br>

<b>1. スポーツの採点</b><br>
• 体操競技やフィギュアスケート<br>
• 最高点と最低点を除外して平均<br>
• 審判の偏りを排除<br>
<br>

<b>2. 外れ値を含むデータ</b><br>
• 所得データ（超高額所得者の影響を除く）<br>
• 実験データ（測定ミスの影響を除く）<br>
• アンケート結果（極端な回答を除く）<br>
<br>

<b>3. 頑健な統計量が必要な場合</b><br>
• ロバスト統計（robust statistics）<br>
• 外れ値に対して頑健な推定<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>トリム平均の特徴:</b><br>
• 外れ値の影響を受けにくい<br>
• 中央値より情報を多く保持<br>
• 算術平均より頑健<br>
<br>

<b>どのくらい除外するか:</b><br>
• 5％〜25％が一般的<br>
• データの性質によって調整<br>
• 除外しすぎると情報損失<br>
<br>

<b>統計検定2級では:</b><br>
• 算術平均との使い分けを理解<br>
• 外れ値への対処方法として重要<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-4. いろいろな平均」<br>
複数の統計サイトで使用場面を検証
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'trimmed-mean', 'usage']
        },

        # カード3: トリム平均の計算例
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【トリム平均】<br>計算例: 10％トリム平均</b><br>
    <br>
    以下のデータの10％トリム平均は？<br>
    <br>
    11, 12, 14, 15, 16, 18, 18, 19, 19, 25<br>
    （10個のデータ）
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>解答:</b><br>
<br>

<b>ステップ1: データを並べる</b><br>
11, 12, 14, 15, 16, 18, 18, 19, 19, 25<br>
（すでに昇順に並んでいる）<br>
<br>

<b>ステップ2: 除外する個数を計算</b><br>
10％トリム平均 = 片側10％ずつ除外<br>
10個 × 10％ = 1個<br>
→ 片側から1個ずつ除外<br>
<br>

<b>ステップ3: 両端を除外</b><br>
<s>11</s>, 12, 14, 15, 16, 18, 18, 19, 19, <s>25</s><br>
→ 最小値11と最大値25を除外<br>
<br>

<b>ステップ4: 残りのデータの平均を計算</b><br>
\\[\\bar{x}_{10\\%} = \\frac{12+14+15+16+18+18+19+19}{8}\\]
<br>

\\[= \\frac{131}{8} = 16.375\\]
<br>

<b>答え:</b> 10％トリム平均 = <b>16.375</b><br>
<br>

<hr>

<b>比較:</b><br>
<br>

<b>通常の算術平均:</b><br>
(11+12+14+15+16+18+18+19+19+25) / 10 = 16.7<br>
<br>

<b>10％トリム平均:</b><br>
16.375<br>
<br>

→ 最大値25の影響が軽減されている<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>除外個数の計算:</b><br>
• n × (除外割合) = 除外個数（片側）<br>
• 小数になる場合は切り捨て<br>
<br>

<b>Excelでの計算（注意！）:</b><br>
=TRIMMEAN(データ範囲, 0.2)<br>
→ Excelは「両側合計」の割合を指定<br>
→ 10％トリム平均なら0.2を指定<br>
<br>

<b>公式:</b><br>
\\[\\bar{x}_k = \\frac{1}{n-2k} \\sum_{i=k+1}^{n-k} x_i\\]
<br>
この例では: n=10, k=1<br>
\\[\\bar{x}_1 = \\frac{1}{10-2} \\sum_{i=2}^{9} x_i = \\frac{131}{8}\\]
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計学情報局「トリム平均の意味と計算の方法」の例題<br>
計算結果を検算して検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'trimmed-mean', 'example', 'calculation']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("トリム平均 - 検証済みAnkiカード生成")
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
    cards = create_trimmed_mean_cards(deck_name, model_name)
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
    print("✨ トリム平均カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: トリム平均の定義と公式")
    print("  カード2: トリム平均の使い方と使用場面")
    print("  カード3: トリム平均の計算例（10％トリム平均）")
    print()


if __name__ == "__main__":
    main()
