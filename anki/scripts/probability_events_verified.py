#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
さまざまな事象（Probability Events） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「事象」https://bellcurve.jp/statistics/course/6195.html
- 統計WEB「事象の関係」https://bellcurve.jp/statistics/course/6199.html
- 統計WEB「和事象」https://bellcurve.jp/statistics/course/6201.html
- 統計WEB「積事象」https://bellcurve.jp/statistics/course/6203.html
- 統計WEB「ベン図」https://bellcurve.jp/statistics/course/6197.html
- 統計WEB「加法定理」https://bellcurve.jp/statistics/course/23780.html
- 統計WEB「乗法定理」https://bellcurve.jp/statistics/course/6442.html
- 統計WEB「独立な事象」https://bellcurve.jp/statistics/course/6440.html
- 統計WEB「余事象を使った確率計算」https://bellcurve.jp/statistics/course/6345.html
- 統計WEB「独立と排反の違い」https://bellcurve.jp/statistics/blog/27752.html
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


def create_probability_events_cards(deck_name, model_name):
    """さまざまな事象カードを作成（検証済み）"""

    cards = [
        # カード1: 事象の基本用語
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【事象の基本用語】<br>試行・標本空間・根元事象とは？<br>記号と具体例は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【確率論の基本用語】</b><br>
<br>

<hr>

<b>【試行（Trial）】</b><br>
<br>

<b>定義:</b><br>
実験や観察を行い試すこと<br>
<br>

<b>具体例:</b><br>
• サイコロを1回振る<br>
• コインを投げる<br>
• トランプを1枚引く<br>
• くじを引く<br>
<br>

<b>特徴:</b><br>
• 結果が偶然で決まる<br>
• 同じ試行を繰り返し行える<br>
<br>

<hr>

<b>【標本空間（Sample Space）】</b><br>
<br>

<b>定義:</b><br>
試行によって起こりうる<b>すべての事象の集合</b><br>
<br>

<b>記号:</b><br>
• Ω（オメガ）<br>
• または U（Universal set）<br>
<br>

<b>具体例:</b><br>
<br>

<b>例1: サイコロを1回振る</b><br>
\\[\\\\\Omega = \\\\{1, 2, 3, 4, 5, 6\\\\}\\]
<br>

6つの根元事象がある<br>
<br>

<b>例2: コインを1回投げる</b><br>
\\[\\\\\Omega = \\\\{表}, 裏}\\\\}\\]
<br>

2つの根元事象がある<br>
<br>

<b>例3: サイコロを2回振る</b><br>
\\[\\\\\Omega = \\\\{(1,1), (1,2), \\ldots, (6,6)\\\\}\\]
<br>

6 × 6 = 36通りの根元事象<br>
<br>

<b>例4: コインを2回投げる</b><br>
\\[\\\\\Omega = \\\\{(表,表}), (表,裏}), (裏,表}), (裏,裏})\\\\}\\]
<br>

4通りの根元事象<br>
<br>

<b>重要:</b><br>
標本空間は確率計算の<b>全体</b>（分母）になる<br>
<br>

<hr>

<b>【根元事象（Elementary Event）】</b><br>
<br>

<b>定義:</b><br>
それ以上<b>細分化できない</b>事象<br>
最も基本的な事象<br>
<br>

<b>特徴:</b><br>
• 標本空間の要素1つ1つ<br>
• 互いに排反（同時に起こらない）<br>
• すべての根元事象の和 = 標本空間<br>
<br>

<b>具体例:</b><br>
<br>

<b>サイコロを1回振る場合:</b><br>
• 「1の目が出る」→ 根元事象<br>
• 「2の目が出る」→ 根元事象<br>
• ...（計6つの根元事象）<br>
<br>

<b>「偶数の目が出る」→ 根元事象ではない!</b><br>
• {2, 4, 6}に細分化できる<br>
• これは<b>複合事象</b>と呼ぶ<br>
<br>

<hr>

<b>【事象（Event）】</b><br>
<br>

<b>定義:</b><br>
標本空間の部分集合<br>
試行によって起こりうる結果の集まり<br>
<br>

<b>種類:</b><br>
<br>

<b>①根元事象:</b><br>
1つの結果のみ<br>
例: サイコロで「3の目」= {3}<br>
<br>

<b>②複合事象:</b><br>
複数の根元事象の集まり<br>
例: サイコロで「偶数の目」= {2, 4, 6}<br>
<br>

<hr>

<b>【関係図】</b><br>
<br>

<pre style="font-size:16px; line-height:1.6;">
試行（サイコロを振る）
    ↓
標本空間 Ω = {1, 2, 3, 4, 5, 6}
    ↓
根元事象: {1}, {2}, {3}, {4}, {5}, {6}
    ↓
複合事象（例）:
  • 偶数の目 = {2, 4, 6}
  • 3以下の目 = {1, 2, 3}
  • 素数の目 = {2, 3, 5}
</pre>
<br>

<hr>

<b>【確率の計算】</b><br>
<br>

<b>根元事象が同様に確からしい場合:</b><br>
<br>

\\[P(A) = \\frac{Aに含まれる根元事象の数}}{標本空間の根元事象の総数}}\\]
<br>

<b>例: サイコロで偶数の目が出る確率</b><br>
<br>

• 事象A: 偶数の目 = {2, 4, 6}<br>
• |A| = 3（Aに含まれる根元事象の数）<br>
• |Ω| = 6（標本空間の根元事象の総数）<br>
<br>

\\[P(A) = \\frac{3}{6} = \\frac{1}{2}\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>標本空間は常に最初に確認</b><br>
  - 確率計算の分母になる<br>
  - すべての可能性を含んでいるか確認<br>
<br>

• <b>根元事象の数 = 場合の数</b><br>
  - 順列・組み合わせの知識が必要<br>
<br>

• <b>根元事象は互いに排反</b><br>
  - 同時に2つの根元事象は起こらない<br>
  - サイコロで「1と2が同時に出る」は不可能<br>
<br>

• <b>統計検定2級では</b><br>
  - 用語と記号の正確な理解が必須<br>
  - 標本空間を正しく設定できること<br>
  - 複雑な試行でも根元事象を数えられること<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「事象」<br>
統計WEB「ベン図」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'probability', 'events', 'basic', 'sample-space']
        },

        # カード2: 特殊な事象（全事象・空事象・余事象）
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【特殊な事象】<br>全事象・空事象・余事象とは？<br>記号と確率は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【3つの特殊な事象】</b><br>
<br>

<hr>

<b>【全事象（Universal Event / Certain Event）】</b><br>
<br>

<b>定義:</b><br>
標本空間そのもの<br>
<b>必ず起こる事象</b>（確定事象）<br>
<br>

