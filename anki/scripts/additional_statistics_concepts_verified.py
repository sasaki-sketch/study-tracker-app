#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
追加の統計概念 - 検証済みAnkiカード
統計検定2級対策

情報源：
- 各種統計教科書
- 統計WEB
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


def create_additional_concepts_cards(deck_name, model_name):
    """追加の統計概念カードを作成（検証済み）"""

    cards = [
        # カード1: zスコア（標準化得点）
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【標準化得点（zスコア）】<br>z = 2 は何を意味する？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>zスコア（標準化得点）とは:</b><br>
データを平均0、標準偏差1に変換した値<br>
<br>

<b>公式:</b><br>
\\[z = \\frac{x - \\bar{x}}{s}\\]
<br>

または母集団の場合:<br>
\\[z = \\frac{x - \\mu}{\\sigma}\\]
<br>

<hr>

<b>z = 2 の意味:</b><br>
<br>

• その値は<b>平均より2標準偏差上</b>にある<br>
• <b>平均より2σ大きい</b><br>
<br>

<b>具体例:</b><br>
テストの平均が60点、標準偏差が10点の場合:<br>
• z = 2 なら、得点は 60 + 2×10 = <b>80点</b><br>
• z = -1 なら、得点は 60 - 1×10 = <b>50点</b><br>
<br>

<hr>

<b>【zスコアの解釈】</b><br>
<br>

<b>正規分布の場合:</b><br>
• <b>|z| < 1</b>: 約68%のデータが該当（よくある値）<br>
• <b>|z| < 2</b>: 約95%のデータが該当<br>
• <b>|z| < 3</b>: 約99.7%のデータが該当<br>
• <b>|z| > 3</b>: 外れ値の可能性<br>
<br>

<b>z = 2 は:</b><br>
• 上位約2.5%に入る<br>
• やや珍しい高い値<br>
<br>

<hr>

<b>【zスコアの用途】</b><br>
<br>

• <b>異なる単位のデータを比較</b>できる<br>
• 身長と体重を同じ尺度で比較<br>
• テストの科目間比較<br>
• 外れ値の検出<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計学の基礎教科書<br>
統計WEB「標準化と偏差値」
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'z-score', 'standardization']
        },

        # カード2: 2変数の可視化
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【2変数の関連】<br>2変数の関連を面積で<br>可視化するグラフは？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>答え: ヒートマップ（モザイクプロット）</b><br>
<br>

<hr>

<b>【主な2変数の可視化方法】</b><br>
<br>

<b>①散布図（Scatter Plot）</b><br>
• <b>量的変数 × 量的変数</b><br>
• 点で表現<br>
• 相関関係を見る<br>
• 例: 身長と体重の関係<br>
<br>

<b>②ヒートマップ（Heat Map）</b><br>
• <b>質的変数 × 質的変数</b><br>
• <b>面積と色</b>で頻度を表現<br>
• クロス集計表の可視化<br>
• 例: 性別×購買行動<br>
<br>

<b>③箱ひげ図（複数）</b><br>
• <b>質的変数 × 量的変数</b><br>
• カテゴリごとの分布比較<br>
• 例: 学年別のテスト得点<br>
<br>

<b>④バブルチャート</b><br>
• 散布図に<b>第3変数を円の大きさ</b>で追加<br>
• 3変数を同時表示<br>
<br>

<hr>

<b>【ヒートマップの特徴】</b><br>
<br>

• <b>面積</b>が相対頻度を表す<br>
• <b>色</b>の濃淡で値の大小を表現<br>
• パターンを直感的に把握しやすい<br>
• クロス集計の可視化に最適<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
データ可視化の基礎<br>
統計グラフの種類と使い分け
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'visualization', 'bivariate']
        },

        # カード3: 説明変数と目的変数
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【回帰分析の基本】<br>「広告費と売上の関係」で<br>説明変数と目的変数はどっち?</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>答え:</b><br>
• <b>説明変数（独立変数）</b>: 広告費<br>
• <b>目的変数（従属変数）</b>: 売上<br>
<br>

<hr>

<b>【変数の役割】</b><br>
<br>

<b>説明変数（Explanatory Variable）</b><br>
• <b>原因となる変数</b><br>
• 独立変数、予測変数とも呼ぶ<br>
• <b>xで表記</b><br>
• 例: 広告費、勉強時間、気温<br>
<br>

<b>目的変数（Response Variable）</b><br>
• <b>結果となる変数</b><br>
• 従属変数、応答変数とも呼ぶ<br>
• <b>yで表記</b><br>
• 例: 売上、テスト得点、アイス売上<br>
<br>

<hr>

<b>【見分け方】</b><br>
<br>

