#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
歪度・尖度 - シンプル版
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


def create_shape_cards(deck_name, model_name):
    """歪度・尖度カードを作成（シンプル版）"""

    cards = [
        # カード1: 歪度とは
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【歪度】（わいど）<br>Skewnessとは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
分布が正規分布からどれだけ歪んでいるかを表す統計量<br>
左右対称性を示す指標<br>
<br>
<hr>
<b>計算公式（標本）:</b><br>
<br>
歪度 = n/[(n-1)(n-2)] × Σ[(xᵢ - x̄)/s]³<br>
<br>
n = データ数<br>
xᵢ = 各データ<br>
x̄ = 平均<br>
s = 標準偏差<br>
<br>
<hr>
<b>英語:</b><br>
Skewness（スキューネス）
</div>''',
            'tags': ['shape', 'skewness']
        },

        # カード2: 歪度の正負の意味
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>歪度の正負は<br>何を意味する?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>歪度 = 0</b><br>
• 左右対称の分布<br>
• 正規分布<br>
<br>
<b>歪度 > 0（正の値）</b><br>
• <b>右裾が長い</b> 分布<br>
• <b>左に偏った</b> 分布<br>
• 平均 > 中央値<br>
• 例: 所得分布（高所得者が少数）<br>
<br>
<b>歪度 < 0（負の値）</b><br>
• <b>左裾が長い</b> 分布<br>
• <b>右に偏った</b> 分布<br>
• 平均 < 中央値<br>
• 例: 試験の点数（多くが高得点）<br>
<br>
<hr>
<b>覚え方:</b><br>
正 → 右に尾が伸びる<br>
負 → 左に尾が伸びる
</div>''',
            'tags': ['shape', 'skewness', 'interpretation']
        },

        # カード3: 尖度とは
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【尖度】（せんど）<br>Kurtosisとは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
分布が正規分布からどれだけ尖っているかを示す統計量<br>
山の尖り度と裾の広がり度を示す<br>
<br>
<hr>
<b>計算公式（標本）:</b><br>
<br>
尖度 = n(n+1)/[(n-1)(n-2)(n-3)] × Σ[(xᵢ-x̄)/s]⁴<br>
      - 3(n-1)²/[(n-2)(n-3)]<br>
<br>
<hr>
<b>注意:</b><br>
• この公式は【-3を引いた値】<br>
• 正規分布で尖度 = 0<br>
<br>
<b>別の定義:</b><br>
• -3を引かない定義もある<br>
• その場合、正規分布で尖度 = 3<br>
<br>
<hr>
<b>英語:</b><br>
Kurtosis（カートシス）
</div>''',
            'tags': ['shape', 'kurtosis']
        },

        # カード4: 尖度の正負の意味
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>尖度の正負は<br>何を意味する?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>尖度 = 0</b><br>
• 正規分布と同じ形状<br>
<br>
<b>尖度 > 0（正の値）</b><br>
• <b>正規分布より尖った</b> 分布<br>
• 平均付近にデータが集中<br>
• 裾が重い（外れ値が多い）<br>
• 鋭峰分布（Leptokurtic）<br>
<br>
<b>尖度 < 0（負の値）</b><br>
• <b>正規分布より扁平</b> な分布<br>
• データが散らばっている<br>
• 裾が軽い（外れ値が少ない）<br>
• 扁平分布（Platykurtic）<br>
<br>
<hr>
<b>覚え方:</b><br>
正 → 尖っている（ピークが高い）<br>
負 → 平べったい（ピークが低い）
</div>''',
            'tags': ['shape', 'kurtosis', 'interpretation']
        },

        # カード5: 歪度と尖度の違い
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>歪度と尖度の違いは?<br>何を測っている?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【歪度】Skewness</b><br>
<b>測定対象:</b> 左右対称性<br>
<b>特徴:</b><br>
• 分布の偏り<br>
• 尾の方向<br>
• 3次モーメント（³乗）を使用<br>
<br>
<hr>
<b>【尖度】Kurtosis</b><br>
<b>測定対象:</b> 尖り度<br>
<b>特徴:</b><br>
• 分布の鋭さ<br>
• 裾の重さ<br>
• 4次モーメント（⁴乗）を使用<br>
<br>
<hr>
<b>両方とも:</b><br>
• 正規分布からのズレを測定<br>
• 正規分布では両方ともゼロ<br>
• データの形状を理解する指標
</div>''',
            'tags': ['shape', 'comparison']
        },

        # カード6: 統計検定での注意点
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>統計検定2級で<br>歪度・尖度を扱う際の注意点は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【注意1】尖度の定義</b><br>
<br>
<b>定義A:</b> -3を引いた値<br>
• 正規分布で尖度 = 0<br>
• Excess Kurtosis（超過尖度）<br>
<br>
<b>定義B:</b> -3を引かない値<br>
• 正規分布で尖度 = 3<br>
<br>
→ 問題文で確認すること！<br>
<br>
<hr>
<b>【注意2】計算の複雑さ</b><br>
• 試験では公式の暗記より解釈が重要<br>
• グラフから歪度・尖度の正負を判定<br>
<br>
<hr>
<b>【注意3】よく出る問題パターン</b><br>
• グラフを見て歪度の正負を答える<br>
• 正規分布と比較した形状の説明<br>
• 平均と中央値の大小関係<br>
<br>
<hr>
<b>【覚えるべき関係】</b><br>
右に歪む（正） → 平均 > 中央値<br>
左に歪む（負） → 平均 < 中央値
</div>''',
            'tags': ['shape', 'exam-tips']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("歪度・尖度 - シンプル版カード生成")
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
    cards = create_shape_cards(deck_name, model_name)
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
    print("✨ 歪度・尖度カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()


if __name__ == "__main__":
    main()