<b>記号:</b><br>
\\[\\\\Omega\\]
<br>

<b>確率:</b><br>
\\[P(\\\\Omega) = 1\\]
<br>

<b>具体例:</b><br>
<br>

<b>サイコロを1回振る場合:</b><br>
• 事象: 「1から6のいずれかの目が出る」<br>
• Ω = {1, 2, 3, 4, 5, 6}<br>
• 必ず起こる → P(Ω) = 1<br>
<br>

<b>コインを投げる場合:</b><br>
• 事象: 「表または裏が出る」<br>
• Ω = {表, 裏}<br>
• 必ず起こる → P(Ω) = 1<br>
<br>

<b>重要:</b><br>
すべての事象の確率の和は1（全事象の確率）<br>
<br>

<hr>

<b>【空事象（Empty Event / Impossible Event）】</b><br>
<br>

<b>定義:</b><br>
<b>決して起こらない事象</b><br>
要素を1つも持たない事象<br>
<br>

<b>記号:</b><br>
\\[\\\\phi\\\ または }\\\\emptyset\\]
<br>

（ファイと読む）<br>
<br>

<b>確率:</b><br>
\\[P(\\\\phi) = 0\\]
<br>

<b>具体例:</b><br>
<br>

<b>サイコロを1回振る場合:</b><br>
• 「7の目が出る」→ 空事象<br>
• 「0の目が出る」→ 空事象<br>
• 「偶数でも奇数でもない目が出る」→ 空事象<br>
<br>

<b>トランプから1枚引く場合:</b><br>
• 「スペードとハートの両方のマークが同時に出る」→ 空事象<br>
<br>

<b>コインを1回投げる場合:</b><br>
• 「表でも裏でもない」→ 空事象<br>
<br>

<b>注意:</b><br>
• 確率0 ≠ 必ず空事象（連続分布では確率0でも可能な場合あり）<br>
• 離散的な場合、P(A) = 0 ⇔ A = φ<br>
<br>

<hr>

<b>【余事象（Complement Event）】</b><br>
<br>

<b>定義:</b><br>
ある事象A<b>以外</b>の場合<br>
「Aが起こらない」事象<br>
<br>

<b>記号:</b><br>
\\[A^c\\\ または }\\bar{A}\\\ または }A'\\]
<br>

（A complementまたはAバー）<br>
<br>

<b>重要な性質:</b><br>
<br>

<b>①事象と余事象の和は全事象:</b><br>
\\[A \\\\cup A^c = \\\\Omega\\]
<br>

<b>②事象と余事象の積は空事象:</b><br>
\\[A \\\\cap A^c = \\\\phi\\]
<br>

（互いに排反）<br>
<br>

<b>③確率の関係:</b><br>
\\[P(A^c) = 1 - P(A)\\]
<br>

または<br>
\\[P(A) + P(A^c) = 1\\]
<br>

<b>具体例:</b><br>
<br>

<b>サイコロを1回振る場合:</b><br>
<br>

事象A: 偶数の目 = {2, 4, 6}<br>
余事象A^c: 奇数の目 = {1, 3, 5}<br>
<br>

• P(A) = 3/6 = 1/2<br>
• P(A^c) = 3/6 = 1/2<br>
• P(A) + P(A^c) = 1/2 + 1/2 = 1 ✓<br>
<br>

<b>トランプから1枚引く場合:</b><br>
<br>

事象A: スペード = 13枚<br>
余事象A^c: スペード以外（ハート・ダイヤ・クラブ）= 39枚<br>
<br>

• P(A) = 13/52 = 1/4<br>
• P(A^c) = 39/52 = 3/4<br>
• P(A) + P(A^c) = 1/4 + 3/4 = 1 ✓<br>
<br>

<hr>

<b>【余事象の活用】</b><br>
<br>

<b>「少なくとも〜」の問題で威力を発揮</b><br>
<br>

<b>問題: 白3個・赤7個のボールから3個取り出す<br>赤が少なくとも1個出る確率は？</b><br>
<br>

<b>直接計算（大変）:</b><br>
赤1個 + 赤2個 + 赤3個の3パターンを計算<br>
<br>

<b>余事象を使う（簡単）:</b><br>
<br>

• 余事象 = 「赤が0個」= 「白が3個」<br>
• P(白3個) = 3C3 / 10C3 = 1/120<br>
• P(赤が少なくとも1個) = 1 - 1/120 = 119/120<br>
<br>

<b>圧倒的に簡単!</b><br>
<br>

<hr>

<b>【3つの事象の関係】</b><br>
<br>

<table border="1" cellpadding="5" style="border-collapse:collapse; max-width:100%; font-size:16px; overflow-x:auto;">
<tr style="background-color:#e0e0e0;">
  <th>事象</th>
  <th>記号</th>
  <th>確率</th>
  <th>意味</th>
</tr>
<tr>
  <td><b>全事象</b></td>
  <td>Ω</td>
  <td>P(Ω) = 1</td>
  <td>必ず起こる</td>
</tr>
<tr>
  <td><b>空事象</b></td>
  <td>φ</td>
  <td>P(φ) = 0</td>
  <td>決して起こらない</td>
</tr>
<tr>
  <td><b>余事象</b></td>
  <td>A^c</td>
  <td>P(A^c) = 1 - P(A)</td>
  <td>Aが起こらない</td>
</tr>
</table>
<br>

<hr>

<b>【ベン図での表現】</b><br>
<br>

<pre style="font-size:16px;">
┌─────────────────────┐
│  Ω（全事象）        │
│   ┌───────┐          │
│   │   A   │   A^c    │
│   │       │  （余事象）│
│   └───────┘          │
│                     │
└─────────────────────┘

• 四角形全体: Ω（全事象）
• 円の内側: 事象A
• 円の外側: 余事象A^c
</pre>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>全事象の確率は必ず1</b><br>
  - すべての確率の合計 = 1<br>
  - 確率の検算に使える<br>
<br>

• <b>空事象 ≠ 確率0</b>（厳密には）<br>
  - 離散的な場合は同じ<br>
  - 連続分布では異なる場合がある<br>
<br>

• <b>余事象は計算の強力な武器</b><br>
  - 「少なくとも〜」の問題で活用<br>
  - P(A) = 1 - P(A^c)で簡略化<br>
<br>

• <b>統計検定2級では</b><br>
  - 余事象の計算が頻出<br>
  - 記号の意味を正確に理解<br>
  - 確率の和が1になることを検算に使う<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「事象の関係」<br>
統計WEB「余事象を使った確率計算」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'probability', 'events', 'complement', 'universal', 'empty']
        },

        # カード3: 事象の演算（和事象・積事象）
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【事象の演算】<br>和事象と積事象とは？<br>記号とベン図は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【事象の演算】</b><br>
<br>

