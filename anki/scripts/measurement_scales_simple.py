#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
測定尺度 - シンプル版（色なし）
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


def create_scale_cards(deck_name, model_name):
    """尺度カードを作成（シンプル版）"""

    cards = [
        # カード1: 4つの尺度
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>データの4つの尺度を<br>弱い順に説明してください</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>1. 名義尺度（質的）</b><br>
• カテゴリーの分類のみ<br>
• 例：性別、血液型、色<br>
<br>
<b>2. 順序尺度（質的）</b><br>
• 順序・ランク付けが可能<br>
• 例：成績（A/B/C）、満足度<br>
<br>
<b>3. 間隔尺度（量的）</b><br>
• 間隔が等しい、ゼロは相対的<br>
• 例：温度（℃）、年代<br>
<br>
<b>4. 比率尺度（量的）</b><br>
• 絶対的なゼロがある<br>
• 例：身長、体重、価格<br>
<br>
<hr>
<b>覚え方:</b><br>
名義 → 順序 → 間隔 → 比率（弱→強）
</div>''',
            'tags': ['scales', 'overview']
        },

        # カード2: 名義尺度
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【名義尺度】とは?<br>特徴と例を説明</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
カテゴリーの分類のみ可能な尺度<br>
<br>
<hr>
<b>特徴:</b><br>
• 数値は単なるラベル<br>
• 順序に意味がない<br>
• 計算できない<br>
<br>
<b>例:</b><br>
• 性別（男/女）<br>
• 血液型（A/B/O/AB）<br>
• 色（赤/青/緑）<br>
• 背番号<br>
<br>
<hr>
<b>可能な統計:</b><br>
• 度数（カウント）<br>
• 最頻値（モード）
</div>''',
            'tags': ['scales', 'nominal']
        },

        # カード3: 順序尺度
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【順序尺度】とは?<br>特徴と例を説明</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
順序・ランク付けが可能な尺度<br>
<br>
<hr>
<b>特徴:</b><br>
• 大小関係がある<br>
• 間隔は等しくない<br>
• 足し算・引き算は無意味<br>
<br>
<b>例:</b><br>
• 成績（A/B/C/D）<br>
• 満足度（とても満足/満足/不満）<br>
• 順位（1位、2位、3位）<br>
<br>
<hr>
<b>可能な統計:</b><br>
• 中央値<br>
• パーセンタイル
</div>''',
            'tags': ['scales', 'ordinal']
        },

        # カード4: 間隔尺度
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【間隔尺度】とは?<br>特徴と例を説明</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
等間隔だが、絶対的なゼロがない尺度<br>
<br>
<hr>
<b>特徴:</b><br>
• 間隔が等しい<br>
• 足し算・引き算が可能<br>
• ゼロは相対的（ゼロでも存在する）<br>
• 比は意味がない（2倍とは言えない）<br>
<br>
<b>例:</b><br>
• 温度（℃、℉）→ 0℃でも温度は存在<br>
• 年代（西暦）→ 0年でも時間は存在<br>
<br>
<hr>
<b>可能な統計:</b><br>
• 平均、標準偏差<br>
• 相関係数
</div>''',
            'tags': ['scales', 'interval']
        },

        # カード5: 比率尺度
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【比率尺度】とは?<br>特徴と例を説明</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
絶対的なゼロがあり、比が意味を持つ尺度<br>
<br>
<hr>
<b>特徴:</b><br>
• 最も強い尺度<br>
• すべての計算が可能<br>
• 絶対的なゼロ（ゼロ = 存在しない）<br>
• 比が意味を持つ（2倍、3倍が言える）<br>
<br>
<b>例:</b><br>
• 身長、体重<br>
• 距離、時間<br>
• 価格、売上<br>
<br>
<hr>
<b>可能な統計:</b><br>
すべての統計手法が使える
</div>''',
            'tags': ['scales', 'ratio']
        },

        # カード6: 間隔と比率の違い
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>間隔尺度と比率尺度の<br>決定的な違いは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【絶対的なゼロの有無】</b><br>
<br>
<hr>
<b>間隔尺度:</b><br>
• ゼロは相対的<br>
• ゼロでも「存在する」<br>
• 比は意味がない<br>
• 例：0℃ でも温度は存在する<br>
<br>
<b>比率尺度:</b><br>
• ゼロは絶対的<br>
• ゼロ = 「存在しない」<br>
• 比が意味を持つ<br>
• 例：0kg = 重さが存在しない<br>
<br>
<hr>
<b>判別方法:</b><br>
「ゼロの時、それは存在しないか?」<br>
→ はい = 比率尺度<br>
→ いいえ = 間隔尺度
</div>''',
            'tags': ['scales', 'comparison']
        },

        # カード7: 温度の尺度（難問）
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>温度（℃）と温度（K）は<br>それぞれ何尺度?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>答え:</b><br>
• 温度（℃） = <b>間隔尺度</b><br>
• 温度（K） = <b>比率尺度</b><br>
<br>
<hr>
<b>理由:</b><br>
<br>
<b>℃（セルシウス）:</b><br>
• 0℃ = 水の凝固点（相対的）<br>
• 0℃でも温度は存在する<br>
• 20℃は10℃の2倍熱いとは言えない<br>
<br>
<b>K（ケルビン）:</b><br>
• 0K = 絶対零度（存在しない）<br>
• 絶対的なゼロ<br>
• 200Kは100Kの2倍の熱エネルギー<br>
<br>
<hr>
<b>これが統計検定の引っかけ問題!</b>
</div>''',
            'tags': ['scales', 'tricky']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("測定尺度 - シンプル版カード生成")
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
    cards = create_scale_cards(deck_name, model_name)
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
    print("✨ 尺度カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()


if __name__ == "__main__":
    main()