<b>時間的順序:</b><br>
• 先に起こる → 説明変数<br>
• 後に起こる → 目的変数<br>
<br>

<b>因果関係:</b><br>
• 「〇〇が△△に影響する」<br>
• 〇〇 → 説明変数<br>
• △△ → 目的変数<br>
<br>

<b>予測の文脈:</b><br>
• 「〇〇から△△を予測する」<br>
• 〇〇 → 説明変数<br>
• △△ → 目的変数<br>
<br>

<hr>

<b>【具体例】</b><br>
<br>

<b>例1: 勉強時間とテスト得点</b><br>
• 説明変数: 勉強時間<br>
• 目的変数: テスト得点<br>
<br>

<b>例2: 気温とアイス売上</b><br>
• 説明変数: 気温<br>
• 目的変数: アイス売上<br>
<br>

<b>例3: 身長と体重</b><br>
• どちらとも決められない場合もある<br>
• 文脈による<br>
<br>

<hr>

<b>【注意点】</b><br>
<br>

• <b>相関 ≠ 因果</b><br>
• 説明変数が原因とは限らない<br>
• 第三の要因がある可能性<br>
• 逆の因果関係の可能性<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
回帰分析の基礎<br>
統計学入門テキスト
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'regression', 'variables']
        },

        # カード4: 名義尺度
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【尺度水準】<br>【名義尺度】とは?<br>特徴と例を説明</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>名義尺度（Nominal Scale）:</b><br>
カテゴリーを<b>区別するだけ</b>の尺度<br>
<br>

<hr>

<b>【特徴】</b><br>
<br>

<b>できること:</b><br>
• ✅ <b>分類</b>（区別）<br>
• ✅ <b>同じか違うか</b>を判断<br>
• ✅ 度数を数える<br>
<br>

<b>できないこと:</b><br>
• ❌ 大小比較<br>
• ❌ 順序づけ<br>
• ❌ 足し算・引き算<br>
• ❌ 平均の計算<br>
<br>

<b>数字の意味:</b><br>
• 数字は<b>ラベル</b>に過ぎない<br>
• 背番号のようなもの<br>
• 1番が2番より優れているわけではない<br>
<br>

<hr>

<b>【具体例】</b><br>
<br>

• <b>性別</b>: 男性、女性<br>
• <b>血液型</b>: A型、B型、O型、AB型<br>
• <b>職業</b>: 会社員、学生、自営業<br>
• <b>住んでいる都道府県</b><br>
• <b>好きな色</b><br>
• <b>スポーツチームの背番号</b><br>
<br>

<hr>

<b>【統計分析】</b><br>
<br>

<b>使える統計量:</b><br>
• <b>度数</b>（カウント）<br>
• <b>最頻値</b>（モード）<br>
• <b>割合・比率</b><br>
<br>

<b>使える検定:</b><br>
• <b>カイ二乗検定</b><br>
• フィッシャーの正確確率検定<br>
<br>

<b>使えない統計量:</b><br>
• ❌ 平均値<br>
• ❌ 中央値<br>
• ❌ 標準偏差<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
<br>

• 最も情報量が少ない尺度<br>
• カテゴリー間に順序がない<br>
• 質的データ（カテゴリカルデータ）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計学の基礎<br>
スティーブンスの尺度水準
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'scales', 'nominal']
        },

        # カード5: 順序尺度
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【尺度水準】<br>【順序尺度】とは?<br>特徴と例を説明</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>順序尺度（Ordinal Scale）:</b><br>
カテゴリーに<b>順序がある</b>尺度<br>
<br>

<hr>

<b>【特徴】</b><br>
<br>

<b>できること:</b><br>
• ✅ <b>分類</b>（区別）<br>
• ✅ <b>順序づけ</b><br>
• ✅ 大小比較<br>
• ✅ 度数を数える<br>
<br>

<b>できないこと:</b><br>
• ❌ 間隔が等しくない<br>
• ❌ 足し算・引き算（意味がない）<br>
• ❌ 平均値（厳密には不適切）<br>
<br>

<b>数字の意味:</b><br>
• 順位を表す<br>
• 1位と2位の差 ≠ 2位と3位の差<br>
<br>

<hr>

<b>【具体例】</b><br>
<br>

• <b>満足度</b>: 不満、普通、満足、とても満足<br>
• <b>成績</b>: 優、良、可、不可<br>
• <b>順位</b>: 1位、2位、3位<br>
• <b>学年</b>: 小1、小2、小3<br>
• <b>Tシャツのサイズ</b>: S、M、L、XL<br>
• <b>硬度</b>: モース硬度（1〜10）<br>
<br>

<hr>

<b>【統計分析】</b><br>
<br>

