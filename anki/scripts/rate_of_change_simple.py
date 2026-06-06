#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
変化率 - シンプル版（色なし）
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


def create_rate_cards(deck_name, model_name):
    """変化率カードを作成（シンプル版）"""

    cards = [
        # カード1: 基本公式
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【変化率】の計算方法は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>基本公式:</b><br>
<br>
変化率 = （新しい値 - 古い値）÷ 古い値<br>
<br>
<hr>
<b>ポイント:</b><br>
• 分母は必ず【古い値（基準）】<br>
• 答えは小数（0.2など）<br>
• パーセント表示 = 小数 × 100<br>
<br>
<hr>
<b>例:</b><br>
100 → 120 に増加<br>
<br>
変化率 = (120 - 100) ÷ 100<br>
      = 20 ÷ 100<br>
      = 0.2<br>
      = <b>20%</b>
</div>''',
            'tags': ['rate', 'formula']
        },

        # カード2: 分子と分母
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>変化率の<br>分子と分母は何?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>分子:</b> 変化額（新しい値 - 古い値）<br>
<b>分母:</b> 古い値（基準）<br>
<br>
<hr>
<b>具体例:</b><br>
売上: 50万円 → 60万円<br>
<br>
<b>分子:</b> 60 - 50 = <b>10万円</b>（変化幅）<br>
<b>分母:</b> <b>50万円</b>（元の売上=基準）<br>
<b>変化率:</b> 10 ÷ 50 = 0.2 = <b>20%増</b><br>
<br>
<hr>
<b>重要:</b><br>
分母を間違えると全て間違い!<br>
必ず「古い値」で割る
</div>''',
            'tags': ['rate', 'components']
        },

        # カード3: よくある間違い
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>変化率計算の<br>よくある間違いは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【間違い】分母を「新しい値」にする</b><br>
<br>
<hr>
<b>例: 100 → 120 の変化率</b><br>
<br>
❌ <b>誤り:</b><br>
(120 - 100) ÷ 120 = 0.167 = 16.7%<br>
<br>
✓ <b>正解:</b><br>
(120 - 100) ÷ 100 = 0.2 = 20%<br>
<br>
<hr>
<b>覚え方:</b><br>
分母は必ず【古い値（基準）】<br>
<br>
「元の値から何%変化したか」を計算する
</div>''',
            'tags': ['rate', 'mistake']
        },

        # カード4: 練習問題
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>売上が 100万円 から<br>120万円 に増加<br><br>変化率は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>ステップ1: 変化額を計算</b><br>
変化額 = 120 - 100 = 20万円<br>
<br>
<b>ステップ2: 変化率を計算</b><br>
変化率 = 20 ÷ 100 = 0.2<br>
<br>
<b>ステップ3: パーセントで表す</b><br>
0.2 × 100 = <b>20%増加</b><br>
<br>
<hr>
<b>答え: 20%の増加</b>
</div>''',
            'tags': ['rate', 'practice']
        },

        # カード5: 減少の変化率
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>売上が 200万円 から<br>150万円 に減少<br><br>変化率は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>ステップ1: 変化額を計算</b><br>
変化額 = 150 - 200 = -50万円<br>
<br>
<b>ステップ2: 変化率を計算</b><br>
変化率 = (-50) ÷ 200 = -0.25<br>
<br>
<b>ステップ3: パーセントで表す</b><br>
-0.25 × 100 = <b>-25%</b><br>
<br>
<hr>
<b>答え: 25%の減少</b><br>
<br>
<b>注意:</b> マイナス記号は「減少」を意味する
</div>''',
            'tags': ['rate', 'decrease']
        },

        # カード6: まとめ
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>変化率を一言でまとめると?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【変化率 = 変化の割合】</b><br>
<br>
元の値を基準にして、<br>
どれだけ変化したかを割合で表す<br>
<br>
<hr>
<b>公式:</b><br>
変化率 = 変化額 ÷ 古い値<br>
<br>
<b>ポイント:</b><br>
• 分母は必ず「古い値」<br>
• 増加 → プラス<br>
• 減少 → マイナス<br>
<br>
<hr>
<b>用語:</b><br>
• 前年比 = 前年からの変化率<br>
• 前月比 = 前月からの変化率<br>
• 成長率 = 変化率（特に増加の場合）
</div>''',
            'tags': ['rate', 'summary']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("変化率 - シンプル版カード生成")
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
    cards = create_rate_cards(deck_name, model_name)
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
    print("✨ 変化率カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()


if __name__ == "__main__":
    main()