事象どうしを組み合わせて新しい事象を作る<br>
<br>

<hr>

<b>【和事象（Union）】</b><br>
<br>

<b>定義:</b><br>
2つの事象AとBのうち、<b>AまたはBが起こる</b>事象<br>
<br>

<b>記号:</b><br>
\\[A \\\\cup B\\]
<br>

（「A cup B」または「A union B」と読む）<br>
<br>

<b>集合論の意味:</b><br>
AとBの和集合<br>
AまたはBに属する要素すべて<br>
<br>

<b>ベン図:</b><br>
<pre style="font-size:16px;">
   ┌────────┐
   │ A      │
   │   ┌────┼────┐
   │   │ A∩B│    │
   └───┼────┘    │
       │      B  │
       └─────────┘

斜線部分全体がA∪B
（両方の円の領域すべて）
</pre>
<br>

<b>具体例1: サイコロ1回</b><br>
<br>

• 事象A: 偶数の目 = {2, 4, 6}<br>
• 事象B: 3で割り切れる目 = {3, 6}<br>
<br>

\\[A \\\\cup B = \\\\{2, 3, 4, 6\\\\}\\]
<br>

「偶数<b>または</b>3で割り切れる目」<br>
<br>

<b>具体例2: トランプ1枚</b><br>
<br>

• 事象A: スペード（13枚）<br>
• 事象B: 絵札（各スート3枚×4 = 12枚）<br>
<br>

A∪B: スペードまたは絵札<br>
= 13 + 12 - 3（スペードの絵札が重複）<br>
= 22枚<br>
<br>

<hr>

<b>【積事象（Intersection）】</b><br>
<br>

<b>定義:</b><br>
2つの事象AとBのうち、<b>AかつBが同時に起こる</b>事象<br>
<br>

<b>記号:</b><br>
\\[A \\\\cap B\\]
<br>

（「A cap B」または「A intersection B」と読む）<br>
<br>

<b>集合論の意味:</b><br>
AとBの積集合<br>
AとB両方に属する要素<br>
<br>

<b>ベン図:</b><br>
<pre style="font-size:16px;">
   ┌────────┐
   │ A      │
   │   ┌────┼────┐
   │   │■■■│    │
   └───┼────┘    │
       │      B  │
       └─────────┘

■部分（重なり）がA∩B
</pre>
<br>

<b>具体例1: サイコロ1回</b><br>
<br>

• 事象A: 偶数の目 = {2, 4, 6}<br>
• 事象B: 3で割り切れる目 = {3, 6}<br>
<br>

\\[A \\\\cap B = \\\\{6\\\\}\\]
<br>

「偶数<b>かつ</b>3で割り切れる目」= 6のみ<br>
<br>

<b>具体例2: トランプ1枚</b><br>
<br>

• 事象A: スペード（13枚）<br>
• 事象B: 絵札（12枚）<br>
<br>

A∩B: スペードかつ絵札<br>
= スペードのJ, Q, K<br>
= 3枚<br>
<br>

<hr>

<b>【排反事象の場合】</b><br>
<br>

<b>排反事象:</b> 同時に起こらない事象<br>
<br>

<b>積事象が空事象:</b><br>
\\[A \\\\cap B = \\\\phi\\]
<br>

<b>ベン図:</b><br>
<pre style="font-size:16px;">
   ┌────┐      ┌────┐
   │ A  │      │ B  │
   │    │      │    │
   └────┘      └────┘

円が重ならない
</pre>
<br>

<b>具体例: サイコロ1回</b><br>
<br>

• 事象A: 偶数の目 = {2, 4, 6}<br>
• 事象B: 奇数の目 = {1, 3, 5}<br>
<br>

\\[A \\\\cap B = \\\\phi\\]
<br>

同時に偶数かつ奇数は不可能<br>
<br>

\\[A \\\\cup B = \\\\\Omega = \\\\{1, 2, 3, 4, 5, 6\\\\}\\]
<br>

和事象は全事象<br>
<br>

<hr>

<b>【和事象と積事象の確率】</b><br>
<br>

<b>積事象の確率:</b><br>
\\[P(A \\\\cap B)\\]
<br>

「AとBが同時に起こる確率」<br>
<br>

<b>和事象の確率（加法定理）:</b><br>
\\[P(A \\\\cup B) = P(A) + P(B) - P(A \\\\cap B)\\]
<br>

<b>なぜP(A∩B)を引くか:</b><br>
重複部分を二重に数えないため<br>
<br>

<b>排反事象の場合:</b><br>
\\[P(A \\\\cup B) = P(A) + P(B)\\]
<br>

A∩B = φなので、P(A∩B) = 0<br>
<br>

<hr>

<b>【具体的な計算例】</b><br>
<br>

<b>サイコロを1回振る:</b><br>
<br>

• 事象A: 偶数 = {2, 4, 6}、P(A) = 3/6 = 1/2<br>
• 事象B: 3の倍数 = {3, 6}、P(B) = 2/6 = 1/3<br>
• A∩B = {6}、P(A∩B) = 1/6<br>
<br>

<b>和事象の確率:</b><br>
\\[P(A \\\\cup B) = \\frac{1}{2} + \\frac{1}{3} - \\frac{1}{6} = \\frac{3 + 2 - 1}{6} = \\frac{4}{6} = \\frac{2}{3}\\]
<br>

検算: A∪B = {2, 3, 4, 6}（4個）→ 4/6 = 2/3 ✓<br>
<br>

<hr>

<b>【3つ以上の事象】</b><br>
<br>

<b>和事象:</b><br>
\\[A \\\\cup B \\\\cup C\\]
<br>

A、B、Cのいずれか（少なくとも1つ）が起こる<br>
<br>

<b>積事象:</b><br>
\\[A \\\\cap B \\\\cap C\\]
<br>

A、B、Cがすべて同時に起こる<br>
<br>

<hr>

<b>【重要な関係式】</b><br>
<br>

<b>①分配法則:</b><br>
\\[A \\\\cap (B \\\\cup C) = (A \\\\cap B) \\\\cup (A \\\\cap C)\\]
\\[A \\\\cup (B \\\\cap C) = (A \\\\cup B) \\\\cap (A \\\\cup C)\\]
<br>

<b>②ド・モルガンの法則:</b><br>
\\[(A \\\\cup B)^c = A^c \\\\cap B^c\\]
\\[(A \\\\cap B)^c = A^c \\\\cup B^c\\]
<br>

「和の補集合 = 補集合の積」<br>
「積の補集合 = 補集合の和」<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>「または」→ 和事象（∪）</b><br>
• <b>「かつ」→ 積事象（∩）</b><br>
<br>

