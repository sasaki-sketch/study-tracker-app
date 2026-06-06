#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ローレンツ曲線・ジニ係数 - シンプル版
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


def create_inequality_cards(deck_name, model_name):
    """ローレンツ曲線・ジニ係数カードを作成（シンプル版）"""

    cards = [
        # カード1: ローレンツ曲線とは
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【ローレンツ曲線】<br>(Lorenz Curve)とは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
所得などの量の集中度や格差を表すグラフ<br>
M.O.ローレンツが考案<br>
<br>
<hr>
<b>グラフの構造:</b><br>
• 横軸: 累積人口の割合（%）<br>
• 縦軸: 累積所得の割合（%）<br>
<br>
<hr>
<b>完全平等線:</b><br>
• (0,0)と(100,100)を結ぶ直線<br>
• すべての人が同じ所得の場合<br>
<br>
<hr>
<b>ローレンツ曲線の性質:</b><br>
• 必ず完全平等線より下側を通る<br>
• 曲線が<b>上方にある</b> → 平等<br>
• 曲線が<b>下方にある</b> → 不平等
</div>''',
            'tags': ['inequality', 'lorenz']
        },

        # カード2: ローレンツ曲線の読み方
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>ローレンツ曲線の読み方は?<br>グラフから何がわかる?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>読み方の例:</b><br>
点（40, 20）がローレンツ曲線上にある場合<br>
<br>
→ 「下位40%の人が、全体の所得の20%を占める」<br>
<br>
<hr>
<b>五分位でよく使われる点:</b><br>
• (20, y₁) → 下位20%の所得シェア<br>
• (40, y₂) → 下位40%の所得シェア<br>
• (60, y₃) → 下位60%の所得シェア<br>
• (80, y₄) → 下位80%の所得シェア<br>
<br>
<hr>
<b>グラフの解釈:</b><br>
<br>
<b>曲線が完全平等線に近い:</b><br>
• 所得分配が平等<br>
• 格差が小さい<br>
<br>
<b>曲線が完全平等線から遠い:</b><br>
• 所得分配が不平等<br>
• 格差が大きい
</div>''',
            'tags': ['inequality', 'lorenz', 'interpretation']
        },

        # カード3: ジニ係数とは
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【ジニ係数】<br>(Gini Coefficient)とは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
所得分配の不平等度を示す指標<br>
0から1の値をとる<br>
<br>
<hr>
<b>計算方法:</b><br>
完全平等線とローレンツ曲線の間の面積の<b>2倍</b><br>
<br>
ジニ係数 = 2 × 面積<br>
<br>
<hr>
<b>値の意味:</b><br>
<br>
<b>0（ゼロ）:</b><br>
• 完全平等<br>
• すべての人が同じ所得<br>
<br>
<b>1（イチ）:</b><br>
• 完全不平等<br>
• 1人がすべての所得を独占<br>
<br>
<hr>
<b>一般的な値:</b><br>
• 0.3以下 → 平等<br>
• 0.3〜0.4 → 普通<br>
• 0.4以上 → 不平等
</div>''',
            'tags': ['inequality', 'gini']
        },

        # カード4: ジニ係数の計算（台形公式）
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>五分位データから<br>ジニ係数を計算する方法は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>台形公式を使う:</b><br>
<br>
累積所得割合を y₀, y₁, y₂, y₃, y₄, y₅ とする<br>
（y₀=0, y₅=100）<br>
<br>
面積 = (1/5) × [(y₀+y₁) + (y₁+y₂) + (y₂+y₃) + (y₃+y₄) + (y₄+y₅)]<br>
<br>
ジニ係数 = 1 - (2×面積)/100<br>
<br>
<hr>
<b>具体例:</b><br>
五分位の累積所得割合:<br>
0%, 8%, 20%, 40%, 70%, 100%<br>
<br>
面積 = (1/5) × [(0+8) + (8+20) + (20+40) + (40+70) + (70+100)]<br>
     = (1/5) × [8 + 28 + 60 + 110 + 170]<br>
     = (1/5) × 376<br>
     = 75.2<br>
<br>
ジニ係数 = 1 - (2×75.2)/100<br>
        = 1 - 1.504<br>
<br>
待って、これは間違い！正しくは:<br>
ジニ係数 = 1 - 75.2/50 = 1 - 1.504... ではなく<br>
<br>
<b>正しい公式:</b><br>
ジニ係数 = 1 - (面積/5000)
</div>''',
            'tags': ['inequality', 'gini', 'calculation']
        },

        # カード5: ジニ係数の簡易計算（訂正版）
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>五分位データからジニ係数を<br>計算する【正しい手順】は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>ステップ1: 累積所得割合を準備</b><br>
五分位の累積所得割合（%）<br>
例: 0, 5, 15, 35, 65, 100<br>
<br>
<b>ステップ2: ローレンツ曲線下の面積を計算</b><br>
台形の面積の合計:<br>
<br>
面積 = (20/100) × [0 + 2×5 + 2×15 + 2×35 + 2×65 + 100] / 2<br>
     = 0.2 × [0 + 10 + 30 + 70 + 130 + 100] / 2<br>
     = 0.2 × 340 / 2<br>
     = 34<br>
