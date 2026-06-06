#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
幾何平均（Geometric Mean） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「いろいろな平均」https://bellcurve.jp/statistics/course/4324.html
- 統計WEB用語集「幾何平均」https://bellcurve.jp/statistics/glossary/872.html
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


def create_geometric_mean_cards(deck_name, model_name):
    """幾何平均カードを作成（検証済み）"""

    cards = [
        # カード1: 幾何平均の定義と公式
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【幾何平均】<br>定義と公式は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
n個の正の数の積のn乗根<br>
別名: 相乗平均（そうじょうへいきん）<br>
<br>

<b>公式:</b><br>
\\[\\bar{x}_G = \\sqrt[n]{x_1 \\times x_2 \\times \\cdots \\times x_n}\\]
<br>

または対数を使って:<br>
\\[\\log \\bar{x}_G = \\frac{1}{n} \\sum_{i=1}^{n} \\log x_i\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
• すべての値は正の数でなければならない<br>
• 比率や成長率の平均に使用<br>
• 算術平均とは使い分けが必要<br>
<br>

<b>英語:</b> Geometric Mean<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-4. いろいろな平均」<br>
統計WEB用語集「幾何平均」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'geometric-mean', 'definition']
        },

        # カード2: 幾何平均の使い方と使用場面
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【幾何平均】<br>いつ使う？<br>算術平均との使い分けは？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>幾何平均を使う場面:</b><br>
• <b>比率や割合で変化するデータ</b>の平均<br>
• <b>成長率</b>の平均<br>
• <b>変化率</b>の平均<br>
• 複利計算<br>
<br>

<b>具体例:</b><br>
• 年平均成長率（CAGR）<br>
• 投資リターンの平均<br>
• 物価上昇率の平均<br>
• 人口増加率の平均<br>
<br>

<hr>

<b>算術平均との使い分け:</b><br>
<br>

<b>幾何平均:</b><br>
• 乗法的な変化（倍率）<br>
• 1.2倍 × 1.1倍 × 1.15倍 → 幾何平均<br>
<br>

<b>算術平均:</b><br>
• 加法的な変化（差分）<br>
• 10点 + 20点 + 30点 → 算術平均<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<b>統計検定2級では:</b><br>
• 算術平均と幾何平均の使い分けがよく出題される<br>
• 「成長率」「変化率」のキーワードに注目<br>
<br>

<b>平均の大小関係:</b><br>
調和平均 ≤ 幾何平均 ≤ 算術平均<br>
（すべて正の数で、等号は全て同じ値の時のみ成立）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-4. いろいろな平均」<br>
複数の統計サイトで使用場面を検証
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'geometric-mean', 'usage']
        },

        # カード3: 幾何平均の計算例
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【幾何平均】<br>計算例: 家賃の年平均上昇率</b><br>
    <br>
    過去3年間の家賃上昇率:<br>
    • 1年目: 20%上昇（1.2倍）<br>
    • 2年目: 10%上昇（1.1倍）<br>
    • 3年目: 15%上昇（1.15倍）<br>
    <br>
    年平均上昇率は？
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>解答:</b><br>
<br>

<b>ステップ1: 幾何平均を使う理由</b><br>
成長率（倍率）の平均を求めるため、幾何平均を使用<br>
<br>

<b>ステップ2: 公式を適用</b><br>
\\[\\bar{x}_G = \\sqrt[3]{1.2 \\times 1.1 \\times 1.15}\\]
<br>

<b>ステップ3: 計算</b><br>
\\[\\bar{x}_G = \\sqrt[3]{1.518} = 1.149\\]
<br>

<b>答え:</b><br>
年平均上昇率は <b>約14.9%</b><br>
（1.149 - 1 = 0.149 = 14.9%）<br>
<br>

<hr>

<b>検算:</b><br>
3年間で1.149 × 1.149 × 1.149 ≈ 1.518<br>
元の積1.2 × 1.1 × 1.15 = 1.518 ✓<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>算術平均を使うと間違い:</b><br>
(1.2 + 1.1 + 1.15) / 3 = 1.15 (15%)<br>
→ これは正しくない！<br>
<br>

<b>理由:</b><br>
成長率は乗法的に作用するため、<br>
単純な算術平均では実際の成長と一致しない<br>
<br>

<b>計算方法（一般電卓の場合）:</b><br>
統計検定2級では関数電卓が使えないため、<br>
3乗根は √ を複数回使う<br>
例: ∛x = √(√(√x)) ← 誤り<br>
正しくは: ∛x ≈ x^(1/3) を近似計算<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-4. いろいろな平均」の例題<br>
計算結果を検算して検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'geometric-mean', 'example', 'calculation']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("幾何平均 - 検証済みAnkiカード生成")
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
    cards = create_geometric_mean_cards(deck_name, model_name)
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

        # deleteNotesと同様、addNoteも成功時にノートIDまたはNoneを返す可能性
        if result or result == 0:
            cards_added += 1
            print(f"  ✓ カード{i}: 追加成功")
        else:
            print(f"  ⚠ カード{i}: スキップ（重複の可能性）")

    print()
    print("=" * 70)
    print("✨ 幾何平均カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 幾何平均の定義と公式")
    print("  カード2: 幾何平均の使い方と使用場面")
    print("  カード3: 幾何平均の計算例（家賃上昇率）")
    print()


if __name__ == "__main__":
    main()
