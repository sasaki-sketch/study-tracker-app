#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
測定尺度（名義・順序・間隔・比例）- Ankiカード生成
統計検定2級頻出問題
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
    """尺度問題カードを作成"""

    cards = [
        # ========================================
        # 全体理解カード
        # ========================================
        {
            'front': '<div class="question"><h3>測定尺度4種類の違いは?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">名義 < 順序 < 間隔 < 比例（下位→上位）</h3>

<div class="mnemonic">
<strong>💡 一発で覚える表:</strong>
<table style="width:100%; margin-top:15px; font-size:20px; border-collapse: collapse;">
<tr style="background:#e8f4f8; font-weight:bold;">
<td style="padding:12px; border:1px solid #ddd;">尺度</td>
<td style="padding:12px; border:1px solid #ddd;">分類</td>
<td style="padding:12px; border:1px solid #ddd;">大小</td>
<td style="padding:12px; border:1px solid #ddd;">差</td>
<td style="padding:12px; border:1px solid #ddd;">比</td>
<td style="padding:12px; border:1px solid #ddd;">0の意味</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;"><strong>名義</strong></td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
<td style="padding:10px; border:1px solid #ddd;">-</td>
<td style="padding:10px; border:1px solid #ddd;">-</td>
<td style="padding:10px; border:1px solid #ddd;">-</td>
<td style="padding:10px; border:1px solid #ddd;">なし</td>
</tr>
<tr style="background:#f8f9fa;">
<td style="padding:10px; border:1px solid #ddd;"><strong>順序</strong></td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
<td style="padding:10px; border:1px solid #ddd;">-</td>
<td style="padding:10px; border:1px solid #ddd;">-</td>
<td style="padding:10px; border:1px solid #ddd;">なし</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ddd;"><strong>間隔</strong></td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
<td style="padding:10px; border:1px solid #ddd;">-</td>
<td style="padding:10px; border:1px solid #ddd;">相対的</td>
</tr>
<tr style="background:#f8f9fa;">
<td style="padding:10px; border:1px solid #ddd;"><strong>比例</strong></td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
<td style="padding:10px; border:1px solid #ddd;">✓</td>
<td style="padding:10px; border:1px solid #ddd;"><strong>絶対的</strong></td>
</tr>
</table>
</div>

<div class="context">
<strong>📊 判定フローチャート:</strong>
<p style="line-height:2.0; margin-top:10px;">
1. 分類だけ？ → <strong>名義</strong><br>
2. 順番ある？ → <strong>順序</strong><br>
3. 差に意味ある？ → <strong>間隔 or 比例</strong><br>
4. <strong>比をとれる?/0が絶対的?</strong> → Yes=比例, No=間隔
</p>
</div>

<div class="mnemonic">
<strong>🎯 究極の覚え方:</strong>
<p><strong>「名は名前、順は順番、間は間隔、比は比較」</strong></p>
<p style="margin-top:10px; font-size:19px; color:#4b5563;">
上位の尺度ほど、数学的演算ができる!
</p>
</div>
</div>''',
            'tags': ['measurement-scales', 'overview', 'essential', 'statistics-exam']
        },

        # ========================================
        # 名義尺度 2問
        # ========================================
        {
            'front': '<div class="question"><h3>「血液型（A, B, O, AB）」は何尺度?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">名義尺度</h3>

<div class="mnemonic">
<strong>💡 判定理由:</strong>
<p>✓ 分類するだけ（グループ分け）</p>
<p>✗ 大小関係なし（A型>B型は意味不明）</p>
<p>✗ 差も計算できない</p>
<p>✗ 比もとれない</p>
</div>

<div class="context">
<strong>📊 名義尺度の特徴:</strong>
<p><strong>「ラベル貼り」だけ</strong></p>
<p style="margin-top:10px;">
・カテゴリーを区別するだけ<br>
・番号に意味なし<br>
・計算不可（足し算も引き算もNG）
</p>
</div>

<div class="mnemonic">
<strong>🎯 他の例:</strong>
<p>性別、国籍、職業、背番号、郵便番号</p>
<p style="margin-top:5px; font-size:19px; color:#4b5563;">
すべて「名前をつけてるだけ」
</p>
</div>
</div>''',
            'tags': ['measurement-scales', 'nominal', 'essential', 'statistics-exam']
        },

        {
            'front': '<div class="question"><h3>「電話番号」は何尺度?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">名義尺度</h3>

<div class="mnemonic">
<strong>💡 引っかけポイント:</strong>
<p>❌ 「数字だから計算できそう」→ 罠!</p>
<p>✅ 090-1234-5678 は単なる<strong>識別子</strong></p>
<p>✅ 大きい電話番号が偉いわけではない</p>
</div>

<div class="context">
<strong>📊 考え方:</strong>
<p>「2つの電話番号の差」に意味ある?</p>
<p>→ <strong>ない!</strong> だから名義尺度</p>
<p style="margin-top:10px;">
例: 090-1111-1111 と 090-2222-2222<br>
差 = 1111-1111? → 意味不明!
</p>
</div>

<div class="mnemonic">
<strong>🎯 名義尺度の見分け方:</strong>
<p><strong>「入れ替えても影響ない?」</strong></p>
<p>電話番号をシャッフルしても、それぞれの人を識別できればOK → 名義尺度</p>
</div>
</div>''',
            'tags': ['measurement-scales', 'nominal', 'tricky', 'statistics-exam']
        },

        # ========================================
        # 順序尺度 2問
        # ========================================
        {
            'front': '<div class="question"><h3>「満足度（とても満足・満足・普通・不満・とても不満）」は何尺度?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">順序尺度</h3>

<div class="mnemonic">
<strong>💡 判定理由:</strong>
<p>✓ 分類できる</p>
<p>✓ <strong>順序がある</strong>（とても満足 > 満足 > 普通...）</p>
<p>✗ 差は計算できない</p>
<p>✗ 「とても満足」と「満足」の差 ≠ 「満足」と「普通」の差</p>
</div>

<div class="context">
<strong>📊 順序尺度の特徴:</strong>
<p><strong>「順番はあるが、間隔は不明」</strong></p>
<p style="margin-top:10px;">
・ランキング的<br>
・大小比較はOK<br>
・差の計算はNG（等間隔じゃない）
</p>
</div>

<div class="mnemonic">
<strong>🎯 他の例:</strong>
<p>学歴（小中高大）、成績(A B C D)、競技の順位(1位2位3位)</p>
<p style="margin-top:5px; font-size:19px; color:#4b5563;">
すべて「順番はわかるけど、差はわからない」
</p>
</div>
</div>''',
            'tags': ['measurement-scales', 'ordinal', 'essential', 'statistics-exam']
        },

        {
            'front': '<div class="question"><h3>「マラソンの順位（1位、2位、3位...）」は何尺度?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">順序尺度</h3>

<div class="mnemonic">
<strong>💡 判定理由:</strong>
<p>✓ 順序がある（1位 > 2位 > 3位）</p>
<p>✗ 1位と2位の差 ≠ 2位と3位の差</p>
<p style="margin-top:10px;">
例: 1位と2位のタイム差0.1秒<br>
　　2位と3位のタイム差30秒<br>
→ 順位の差は同じ「1」だが、実力差は違う!
</p>
</div>

<div class="context">
<strong>📊 注意:</strong>
<p><strong>「タイム」なら比例尺度!</strong></p>
<p>2時間10分 vs 2時間20分 → 比がとれる</p>
<p style="margin-top:10px;">
でも「順位」は順序尺度<br>
→ 同じデータでも見方で尺度が変わる!
</p>
</div>

<div class="mnemonic">
<strong>🎯 順序尺度の本質:</strong>
<p><strong>「並べられるけど、等間隔じゃない」</strong></p>
</div>
</div>''',
            'tags': ['measurement-scales', 'ordinal', 'essential', 'statistics-exam']
        },

        # ========================================
        # 間隔尺度 2問
        # ========================================
        {
            'front': '<div class="question"><h3>「テストの点数（0〜100点）」は何尺度?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">間隔尺度</h3>

<div class="mnemonic">
<strong>💡 判定理由:</strong>
<p>✓ 順序がある</p>
<p>✓ <strong>差に意味がある</strong>（80点-60点 = 20点）</p>
<p>✗ 比はとれない（80点は40点の2倍頭がいい?）</p>
<p>✗ 0点 = 「知識ゼロ」ではない（たまたま0点）</p>
</div>

<div class="context">
<strong>📊 間隔尺度の特徴:</strong>
<p><strong>「等間隔だけど、絶対的な0点がない」</strong></p>
<p style="margin-top:10px;">
・差は計算できる<br>
・平均値を出せる<br>
・でも比はNG（2倍、3倍は言えない）
</p>
</div>

<div class="mnemonic">
<strong>🎯 間隔尺度の見分け方:</strong>
<p><strong>「0が相対的」</strong></p>
<p>テスト0点でも知識は「ある」<br>
→ 0は「基準点」であって「無」ではない
</p>
</div>
</div>''',
            'tags': ['measurement-scales', 'interval', 'essential', 'statistics-exam']
        },

        {
            'front': '<div class="question"><h3>「西暦（2024年、2025年...）」は何尺度?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">間隔尺度</h3>

<div class="mnemonic">
<strong>💡 判定理由:</strong>
<p>✓ 差に意味がある（2025-2020 = 5年）</p>
<p>✗ 比はNG（2000年は1000年の2倍古い？）</p>
<p>✗ 西暦0年 = 「時間がない」わけではない</p>
</div>

<div class="context">
<strong>📊 重要ポイント:</strong>
<p><strong>「0が任意に決められた基準点」</strong></p>
<p style="margin-top:10px;">
西暦0年 = キリスト生誕年（約）<br>
→ 人間が勝手に決めた起点<br>
→ 絶対的な「時間ゼロ」ではない
</p>
</div>

<div class="mnemonic">
<strong>🎯 間隔vs比例の決め手:</strong>
<p><strong>「2倍、3倍と言えるか?」</strong></p>
<p>❌ 2000年は1000年の2倍長い歴史? → 意味不明</p>
<p>✅ でも差は計算できる → 間隔尺度</p>
</div>
</div>''',
            'tags': ['measurement-scales', 'interval', 'tricky', 'statistics-exam']
        },

        # ========================================
        # 比例尺度 2問
        # ========================================
        {
            'front': '<div class="question"><h3>「身長（cm）」は何尺度?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">比例尺度</h3>

<div class="mnemonic">
<strong>💡 判定理由:</strong>
<p>✓ 順序がある</p>
<p>✓ 差に意味がある</p>
<p>✓ <strong>比がとれる</strong>（180cmは90cmの2倍）</p>
<p>✓ <strong>0が絶対的</strong>（0cm = 「身長が存在しない」）</p>
</div>

<div class="context">
<strong>📊 比例尺度の特徴:</strong>
<p><strong>「最強の尺度 - すべての演算が可能」</strong></p>
<p style="margin-top:10px;">
・四則演算すべてOK<br>
・比率を計算できる<br>
・絶対的な0点がある
</p>
</div>

<div class="mnemonic">
<strong>🎯 比例尺度の見分け方:</strong>
<p><strong>「0 = 無い(存在しない)」</strong></p>
<p>身長0cm = 身長が無い<br>
体重0kg = 体重が無い<br>
→ 0が絶対的 → 比例尺度
</p>
</div>
</div>''',
            'tags': ['measurement-scales', 'ratio', 'essential', 'statistics-exam']
        },

        {
            'front': '<div class="question"><h3>「年収（万円）」は何尺度?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">比例尺度</h3>

<div class="mnemonic">
<strong>💡 判定理由:</strong>
<p>✓ 差に意味がある（600万-400万 = 200万）</p>
<p>✓ <strong>比がとれる</strong>（600万は300万の2倍）</p>
<p>✓ <strong>0円 = 収入が無い</strong>（絶対的な0）</p>
</div>

<div class="context">
<strong>📊 具体例:</strong>
<p>Aさん: 400万円<br>
Bさん: 800万円</p>
<p style="margin-top:10px;">
✅ 差: 800-400 = 400万円<br>
✅ 比: 800÷400 = 2倍<br>
→ 両方意味がある = 比例尺度
</p>
</div>

<div class="mnemonic">
<strong>🎯 他の比例尺度例:</strong>
<p>体重、距離、時間(秒)、売上、人数、温度(K)</p>
<p style="margin-top:5px; font-size:19px; color:#4b5563;">
すべて「0 = 無い」が成立
</p>
</div>
</div>''',
            'tags': ['measurement-scales', 'ratio', 'essential', 'statistics-exam']
        },

        # ========================================
        # 難問・引っかけ問題
        # ========================================
        {
            'front': '<div class="question"><h3>「温度(℃)」と「温度(K)」は何尺度?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">℃ = 間隔尺度　/　K = 比例尺度</h3>

<div class="mnemonic">
<strong>💡 重要な違い:</strong>
<p><strong>℃（摂氏）:</strong></p>
<p>✗ 0℃ = 「温度がない」ではない</p>
<p>✗ 20℃は10℃の2倍暖かい? → NO</p>
<p>→ <strong>間隔尺度</strong></p>
<p style="margin-top:15px;">
<strong>K（ケルビン・絶対温度）:</strong></p>
<p>✓ 0K = 絶対零度（分子運動停止）</p>
<p>✓ 300Kは150Kの2倍の熱エネルギー</p>
<p>→ <strong>比例尺度</strong></p>
</div>

<div class="context">
<strong>📊 なぜ違う?</strong>
<p>℃は水の凍結点を「0」と<strong>任意に</strong>設定<br>
Kは熱力学的な「絶対ゼロ」が0K</p>
<p style="margin-top:10px;">
→ 0の意味が違う!<br>
→ 尺度が違う!
</p>
</div>

<div class="mnemonic">
<strong>🎯 統計検定の超頻出ポイント!</strong>
<p>「同じ温度でも単位で尺度が変わる」<br>
→ 間隔vs比例の最難問
</p>
</div>
</div>''',
            'tags': ['measurement-scales', 'interval-vs-ratio', 'tricky', 'essential', 'statistics-exam']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("測定尺度（名義・順序・間隔・比例）- Ankiカード生成")
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
    deck_name = "Greek Letters & Statistics"
    model_name = "Greek Letters v2 (Super Readable)"

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
    print("✨ 測定尺度カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print(f"🎯 カード内容:")
    print(f"  1. 全体理解（4尺度の比較表）")
    print(f"  2-3. 名義尺度 × 2（血液型、電話番号）")
    print(f"  4-5. 順序尺度 × 2（満足度、順位）")
    print(f"  6-7. 間隔尺度 × 2（点数、西暦）")
    print(f"  8-9. 比例尺度 × 2（身長、年収）")
    print(f"  10. 難問（温度℃ vs K）")
    print()
    print(f"🔍 Ankiで確認:")
    print(f"  tag:measurement-scales で検索")
    print(f"  tag:essential で重要カードのみ")
    print(f"  tag:tricky で引っかけ問題のみ")
    print()


if __name__ == "__main__":
    main()
