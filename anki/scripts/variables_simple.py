#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
説明変数と目的変数 - シンプル版（色なし）
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


def create_variable_cards(deck_name, model_name):
    """変数カードを作成（シンプル版）"""

    cards = [
        # カード1: 説明変数と目的変数の違い
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【説明変数】と【目的変数】の違いは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>説明変数（独立変数）</b><br>
• 原因となる変数<br>
• 予測に使う変数<br>
• <b>X</b> で表す<br>
<br>
<b>目的変数（従属変数）</b><br>
• 結果となる変数<br>
• 予測したい変数<br>
• <b>Y</b> で表す<br>
<br>
<hr>
<b>例：勉強時間 → テストの点数</b><br>
勉強時間 = 【説明変数】<br>
テストの点数 = 【目的変数】
</div>''',
            'tags': ['variables', 'basic']
        },

        # カード2: 見分け方
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>説明変数と目的変数の見分け方は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【質問で判定】</b><br>
<br>
<b>ステップ1:</b> 「何を知りたい?」<br>
→ これが <b>目的変数（Y）</b><br>
<br>
<b>ステップ2:</b> 「何で予測する?」<br>
→ これが <b>説明変数（X）</b><br>
<br>
<hr>
<b>魔法の質問:</b><br>
「Xが変わると、Yが変わる?」<br>
→ YES なら X=説明変数、Y=目的変数
</div>''',
            'tags': ['variables', 'method']
        },

        # カード3: 具体例（広告費と売上）
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>「広告費と売上の関係」で<br>説明変数と目的変数はどっち?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>答え:</b><br>
説明変数 = <b>広告費（X）</b><br>
目的変数 = <b>売上（Y）</b><br>
<br>
<hr>
<b>判定理由:</b><br>
「広告費を増やすと、売上が増えるか?」<br>
→ 広告費が原因、売上が結果<br>
<br>
<b>回帰式:</b><br>
売上 = α + β × 広告費<br>
<br>
例: 売上 = 100万 + 5 × 広告費<br>
→ 広告費10万円なら、売上150万円と予測
</div>''',
            'tags': ['variables', 'example']
        },

        # カード4: 回帰係数の意味
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>「Y = 2 + 3X」で<br>係数3の意味は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>答え: Xが1増えると、Yは3増える</b><br>
<br>
<hr>
<b>回帰係数の解釈:</b><br>
Y = <b>2</b> + <b>3</b>X<br>
<br>
<b>2</b> = 切片（α）<br>
→ X=0のときのY<br>
<br>
<b>3</b> = 傾き（β）<br>
→ <b>【Xの効果の大きさ】</b><br>
<br>
<hr>
<b>具体例:</b><br>
売上 = 100 + 5 × 広告費<br>
<br>
β = 5 の意味:<br>
→ 広告費1万円増やすと、売上5万円増<br>
→ これが【説明変数（X）の影響力】
</div>''',
            'tags': ['variables', 'regression']
        },

        # カード5: まとめ
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>回帰分析の式<br>Y = α + βX<br>の各要素の名前は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>Y</b> = <b>目的変数</b>（従属変数、被説明変数）<br>
<b>X</b> = <b>説明変数</b>（独立変数、予測変数）<br>
<b>α</b> = 切片<br>
<b>β</b> = 回帰係数（傾き）<br>
<br>
<hr>
<b>覚え方:</b><br>
• Y = 予測したいもの（目的）<br>
• X = 予測に使うもの（説明）<br>
• β = Xの影響力<br>
<br>
<b>統計検定のポイント:</b><br>
• β=0 → Xは影響なし<br>
• β>0 → X増加でY増加<br>
• β<0 → X増加でY減少
</div>''',
            'tags': ['variables', 'summary']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("説明変数と目的変数 - シンプル版カード生成")
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
    print("✨ 変数カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()


if __name__ == "__main__":
    main()
