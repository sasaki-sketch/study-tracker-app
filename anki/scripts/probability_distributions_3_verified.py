#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級 - いろいろな確率分布3（検証済み）
===================================================
トピック: 2変数の期待値と分散、指数分布、2変数の確率分布
検証日: 2026-01-20
出典: 統計WEB、統計検定2級対策教材、複数の統計学サイト
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


def create_cards():
    """確率分布カードを作成"""
    cards = [
        # ===== 2変数の期待値と分散 =====
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【共分散】共分散とは何か？また、その計算公式は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
共分散とは、2つの確率変数X、Yの関係の強さを表す指標の一つです。<br>
正の値なら正の相関、負の値なら負の相関を示します。<br>
<br>

<b>公式:</b><br>
\\[\\text{Cov}(X, Y) = E[(X - \\mu_X)(Y - \\mu_Y)]\\]
\\[\\text{Cov}(X, Y) = E(XY) - E(X)E(Y)\\]
<br>

<hr>

<b>具体例:</b><br>
X、Yが独立な確率変数の場合: E(XY) = E(X)E(Y)<br>
したがって、Cov(X, Y) = 0<br>
<br>

<b>性質:</b><br>
・線形変換: Cov(aX+b, cY+d) = ac·Cov(X, Y)<br>
・Cov(X, X) = V(X)（自分自身との共分散は分散）<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・共分散が0でも、必ずしも独立とは限らない<br>
・共分散の値の大きさだけでは相関の強さを比較できない（単位に依存するため）<br>
・統計検定2級では、共分散を用いた分散の計算が頻出<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「15-6. 2変数の期待値と分散」<br>
・統計検定2級CBT公式問題集の解説（2変数記述統計の分野）<br>
・複数の統計学教材で検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'covariance', '2variables', 'grade2']
        },

        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【相関係数】相関係数の定義と公式は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
相関係数は、共分散を標準偏差で正規化した指標で、2変数間の線形関係の強さを表します。<br>
-1 ≤ ρ ≤ 1 の範囲の値をとります。<br>
<br>

<b>公式:</b><br>
\\[\\rho(X, Y) = \\frac{\\text{Cov}(X, Y)}{\\sqrt{V(X)}\\sqrt{V(Y)}}\\]
\\[\\rho(X, Y) = \\frac{\\text{Cov}(X, Y)}{\\sigma_X \\sigma_Y}\\]
<br>

<hr>

<b>値の解釈:</b><br>
・ρ = 1: 完全な正の相関（一方が増えると他方も同じ割合で増加）<br>
・ρ = 0: 無相関（線形関係なし）<br>
・ρ = -1: 完全な負の相関（一方が増えると他方は同じ割合で減少）<br>
<br>

<b>計算例:</b><br>
Cov(X, Y) = 4、V(X) = 16、V(Y) = 9 のとき<br>
\\[\\rho = \\frac{4}{\\sqrt{16}\\sqrt{9}} = \\frac{4}{4 \\times 3} = \\frac{4}{12} = \\frac{1}{3} \\approx 0.33\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・相関係数は単位に依存しない（共分散との違い）<br>
・線形変換: ρ(aX+b, cY+d) = (ac/|ac|)·ρ(X, Y)<br>
・相関係数=0でも、非線形な関係がある可能性がある<br>
・統計検定2級では、散布図と相関係数を対応させる問題が頻出<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「15-6. 2変数の期待値と分散」<br>
・統計WEB「26-3. 相関係数」<br>
・統計検定2級対策教材で検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'correlation', '2variables', 'grade2']
        },

        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【2変数の分散】X+YとX-Yの分散の公式は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>公式:</b><br>
\\[V(X + Y) = V(X) + V(Y) + 2\\text{Cov}(X, Y)\\]
\\[V(X - Y) = V(X) + V(Y) - 2\\text{Cov}(X, Y)\\]
<br>

<b>独立な場合（Cov(X, Y) = 0）:</b><br>
\\[V(X + Y) = V(X) + V(Y)\\]
\\[V(X - Y) = V(X) + V(Y)\\]
<br>

<hr>

<b>具体例:</b><br>
V(X) = 4、V(Y) = 9、Cov(X, Y) = 2 のとき<br>
<br>
和の分散:<br>
\\[V(X + Y) = 4 + 9 + 2(2) = 13 + 4 = 17\\]
<br>
差の分散:<br>
\\[V(X - Y) = 4 + 9 - 2(2) = 13 - 4 = 9\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・期待値は常に加法的: E(X+Y) = E(X) + E(Y)、E(X-Y) = E(X) - E(Y)<br>
・分散は加法的ではない（共分散の項が加わる）<br>
・独立な場合、和の分散も差の分散も V(X) + V(Y) になる<br>
・統計検定2級では、この公式を使った計算問題が頻出<br>
・共分散が正なら V(X+Y) > V(X-Y)、負なら逆転する<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「15-6. 2変数の期待値と分散」<br>
・統計検定2級公式問題集で頻出<br>
・複数の統計学教材で検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'variance', '2variables', 'grade2']
        },

        # ===== 指数分布 =====
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【指数分布】指数分布の確率密度関数は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
指数分布は、「次に何かが起こるまでの期間」を表す連続型確率分布です。<br>
機械故障、災害発生、顧客来店などの待ち時間をモデル化します。<br>
<br>

<b>確率密度関数:</b><br>
\\[f(x) = \\lambda e^{-\\lambda x} \\quad (x \\geq 0, \\lambda > 0)\\]
<br>