• <b>ベン図で視覚的に理解</b><br>
  - 和事象: 両方の円の領域すべて<br>
  - 積事象: 重なり部分のみ<br>
<br>

• <b>確率計算での注意</b><br>
  - 和事象: 重複を引く（加法定理）<br>
  - 積事象: 条件付き確率（乗法定理）<br>
<br>

• <b>統計検定2級では</b><br>
  - 記号の意味を正確に<br>
  - ベン図を描いて考える<br>
  - 加法定理・乗法定理との関連<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「和事象」<br>
統計WEB「積事象」<br>
統計WEB「ベン図」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'probability', 'events', 'union', 'intersection', 'venn-diagram']
        },

        # カード4: 排反事象と独立事象の違い
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【排反と独立】<br>排反事象と独立事象の違いは？<br>なぜ排反は独立でないのか？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【最も重要な違い】</b><br>
<br>

排反事象と独立事象は<b>全く異なる概念</b><br>
<b>混同しやすいが、逆の関係</b>にある<br>
<br>

<hr>

<b>【排反事象（Mutually Exclusive Events）】</b><br>
<br>

<b>定義:</b><br>
<b>同時には起こらない</b>事象<br>
<br>

<b>数学的表現:</b><br>
\\[A \\\\cap B = \\\\phi\\]
\\[P(A \\\\cap B) = 0\\]
<br>

<b>意味:</b><br>
• 一方が起これば、他方は<b>必ず起こらない</b><br>
• ベン図で円が重ならない<br>
<br>

<b>確率の関係:</b><br>
• 和事象の確率（加法定理の簡略版）:<br>
\\[P(A \\\\cup B) = P(A) + P(B)\\]
<br>

• 条件付き確率:<br>
\\[P(A|B) = 0\\]
<br>

Bが起これば、Aは必ず起こらない<br>
<br>

<b>具体例:</b><br>
<br>

<b>例1: サイコロを1回振る</b><br>
• 事象A: 偶数の目 {2, 4, 6}<br>
• 事象B: 奇数の目 {1, 3, 5}<br>
<br>

同時には起こらない → <b>排反</b><br>
<br>

<b>例2: トランプを1枚引く</b><br>
• 事象A: スペードを引く<br>
• 事象B: ハートを引く<br>
<br>

同時には起こらない → <b>排反</b><br>
<br>

<b>例3: くじ引き</b><br>
• 事象A: 1等が当たる<br>
• 事象B: 2等が当たる<br>
<br>

同時には起こらない → <b>排反</b><br>
<br>

<hr>

<b>【独立事象（Independent Events）】</b><br>
<br>

<b>定義:</b><br>
お互いの結果が<b>影響し合わない</b>事象<br>
<br>

<b>数学的表現:</b><br>
\\[P(A \\\\cap B) = P(A) \\times P(B)\\]
<br>

または<br>
\\[P(A|B) = P(A)\\]
\\[P(B|A) = P(B)\\]
<br>

<b>意味:</b><br>
• 一方の結果が他方の確率に<b>影響しない</b><br>
• Bが起こっても起こらなくても、P(A)は変わらない<br>
<br>

<b>具体例:</b><br>
<br>

<b>例1: コイン投げとサイコロ</b><br>
• 事象A: コインで表が出る<br>
• 事象B: サイコロで6が出る<br>
<br>

互いに影響しない → <b>独立</b><br>
\\[P(A \\\\cap B) = \\frac{1}{2} \\times \\frac{1}{6} = \\frac{1}{12}\\]
<br>

<b>例2: サイコロを2回振る</b><br>
• 事象A: 1回目が6<br>
• 事象B: 2回目が6<br>
<br>

互いに影響しない → <b>独立</b><br>
\\[P(A \\\\cap B) = \\frac{1}{6} \\times \\frac{1}{6} = \\frac{1}{36}\\]
<br>

<b>例3: 復元抽出（戻す）</b><br>
袋から玉を取り出し、<b>戻して</b>から次を取る<br>
→ <b>独立</b><br>
<br>

<hr>

<b>【なぜ排反事象は独立ではないのか】</b><br>
<br>

<b>結論: 排反事象は従属関係にある</b><br>
<br>

<b>理由:</b><br>
<br>

排反事象の定義より:<br>
\\[P(A \\\\cap B) = 0\\]
<br>

もし独立なら:<br>
\\[P(A \\\\cap B) = P(A) \\times P(B)\\]
<br>

両方が成り立つには:<br>
\\[P(A) \\times P(B) = 0\\]
<br>

→ P(A) = 0 または P(B) = 0<br>
<br>

<b>つまり、どちらかが不可能事象でない限り、<br>排反と独立は同時に成り立たない</b><br>
<br>

<b>直感的な説明:</b><br>
<br>

排反事象では:<br>
• Aが起これば、Bは<b>必ず起こらない</b><br>
• P(B|A) = 0 ≠ P(B)<br>
<br>

→ Aの結果がBに<b>強く影響している</b><br>
→ <b>従属関係</b><br>
<br>

<hr>

<b>【2つの概念の比較表】</b><br>
<br>

<table border="1" cellpadding="5" style="border-collapse:collapse; max-width:100%; font-size:16px; overflow-x:auto;">
<tr style="background-color:#e0e0e0;">
  <th>項目</th>
  <th>排反事象</th>
  <th>独立事象</th>
</tr>
<tr>
  <td><b>定義</b></td>
  <td>同時に起こらない</td>
  <td>互いに影響しない</td>
</tr>
<tr>
  <td><b>数式</b></td>
  <td>P(A∩B) = 0</td>
  <td>P(A∩B) = P(A)P(B)</td>
</tr>
<tr>
  <td><b>条件付き</b></td>
  <td>P(A|B) = 0</td>
  <td>P(A|B) = P(A)</td>
</tr>
<tr>
  <td><b>関係性</b></td>
  <td>従属（強い影響）</td>
  <td>独立（影響なし）</td>
</tr>
<tr>
  <td><b>ベン図</b></td>
  <td>円が重ならない</td>
  <td>重なりの面積=P(A)P(B)</td>
</tr>
<tr>
  <td><b>加法定理</b></td>
  <td>P(A∪B)=P(A)+P(B)</td>
  <td>一般形を使用</td>
</tr>
<tr>
  <td><b>例</b></td>
  <td>偶数と奇数</td>
  <td>コインとサイコロ</td>
</tr>
</table>
<br>

<hr>

<b>【従属事象（Dependent Events）】</b><br>
<br>

<b>定義:</b><br>
独立でない事象（一方が他方に影響する）<br>
<br>

<b>数式:</b><br>
\\[P(A|B) \\\\neq P(A)\\]
<br>

<b>具体例: 非復元抽出（戻さない）</b><br>
<br>

10本のくじ（当たり4本）から2人が順に引く<br>
<br>