<b>使える統計量:</b><br>
• <b>最頻値</b>（モード）<br>
• <b>中央値</b>（メジアン）<br>
• <b>パーセンタイル</b><br>
• 度数、割合<br>
<br>

<b>使える検定:</b><br>
• <b>マン・ホイットニーのU検定</b><br>
• <b>クラスカル・ウォリス検定</b><br>
• <b>ウィルコクソンの符号順位検定</b><br>
• スピアマンの順位相関<br>
<br>

<b>使えない統計量:</b><br>
• ❌ 平均値（使う場合もあるが厳密には不適切）<br>
• ❌ 標準偏差<br>
<br>

<hr>

<b>【名義尺度との違い】</b><br>
<br>

• 名義尺度: <b>順序なし</b>（例: 血液型）<br>
• 順序尺度: <b>順序あり</b>（例: 成績）<br>
<br>

<b>【間隔尺度との違い】</b><br>
<br>

• 順序尺度: <b>間隔が不等</b>（優と良の差 ≠ 良と可の差）<br>
• 間隔尺度: <b>間隔が等しい</b>（10℃と20℃の差 = 20℃と30℃の差）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計学の基礎<br>
ノンパラメトリック検定
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'scales', 'ordinal']
        },

        # カード6: 間隔尺度
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【尺度水準】<br>【間隔尺度】とは?<br>特徴と例を説明</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>間隔尺度（Interval Scale）:</b><br>
<b>間隔が等しい</b>が<b>絶対零点がない</b>尺度<br>
<br>

<hr>

<b>【特徴】</b><br>
<br>

<b>できること:</b><br>
• ✅ <b>分類</b><br>
• ✅ <b>順序づけ</b><br>
• ✅ <b>足し算・引き算</b><br>
• ✅ 間隔を比較<br>
• ✅ 平均値の計算<br>
<br>

<b>できないこと:</b><br>
• ❌ 比率の比較（2倍、半分など）<br>
• ❌ 掛け算・割り算（意味がない）<br>
<br>

<b>理由:</b><br>
• <b>絶対零点（真のゼロ）がない</b><br>
• 0℃は「温度がない」わけではない<br>
• 20℃は10℃の「2倍暑い」とは言えない<br>
<br>

<hr>

<b>【具体例】</b><br>
<br>

• <b>摂氏温度（℃）</b><br>
• <b>華氏温度（°F）</b><br>
• <b>西暦（年）</b><br>
• <b>偏差値</b><br>
• <b>IQスコア</b><br>
• <b>標準化得点（zスコア）</b><br>
<br>

<hr>

<b>【統計分析】</b><br>
<br>

<b>使える統計量:</b><br>
• <b>平均値</b><br>
• <b>中央値</b><br>
• <b>標準偏差</b><br>
• <b>分散</b><br>
• すべての記述統計量<br>
<br>

<b>使える検定:</b><br>
• <b>t検定</b><br>
• <b>分散分析（ANOVA）</b><br>
• <b>ピアソンの相関</b><br>
• <b>回帰分析</b><br>
• ほぼすべての検定<br>
<br>

<hr>

<b>【なぜ比率が使えないのか】</b><br>
<br>

<b>温度の例:</b><br>
• 10℃と20℃<br>
• 「20℃は10℃の2倍暑い」とは言えない<br>
• なぜなら、ケルビン温度では:<br>
  - 10℃ = 283K<br>
  - 20℃ = 293K<br>
  - 293K ≠ 283K × 2<br>
<br>

<hr>

<b>【比率尺度との違い】</b><br>
<br>

• 間隔尺度: <b>絶対零点なし</b>（例: 温度）<br>
• 比率尺度: <b>絶対零点あり</b>（例: 身長、体重）<br>
<br>

<b>比率尺度の例:</b><br>
• 身長: 0cmは「身長がない」<br>
• 180cmは90cmの2倍<br>
• 体重、時間、距離など<br>
<br>

<hr>

<b>【重要ポイント】</b><br>
<br>

• 量的データ<br>
• 間隔が等しい = 足し算・引き算OK<br>
• 絶対零点なし = 掛け算・割り算NG<br>
• ほとんどの統計分析が可能<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計学の基礎<br>
尺度水準と統計分析
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'scales', 'interval']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("追加の統計概念 - 検証済みAnkiカード生成")
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
    cards = create_additional_concepts_cards(deck_name, model_name)
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
    print("✨ 追加の統計概念カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: zスコア（標準化得点）")
    print("  カード2: 2変数の可視化グラフ")
    print("  カード3: 説明変数と目的変数")
    print("  カード4: 名義尺度")
    print("  カード5: 順序尺度")
    print("  カード6: 間隔尺度")
    print()


if __name__ == "__main__":
    main()
