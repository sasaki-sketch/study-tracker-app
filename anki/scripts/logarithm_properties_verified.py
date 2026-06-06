#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
対数の性質（Logarithm Properties） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「対数（log）」https://bellcurve.jp/statistics/course/27418.html
- 理系ラボ「対数(log)の公式・変換のまとめ」
- 複数の数学サイトで検証済み
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


def create_logarithm_properties_cards(deck_name, model_name):
    """対数の性質カードを作成（検証済み）"""

    cards = [
        # カード1: 対数の基本性質と定義
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【対数の基本】<br>定義と基本性質は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>定義:</b><br>
底aをr乗したものがPになるとき、<br>
rを「<b>aを底とするPの対数</b>」という<br>
<br>

\\[r = \\log_a P \\Leftrightarrow a^r = P\\]
<br>

ここで: a > 0, a ≠ 1, P > 0<br>
<br>

<hr>

<b>【基本性質】</b><br>
<br>

<b>性質1:</b><br>
\\[\\log_a a = 1\\]
<br>

（底と真数が同じ → 指数は1）<br>
<br>

例: \\(\\log_2 2 = 1\\)（2¹ = 2）<br>
例: \\(\\log_{10} 10 = 1\\)（10¹ = 10）<br>
<br>

<b>性質2:</b><br>
\\[\\log_a 1 = 0\\]
<br>

（真数が1 → 指数は0）<br>
<br>

例: \\(\\log_2 1 = 0\\)（2⁰ = 1）<br>
例: \\(\\log_{10} 1 = 0\\)（10⁰ = 1）<br>
<br>

<b>性質3:</b><br>
\\[\\log_a a^k = k\\]
<br>

（底のk乗の対数 → k）<br>
<br>

例: \\(\\log_2 8 = \\log_2 2^3 = 3\\)<br>
例: \\(\\log_{10} 100 = \\log_{10} 10^2 = 2\\)<br>
<br>

<b>性質4:</b><br>
\\[a^{\\log_a P} = P\\]
<br>

（指数と対数の相互関係）<br>
<br>

<hr>

<b>【重要な対数の種類】</b><br>
<br>

<b>常用対数（底10）:</b><br>
\\[\\log_{10} P = \\log P\\]
<br>

• 計算機で標準的に使用<br>
• 大きな数の桁数計算に活用<br>
<br>

<b>自然対数（底e）:</b><br>
\\[\\log_e P = \\ln P\\]
<br>

• e ≈ 2.71828...(ネイピア数)<br>
• 統計学で確率分布の計算に頻出<br>
• 微積分で重要<br>
<br>

<b>二進対数（底2）:</b><br>
\\[\\log_2 P\\]
<br>

• スタージェスの公式で使用<br>
• 情報理論で重要<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>対数が定義されない場合:</b><br>
• 真数が0以下: \\(\\log_a 0\\), \\(\\log_a (-5)\\) は定義されない<br>
• 底が1または負: \\(\\log_1 P\\), \\(\\log_{-2} P\\) は定義されない<br>
<br>

<b>統計検定2級では:</b><br>
• 対数の基本性質を理解<br>
• 底の変換公式が重要<br>
• スタージェスの公式でlog₂を使用<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「対数（log）」<br>
複数の数学サイトで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'logarithm', 'definition', 'basic-properties']
        },

        # カード2: 対数の計算公式（積・商・累乗）
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【対数の計算公式】<br>積・商・累乗の法則は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>対数の3つの計算公式:</b><br>
<br>

<hr>

<b>①積の法則（Product Rule）</b><br>
\\[\\log_a (MN) = \\log_a M + \\log_a N\\]
<br>

積の対数 = 対数の和<br>
<br>

<b>例:</b><br>
\\[\\log_2 (8 \\times 4) = \\log_2 8 + \\log_2 4\\]
\\[= 3 + 2 = 5\\]
<br>

検算: \\(\\log_2 32 = \\log_2 2^5 = 5\\) ✓<br>
<br>

<hr>

<b>②商の法則（Quotient Rule）</b><br>
\\[\\log_a \\left(\\frac{M}{N}\\right) = \\log_a M - \\log_a N\\]
<br>

商の対数 = 対数の差<br>
<br>

<b>例:</b><br>
\\[\\log_{10} \\left(\\frac{1000}{10}\\right) = \\log_{10} 1000 - \\log_{10} 10\\]
\\[= 3 - 1 = 2\\]
<br>

検算: \\(\\log_{10} 100 = 2\\) ✓<br>
<br>

<hr>

<b>③累乗の法則（Power Rule）</b><br>
\\[\\log_a M^t = t \\log_a M\\]
<br>

累乗の対数 = 指数 × 対数<br>
<br>

<b>例:</b><br>
\\[\\log_2 16 = \\log_2 2^4 = 4 \\log_2 2 = 4 \\times 1 = 4\\]
<br>

\\[\\log_{10} \\sqrt{10} = \\log_{10} 10^{1/2} = \\frac{1}{2} \\log_{10} 10 = \\frac{1}{2}\\]
<br>

