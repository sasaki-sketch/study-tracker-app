#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
変化率の計算式 - Ankiカード生成
血肉にするための直感的理解
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


def create_rate_of_change_cards(deck_name, model_name):
    """変化率カードを作成"""

    cards = [
        # カード1: 基本公式
        {
            'front': '<div class="question"><h3>変化率の基本公式は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">変化率 = (新しい値 - 古い値) ÷ 古い値 × 100</h3>

<div class="mnemonic">
<strong>💡 直感的理解:</strong>
<p><strong>「変化幅を、元の大きさで割る」</strong></p>
<p style="margin-top:10px;">
例: 100円→120円に値上げ<br>
変化幅 = 20円<br>
元の大きさ = 100円<br>
変化率 = 20 ÷ 100 = 0.2 = <strong>20%</strong>
</p>
</div>

<div class="context">
<strong>📊 別の書き方:</strong>
<p>変化率 = (新 - 旧) / 旧 × 100</p>
<p>変化率 = (後 - 前) / 前 × 100</p>
<p>変化率 = Δ値 / 基準値 × 100</p>
</div>

<div class="mnemonic">
<strong>🎯 記憶の鍵:</strong>
<p><strong>「分母は常に古い値(Before)」</strong></p>
<p>↑これさえ覚えればOK!</p>
</div>
</div>''',
            'tags': ['rate-of-change', 'formula', 'essential', 'statistics']
        },

        # カード2: 分子と分母の意味
        {
            'front': '<div class="question"><h3>変化率の分子と分母は何を意味する?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">分子 = 変化の幅　/　分母 = 比較の基準</h3>

<div class="mnemonic">
<strong>💡 イメージ:</strong>
<p><strong>分子(上):</strong> 「どれだけ変わったか」= 差分</p>
<p><strong>分母(下):</strong> 「何と比べるか」= スタート地点</p>
</div>

<div class="context">
<strong>📊 具体例:</strong>
<p>売上: 50万円 → 60万円</p>
<p>
<strong>分子:</strong> 60 - 50 = <font color="#e74c3c">10万円</font> (変化幅)<br>
<strong>分母:</strong> <font color="#3498db">50万円</font> (元の売上=基準)<br>
<strong>変化率:</strong> 10 ÷ 50 = 0.2 = <strong>20%増</strong>
</p>
</div>

<div class="mnemonic">
<strong>🎯 間違えやすいポイント:</strong>
<p>❌ 分母を「新しい値」にしない!</p>
<p>✅ 分母は必ず「古い値(前の値)」</p>
</div>
</div>''',
            'tags': ['rate-of-change', 'understanding', 'essential']
        },

        # カード3: なぜ古い値で割るのか
        {
            'front': '<div class="question"><h3>なぜ変化率は「古い値」で割るの?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">「元の大きさ」を基準にするため</h3>

<div class="mnemonic">
<strong>💡 直感的説明:</strong>
<p>変化率は「<strong>元の大きさに対して何倍変化したか</strong>」を測る指標</p>
<p style="margin-top:10px;">
例: 体重60kg→66kg (6kg増)<br>
→ 元の体重60kgに対して、6kg増えた<br>
→ 6 ÷ 60 = 10% の増加
</p>
</div>

<div class="context">
<strong>📊 比較の例:</strong>
<table style="width:100%; margin-top:10px; font-size:19px;">
<tr style="background:#f8f9fa;">
<td><strong>項目</strong></td>
<td><strong>変化幅</strong></td>
<td><strong>元の値</strong></td>
<td><strong>変化率</strong></td>
</tr>
<tr>
<td>A商品</td>
<td>+10万</td>
<td>100万</td>
<td>10%</td>
</tr>
<tr style="background:#f8f9fa;">
<td>B商品</td>
<td>+10万</td>
<td>50万</td>
<td>20%</td>
</tr>
</table>
<p style="margin-top:10px;">同じ10万円増でも、元の大きさで変化率が違う!</p>
</div>

<div class="mnemonic">
<strong>🎯 覚え方:</strong>
<p><strong>「過去が基準(Past is Base)」</strong></p>
</div>
</div>''',
            'tags': ['rate-of-change', 'intuition', 'why']
        },

        # カード4: 増加率と減少率
        {
            'front': '<div class="question"><h3>増加率と減少率の計算は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">同じ公式! 符号で判断</h3>

<div class="mnemonic">
<strong>💡 公式は同じ:</strong>
<p>変化率 = (新 - 旧) / 旧 × 100</p>
<p style="margin-top:10px;">
<strong>プラス → 増加率</strong><br>
<strong>マイナス → 減少率</strong>
</p>
</div>

<div class="context">
<strong>📊 例:</strong>
<p><strong>増加:</strong> 100 → 120</p>
<p>(120-100)/100 = +20% (増加率20%)</p>
<p style="margin-top:15px;">
<strong>減少:</strong> 100 → 80</p>
<p>(80-100)/100 = -20% (減少率20%)</p>
</div>

<div class="mnemonic">
<strong>🎯 言葉の使い分け:</strong>
<p>✓ 増加率 = 伸び率 = 成長率</p>
<p>✓ 減少率 = 低下率 = 下落率</p>
<p>✓ 変化率 = 両方を含む総称</p>
</div>
</div>''',
            'tags': ['rate-of-change', 'increase-decrease', 'essential']
        },

        # カード5: 前年比・前月比
        {
            'front': '<div class="question"><h3>「前年比」「前月比」の計算は?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">前年比 = (今年 - 去年) / 去年 × 100</h3>

<div class="mnemonic">
<strong>💡 パターン:</strong>
<p><strong>「前◯◯比」= 前の◯◯が分母</strong></p>
<p style="margin-top:10px;">
前<strong>年</strong>比 → <strong>前年</strong>が分母<br>
前<strong>月</strong>比 → <strong>前月</strong>が分母<br>
前<strong>日</strong>比 → <strong>前日</strong>が分母
</p>
</div>

<div class="context">
<strong>📊 具体例:</strong>
<p><strong>前年比の計算:</strong></p>
<p>2024年売上: 500万円<br>
2025年売上: 550万円</p>
<p>前年比 = (550-500)/500 × 100 = <strong>+10%</strong></p>
<p style="margin-top:10px; font-size:19px; color:#666;">
「2025年は前年比10%増」と表現
</p>
</div>

<div class="mnemonic">
<strong>🎯 英語で理解:</strong>
<p>前年比 = Year-over-Year (YoY)</p>
<p>前月比 = Month-over-Month (MoM)</p>
<p>"over" = 「〜と比べて」= 分母!</p>
</div>
</div>''',
            'tags': ['rate-of-change', 'yoy', 'mom', 'statistics']
        },

        # カード6: よくある間違い
        {
            'front': '<div class="question"><h3>変化率計算でよくある間違いは?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">新しい値を分母にする間違い</h3>

<div class="mnemonic">
<strong>💡 NG例:</strong>
<p>100円 → 120円</p>
<p>❌ (120-100) / <font color="#e74c3c">120</font> = 16.7% (新しい値で割るのは誤り)</p>
<p>✅ (120-100) / <font color="#16a34a">100</font> = 20% (古い値で割るのが正解)</p>
</div>

<div class="context">
<strong>📊 なぜ間違える?</strong>
<p>「120円になった」という<strong>結果</strong>に目が行きがち</p>
<p>→ でも基準は<strong>スタート地点(100円)</strong>!</p>
</div>

<div class="mnemonic">
<strong>🎯 防止策:</strong>
<p><strong>時間軸で考える:</strong></p>
<p>過去(古い値) ──→ 現在(新しい値)</p>
<p>↑分母　　　　　↑分子に使う</p>
<p style="margin-top:10px;">
<strong>「スタートラインで割る」</strong>と覚える
</p>
</div>
</div>''',
            'tags': ['rate-of-change', 'common-mistakes', 'essential']
        },

        # カード7: 統計検定での出題
        {
            'front': '<div class="question"><h3>統計検定で変化率はどう出題される?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">時系列データの分析問題で頻出</h3>

<div class="mnemonic">
<strong>💡 典型的な問題:</strong>
<p>「2020年から2021年の売上変化率は?」</p>
<p>「前年比で最も成長した月は?」</p>
<p>「増加率が10%のとき、元の値は?」</p>
</div>

<div class="context">
<strong>📊 計算のポイント:</strong>
<p>✓ 電卓を使ってOK</p>
<p>✓ パーセント表示を忘れずに</p>
<p>✓ プラス/マイナスの符号に注意</p>
<p>✓ 小数第1位まで求める場合が多い</p>
</div>

<div class="mnemonic">
<strong>🎯 時短テクニック:</strong>
<p><strong>変化率 = (新 ÷ 旧 - 1) × 100</strong></p>
<p>例: 100→120<br>
120÷100 = 1.2<br>
1.2 - 1 = 0.2<br>
0.2 × 100 = 20%
</p>
<p style="margin-top:10px; font-size:19px; color:#666;">
電卓で「新÷旧」を先に計算すると楽!
</p>
</div>
</div>''',
            'tags': ['rate-of-change', 'statistics-exam', 'test-tips']
        },

        # カード8: 変化率と変化幅の違い
        {
            'front': '<div class="question"><h3>変化率と変化幅の違いは?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">変化幅 = 絶対値　/　変化率 = 相対値</h3>

<div class="mnemonic">
<strong>💡 イメージ:</strong>
<p><strong>変化幅:</strong> 「何円増えた?」→ 単位がある</p>
<p><strong>変化率:</strong> 「何倍になった?」→ %で表現</p>
</div>

<div class="context">
<strong>📊 比較例:</strong>
<table style="width:100%; margin-top:10px; font-size:19px;">
<tr style="background:#f8f9fa;">
<td><strong>商品</strong></td>
<td><strong>変化</strong></td>
<td><strong>変化幅</strong></td>
<td><strong>変化率</strong></td>
</tr>
<tr>
<td>A</td>
<td>100→110</td>
<td>+10円</td>
<td>+10%</td>
</tr>
<tr style="background:#f8f9fa;">
<td>B</td>
<td>1000→1010</td>
<td>+10円</td>
<td>+1%</td>
</tr>
</table>
<p style="margin-top:10px;">
変化幅は同じでも、変化率は違う!<br>
<strong>変化率は元の大きさを考慮した指標</strong>
</p>
</div>

<div class="mnemonic">
<strong>🎯 使い分け:</strong>
<p>変化幅 → 「実際にいくら増減したか」</p>
<p>変化率 → 「影響の大きさを比較」</p>
</div>
</div>''',
            'tags': ['rate-of-change', 'vs-absolute-change', 'understanding']
        },

        # カード9: 2倍・3倍と変化率
        {
            'front': '<div class="question"><h3>「2倍になった」は変化率何%?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">2倍 = 変化率100%増</h3>

<div class="mnemonic">
<strong>💡 直感的理解:</strong>
<p>元の値: 100<br>
2倍: 200<br>
変化率 = (200-100)/100 = <strong>100%</strong>
</p>
<p style="margin-top:10px;">
<strong>元の値と同じだけ増えた = 100%増</strong>
</p>
</div>

<div class="context">
<strong>📊 パターン:</strong>
<table style="width:100%; margin-top:10px; font-size:19px;">
<tr style="background:#f8f9fa;">
<td><strong>倍率</strong></td>
<td><strong>変化率</strong></td>
<td><strong>計算</strong></td>
</tr>
<tr>
<td>2倍</td>
<td>+100%</td>
<td>(2-1) × 100</td>
</tr>
<tr style="background:#f8f9fa;">
<td>3倍</td>
<td>+200%</td>
<td>(3-1) × 100</td>
</tr>
<tr>
<td>半分(0.5倍)</td>
<td>-50%</td>
<td>(0.5-1) × 100</td>
</tr>
<tr style="background:#f8f9fa;">
<td>1.5倍</td>
<td>+50%</td>
<td>(1.5-1) × 100</td>
</tr>
</table>
</div>

<div class="mnemonic">
<strong>🎯 公式:</strong>
<p><strong>変化率(%) = (倍率 - 1) × 100</strong></p>
<p>逆算: <strong>倍率 = 変化率 ÷ 100 + 1</strong></p>
</div>
</div>''',
            'tags': ['rate-of-change', 'multiplication', 'conversion']
        },

        # カード10: 統合カード
        {
            'front': '<div class="question"><h3>変化率の計算を一言でまとめると?</h3></div>',
            'back': '''<div class="answer">
<h3 class="meaning">「変化幅を、元の大きさで割る」</h3>

<div class="mnemonic">
<strong>💡 究極の覚え方:</strong>
<p style="font-size:24px; color:#e74c3c; font-weight:bold; margin:20px 0;">
変化率 = 差分 ÷ スタート × 100
</p>
<p><strong>分母は必ずスタート地点!</strong></p>
</div>

<div class="context">
<strong>📊 チェックリスト:</strong>
<p>✓ 分子 = 新しい値 - 古い値</p>
<p>✓ 分母 = <strong>古い値</strong>(前、過去、基準)</p>
<p>✓ 100を掛けて%表示</p>
<p>✓ プラスなら増加、マイナスなら減少</p>
</div>

<div class="mnemonic">
<strong>🎯 血肉化のための習慣:</strong>
<p>日常で見る数字で練習!</p>
<p>・株価の変動 → 変化率は?</p>
<p>・給料が上がった → 変化率は?</p>
<p>・体重が減った → 変化率は?</p>
<p style="margin-top:10px; font-size:19px; color:#666;">
すべて「(新-旧)/旧」で計算!
</p>
</div>
</div>''',
            'tags': ['rate-of-change', 'summary', 'essential', 'master-card']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("変化率の計算式 - Ankiカード生成")
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
    cards = create_rate_of_change_cards(deck_name, model_name)
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
    print(f"🎯 カード内容:")
    print(f"  1. 基本公式")
    print(f"  2. 分子と分母の意味")
    print(f"  3. なぜ古い値で割るのか")
    print(f"  4. 増加率と減少率")
    print(f"  5. 前年比・前月比")
    print(f"  6. よくある間違い")
    print(f"  7. 統計検定での出題")
    print(f"  8. 変化率と変化幅の違い")
    print(f"  9. 2倍・3倍と変化率")
    print(f" 10. 統合カード（一言まとめ）")
    print()
    print(f"🔍 Ankiで確認:")
    print(f"  tag:rate-of-change で検索")
    print(f"  tag:essential で重要カードのみ表示")
    print()


if __name__ == "__main__":
    main()
