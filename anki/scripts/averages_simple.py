#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
平均値（幾何平均・調和平均・トリム平均） - シンプル版
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


def create_average_cards(deck_name, model_name):
    """平均値カードを作成（シンプル版）"""

    cards = [
        # カード1: 3つの平均の違い
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【幾何平均】【調和平均】【算術平均】の違いは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>算術平均（相加平均）:</b><br>
• 最も一般的な平均<br>
• 全データの合計 ÷ データ数<br>
<br>
<b>幾何平均（相乗平均）:</b><br>
• データの積のn乗根<br>
• 比率・倍率・成長率の平均に使う<br>
<br>
<b>調和平均:</b><br>
• データの逆数の算術平均の逆数<br>
• 速度・レートの平均に使う<br>
<br>
<hr>
<b>大小関係:</b><br>
調和平均 ≤ 幾何平均 ≤ 算術平均
</div>''',
            'tags': ['averages', 'basic']
        },

        # カード2: 幾何平均の定義と公式
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【幾何平均】とは?<br>公式と使用例を説明</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
データの積のn乗根<br>
<br>
<b>公式:</b><br>
幾何平均 = ⁿ√(x₁ × x₂ × ... × xₙ)<br>
<br>
<hr>
<b>使用例:</b><br>
• 成長率の平均<br>
• 変化率の平均<br>
• 投資収益率の平均<br>
<br>
<hr>
<b>具体例:</b><br>
家賃が3年間で20%、10%、15%上昇<br>
<br>
倍率: 1.20、1.10、1.15<br>
幾何平均 = ³√(1.20 × 1.10 × 1.15)<br>
        ≈ 1.149<br>
<br>
→ <b>年平均14.9%の上昇</b>
</div>''',
            'tags': ['averages', 'geometric']
        },

        # カード3: 調和平均の定義と公式
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【調和平均】とは?<br>公式と使用例を説明</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
データの逆数の算術平均の逆数<br>
<br>
<b>公式:</b><br>
調和平均 = n ÷ (1/x₁ + 1/x₂ + ... + 1/xₙ)<br>
<br>
<hr>
<b>使用例:</b><br>
• 速度の平均<br>
• レート（率）の平均<br>
<br>
<hr>
<b>具体例:</b><br>
往路60km/h、復路80km/hで往復<br>
<br>
調和平均 = 2 ÷ (1/60 + 1/80)<br>
        = 2 ÷ (4/240 + 3/240)<br>
        = 2 ÷ (7/240)<br>
        ≈ 68.57 km/h<br>
<br>
→ <b>平均速度は68.57km/h</b><br>
（算術平均70km/hとは異なる！）
</div>''',
            'tags': ['averages', 'harmonic']
        },

        # カード4: なぜ速度は調和平均？
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>速度の平均に<br>調和平均を使う理由は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>理由: 距離が同じだから</b><br>
<br>
往復の場合、往路と復路の【距離は同じ】<br>
→ 時間の重みが異なる<br>
<br>
<hr>
<b>具体例で比較:</b><br>
距離10km、往路60km/h、復路80km/h<br>
<br>
<b>往路の時間:</b> 10 ÷ 60 = 0.167時間<br>
<b>復路の時間:</b> 10 ÷ 80 = 0.125時間<br>
<b>合計時間:</b> 0.292時間<br>
<b>合計距離:</b> 20km<br>
<br>
<b>真の平均速度:</b><br>
20 ÷ 0.292 ≈ 68.57 km/h<br>
<br>
→ これが調和平均と一致！<br>
<br>
<hr>
<b>算術平均だと:</b><br>
(60 + 80) ÷ 2 = 70 km/h ← 間違い
</div>''',
            'tags': ['averages', 'harmonic', 'application']
        },

        # カード5: トリム平均（刈り込み平均）
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【トリム平均】<br>（刈り込み平均）とは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
データの両端から一定割合を除外して<br>
残りで計算する平均値<br>
<br>
<hr>
<b>計算手順:</b><br>
1. データを小さい順に並べる<br>
2. 両端から同じ割合だけ削除<br>
3. 残ったデータで算術平均を計算<br>
<br>
<hr>
<b>パーセンテージの表記:</b><br>
• 5%トリム平均 → 両端から5%ずつ削除<br>
• 25%トリム平均 → 中央平均<br>
<br>
<hr>
<b>メリット:</b><br>
• 外れ値の影響を減らせる<br>
• 異常値に強い（ロバスト）<br>
<br>
<hr>
<b>使用例:</b><br>
• フィギュアスケート・体操の採点<br>
• 最高点と最低点を除いて平均
</div>''',
            'tags': ['averages', 'trimmed']
        },

        # カード6: トリム平均の具体例
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>10個のデータで<br>20%トリム平均を計算すると?<br><br>データ: 2,3,5,7,8,9,10,12,15,100</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>ステップ1: データ確認（既にソート済み）</b><br>
2, 3, 5, 7, 8, 9, 10, 12, 15, 100<br>
<br>
<b>ステップ2: 削除する個数を計算</b><br>
10個 × 20% = 2個<br>
→ 両端から2個ずつ削除<br>
<br>
<b>ステップ3: 削除実行</b><br>
削除 → <s>2, 3</s>, 5, 7, 8, 9, 10, 12, <s>15, 100</s> ← 削除<br>
<br>
<b>残ったデータ:</b> 5, 7, 8, 9, 10, 12<br>
<br>
<b>ステップ4: 算術平均を計算</b><br>
(5 + 7 + 8 + 9 + 10 + 12) ÷ 6<br>
= 51 ÷ 6<br>
= <b>8.5</b><br>
<br>
<hr>
<b>比較:</b><br>
通常の平均 = 17.1（外れ値100の影響大）<br>
20%トリム平均 = 8.5（外れ値の影響小）
</div>''',
            'tags': ['averages', 'trimmed', 'practice']
        },

        # カード7: 統計検定での注意点
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>統計検定2級で<br>平均値を計算する際の注意点は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【注意1】電卓の制限</b><br>
• 一般的な事務用電卓のみ使用可<br>
• 関数電卓は使用不可<br>
• n乗根は平方根（√）のみ計算可能<br>
<br>
→ 幾何平均は2個のデータのみ計算可<br>
<br>
<hr>
<b>【注意2】適切な平均の選択</b><br>
<br>
<b>算術平均を使う:</b><br>
• 通常のデータ<br>
• 各値が同じ重要度<br>
<br>
<b>幾何平均を使う:</b><br>
• 成長率・変化率<br>
• 倍率・比率<br>
<br>
<b>調和平均を使う:</b><br>
• 速度の平均<br>
• レート（率）の平均<br>
<br>
<b>トリム平均を使う:</b><br>
• 外れ値が含まれるデータ<br>
<br>
<hr>
<b>大小関係を覚える:</b><br>
調和平均 ≤ 幾何平均 ≤ 算術平均
</div>''',
            'tags': ['averages', 'exam-tips']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("平均値（幾何平均・調和平均・トリム平均） - シンプル版カード生成")
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
    cards = create_average_cards(deck_name, model_name)
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
    print("✨ 平均値カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()


if __name__ == "__main__":
    main()
