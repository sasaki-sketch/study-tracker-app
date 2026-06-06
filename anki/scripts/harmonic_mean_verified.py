#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
調和平均（Harmonic Mean） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「いろいろな平均」https://bellcurve.jp/statistics/course/4324.html
- 統計WEB用語集「調和平均」https://bellcurve.jp/statistics/glossary/1436.html
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


def create_harmonic_mean_cards(deck_name, model_name):
    """調和平均カードを作成（検証済み）"""

    cards = [
        # カード1: 調和平均の定義と公式
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【調和平均】<br>定義と公式は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
観測値の逆数の算術平均の逆数<br>
<br>

<b>公式:</b><br>
\\[\\bar{x}_H = \\frac{n}{\\frac{1}{x_1} + \\frac{1}{x_2} + \\cdots + \\frac{1}{x_n}}\\]
<br>

総和記号を使うと:<br>
\\[\\bar{x}_H = \\frac{n}{\\sum_{i=1}^{n} \\frac{1}{x_i}}\\]
<br>

または:<br>
\\[\\frac{1}{\\bar{x}_H} = \\frac{1}{n} \\sum_{i=1}^{n} \\frac{1}{x_i}\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• すべての値は正の数でなければならない<br>
• 0や負の数は含めない（逆数が計算できない）<br>
• 速度や率の平均に使用<br>
• 算術平均とは使い分けが必要<br>
<br>

<b>平均の大小関係:</b><br>
調和平均 ≤ 幾何平均 ≤ 算術平均<br>
（すべて正の数で、等号は全て同じ値の時のみ成立）<br>
<br>

<b>英語:</b> Harmonic Mean<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-4. いろいろな平均」<br>
統計WEB用語集「調和平均」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'harmonic-mean', 'definition']
        },

        # カード2: 調和平均の使い方と使用場面
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【調和平均】<br>いつ使う？<br>算術平均との使い分けは？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>調和平均を使う場面:</b><br>
• <b>往復の平均速度</b>を求める時<br>
• <b>同じ距離を異なる速度</b>で移動した場合<br>
• <b>速度や率</b>の平均<br>
• 仕事の処理速度の平均<br>
<br>

<b>具体例:</b><br>
• 往復の平均時速<br>
• 複数の処理速度の平均<br>
• 異なる作業効率の平均<br>
<br>

<hr>

<b>算術平均との使い分け:</b><br>
<br>

<b>調和平均:</b><br>
• <b>同じ距離</b>を異なる速度で移動<br>
• 速度や率（分母が変化する量）<br>
• 例: 行き60km/h、帰り80km/h → 調和平均<br>
<br>

<b>算術平均:</b><br>
• <b>同じ時間</b>を異なる速度で移動<br>
• 通常の数値の平均<br>
• 例: 1時間60km、1時間80km → 算術平均<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<b>統計検定2級では:</b><br>
• 速度問題で算術平均と調和平均の使い分けが出題される<br>
• 「同じ距離」なら調和平均<br>
• 「同じ時間」なら算術平均<br>
<br>

<b>調和平均の特徴:</b><br>
• 算術平均より小さい値になる<br>
• 小さい値の影響を大きく受ける<br>
• 分母が小さくなると全体が大きくなる性質を反映<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-4. いろいろな平均」<br>
複数の統計サイトで使用場面を検証
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'harmonic-mean', 'usage']
        },

        # カード3: 調和平均の計算例
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【調和平均】<br>計算例: 往復の平均時速</b><br>
    <br>
    ドライブで:<br>
    • 行き: 時速60km<br>
    • 帰り: 時速80km<br>
    <br>
    往復の平均時速は？
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>解答:</b><br>
<br>

<b>ステップ1: 調和平均を使う理由</b><br>
「同じ距離」を異なる速度で往復したため、<br>
調和平均を使用<br>
<br>

<b>ステップ2: 公式を適用</b><br>
\\[\\bar{x}_H = \\frac{2}{\\frac{1}{60} + \\frac{1}{80}}\\]
<br>

<b>ステップ3: 計算</b><br>
\\[\\frac{1}{60} + \\frac{1}{80} = \\frac{4}{240} + \\frac{3}{240} = \\frac{7}{240}\\]
<br>

\\[\\bar{x}_H = \\frac{2}{\\frac{7}{240}} = \\frac{2 \\times 240}{7} = \\frac{480}{7} \\approx 68.57\\]
<br>

<b>答え:</b><br>
往復の平均時速は <b>約68.57 km/h</b><br>
<br>

<hr>

<b>検証:</b><br>
例えば240km往復した場合:<br>
• 行き: 240km ÷ 60km/h = 4時間<br>
• 帰り: 240km ÷ 80km/h = 3時間<br>
• 合計: 480km ÷ 7時間 = 68.57km/h ✓<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>算術平均を使うと間違い:</b><br>
(60 + 80) / 2 = 70 km/h<br>
→ これは正しくない！<br>
<br>

<b>理由:</b><br>
遅い速度の区間では時間がかかるため、<br>
単純な算術平均では実際の平均速度より高くなる<br>
<br>

<b>覚え方:</b><br>
• <b>同じ距離</b> → 調和平均<br>
• <b>同じ時間</b> → 算術平均<br>
<br>

<b>調和平均の性質:</b><br>
調和平均(68.57) < 算術平均(70)<br>
調和平均は常に算術平均以下になる<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-4. いろいろな平均」の例題<br>
計算結果を検算して検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'harmonic-mean', 'example', 'calculation']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("調和平均 - 検証済みAnkiカード生成")
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
    cards = create_harmonic_mean_cards(deck_name, model_name)
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
    print("✨ 調和平均カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 調和平均の定義と公式")
    print("  カード2: 調和平均の使い方と使用場面")
    print("  カード3: 調和平均の計算例（往復の平均時速）")
    print()


if __name__ == "__main__":
    main()