<hr>

<b>【公式の組み合わせ】</b><br>
<br>

<b>例: 複雑な計算</b><br>
\\[\\log_2 \\frac{32 \\times 8}{4} = \\log_2 32 + \\log_2 8 - \\log_2 4\\]
\\[= 5 + 3 - 2 = 6\\]
<br>

検算: \\(\\log_2 64 = \\log_2 2^6 = 6\\) ✓<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>よくある間違い:</b><br>
• ✗ \\(\\log_a (M + N) = \\log_a M + \\log_a N\\)<br>
• ✓ 和の対数には公式はない<br>
<br>

• ✗ \\(\\log_a (M - N) = \\log_a M - \\log_a N\\)<br>
• ✓ 差の対数には公式はない<br>
<br>

<b>符号に注意:</b><br>
• 積 → 和（+）<br>
• 商 → 差（-）<br>
• 累乗 → 係数（×）<br>
<br>

<b>統計検定2級では:</b><br>
• これらの公式を使った変形が出題<br>
• 特に累乗の法則が重要<br>
• 対数の和を積に変換する問題など<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「対数（log）」<br>
理系ラボ「対数(log)の公式・変換のまとめ」<br>
計算例を検算して検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'logarithm', 'calculation', 'formulas']
        },

        # カード3: 底の変換公式とスタージェスの公式での応用
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【底の変換公式】<br>公式とスタージェスの公式<br>での応用は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>底の変換公式:</b><br>
\\[\\log_a M = \\frac{\\log_b M}{\\log_b a}\\]
<br>

底aの対数を、底bの対数で表現できる<br>
<br>

<b>特に重要な変換:</b><br>
\\[\\log_2 M = \\frac{\\log_{10} M}{\\log_{10} 2}\\]
<br>

\\(\\log_{10} 2 \\approx 0.301\\) なので:<br>
\\[\\log_2 M \\approx \\frac{\\log_{10} M}{0.301} \\approx 3.32 \\times \\log_{10} M\\]
<br>

<hr>

<b>【スタージェスの公式での応用】</b><br>
<br>

<b>スタージェスの公式（底2）:</b><br>
\\[k = 1 + \\log_2 n\\]
<br>

<b>常用対数での表現:</b><br>
\\[k = 1 + 3.32 \\times \\log_{10} n\\]
<br>

この2つは同じ式！<br>
<br>

<b>具体例: n = 100</b><br>
<br>

<b>方法1: 底2で計算</b><br>
\\(2^6 = 64 < 100 < 128 = 2^7\\)<br>
→ \\(\\log_2 100 \\approx 6.64\\)<br>
\\(k = 1 + 6.64 \\approx 7.64\\) → 四捨五入して <b>8</b><br>
<br>

<b>方法2: 底10で計算</b><br>
\\(\\log_{10} 100 = 2\\)<br>
\\(k = 1 + 3.32 \\times 2 = 1 + 6.64 = 7.64\\) → 四捨五入して <b>8</b><br>
<br>

→ 同じ結果！ ✓<br>
<br>

<hr>

<b>【底の変換公式の証明（参考）】</b><br>
<br>

\\(\\log_a M = x\\) とすると \\(a^x = M\\)<br>
両辺の底bの対数をとると:<br>
\\[\\log_b a^x = \\log_b M\\]
\\[x \\log_b a = \\log_b M\\]
\\[x = \\frac{\\log_b M}{\\log_b a}\\]
<br>

よって:<br>
\\[\\log_a M = \\frac{\\log_b M}{\\log_b a}\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>底の変換を使う場面:</b><br>
• 計算機にない底を計算したい時<br>
• 底2の対数を底10で計算<br>
• 自然対数を常用対数で計算<br>
<br>

<b>統計検定2級では:</b><br>
• スタージェスの公式で頻出<br>
• 関数電卓不可のため暗算が必要<br>
• \\(\\log_2 n \\approx 3.32 \\times \\log_{10} n\\) を覚える<br>
• または2の累乗で挟んで概算<br>
<br>

<b>覚えておくと便利な値:</b><br>
• \\(\\log_{10} 2 \\approx 0.301\\)<br>
• \\(\\log_{10} 3 \\approx 0.477\\)<br>
• \\(\\log_2 10 \\approx 3.32\\)<br>
• \\(\\ln 10 \\approx 2.303\\)<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「対数（log）」<br>
理系ラボ「対数(log)の公式・変換のまとめ」<br>
スタージェスの公式との関係を検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'logarithm', 'base-conversion', 'sturges', 'application']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("対数の性質 - 検証済みAnkiカード生成")
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
    cards = create_logarithm_properties_cards(deck_name, model_name)
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
    print("✨ 対数の性質カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 対数の基本性質と定義")
    print("  カード2: 対数の計算公式（積・商・累乗）")
    print("  カード3: 底の変換公式とスタージェスの公式での応用")
    print()


if __name__ == "__main__":
    main()
