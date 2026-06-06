#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学公式（微分・積分・対数） - 統計用シンプル版
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


def create_math_cards(deck_name, model_name):
    """数学公式カードを作成（統計用シンプル版）"""

    cards = [
        # カード1: 対数の基本性質
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>対数の基本性質<br>（積・商・べき乗）は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【積の対数】</b><br>
log(AB) = log A + log B<br>
<br>
<b>【商の対数】</b><br>
log(A/B) = log A - log B<br>
<br>
<b>【べき乗の対数】</b><br>
log(A^n) = n × log A<br>
<br>
<hr>
<b>具体例:</b><br>
log(100) = log(10 × 10)<br>
        = log 10 + log 10<br>
        = 1 + 1<br>
        = 2<br>
<br>
log(1000) = log(10³)<br>
         = 3 × log 10<br>
         = 3<br>
<br>
<hr>
<b>統計での使用例:</b><br>
• 幾何平均の計算<br>
• 対数変換<br>
• 尤度関数の最大化
</div>''',
            'tags': ['math', 'logarithm']
        },

        # カード2: 対数の底の変換
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>対数の底の変換公式は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>底の変換公式:</b><br>
<br>
log_a B = log_c B / log_c A<br>
<br>
（任意の底cを使って計算できる）<br>
<br>
<hr>
<b>よく使う形:</b><br>
<br>
log₂ n = log₁₀ n / log₁₀ 2<br>
       = log₁₀ n / 0.301<br>
       ≈ 3.32 × log₁₀ n<br>
<br>
<hr>
<b>自然対数への変換:</b><br>
<br>
log₁₀ x = ln x / ln 10<br>
        ≈ ln x / 2.303<br>
<br>
<hr>
<b>統計検定での使用:</b><br>
• スタージェスの公式<br>
  k = 1 + log₂ n<br>
  → log₂を計算できない時に使う
</div>''',
            'tags': ['math', 'logarithm', 'conversion']
        },

        # カード3: 自然対数と指数関数の関係
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>自然対数 ln と<br>指数関数 e^x の関係は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【基本関係】</b><br>
ln(e^x) = x<br>
e^(ln x) = x<br>
<br>
<hr>
<b>【ネイピア数 e】</b><br>
e ≈ 2.71828...<br>
<br>
<b>定義:</b><br>
e = lim(n→∞) (1 + 1/n)^n<br>
<br>
<hr>
<b>【自然対数の性質】</b><br>
ln 1 = 0<br>
ln e = 1<br>
ln(e²) = 2<br>
<br>
<hr>
<b>統計での使用例:</b><br>
• 正規分布の確率密度関数<br>
• 指数分布<br>
• ロジスティック回帰<br>
• 最尤推定
</div>''',
            'tags': ['math', 'exponential', 'logarithm']
        },

        # カード4: 指数関数の微分
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>e^x と a^x の微分は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【e^x の微分】</b><br>
<br>
d/dx (e^x) = e^x<br>
<br>
→ 微分しても変わらない！<br>
<br>
<hr>
<b>【a^x の微分】</b><br>
<br>
d/dx (a^x) = a^x × ln a<br>
<br>
<hr>
<b>【合成関数】</b><br>
<br>
d/dx (e^(f(x))) = e^(f(x)) × f'(x)<br>
<br>
<b>例:</b><br>
d/dx (e^(2x)) = e^(2x) × 2 = 2e^(2x)<br>
<br>
<hr>
<b>統計での使用:</b><br>
• 正規分布の最大値を求める<br>
• 尤度関数の最大化
</div>''',
            'tags': ['math', 'differentiation', 'exponential']
        },

        # カード5: 対数関数の微分
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>ln x と log_a x の微分は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【自然対数の微分】</b><br>
<br>
d/dx (ln x) = 1/x<br>
<br>
<hr>
<b>【一般の対数の微分】</b><br>
<br>
d/dx (log_a x) = 1 / (x × ln a)<br>
<br>
<hr>
<b>【合成関数】</b><br>
<br>
d/dx (ln f(x)) = f'(x) / f(x)<br>
<br>
<b>例:</b><br>
d/dx (ln(x²)) = 2x / x² = 2/x<br>
<br>
<hr>
<b>統計での使用:</b><br>
• 対数尤度関数の微分<br>
• 最尤推定<br>
• パラメータの推定
</div>''',
            'tags': ['math', 'differentiation', 'logarithm']
        },

        # カード6: 指数関数の積分
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>e^x と e^(ax) の積分は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【e^x の積分】</b><br>
<br>
∫ e^x dx = e^x + C<br>
<br>
→ 積分しても変わらない！<br>
<br>
<hr>
<b>【e^(ax) の積分】</b><br>
<br>
∫ e^(ax) dx = (1/a) × e^(ax) + C<br>
<br>
<b>例:</b><br>
∫ e^(2x) dx = (1/2) × e^(2x) + C<br>
<br>
<hr>
<b>【重要な積分（ガウス積分）】</b><br>
<br>
∫_{-∞}^{∞} e^(-x²) dx = √π<br>
<br>
<hr>
<b>統計での使用:</b><br>
• 正規分布の確率計算<br>
• 期待値の計算
</div>''',
            'tags': ['math', 'integration', 'exponential']
        },

        # カード7: 対数関数の積分
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>ln x の積分は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【自然対数の積分】</b><br>
<br>
∫ ln x dx = x ln x - x + C<br>
<br>
<hr>
<b>【導出（部分積分）】</b><br>
<br>
∫ ln x dx = ∫ 1 × ln x dx<br>
<br>
u = ln x, dv = dx とすると<br>
du = (1/x)dx, v = x<br>
<br>
∫ ln x dx = x ln x - ∫ x × (1/x) dx<br>
         = x ln x - ∫ 1 dx<br>
         = x ln x - x + C<br>
<br>
<hr>
<b>【覚え方】</b><br>
「x かけ ln x、マイナス x」<br>
<br>
<hr>
<b>統計での使用:</b><br>
• エントロピーの計算<br>
• 情報理論
</div>''',
            'tags': ['math', 'integration', 'logarithm']
        },

        # カード8: 統計でよく使う公式まとめ
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>統計検定2級で<br>よく使う数学公式まとめ</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【対数】</b><br>
• log(AB) = log A + log B<br>
• log(A/B) = log A - log B<br>
• log(A^n) = n log A<br>
• log_a B = log B / log A<br>
<br>
<b>【指数】</b><br>
• e^(a+b) = e^a × e^b<br>
• (e^a)^n = e^(an)<br>
• e^0 = 1<br>
<br>
<b>【微分】</b><br>
• d/dx (e^x) = e^x<br>
• d/dx (ln x) = 1/x<br>
• d/dx (x^n) = n x^(n-1)<br>
<br>
<b>【積分】</b><br>
• ∫ e^x dx = e^x + C<br>
• ∫ 1/x dx = ln |x| + C<br>
• ∫ x^n dx = x^(n+1)/(n+1) + C (n≠-1)<br>
<br>
<hr>
<b>【統計検定のポイント】</b><br>
公式の暗記より、使い方を理解する
</div>''',
            'tags': ['math', 'summary']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("数学公式（微分・積分・対数） - 統計用シンプル版カード生成")
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
    cards = create_math_cards(deck_name, model_name)
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
    print("✨ 数学公式カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()


if __name__ == "__main__":
    main()