• 太郎が当たる確率: 4/10<br>
• 太郎が当たった後、花子が当たる確率: 3/9<br>
<br>

\\[P(両者当たる}) = \\frac{4}{10} \\times \\frac{3}{9} = \\frac{2}{15}\\]
<br>

→ <b>従属事象</b><br>
<br>

もし独立なら（戻す場合）:<br>
\\[P = \\frac{4}{10} \\times \\frac{4}{10} = \\frac{4}{25}\\]
<br>

明らかに異なる<br>
<br>

<hr>

<b>【よくある間違い】</b><br>
<br>

<b>❌ 間違い1:</b><br>
「排反だから独立」と考える<br>
<br>

<b>✓ 正しい:</b><br>
排反 → 従属（一方が起これば他方は起こらない）<br>
<br>

<b>❌ 間違い2:</b><br>
戻さないくじを独立として計算<br>
<br>

<b>✓ 正しい:</b><br>
戻さない → 従属、条件付き確率を使用<br>
<br>

<b>❌ 間違い3:</b><br>
「別々の試行だから独立」と思い込む<br>
<br>

<b>✓ 正しい:</b><br>
別々でも影響があれば従属（例: 同じ袋から連続で取る）<br>
<br>

<hr>

<b>【判断基準】</b><br>
<br>

<b>排反かどうか:</b><br>
→ 「同時に起こるか？」を考える<br>
<br>

<b>独立かどうか:</b><br>
→ 「一方の結果が他方の確率を変えるか？」を考える<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>排反と独立は別概念</b><br>
  - 排反: 同時性の問題<br>
  - 独立: 影響の問題<br>
<br>

• <b>排反 → 従属</b>（ほとんどの場合）<br>
  - 一方が起これば他方の確率が0になる<br>
  - これは「影響がある」ことを意味<br>
<br>

• <b>統計検定2級では</b><br>
  - この違いを問う問題が頻出<br>
  - 正確な理解が必須<br>
  - 計算方法も全く異なる<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「事象の関係」<br>
統計WEB「独立な事象」<br>
統計WEB「独立と排反の違い」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'probability', 'events', 'mutually-exclusive', 'independent', 'comparison']
        },

        # カード5: 確率の加法定理
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【確率の加法定理】<br>一般形と排反事象の場合は？<br>なぜP(A∩B)を引くのか？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【確率の加法定理（Addition Theorem）】</b><br>
<br>

和事象の確率を求める定理<br>
<br>

<hr>

<b>【一般形（非排反事象の場合）】</b><br>
<br>

<b>公式:</b><br>
\\[P(A \\\\cup B) = P(A) + P(B) - P(A \\\\cap B)\\]
<br>

<b>意味:</b><br>
「AまたはBが起こる確率」<br>
= 「Aの確率」+ 「Bの確率」- 「両方起こる確率」<br>
<br>

<b>読み方:</b><br>
P(A cup B) = P(A) plus P(B) minus P(A cap B)<br>
<br>

<hr>

<b>【なぜP(A∩B)を引くのか】</b><br>
<br>

<b>理由: 重複部分を二重に数えないため</b><br>
<br>

<b>ベン図で考える:</b><br>
<pre style="font-size:16px;">
   ┌────────┐
   │ A      │
   │   ┌────┼────┐
   │   │★★★│    │ ← この★部分（A∩B）
   └───┼────┘    │   がP(A)にもP(B)にも
       │      B  │   含まれている
       └─────────┘
</pre>
<br>

<b>計算の流れ:</b><br>
<br>

1. P(A)を足す → A全体を数える<br>
2. P(B)を足す → B全体を数える<br>
3. <b>問題:</b> 重なり部分★を<b>2回</b>数えてしまった!<br>
4. <b>解決:</b> P(A∩B)を1回引く<br>
<br>

\\[正しい確率} = P(A) + P(B) - P(A \\\\cap B)\\]
<br>

<hr>

<b>【排反事象の場合の簡略化】</b><br>
<br>

<b>排反事象の定義:</b><br>
\\[A \\\\cap B = \\\\phi\\]
\\[P(A \\\\cap B) = 0\\]
<br>

<b>加法定理に代入:</b><br>
\\[P(A \\\\cup B) = P(A) + P(B) - 0\\]
<br>

<b>簡略形:</b><br>
\\[P(A \\\\cup B) = P(A) + P(B)\\]
<br>

<b>ベン図:</b><br>
<pre style="font-size:16px;">
   ┌────┐      ┌────┐
   │ A  │      │ B  │
   │    │      │    │
   └────┘      └────┘

円が重ならない
→ 重複なし → 単純に足す
</pre>
<br>

<hr>

<b>【具体例1: 非排反事象（サイコロ）】</b><br>
<br>

<b>問題: サイコロを1回振る</b><br>
「偶数または3の倍数の目が出る確率は？」<br>
<br>

• 事象A: 偶数 = {2, 4, 6}<br>
• 事象B: 3の倍数 = {3, 6}<br>
• A∩B: 偶数かつ3の倍数 = {6}<br>
<br>

<b>確率:</b><br>
• P(A) = 3/6 = 1/2<br>
• P(B) = 2/6 = 1/3<br>
• P(A∩B) = 1/6<br>
<br>

<b>加法定理を適用:</b><br>
\\[P(A \\\\cup B) = \\frac{1}{2} + \\frac{1}{3} - \\frac{1}{6}\\]
\\[= \\frac{3 + 2 - 1}{6} = \\frac{4}{6} = \\frac{2}{3}\\]
<br>

<b>検算:</b><br>
A∪B = {2, 3, 4, 6}（4個）<br>
→ 4/6 = 2/3 ✓<br>
<br>

<b>もし引き忘れたら:</b><br>
1/2 + 1/3 = 5/6（間違い!）<br>
<br>

<hr>

<b>【具体例2: 非排反事象（クラス調査）】</b><br>
<br>

<b>問題: 30人のクラス</b><br>
• 野球好き: 12人<br>
• サッカー好き: 18人<br>
• 両方好き: 6人<br>
<br>

「野球またはサッカーが好きな人の割合は？」<br>
<br>

<b>確率:</b><br>
• P(野球) = 12/30<br>
• P(サッカー) = 18/30<br>
• P(両方) = 6/30<br>
<br>

<b>加法定理:</b><br>
\\[P(野球∪サッカー}) = \\frac{12}{30} + \\frac{18}{30} - \\frac{6}{30}\\]
\\[= \\frac{24}{30} = \\frac{4}{5} = 0.8\\]
<br>

<b>80%の生徒が野球かサッカーが好き</b><br>
<br>

<b>もし引き忘れたら:</b><br>
12/30 + 18/30 = 30/30 = 1（100%）<br>
→ 明らかにおかしい（全員が好きなわけではない）<br>
<br>