<b>累積分布関数:</b><br>
\\[F(x) = P(X \\leq x) = 1 - e^{-\\lambda x}\\]
<br>

<hr>

<b>具体例:</b><br>
1時間に平均10人来店する店（λ = 10）で、次の客まで6分（0.1時間）以内の確率:<br>
\\[P(X \\leq 0.1) = 1 - e^{-10 \\times 0.1} = 1 - e^{-1} \\approx 1 - 0.368 = 0.632\\]
約63.2%の確率で6分以内に次の客が来る。<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・パラメータλは「単位時間あたりの平均発生回数」<br>
・ポアソン分布（回数）と密接に関連（指数分布は期間）<br>
・無記憶性: P(X>s+t | X>s) = P(X>t)（過去の情報が未来に影響しない）<br>
・統計検定2級では、累積分布関数を使った確率計算が頻出<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「15-1. 指数分布」<br>
・とけたろうブログ「指数分布【統計検定準1級のための数学③】」<br>
・複数の統計学教材で公式を検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'exponential-distribution', 'grade2']
        },

        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【指数分布】指数分布の期待値と分散は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>公式:</b><br>
指数分布 Exp(λ) に従う確率変数Xについて:<br>
\\[E(X) = \\frac{1}{\\lambda}\\]
\\[V(X) = \\frac{1}{\\lambda^2}\\]
\\[\\sigma(X) = \\frac{1}{\\lambda}\\]
<br>

期待値と標準偏差が等しいことが特徴です。<br>
<br>

<hr>

<b>具体例:</b><br>
1時間に平均5回起こる現象（λ = 5）の場合:<br>
<br>
期待値（平均待ち時間）:<br>
\\[E(X) = \\frac{1}{5} = 0.2\\text{時間} = 12\\text{分}\\]
<br>
分散:<br>
\\[V(X) = \\frac{1}{5^2} = \\frac{1}{25} = 0.04\\]
<br>
標準偏差:<br>
\\[\\sigma(X) = \\frac{1}{5} = 0.2\\text{時間} = 12\\text{分}\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・λが大きいほど、平均待ち時間は短くなる（頻繁に起こる）<br>
・期待値 = 標準偏差 = 1/λ という関係は指数分布特有<br>
・ポアソン分布との関係: ポアソン分布のλと同じ値を使う<br>
・統計検定2級では、期待値・分散の計算と解釈が問われる<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「15-1. 指数分布」<br>
・複数の統計学教材で検証済み<br>
・公式の導出は積分を用いた計算による
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'exponential-distribution', 'expectation', 'variance', 'grade2']
        },

        # ===== 2変数の確率分布 =====
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【2変数の確率分布】同時確率分布と周辺確率分布の違いは？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>同時確率分布（Joint Probability Distribution）:</b><br>
2つの確率変数X、Yがそれぞれ特定の値をとるときの確率の対応関係。<br>
離散型: \\(f(x_i, y_j) = P(X = x_i, Y = y_j)\\)<br>
連続型: 同時確率密度関数 f(x, y) で表現<br>
<br>

<b>周辺確率分布（Marginal Probability Distribution）:</b><br>
一方の変数について、もう一方の変数のすべての値を足し合わせた（積分した）分布。<br>
離散型: \\(f_X(x_i) = \\sum_j f(x_i, y_j)\\)<br>
連続型: \\(f_X(x) = \\int f(x, y) dy\\)<br>
<br>

<hr>

<b>具体例（離散型）:</b><br>
血液型（A, B, O, AB）と性別（男, 女）の同時分布表から:<br>
<br>
同時確率: P(血液型=A かつ 性別=男) = 0.18<br>
周辺確率: P(血液型=A) = P(A, 男) + P(A, 女) = 0.18 + 0.20 = 0.38<br>
周辺確率: P(性別=男) = すべての血液型について男性の確率を合計<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・同時確率の総和は必ず1: \\(\\sum_i \\sum_j f(x_i, y_j) = 1\\)<br>
・周辺確率は、同時確率表の「周辺」（行または列の合計）に相当<br>
・独立な場合: \\(f(x, y) = f_X(x) \\cdot f_Y(y)\\)<br>
・統計検定2級では、同時分布表から周辺分布を求める問題が頻出<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「15-5. 2変数の確率分布」<br>
・統計検定2級CBT公式問題集の解説（確率分布の分野）<br>
・複数の統計学教材で検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'joint-distribution', 'marginal-distribution', '2variables', 'grade2']
        },
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("統計検定2級 - いろいろな確率分布3（検証済み）")
    print("=" * 70)
    print()

    # AnkiConnect接続確認
    print("🔌 AnkiConnectに接続中...")
    version = invoke_anki('version')
    if version is None:
        print("❌ Ankiが起動していないか、AnkiConnectがインストールされていません")
        print("   Ankiを起動してから再度実行してください。")
        return

    print(f"✅ AnkiConnect接続成功")
    print()

    # デッキとモデル名
    deck_name = "統計学v2"
    model_name = "Basic"

    # カード作成
    cards = create_cards()
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
                    'allowDuplicate': False
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
    print("✨ いろいろな確率分布3 カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 共分散の定義と公式")
    print("  カード2: 相関係数の定義と公式")
    print("  カード3: 2変数の和と差の分散")
    print("  カード4: 指数分布の確率密度関数")
    print("  カード5: 指数分布の期待値と分散")
    print("  カード6: 同時確率分布と周辺確率分布")
    print()


if __name__ == "__main__":
    main()