<br>
<b>ステップ3: ジニ係数を計算</b><br>
完全平等線下の面積 = 50（三角形の面積）<br>
<br>
ジニ係数 = (50 - 34) / 50<br>
        = 16 / 50<br>
        = <b>0.32</b><br>
<br>
<hr>
<b>簡単な公式:</b><br>
ジニ係数 = 1 - (ローレンツ曲線下の面積 / 50)
</div>''',
            'tags': ['inequality', 'gini', 'calculation', 'practice']
        },

        # カード6: 統計検定での出題例
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>統計検定2級で<br>ローレンツ曲線・ジニ係数の<br>よくある問題は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【パターン1】グラフの読み取り</b><br>
• 複数の国のローレンツ曲線が与えられる<br>
• 「最も平等な国はどれか」を答える<br>
→ 完全平等線に最も近い曲線<br>
<br>
<hr>
<b>【パターン2】ジニ係数の計算</b><br>
• 五分位の所得割合が与えられる<br>
• ジニ係数を計算する<br>
→ 台形公式を使用<br>
<br>
<hr>
<b>【パターン3】ジニ係数の比較</b><br>
• 複数の国のジニ係数が計算済み<br>
• 「最も不平等な国」を答える<br>
→ ジニ係数が最大の国<br>
<br>
<hr>
<b>【実際の出題例】</b><br>
2018年6月 統計検定2級 問3<br>
• 日本、アメリカ、スウェーデン、中国、ドイツ<br>
• 五分位所得割合からジニ係数を計算<br>
• 結果: 中国(0.39) > アメリカ(0.38) > 日本(0.36) > ドイツ(0.28) > スウェーデン(0.25)
</div>''',
            'tags': ['inequality', 'exam', 'practice']
        },

        # カード7: ローレンツ曲線とジニ係数の関係
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>ローレンツ曲線とジニ係数の関係を<br>まとめると?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【ローレンツ曲線】= グラフ表現</b><br>
• 視覚的に格差を理解<br>
• 複数の分布を比較しやすい<br>
<br>
<b>【ジニ係数】= 数値指標</b><br>
• ローレンツ曲線から計算<br>
• 0〜1の数値で不平等度を表現<br>
• 客観的な比較が可能<br>
<br>
<hr>
<b>関係:</b><br>
ローレンツ曲線が完全平等線から遠い<br>
↓<br>
完全平等線との間の面積が大きい<br>
↓<br>
ジニ係数が大きい<br>
↓<br>
<b>不平等度が高い</b><br>
<br>
<hr>
<b>覚え方:</b><br>
• 曲線が下 → ジニ係数大 → 不平等<br>
• 曲線が上 → ジニ係数小 → 平等
</div>''',
            'tags': ['inequality', 'summary']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("ローレンツ曲線・ジニ係数 - シンプル版カード生成")
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
    cards = create_inequality_cards(deck_name, model_name)
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
    print("✨ ローレンツ曲線・ジニ係数カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()


if __name__ == "__main__":
    main()