<hr>

<b>【具体例3: 排反事象（サイコロ）】</b><br>
<br>

<b>問題: サイコロを1回振る</b><br>
「偶数または奇数の目が出る確率は？」<br>
<br>

• 事象A: 偶数 = {2, 4, 6}<br>
• 事象B: 奇数 = {1, 3, 5}<br>
• A∩B = φ（排反）<br>
<br>

<b>確率:</b><br>
• P(A) = 3/6 = 1/2<br>
• P(B) = 3/6 = 1/2<br>
• P(A∩B) = 0<br>
<br>

<b>排反事象の加法定理:</b><br>
\\[P(A \\\\cup B) = \\frac{1}{2} + \\frac{1}{2} = 1\\]
<br>

→ <b>必ず起こる（全事象）</b><br>
<br>

<hr>

<b>【3つの事象の場合】</b><br>
<br>

<b>3つの事象A, B, Cの和事象:</b><br>
<br>

\\[P(A \\\\cup B \\\\cup C) = P(A) + P(B) + P(C)\\]
\\[- P(A \\\\cap B) - P(B \\\\cap C) - P(C \\\\cap A)\\]
\\[+ P(A \\\\cap B \\\\cap C)\\]
<br>

<b>包除原理（Inclusion-Exclusion Principle）</b><br>
<br>

• 各事象を足す<br>
• 2つずつの重なりを引く<br>
• 3つ全部の重なりを足す（引きすぎた分を戻す）<br>
<br>

<hr>

<b>【よくある間違い】</b><br>
<br>

<b>❌ 間違い1:</b><br>
非排反なのにP(A∩B)を引き忘れる<br>
→ 確率が1を超えることもある<br>
<br>

<b>❌ 間違い2:</b><br>
排反なのにP(A∩B)を引いてしまう<br>
→ 答えが小さくなりすぎる（でも0なので結果は同じ）<br>
<br>

<b>❌ 間違い3:</b><br>
P(A∩B)を2回引いてしまう<br>
<br>

<hr>

<b>【計算の手順】</b><br>
<br>

<b>ステップ1:</b> 排反かどうか確認<br>
• A∩B = φ か？<br>
<br>

<b>ステップ2:</b> 適切な公式を選択<br>
• 排反 → P(A∪B) = P(A) + P(B)<br>
• 非排反 → P(A∪B) = P(A) + P(B) - P(A∩B)<br>
<br>

<b>ステップ3:</b> 各確率を計算<br>
<br>

<b>ステップ4:</b> 公式に代入<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>重複に注意</b><br>
  - ベン図を描いて確認<br>
  - P(A∩B)を必ず確認<br>
<br>

• <b>排反の判定</b><br>
  - 同時に起こるか考える<br>
  - A∩B = φ なら排反<br>
<br>

• <b>確率の合計が1を超えたら要注意</b><br>
  - 引き忘れの可能性<br>
<br>

• <b>統計検定2級では</b><br>
  - 加法定理の計算問題が頻出<br>
  - 排反・非排反の判断が重要<br>
  - ベン図を描く習慣をつける<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「加法定理」<br>
統計WEB「和事象」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'probability', 'addition-theorem', 'union', 'formula']
        },

        # カード6: 確率の乗法定理
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【確率の乗法定理】<br>一般形と独立事象の場合は？<br>戻さないくじ引きの計算は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【確率の乗法定理（Multiplication Theorem）】</b><br>
<br>

積事象の確率を求める定理<br>
<br>

<hr>

<b>【一般形（従属事象の場合）】</b><br>
<br>

<b>公式:</b><br>
\\[P(A \\\\cap B) = P(A) \\times P(B|A)\\]
<br>

または<br>
\\[P(A \\\\cap B) = P(B) \\times P(A|B)\\]
<br>

<b>意味:</b><br>
「AとBが同時に起こる確率」<br>
= 「Aの確率」× 「Aが起こった後のBの条件付き確率」<br>
<br>

<b>P(B|A):</b> 「Aが起こったという条件の下でBが起こる確率」<br>
<br>

<hr>

<b>【独立事象の場合の簡略化】】</b><br>
<br>

<b>独立の定義:</b><br>
\\[P(B|A) = P(B)\\]
<br>

（Aが起こっても起こらなくても、Bの確率は変わらない）<br>
<br>

<b>乗法定理に代入:</b><br>
\\[P(A \\\\cap B) = P(A) \\times P(B)\\]
<br>

<b>簡略形（独立事象）:</b><br>
\\[P(A \\\\cap B) = P(A) \\times P(B)\\]
<br>

<b>非常にシンプル!</b><br>
<br>

<hr>

<b>【具体例1: 独立事象（コインとサイコロ）】</b><br>
<br>

<b>問題:</b><br>
コインを投げて表、かつサイコロで6が出る確率は？<br>
<br>

• 事象A: コインで表 → P(A) = 1/2<br>
• 事象B: サイコロで6 → P(B) = 1/6<br>
<br>

<b>互いに影響しない → 独立</b><br>
<br>

<b>乗法定理（独立）:</b><br>
\\[P(A \\\\cap B) = \\frac{1}{2} \\times \\frac{1}{6} = \\frac{1}{12}\\]
<br>

<hr>

<b>【具体例2: 独立事象（サイコロ2回）】</b><br>
<br>

<b>問題:</b><br>
サイコロを2回振って、両方とも6が出る確率は？<br>
<br>

• 1回目が6: P(A) = 1/6<br>
• 2回目が6: P(B) = 1/6<br>
<br>

<b>互いに影響しない → 独立</b><br>
<br>

\\[P(A \\\\cap B) = \\frac{1}{6} \\times \\frac{1}{6} = \\frac{1}{36}\\]
<br>

<hr>

<b>【具体例3: 従属事象（戻さないくじ引き）】</b><br>
<br>

<b>問題:</b><br>
10本のくじ（当たり4本、はずれ6本）から太郎さんと花子さんが順に引く（<b>戻さない</b>）<br>
両者とも当たる確率は？<br>
<br>

<b>分析:</b><br>
• 戻さない → 従属事象<br>
• 太郎の結果が花子の確率に影響する<br>
<br>

<b>計算:</b><br>
<br>

• 事象A: 太郎が当たる<br>
\\[P(A) = \\frac{4}{10}\\]
<br>

• 事象B: 花子が当たる<br>
• Aが起こった後の条件付き確率:<br>
\\[P(B|A) = \\frac{3}{9}\\]
<br>

（太郎が当たったので、残り9本中当たり3本）<br>
<br>

<b>乗法定理（従属）:</b><br>
\\[P(A \\\\cap B) = \\frac{4}{10} \\times \\frac{3}{9} = \\frac{12}{90} = \\frac{2}{15} \\\approx 0.133\\]
<br>

