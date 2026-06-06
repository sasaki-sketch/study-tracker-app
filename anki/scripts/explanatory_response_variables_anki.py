#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
説明変数と目的変数 - Ankiカード生成（コンパクト5枚版）
基本定義/見分け方/具体例/回帰分析 - 統計検定2級レベル
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


def create_variable_cards(deck_name, model_name):
    """説明変数・目的変数カードを作成（5枚厳選）"""

    cards = [
        # カード1: 基本定義（最重要）
        {
            'front': '<div class="question"><h3>説明変数と目的変数の違いは?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">説明変数 = 原因(X)　/　目的変数 = 結果(Y)</h3>

<div class="mnemonic">
<strong>💡 一言で覚える:</strong>
<p style="font-size:24px; margin:15px 0;">
<strong>説明</strong>変数 → <font color="#3498db">「Xで説明する側」</font><br>
<strong>目的</strong>変数 → <font color="#e74c3c">「Yを予測する目的」</font>
</p>
</div>

<div class="context">
<strong>📊 回帰分析での関係:</strong>
<p style="font-size:22px; margin:15px 0;">
<strong>Y = α + βX</strong>
</p>
<p>
<strong><font color="#e74c3c">Y</font></strong> = 目的変数（従属変数、被説明変数）<br>
<strong><font color="#3498db">X</font></strong> = 説明変数（独立変数、予測変数）<br>
α, β = 係数
</p>
</div>

<div class="mnemonic">
<strong>🎯 究極の覚え方:</strong>
<table style="width:100%; margin-top:15px; font-size:20px; border-collapse: collapse;">
<tr style="background:#e8f4f8; font-weight:bold;">
<td style="padding:12px; border:1px solid #ddd;"></td>
<td style="padding:12px; border:1px solid #ddd;">説明変数</td>
<td style="padding:12px; border:1px solid #ddd;">目的変数</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;"><strong>別名</strong></td>
<td style="padding:10px; border:1px solid #ddd;">独立変数、予測変数</td>
<td style="padding:10px; border:1px solid #ddd;">従属変数、被説明変数</td>
</tr>
<tr style="background:#f8f9fa;">
<td style="padding:10px; border:1px solid #ddd;"><strong>記号</strong></td>
<td style="padding:10px; border:1px solid #ddd;">X</td>
<td style="padding:10px; border:1px solid #ddd;">Y</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;"><strong>役割</strong></td>
<td style="padding:10px; border:1px solid #ddd;">原因・入力</td>
<td style="padding:10px; border:1px solid #ddd;">結果・出力</td>
</tr>
<tr style="background:#f8f9fa;">
<td style="padding:10px; border:1px solid #ddd;"><strong>英語</strong></td>
<td style="padding:10px; border:1px solid #ddd;">Explanatory</td>
<td style="padding:10px; border:1px solid #ddd;">Response/Objective</td>
</tr>
</table>
</div>
</div>''',
            'tags': ['variables', 'explanatory-response', 'definition', 'essential', 'statistics-exam']
        },

        # カード2: 見分け方（判定方法）
        {
            'front': '<div class="question"><h3>説明変数と目的変数を見分ける方法は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">「何を予測したいか?」を考える</h3>

<div class="mnemonic">
<strong>💡 見分けフローチャート:</strong>
<p style="line-height:2.2; margin-top:15px;">
<strong>ステップ1:</strong> 「何を知りたい?」 → <span style="color:#e74c3c;">目的変数(Y)</span><br>
<strong>ステップ2:</strong> 「何で予測する?」 → <span style="color:#3498db;">説明変数(X)</span>
</p>
</div>

<div class="context">
<strong>📊 具体的な質問で判定:</strong>
<table style="width:100%; margin-top:15px; font-size:19px; border-collapse: collapse;">
<tr style="background:#f8f9fa; font-weight:bold;">
<td style="padding:10px; border:1px solid #ddd;">質問</td>
<td style="padding:10px; border:1px solid #ddd;">目的変数</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;">「〜に影響される」</td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
</tr>
<tr style="background:#f8f9fa;">
<td style="padding:10px; border:1px solid #ddd;">「〜を予測したい」</td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;">「〜が結果」</td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
</tr>
</table>
<p style="margin-top:10px;">
これらに当てはまらない方が<strong>説明変数</strong>
</p>
</div>

<div class="mnemonic">
<strong>🎯 魔法の質問:</strong>
<p style="font-size:22px; margin:15px 0;">
<strong>「Xが変わると、Yが変わる?」</strong>
</p>
<p>
→ YES なら X=説明変数、Y=目的変数<br>
→ 因果関係の方向を意識!
</p>
</div>
</div>''',
            'tags': ['variables', 'how-to-distinguish', 'essential', 'statistics-exam']
        },

        # カード3: 具体例での練習（ビジネス例）
        {
            'front': '<div class="question"><h3>「広告費と売上の関係」で、説明変数と目的変数はどっち?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">説明変数 = 広告費(X)　/　目的変数 = 売上(Y)</h3>

<div class="mnemonic">
<strong>💡 判定理由:</strong>
<p>「広告費を増やすと、売上が増えるか?」</p>
<p style="margin-top:10px;">
→ <strong>広告費が原因、売上が結果</strong><br>
→ 広告費 = X（説明変数）<br>
→ 売上 = Y（目的変数）
</p>
</div>

<div class="context">
<strong>📊 回帰式:</strong>
<p style="font-size:22px; margin:15px 0;">
売上 = α + β × 広告費
</p>
<p>
例: 売上 = 100万 + 5 × 広告費<br>
→ 広告費10万円なら、売上150万円と予測
</p>
</div>

<div class="mnemonic">
<strong>🎯 よくある間違い:</strong>
<p>❌ 「売上を説明変数にしたい」</p>
<p>→ でも「売上で広告費を予測」は不自然</p>
<p style="margin-top:10px;">
✅ 因果の方向を意識:<br>
「広告費 → 売上」の影響を調べる
</p>
</div>
</div>''',
            'tags': ['variables', 'business-example', 'practice', 'statistics-exam']
        },

        # カード4: 具体例での練習（医療・健康例）
        {
            'front': '<div class="question"><h3>「運動時間と体重減少」で、説明変数と目的変数はどっち?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">説明変数 = 運動時間(X)　/　目的変数 = 体重減少(Y)</h3>

<div class="mnemonic">
<strong>💡 判定理由:</strong>
<p>「週の運動時間が増えると、体重が減る?」</p>
<p style="margin-top:10px;">
→ <strong>運動が原因、体重減少が結果</strong><br>
→ 運動時間 = X（説明変数）<br>
→ 体重減少 = Y（目的変数）
</p>
</div>

<div class="context">
<strong>📊 回帰式の例:</strong>
<p style="font-size:20px; margin:15px 0;">
体重減少(kg) = 0.5 × 運動時間(時間/週)
</p>
<p>
例: 週10時間運動すると、5kg減少と予測<br>
β = 0.5 → 運動1時間で0.5kg減の効果
</p>
</div>

<div class="mnemonic">
<strong>🎯 複数の説明変数:</strong>
<p>実際は複数のXを使うことが多い:</p>
<p style="margin-top:10px;">
体重減少 = β₁×運動時間 + β₂×食事制限 + β₃×年齢
</p>
<p style="font-size:19px; color:#666;">
→ 重回帰分析（説明変数が複数）
</p>
</div>
</div>''',
            'tags': ['variables', 'health-example', 'practice', 'multiple-regression']
        },

        # カード5: 回帰分析との統合理解（応用）
        {
            'front': '<div class="question"><h3>「Y = 2 + 3X」で、係数3の意味は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">Xが1増えると、Yは3増える</h3>

<div class="mnemonic">
<strong>💡 回帰係数の解釈:</strong>
<p style="font-size:22px; margin:15px 0;">
Y = <font color="#6b7280">2</font> + <font color="#e74c3c">3</font>X
</p>
<p>
<strong><font color="#6b7280">2</font></strong> = 切片（α）→ X=0のときのY<br>
<strong><font color="#e74c3c">3</font></strong> = 傾き（β）→ <strong>Xの効果の大きさ</strong>
</p>
</div>

<div class="context">
<strong>📊 具体例で理解:</strong>
<p>売上 = 100 + 5 × 広告費</p>
<p style="margin-top:10px;">
<strong><font color="#e74c3c">β = 5</font></strong> の意味:<br>
→ 広告費1万円増やすと、売上5万円増<br>
→ <strong><font color="#3498db">説明変数(X)の影響力</font></strong>
</p>
<table style="width:100%; margin-top:15px; font-size:19px;">
<tr style="background:#f8f9fa; font-weight:bold;">
<td style="padding:8px;">広告費(X)</td>
<td style="padding:8px;">売上(Y)</td>
</tr>
<tr><td style="padding:8px;">0</td><td style="padding:8px;">100</td></tr>
<tr style="background:#f8f9fa;"><td style="padding:8px;">10</td><td style="padding:8px;">150</td></tr>
<tr><td style="padding:8px;">20</td><td style="padding:8px;">200</td></tr>
</table>
</div>

<div class="mnemonic">
<strong>🎯 統計検定のポイント:</strong>
<p><strong>βが大きい → Xの影響が大きい</strong></p>
<p>β=0 → Xは影響なし<br>
β>0 → X増加でY増加<br>
β<0 → X増加でY減少
</p>
</div>
</div>''',
            'tags': ['variables', 'regression-coefficient', 'application', 'essential', 'statistics-exam']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("説明変数と目的変数 - Ankiカード生成（コンパクト5枚版）")
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
    deck_name = "Greek Letters & Statistics"
    model_name = "Greek Letters v2 (Super Readable)"

    # カード作成
    cards = create_variable_cards(deck_name, model_name)
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
    print("✨ 説明変数・目的変数カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print(f"🎯 カード構成:")
    print(f"  1. 基本定義（説明vs目的の違い）")
    print(f"  2. 見分け方（判定フローチャート）")
    print(f"  3. 具体例1（広告費と売上）")
    print(f"  4. 具体例2（運動時間と体重）")
    print(f"  5. 回帰分析（係数の解釈）")
    print()
    print(f"🔍 Ankiで確認:")
    print(f"  tag:variables で検索")
    print(f"  tag:essential で重要カードのみ")
    print(f"  tag:practice で具体例のみ")
    print()


if __name__ == "__main__":
    main()