<b>約13.3%</b><br>
<br>

<hr>

<b>【よくある間違い: 戻さないくじを独立として計算】</b><br>
<br>

<b>❌ 間違った計算:</b><br>
\\[P = \\frac{4}{10} \\times \\frac{4}{10} = \\frac{16}{100} = \\frac{4}{25} = 0.16\\]
<br>

<b>✓ 正しい計算:</b><br>
\\[P = \\frac{4}{10} \\times \\frac{3}{9} = \\frac{2}{15} \\\approx 0.133\\]
<br>

<b>差: 0.16 - 0.133 = 0.027（約2.7%の誤差）</b><br>
<br>

→ 戻さない場合、確率は<b>低くなる</b><br>
（当たりが減るため）<br>
<br>

<hr>

<b>【具体例4: 従属事象（トランプ）】</b><br>
<br>

<b>問題:</b><br>
52枚のトランプから2枚続けて引く（戻さない）<br>
両方ともスペードである確率は？<br>
<br>

• 1枚目がスペード: P(A) = 13/52 = 1/4<br>
• 1枚目がスペードの後、2枚目もスペード:<br>
\\[P(B|A) = \\frac{12}{51}\\]
<br>

（残り51枚中スペード12枚）<br>
<br>

<b>乗法定理:</b><br>
\\[P(A \\\\cap B) = \\frac{1}{4} \\times \\frac{12}{51} = \\frac{12}{204} = \\frac{1}{17} \\\approx 0.0588\\]
<br>

<b>約5.88%</b><br>
<br>

<hr>

<b>【条件付き確率との関係】</b><br>
<br>

<b>乗法定理を変形すると:</b><br>
\\[P(B|A) = \\frac{P(A \\\\cap B)}{P(A)}\\]
<br>

これが<b>条件付き確率の定義</b><br>
<br>

<b>意味:</b><br>
• Aが起こったという条件の下でBが起こる確率<br>
• 標本空間がAに制限される<br>
<br>

<hr>

<b>【3つの事象の場合】</b><br>
<br>

<b>3つの事象A, B, Cがすべて起こる確率:</b><br>
<br>

<b>従属事象:</b><br>
\\[P(A \\\\cap B \\\\cap C) = P(A) \\times P(B|A) \\times P(C|A \\\\cap B)\\]
<br>

<b>独立事象:</b><br>
\\[P(A \\\\cap B \\\\cap C) = P(A) \\times P(B) \\times P(C)\\]
<br>

<hr>

<b>【独立か従属かの判断】</b><br>
<br>

<b>独立の条件:</b><br>
• 別々の試行（コインとサイコロ）<br>
• 復元抽出（戻す）<br>
• 結果が影響し合わない<br>
<br>

<b>従属の条件:</b><br>
• 非復元抽出（戻さない）<br>
• 同じ母集団から連続で取る<br>
• 一方の結果が他方の確率を変える<br>
<br>

<hr>

<b>【計算の手順】</b><br>
<br>

<b>ステップ1:</b> 独立か従属か判断<br>
• 戻すか戻さないか<br>
• 影響し合うか<br>
<br>

<b>ステップ2:</b> 適切な公式を選択<br>
• 独立 → P(A∩B) = P(A) × P(B)<br>
• 従属 → P(A∩B) = P(A) × P(B|A)<br>
<br>

<b>ステップ3:</b> 条件付き確率を計算<br>
• 従属の場合、Aが起こった後の状況を考える<br>
<br>

<b>ステップ4:</b> 公式に代入<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>戻す・戻さないの区別が最重要</b><br>
  - 戻す → 独立 → P(A)P(B)<br>
  - 戻さない → 従属 → P(A)P(B|A)<br>
<br>

• <b>条件付き確率を正確に</b><br>
  - 前の事象が起こった後の状況<br>
  - 分母・分子が両方変わる<br>
<br>

• <b>「かつ」は乗法、「または」は加法</b><br>
  - A∩B → 乗法定理<br>
  - A∪B → 加法定理<br>
<br>

• <b>統計検定2級では</b><br>
  - くじ引き、トランプの問題が頻出<br>
  - 非復元抽出の計算が重要<br>
  - 条件付き確率との組み合わせ<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「乗法定理」<br>
統計WEB「独立な事象」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'probability', 'multiplication-theorem', 'conditional', 'formula']
        },

        # カード7: 余事象を使った確率計算
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【余事象を使った確率計算】<br>どんな問題で有効？<br>「少なくとも1つ」の余事象は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【余事象を使った確率計算】</b><br>
<br>

<b>基本公式:</b><br>
\\[P(A) = 1 - P(A^c)\\]
<br>

<b>戦略:</b><br>
求める確率が複雑 → 余事象の確率を求めて全体から引く<br>
<br>

<hr>

<b>【有効な場合】</b><br>
<br>

<b>①「少なくとも〜」の問題</b><br>
• 少なくとも1つ<br>
• 少なくとも1人<br>
• 1回以上<br>
<br>

→ 場合分けが多くて大変<br>
→ <b>余事象は「0個」で1パターンのみ</b><br>
<br>

<b>②「いずれかが〜」の問題</b><br>
• いずれかが当たる<br>
• どれか1つでも成功する<br>
<br>

→ 余事象は「すべて失敗」で簡単<br>
<br>

<b>③「すべてでない」の問題</b><br>
• すべてが〜でない<br>
• 全部とは限らない<br>
<br>

→ 余事象は「すべて〜」で簡単<br>
<br>

<hr>

<b>【「少なくとも〜」の余事象】</b><br>
<br>

<b>重要: よく間違える!</b><br>
<br>

<table border="1" cellpadding="5" style="border-collapse:collapse; max-width:100%; font-size:16px; overflow-x:auto;">
<tr style="background-color:#e0e0e0;">
  <th>表現</th>
  <th>余事象</th>
</tr>
<tr>
  <td>少なくとも1つ</td>
  <td><b>0個</b>（1つも〜ない）</td>
</tr>
<tr>
  <td>少なくとも2つ</td>
  <td><b>0個または1個</b></td>
</tr>
<tr>
  <td>少なくとも1人</td>
  <td><b>0人</b>（誰も〜ない）</td>
</tr>
<tr>
  <td>1回以上</td>
  <td><b>0回</b>（1回も〜ない）</td>
</tr>
<tr>
  <td>すべて</td>
  <td><b>少なくとも1つそうでない</b></td>
</tr>
</table>
<br>

<b>注意:</b><br>
• 「少なくとも1つ」の余事象は「1つ未満」ではなく<b>「0個」</b><br>
• 「1つ未満」は曖昧な表現なので使わない<br>
<br>

<hr>

<b>【具体例1: 白3個・赤7個のボール】</b><br>
<br>

<b>問題:</b><br>
白3個、赤7個、計10個のボールから3個取り出す<br>
<b>赤が少なくとも1個出る確率</b>は？<br>
<br>

<b>方法1: 直接計算（大変）</b><br>
<br>

赤1個 + 赤2個 + 赤3個の3パターン<br>
<br>

• 赤1個、白2個: 7C1 × 3C2 / 10C3<br>
• 赤2個、白1個: 7C2 × 3C1 / 10C3<br>
• 赤3個、白0個: 7C3 / 10C3<br>
<br>

これらを足す... 面倒!<br>
<br>

<b>方法2: 余事象を使う（簡単!）</b><br>
<br>

<b>余事象:</b> 赤が0個 = 白が3個<br>
<br>

\\[P(白3個}) = \\frac{_3C_3}{{_{10}C_3}} = \\frac{1}{120}\\]
<br>

<b>求める確率:</b><br>
\\[P(赤が少なくとも1個}) = 1 - \\frac{1}{120} = \\frac{119}{120} \\\approx 0.992\\]
<br>

<b>約99.2%</b><br>
<br>

<b>圧倒的に簡単!</b><br>
<br>

<hr>

<b>【具体例2: サイコロ3回】</b><br>
<br>

<b>問題:</b><br>
サイコロを3回振る<br>
<b>少なくとも1回は6が出る確率</b>は？<br>
<br>

<b>方法1: 直接計算（複雑）</b><br>
<br>

• 6が1回だけ出る<br>
• 6が2回だけ出る<br>
• 6が3回出る<br>
<br>

各パターンを計算して足す... 複雑!<br>
<br>

<b>方法2: 余事象を使う（シンプル!）</b><br>
<br>

<b>余事象:</b> 6が0回（1回も6が出ない）<br>
<br>

• 1回で6が出ない確率: 5/6<br>
• 3回とも6が出ない確率:<br>
\\[P(余事象}) = \\left(\\frac{5}{6}\\right)^3 = \\frac{125}{216}\\]
<br>

<b>求める確率:</b><br>
\\[P(少なくとも1回は6}) = 1 - \\frac{125}{216} = \\frac{91}{216} \\\approx 0.421\\]
<br>

<b>約42.1%</b><br>
<br>

<hr>

<b>【具体例3: 誕生日問題（有名問題）】</b><br>
<br>

<b>問題:</b><br>
23人のクラスで、<b>少なくとも2人の誕生日が同じ確率</b>は？<br>
<br>

<b>直接計算:</b> ほぼ不可能（パターンが膨大）<br>
<br>

<b>余事象を使う:</b><br>
<br>

<b>余事象:</b> 23人全員の誕生日が異なる<br>
<br>

• 1人目: 365/365（自由）<br>
• 2人目: 364/365（1人目と違う）<br>
• 3人目: 363/365（2人と違う）<br>
• ...<br>
• 23人目: 343/365（22人と違う）<br>
<br>

\\[P(全員異なる}) = \\frac{365}{365} \\times \\frac{364}{365} \\times \\cdots \\times \\frac{343}{365} \\\approx 0.493\\]
<br>

<b>求める確率:</b><br>
\\[P(少なくとも2人同じ}) = 1 - 0.493 = 0.507\\]
<br>

<b>約50.7%!</b><br>
<br>

意外と高い!（直感に反する結果）<br>
<br>

<hr>

<b>【具体例4: くじ引き】</b><br>
<br>

<b>問題:</b><br>
10本のくじ（当たり3本）から3人が順に引く（戻さない）<br>
<b>少なくとも1人は当たる確率</b>は？<br>
<br>

<b>余事象:</b> 3人とも外れる<br>
<br>

• 1人目が外れる: 7/10<br>
• 2人目も外れる: 6/9<br>
• 3人目も外れる: 5/8<br>
<br>

\\[P(3人とも外れる) = \\frac{7}{10} \\times \\frac{6}{9} \\times \\frac{5}{8} = \\frac{210}{720} = \\frac{7}{24}\\]
<br>

<b>求める確率:</b><br>
\\[P(少なくとも1人当たる) = 1 - \\frac{7}{24} = \\frac{17}{24} \\approx 0.708\\]
<br>

<b>約70.8%</b><br>
<br>

<hr>

<b>【使い分けの判断基準】</b><br>
<br>

<b>余事象を使う:</b><br>
• 「少なくとも〜」の表現がある<br>
• 場合分けが3つ以上<br>
• 余事象が1パターンまたは単純<br>
<br>

<b>直接計算する:</b><br>
• 場合が少ない（1〜2パターン）<br>
• 余事象の方が複雑<br>
• 問題文が明確な1パターンを求めている<br>
<br>

<hr>

<b>【計算の手順】</b><br>
<br>

<b>ステップ1:</b> 余事象を明確にする<br>
• 「少なくとも1つ」→ 余事象は「0個」<br>
<br>

<b>ステップ2:</b> 余事象の確率P(A^c)を計算<br>
• 通常、こちらが簡単<br>
<br>

<b>ステップ3:</b> 全体から引く<br>
• P(A) = 1 - P(A^c)<br>
<br>

<b>ステップ4:</b> 検算<br>
• 0 ≤ P(A) ≤ 1<br>
• 直感的に妥当か確認<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>「少なくとも」を見たら余事象を考える</b><br>
  - ほぼ確実に簡単になる<br>
<br>

• <b>余事象の定義を正確に</b><br>
  - 「少なくとも1つ」の余は「0個」<br>
  - 「1つ未満」ではない<br>
<br>

• <b>確率の検算</b><br>
  - P(A) + P(A^c) = 1<br>
  - 計算ミスのチェックに使える<br>
<br>

• <b>統計検定2級では</b><br>
  - 余事象の問題が頻出<br>
  - 時間短縮の強力な武器<br>
  - 「少なくとも」問題は余事象で解く習慣を<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「余事象を使った確率計算」<br>
統計WEB「事象の関係」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'probability', 'complement', 'at-least', 'technique']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("さまざまな事象 - 検証済みAnkiカード生成")
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
    cards = create_probability_events_cards(deck_name, model_name)
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
    print("✨ さまざまな事象カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 事象の基本用語（試行・標本空間・根元事象）")
    print("  カード2: 特殊な事象（全事象・空事象・余事象）")
    print("  カード3: 事象の演算（和事象・積事象）")
    print("  カード4: 排反事象と独立事象の違い")
    print("  カード5: 確率の加法定理")
    print("  カード6: 確率の乗法定理")
    print("  カード7: 余事象を使った確率計算")
    print()


if __name__ == "__main__":
    main()
