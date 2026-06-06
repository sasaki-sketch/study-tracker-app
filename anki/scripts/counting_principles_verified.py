#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
場合の数（Counting Principles） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「Pの使い方」https://bellcurve.jp/statistics/course/5760.html
- 統計WEB「Cの使い方」https://bellcurve.jp/statistics/course/5762.html
- 統計WEB「確率の計算」https://bellcurve.jp/statistics/course/6343.html
- 統計WEB「順列と組み合わせ」https://bellcurve.jp/statistics/blog/14067.html
- 統計WEB「練習問題」https://bellcurve.jp/statistics/course/5916.html
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


def create_counting_principles_cards(deck_name, model_name):
    """場合の数カードを作成（検証済み）"""

    cards = [
        # カード1: 順列と組み合わせの基本的な違い
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【順列と組み合わせ】<br>nPrとnCrの違いは？<br>使い分けの判断基準は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【2つの基本概念】</b><br>
<br>

<hr>

<b>【順列（Permutation）: nPr】</b><br>
<br>

<b>定義:</b><br>
異なるn個のものから<b>r個を取り出して順に1列に並べる</b><br>
<br>

<b>特徴:</b><br>
• <b>順序を考慮する</b><br>
• 並べる順番が違えば別のものとして数える<br>
<br>

<b>公式:</b><br>
\\[_nP_r = n \\times (n-1) \\times (n-2) \\times \\cdots \\times (n-r+1)\\]
<br>

または階乗を使って:<br>
\\[_nP_r = \\frac{n!}{(n-r)!}\\]
<br>

<b>具体例: 6人から3人選んで1列に並べる</b><br>
\\[_6P_3 = 6 \\times 5 \\times 4 = 120\\]
<br>

• 「A, B, C」と「C, B, A」は異なる並び方<br>
<br>

<hr>

<b>【組み合わせ（Combination）: nCr】</b><br>
<br>

<b>定義:</b><br>
異なるn個のものから<b>r個を取り出す</b>（並べない）<br>
<br>

<b>特徴:</b><br>
• <b>順序を考慮しない</b><br>
• 選ぶ対象が同じなら順番が違っても同じとみなす<br>
<br>

<b>公式:</b><br>
\\[\\binom{n}{r} = \\frac{_nP_r}{r!} = \\frac{n!}{(n-r)! \\times r!}\\]
<br>

<b>具体例: 6人から3人選ぶ</b><br>
\\[_6C_3 = \\frac{6 \\times 5 \\times 4}{3 \\times 2 \\times 1} = \\frac{120}{6} = 20\\]
<br>

• 「A, B, C」と「C, B, A」は同じ組<br>
<br>

<hr>

<b>【関係性】</b><br>
<br>

\\[\\binom{n}{r} = \\frac{_nP_r}{r!}\\]
<br>

<b>意味:</b><br>
• 順列は組み合わせのr!倍<br>
• 組み合わせで選んだr個を並べる方法がr!通りあるため<br>
<br>

<b>例: 6人から3人</b><br>
• 順列: 120通り<br>
• 組み合わせ: 20通り<br>
• 120 = 20 × 6（6 = 3!）<br>
<br>

<hr>

<b>【使い分けの判断基準】</b><br>
<br>

<b>質問: 「順序を変えると意味が変わるか？」</b><br>
<br>

<b>YES（意味が変わる）→ 順列（P）を使う</b><br>
• 会長、副会長、書記を選ぶ<br>
• 1位、2位、3位を決める<br>
• 暗証番号を作る（1234と4321は別）<br>
• リレーの走順を決める<br>
<br>

<b>NO（意味が変わらない）→ 組み合わせ（C）を使う</b><br>
• 委員3人を選ぶ<br>
• くじを3本引く<br>
• トランプを5枚配る<br>
• チームメンバーを選ぶ<br>
<br>

<hr>

<b>【具体的な比較例】</b><br>
<br>

<b>問題1: 10人から代表3人を選ぶ</b><br>
→ 役職なし → <b>組み合わせ</b><br>
\\[_{10}C_3 = \\frac{10 \\times 9 \\times 8}{3 \\times 2 \\times 1} = 120\\]
<br>

<b>問題2: 10人から会長、副会長、書記を選ぶ</b><br>
→ 役職あり → <b>順列</b><br>
\\[_{10}P_3 = 10 \\times 9 \\times 8 = 720\\]
<br>

<b>問題3: 数字0,1,2,3,4から3桁の整数を作る</b><br>
→ 123と321は違う → <b>順列</b>（ただし0は百の位に来られない）<br>
<br>

<hr>

<b>【Excel関数】</b><br>
<br>

• <b>PERMUT(n, r)</b>: nPrを計算<br>
• <b>COMBIN(n, r)</b>: nCrを計算<br>
• <b>FACT(n)</b>: n!を計算<br>
<br>

<b>例:</b><br>
• =PERMUT(6, 3) → 120<br>
• =COMBIN(6, 3) → 20<br>
• =FACT(5) → 120<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>最も基本的で重要な区別</b><br>
• 間違えると答えが大きく異なる（r!倍の差）<br>
• 問題文をよく読んで判断<br>
• 「選んで並べる」→ P<br>
• 「選ぶだけ」→ C<br>
• 確率計算の基礎として頻出<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「Pの使い方」<br>
統計WEB「Cの使い方」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'counting', 'permutation', 'combination', 'basic']
        },

        # カード2: 階乗と0の階乗
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【階乗】<br>n!とは何か？<br>なぜ0! = 1なのか？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【階乗の定義】</b><br>
<br>

<b>階乗（Factorial）: n!</b><br>
<br>

<b>定義:</b><br>
1からnまでのすべての<b>正の整数の積</b><br>
<br>

\\[n! = n \\times (n-1) \\times (n-2) \\times \\cdots \\times 3 \\times 2 \\times 1\\]
<br>

<b>読み方:</b><br>
• n!（エヌの階乗、エヌファクトリアル）<br>
<br>

<hr>

<b>【具体的な計算例】</b><br>
<br>

\\[1! = 1\\]
\\[2! = 2 \\times 1 = 2\\]
\\[3! = 3 \\times 2 \\times 1 = 6\\]
\\[4! = 4 \\times 3 \\times 2 \\times 1 = 24\\]
\\[5! = 5 \\times 4 \\times 3 \\times 2 \\times 1 = 120\\]
\\[6! = 6 \\times 5 \\times 4 \\times 3 \\times 2 \\times 1 = 720\\]
\\[7! = 7 \\times 6! = 7 \\times 720 = 5040\\]
\\[10! = 3628800\\]
<br>

<b>注意: 階乗は急速に大きくなる</b><br>
<br>

<hr>

<b>【再帰的定義】</b><br>
<br>

\\[n! = n \\times (n-1)!\\]
<br>

<b>例:</b><br>
• 5! = 5 × 4! = 5 × 24 = 120<br>
• 6! = 6 × 5! = 6 × 120 = 720<br>
<br>

<b>利点:</b><br>
• 前の値から計算できる<br>
• プログラミングで効率的<br>
<br>

<hr>

<b>【0の階乗: 0! = 1】</b><br>
<br>

<b>定義: 0! = 1</b><br>
<br>

<b>なぜ1なのか（3つの理由）:</b><br>
<br>

<b>理由1: 再帰的定義の整合性</b><br>
<br>

n! = n × (n-1)! より:<br>
\\[1! = 1 \\times 0!\\]
<br>

1! = 1なので:<br>
\\[1 = 1 \\times 0!\\]
\\[0! = 1\\]
<br>

<b>理由2: 順列・組み合わせの公式の整合性</b><br>
<br>

nPn（n個からn個すべて取り出す）:<br>
\\[_nP_n = \\frac{n!}{(n-n)!} = \\frac{n!}{0!}\\]
<br>

一方、n個をすべて並べる方法はn!通り:<br>
\\[_nP_n = n!\\]
<br>

よって:<br>
\\[\\frac{n!}{0!} = n!\\]
\\[0! = 1\\]
<br>

<b>理由3: 空積（empty product）の概念</b><br>
<br>

• 何も掛けるものがない積は1（数学の約束）<br>
• 0個のものを並べる方法は1通り（何もしない）<br>
• 空集合の順列は1通り<br>
<br>

<hr>

<b>【順列・組み合わせでの使われ方】</b><br>
<br>

<b>順列の公式:</b><br>
\\[_nP_r = \\frac{n!}{(n-r)!}\\]
<br>

<b>例: 5P5（5個全部を並べる）</b><br>
\\[_5P_5 = \\frac{5!}{(5-5)!} = \\frac{5!}{0!} = \\frac{120}{1} = 120\\]
<br>

0! = 1でないと計算できない!<br>
<br>

<b>組み合わせの公式:</b><br>
\\[\\binom{n}{r} = \\frac{n!}{(n-r)! \\times r!}\\]
<br>

<b>例: 5C5（5個から5個すべて選ぶ）</b><br>
\\[_5C_5 = \\frac{5!}{0! \\times 5!} = \\frac{120}{1 \\times 120} = 1\\]
<br>

<b>例: 5C0（5個から0個選ぶ）</b><br>
\\[_5C_0 = \\frac{5!}{5! \\times 0!} = \\frac{120}{120 \\times 1} = 1\\]
<br>

• 何も選ばない方法は1通り → 合理的!<br>
<br>

<hr>

<b>【階乗の計算テクニック】</b><br>
<br>

<b>分数での約分:</b><br>
<br>

\\[\\frac{10!}{8!} = \\frac{10 \\times 9 \\times 8!}{8!} = 10 \\times 9 = 90\\]
<br>

<b>組み合わせの計算:</b><br>
\\[_6C_3 = \\frac{6!}{3! \\times 3!} = \\frac{6 \\times 5 \\times 4 \\times 3!}{3! \\times 3!} = \\frac{6 \\times 5 \\times 4}{3 \\times 2 \\times 1} = 20\\]
<br>

• 共通部分を約分して簡単に計算<br>
<br>

<hr>

<b>【Excel関数】</b><br>
<br>

<b>=FACT(n)</b>: n!を計算<br>
<br>

• =FACT(0) → 1<br>
• =FACT(5) → 120<br>
• =FACT(10) → 3628800<br>
<br>

<b>注意: Excelは170!まで計算可能</b><br>
171!以上は#NUM!エラー（数値が大きすぎる）<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>0! = 1は定義</b>であり、覚える必要がある<br>
• 順列・組み合わせの計算で必須<br>
• 階乗は急速に大きくなる（10! = 約360万）<br>
• 計算では約分を活用<br>
• nCrやnPrを直接計算する方が効率的な場合もある<br>
<br>

<b>統計検定2級では:</b><br>
• 0! = 1を知っていること<br>
• 階乗を使った公式の計算<br>
• 約分テクニックの活用<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「Pの使い方」<br>
統計WEB「順列と組み合わせ」<br>
一般的な数学教材<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'counting', 'factorial', 'zero-factorial']
        },

        # カード3: 円順列と数珠順列
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【円順列と数珠順列】<br>公式と見分け方は？<br>なぜ(n-1)!と(n-1)!/2？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【円順列（Circular Permutation）】</b><br>
<br>

<b>定義:</b><br>
n個の異なるものを<b>円形に並べる</b>順列<br>
<br>

<b>公式:</b><br>
\\[円順列 = (n-1)!\\]
<br>

<b>考え方:</b><br>
• 回転して一致するものは同じとみなす<br>
• 1つを固定して、残りのn-1個を並べる<br>
<br>

<b>なぜ(n-1)!なのか:</b><br>
<br>

通常の順列だと n! 通り<br>
しかし円形では、n通りの回転が同じ配置<br>
→ n! ÷ n = (n-1)!<br>
<br>

<b>別の考え方:</b><br>
1つを固定して考える<br>
→ 残りn-1個を並べる方法 = (n-1)!<br>
<br>

<b>具体例: 6個の異なる宝石を円形に並べる</b><br>
\\[円順列 = (6-1)! = 5! = 120\\]
<br>

<b>図解:</b><br>
通常の順列: 6! = 720通り<br>
円形では6通りの回転が同じ: 720 ÷ 6 = 120通り<br>
<br>

<b>キーワード:</b><br>
• 「円形に並べる」<br>
• 「輪の形に配置する」<br>
• 「円卓に座る」<br>
• 「リングを作る」<br>
<br>

<hr>

<b>【数珠順列（Bracelet Permutation）】</b><br>
<br>

<b>定義:</b><br>
n個の異なるものを円形に並べ、さらに<b>裏返しても同じ</b>とみなす順列<br>
<br>

<b>公式:</b><br>
\\[数珠順列 = \\frac{(n-1)!}{2}\\]
<br>

<b>考え方:</b><br>
• 回転で一致 + 裏返しで一致するものを同じとみなす<br>
• 円順列をさらに2で割る<br>
<br>

<b>なぜ(n-1)!/2なのか:</b><br>
<br>

円順列: (n-1)! 通り<br>
裏返すと同じ配置になる: 2通りが同一<br>
→ (n-1)! ÷ 2<br>
<br>

<b>具体例: 6個の異なる宝石でブレスレットを作る</b><br>
\\[数珠順列 = \\frac{(6-1)!}{2} = \\frac{5!}{2} = \\frac{120}{2} = 60\\]
<br>

<b>キーワード:</b><br>
• 「ブレスレット」<br>
• 「首飾り」<br>
• 「ネックレス」<br>
• 「数珠」<br>
• 「表裏がない」<br>
<br>

<hr>

<b>【2つの違いと見分け方】</b><br>
<br>

<table border="1" cellpadding="5" style="border-collapse:collapse; max-width:100%; font-size:16px; overflow-x:auto;">
<tr style="background-color:#e0e0e0;">
  <th>項目</th>
  <th>円順列</th>
  <th>数珠順列</th>
</tr>
<tr>
  <td><b>公式</b></td>
  <td>(n-1)!</td>
  <td>(n-1)!/2</td>
</tr>
<tr>
  <td><b>回転</b></td>
  <td>同じとみなす</td>
  <td>同じとみなす</td>
</tr>
<tr>
  <td><b>裏返し</b></td>
  <td>別物</td>
  <td>同じとみなす</td>
</tr>
<tr>
  <td><b>例</b></td>
  <td>円卓に座る、輪を作る</td>
  <td>ブレスレット、首飾り</td>
</tr>
</table>
<br>

<b>判断のポイント:</b><br>
• <b>表裏の区別があるか？</b><br>
  - ある → 円順列<br>
  - ない → 数珠順列<br>
<br>

• <b>裏返せるか？</b><br>
  - 裏返せない（椅子に座るなど） → 円順列<br>
  - 裏返せる（アクセサリー） → 数珠順列<br>
<br>

<hr>

<b>【具体例での比較】</b><br>
<br>

<b>5人が円卓に座る</b><br>
→ 椅子は裏返せない → <b>円順列</b><br>
\\[(5-1)! = 4! = 24\\]
<br>

<b>5つの異なる宝石でブレスレットを作る</b><br>
→ ブレスレットは裏返せる → <b>数珠順列</b><br>
\\[\\frac{(5-1)!}{2} = \\frac{4!}{2} = \\frac{24}{2} = 12\\]
<br>

<b>4色の旗を輪の形に並べる</b><br>
→ 旗には表裏がある → <b>円順列</b><br>
\\[(4-1)! = 3! = 6\\]
<br>

<b>4色のビーズで首飾りを作る</b><br>
→ 首飾りは裏返せる → <b>数珠順列</b><br>
\\[\\frac{(4-1)!}{2} = \\frac{3!}{2} = \\frac{6}{2} = 3\\]
<br>

<hr>

<b>【通常の順列との比較】</b><br>
<br>

<b>6個を直線に並べる:</b><br>
6! = 720通り<br>
<br>

<b>6個を円形に並べる:</b><br>
(6-1)! = 5! = 120通り<br>
• 直線の1/6（回転6通りを同一視）<br>
<br>

<b>6個でブレスレットを作る:</b><br>
5!/2 = 60通り<br>
• 円順列の1/2（裏返し2通りを同一視）<br>
• 直線の1/12<br>
<br>

\\[720 : 120 : 60 = 12 : 2 : 1\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>キーワードで判断</b>が重要<br>
• 「円卓」「輪」→ 円順列<br>
• 「ブレスレット」「首飾り」「数珠」→ 数珠順列<br>
<br>

• <b>同じものを含む場合</b><br>
  - 同じものがある場合は、さらに重複で割る必要がある<br>
  - 例: 同じ色が2つ含まれる円順列 → (n-1)!/2!<br>
<br>

• <b>統計検定2級では</b><br>
  - 基本的な円順列の問題が出題される<br>
  - 数珠順列はやや応用的<br>
  - キーワードから判断できるようにする<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「練習問題」<br>
一般的な数学教材<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'counting', 'circular-permutation', 'bracelet']
        },

        # カード4: 同じものを含む順列
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【同じものを含む順列】<br>公式と考え方は？<br>なぜ割るのか？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【同じものを含む順列】</b><br>
<br>

<b>定義:</b><br>
n個の中に、同じものがp個、q個、r個...含まれる場合の順列<br>
<br>

<b>公式:</b><br>
\\[\\frac{n!}{p! \\times q! \\times r! \\times \\cdots}\\]
<br>

<b>条件:</b><br>
• p + q + r + ... = n<br>
• それぞれのグループ内では区別がつかない<br>
<br>

<hr>

<b>【なぜ割るのか（重複の除去）】</b><br>
<br>

<b>考え方:</b><br>
<br>

<b>ステップ1: すべて異なるものとして計算</b><br>
n個すべてが異なると仮定 → n! 通り<br>
<br>

<b>ステップ2: 重複を除去</b><br>
• 同じものp個を入れ替えても同じ配置 → p!通りが重複<br>
• 同じものq個を入れ替えても同じ配置 → q!通りが重複<br>
• これらは独立に起こる → p! × q! × ... で割る<br>
<br>

\\[実際の場合の数 = \\frac{n!}{p! \\times q! \\times r! \\times \\cdots}\\]
<br>

<hr>

<b>【具体例1: "SUCCESS"の並べ替え】</b><br>
<br>

文字列"SUCCESS"を並べ替える方法は何通りか？<br>
<br>

<b>分析:</b><br>
• 全体: 7文字<br>
• S: 3個（同じ）<br>
• C: 2個（同じ）<br>
• U: 1個<br>
• E: 1個<br>
<br>

<b>計算:</b><br>
\\[\\frac{7!}{3! \\times 2!} = \\frac{5040}{6 \\times 2} = \\frac{5040}{12} = 420\\]
<br>

<b>説明:</b><br>
• すべて異なるとすると7! = 5040通り<br>
• 3個のSを入れ替える3! = 6通りは同じ<br>
• 2個のCを入れ替える2! = 2通りは同じ<br>
• → 5040 ÷ (6 × 2) = 420通り<br>
<br>

<hr>

<b>【具体例2: カードの並べ替え】</b><br>
<br>

5枚のカード{1, 1, 2, 3, 4}を1列に並べる方法は何通りか？<br>
<br>

<b>分析:</b><br>
• 全体: 5枚<br>
• "1"が2枚（同じ）<br>
• その他は各1枚<br>
<br>

<b>計算:</b><br>
\\[\\frac{5!}{2!} = \\frac{120}{2} = 60\\]
<br>

<b>検算:</b><br>
• すべて異なるとすると5! = 120通り<br>
• 2枚の"1"を入れ替える2! = 2通りは同じ<br>
• → 120 ÷ 2 = 60通り<br>
<br>

<hr>

<b>【具体例3: 旗の配置】</b><br>
<br>

赤旗3本、白旗2本、青旗1本を1列に並べる方法は何通りか？<br>
<br>

<b>分析:</b><br>
• 全体: 6本<br>
• 赤: 3本（同じ）<br>
• 白: 2本（同じ）<br>
• 青: 1本<br>
<br>

<b>計算:</b><br>
\\[\\frac{6!}{3! \\times 2! \\times 1!} = \\frac{720}{6 \\times 2 \\times 1} = \\frac{720}{12} = 60\\]
<br>

<b>注意: 1! = 1なので省略可能</b><br>
\\[\\frac{6!}{3! \\times 2!} = 60\\]
<br>

<hr>

<b>【具体例4: 0を含む数字の並べ替え】</b><br>
<br>

数字{0, 0, 1, 2, 3}を使って5桁の整数を作る方法は何通りか？<br>
<br>

<b>注意: 0は最高位に来られない!</b><br>
<br>

<b>解法:</b><br>
<br>

<b>方法1: 全体 - 0が最高位のケース</b><br>
<br>

全体: 5!/2! = 60通り（0が2つ）<br>
<br>

0が最高位のケース:<br>
• 最高位が0 → 残り{0, 1, 2, 3}を並べる<br>
• 4!/1! = 24通り<br>
<br>

答え: 60 - 24 = <b>36通り</b><br>
<br>

<b>方法2: 最高位から場合分け</b><br>
<br>

最高位が1: {0, 0, 2, 3}を並べる → 4!/2! = 12通り<br>
最高位が2: {0, 0, 1, 3}を並べる → 4!/2! = 12通り<br>
最高位が3: {0, 0, 1, 2}を並べる → 4!/2! = 12通り<br>
<br>

答え: 12 + 12 + 12 = <b>36通り</b><br>
<br>

<hr>

<b>【一般的なパターン】</b><br>
<br>

<b>パターン1: 2種類のものを並べる</b><br>
n個中、A種類がp個、B種類がn-p個<br>
\\[\\frac{n!}{p! \\times (n-p)!} = _nC_p\\]
<br>

→ 組み合わせと同じ!<br>
<br>

<b>例: 10個の位置に〇を3個、×を7個配置</b><br>
\\[\\frac{10!}{3! \\times 7!} = _{10}C_3 = 120\\]
<br>

<b>パターン2: すべて異なる場合</b><br>
p = q = r = ... = 1<br>
\\[\\frac{n!}{1! \\times 1! \\times \\cdots} = n!\\]
<br>

→ 通常の順列に戻る<br>
<br>

<b>パターン3: すべて同じ場合</b><br>
p = n<br>
\\[\\frac{n!}{n!} = 1\\]
<br>

→ 1通りのみ（当然）<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>最初に分類</b>する<br>
  - 何が何個あるか正確に数える<br>
  - 見落としがないか確認<br>
<br>

• <b>0の扱いに注意</b><br>
  - 整数を作る問題では0は最高位に来られない<br>
  - 全体から引くか、場合分けする<br>
<br>

• <b>組み合わせとの関係</b><br>
  - 2種類の配置問題は組み合わせと同じ<br>
  - どちらの公式を使っても同じ答え<br>
<br>

• <b>統計検定2級では</b><br>
  - 基本的な計算問題が出題される<br>
  - 確率計算の中で使うことが多い<br>
  - 公式を正しく使えることが重要<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「練習問題」<br>
一般的な数学教材<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'counting', 'permutation', 'identical-objects']
        },

        # カード5: 重複順列と重複組み合わせ
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【重複順列と重複組み合わせ】<br>nΠrとnHrの公式は？<br>どう使い分ける？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【重複を許す場合の数】</b><br>
<br>

通常のPとCは「異なるn個から」だが、<br>
<b>同じものを繰り返し選んでもよい</b>場合もある<br>
<br>

<hr>

<b>【重複順列（Permutation with Repetition）: nΠr】</b><br>
<br>

<b>定義:</b><br>
区別できるn個のものから<b>重複を許して</b>r個取り出して1列に並べる<br>
<br>

<b>記号:</b><br>
nΠr（パイと読む）<br>
<br>

<b>公式:</b><br>
\\[_n\\\\Pi_r = n^r\\]
<br>

<b>考え方:</b><br>
• 1個目の選び方: n通り<br>
• 2個目の選び方: n通り（重複OK）<br>
• 3個目の選び方: n通り（重複OK）<br>
• ...<br>
• r個目の選び方: n通り（重複OK）<br>
<br>

積の法則より: n × n × n × ... × n (r個) = n^r<br>
<br>

<b>特徴:</b><br>
• <b>順序を考慮する</b><br>
• <b>重複を許す</b><br>
• 使い終わったものを戻して次を選ぶイメージ<br>
<br>

<hr>

<b>【重複順列の具体例】</b><br>
<br>

<b>例1: 3種類の食事から4日間選ぶ</b><br>
<br>

A, B, C の3種類から、重複を許して4日分選ぶ<br>
<br>

\\[_3\\\\Pi_4 = 3^4 = 81\\]
<br>

• 「A, A, B, C」や「A, A, A, A」もOK<br>
• 4日間の順序が違えば別のパターン<br>
<br>

<b>例2: 4桁の暗証番号（0〜9を使用）</b><br>
<br>

10個の数字から重複を許して4桁<br>
<br>

\\[_{10}\\\\Pi_4 = 10^4 = 10000\\]
<br>

• 「1111」や「9999」もOK<br>
• 0000〜9999の10000通り<br>
<br>

<b>例3: サイコロを3回振る</b><br>
<br>

6通りの目が3回<br>
<br>

\\[_6\\\\Pi_3 = 6^3 = 216\\]
<br>

• 「1, 1, 1」や「6, 6, 6」もOK<br>
• 出る順序が違えば別のパターン<br>
<br>

<hr>

<b>【重複組み合わせ（Combination with Repetition）: nHr】</b><br>
<br>

<b>定義:</b><br>
異なるn個のものから<b>重複を許して</b>r個取り出す（順序を考えない）<br>
<br>

<b>記号:</b><br>
nHr（エイチと読む、Hはhomogeneous重複の意味）<br>
<br>

<b>公式:</b><br>
\\[_nH_r = _{n+r-1}C_r\\]
<br>

または<br>
\\[_nH_r = _{n+r-1}C_{n-1}\\]
<br>

<b>考え方（仕切りを使う方法）:</b><br>
<br>

n種類を仕切りで区切って、r個の〇を配置する問題に置き換える<br>
<br>

• 〇がr個<br>
• 仕切りがn-1個<br>
• 合計n+r-1個を並べる<br>
• このうちr個の〇の位置を選ぶ → n+r-1Cr<br>
<br>

<b>特徴:</b><br>
• <b>順序を考慮しない</b><br>
• <b>重複を許す</b><br>
• 通常の組み合わせよりも場合の数が多い<br>
<br>

<hr>

<b>【重複組み合わせの具体例】</b><br>
<br>

<b>例1: 3種類のケーキから5個買う</b><br>
<br>

A, B, Cの3種類から重複を許して5個選ぶ<br>
<br>

\\[_3H_5 = _{3+5-1}C_5 = _7C_5 = _7C_2 = 21\\]
<br>

• 「A3個, B2個」も「A5個」もOK<br>
• 順序は関係ない（Aを1個目に選ぶか5個目に選ぶか無関係）<br>
<br>

<b>仕切り図解:</b><br>
〇〇〇|〇〇| → A3個, B2個, C0個<br>
〇〇〇〇〇|| → A5個, B0個, C0個<br>
|〇〇|〇〇〇 → A0個, B2個, C3個<br>
<br>

<b>例2: 10個のボールを3人に配る</b><br>
<br>

3人（A, B, C）に10個を配る（もらえない人もいてOK）<br>
<br>

\\[_3H_{10} = _{3+10-1}C_{10} = _{12}C_{10} = _{12}C_2 = 66\\]
<br>

• 「A: 10個, B: 0個, C: 0個」もOK<br>
• 「A: 5個, B: 3個, C: 2個」もOK<br>
<br>

<b>例3: x + y + z = 5（x, y, z ≥ 0の整数解）</b><br>
<br>

3つの変数に合計5を配分する<br>
<br>

\\[_3H_5 = _7C_5 = 21\\]
<br>

• (5, 0, 0), (4, 1, 0), (3, 2, 0), (3, 1, 1), (2, 2, 1), ...<br>
<br>

<hr>

<b>【4つのタイプの比較】</b><br>
<br>

<table border="1" cellpadding="5" style="border-collapse:collapse; max-width:100%; font-size:16px; overflow-x:auto;">
<tr style="background-color:#e0e0e0;">
  <th>種類</th>
  <th>記号</th>
  <th>公式</th>
  <th>特徴</th>
</tr>
<tr>
  <td><b>順列</b></td>
  <td>nPr</td>
  <td>n!/(n-r)!</td>
  <td>順序あり、重複なし</td>
</tr>
<tr>
  <td><b>組み合わせ</b></td>
  <td>nCr</td>
  <td>n!/[(n-r)!r!]</td>
  <td>順序なし、重複なし</td>
</tr>
<tr>
  <td><b>重複順列</b></td>
  <td>nΠr</td>
  <td>n^r</td>
  <td>順序あり、重複あり</td>
</tr>
<tr>
  <td><b>重複組み合わせ</b></td>
  <td>nHr</td>
  <td>n+r-1Cr</td>
  <td>順序なし、重複あり</td>
</tr>
</table>
<br>

<b>判断フローチャート:</b><br>
<br>

1. <b>重複を許すか？</b><br>
   YES → 重複順列 or 重複組み合わせ<br>
   NO → 順列 or 組み合わせ<br>
<br>

2. <b>順序を考慮するか？</b><br>
   YES → 順列系（P or Π）<br>
   NO → 組み合わせ系（C or H）<br>
<br>

<hr>

<b>【使い分けの具体例】</b><br>
<br>

<b>問題: 3人にボール5個を配る</b><br>
<br>

<b>ケース1: ボールに区別がある、もらう順番も考慮</b><br>
→ 重複順列: 3^5 = 243通り<br>
<br>

<b>ケース2: ボールに区別がない、配分だけ考える</b><br>
→ 重複組み合わせ: 3H5 = 7C5 = 21通り<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>重複順列は簡単: n^r</b><br>
  - 各段階でn通りの選択肢<br>
  - 計算が非常に簡単<br>
<br>

• <b>重複組み合わせは複雑: n+r-1Cr</b><br>
  - 仕切りの考え方を理解<br>
  - nCrに変換して計算<br>
<br>

• <b>4つのタイプを整理</b><br>
  - 順序 × 重複の2×2 = 4パターン<br>
  - それぞれの公式を覚える<br>
<br>

• <b>統計検定2級では</b><br>
  - 重複順列（n^r）は頻出<br>
  - 重複組み合わせはやや応用的<br>
  - 問題文から判断できるように<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
一般的な数学教材<br>
統計WEB関連ページ<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'counting', 'permutation-with-repetition', 'combination-with-repetition']
        },

        # カード6: nCrの性質（対称性とパスカルの三角形）
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【nCrの性質】<br>対称性とパスカルの三角形<br>どう活用する？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【組み合わせnCrの重要な性質】</b><br>
<br>

組み合わせnCrには、計算を簡単にする便利な性質がいくつかある<br>
<br>

<hr>

<b>【性質1: 対称性（Symmetry）】</b><br>
<br>

<b>公式:</b><br>
\\[\\binom{n}{r} = \\binom{n}{n-r}\\]
<br>

<b>意味:</b><br>
n個からr個選ぶことと、n-r個選ぶことは同じ<br>
<br>

<b>なぜ成り立つのか:</b><br>
<br>

r個を選ぶ = 残りのn-r個を選ばないことを決める<br>
<br>

選ぶ組と選ばない組は1対1に対応<br>
→ 場合の数は同じ<br>
<br>

<b>公式による証明:</b><br>
\\[\\binom{n}{r} = \\frac{n!}{r! \\times (n-r)!}\\]
<br>

\\[\\binom{n}{n-r} = \\frac{n!}{(n-r)! \\times (n-(n-r))!} = \\frac{n!}{(n-r)! \\times r!}\\]
<br>

分母のr!と(n-r)!の順序が入れ替わるだけ → 同じ値<br>
<br>

<hr>

<b>【対称性の具体例】</b><br>
<br>

<b>例1:</b><br>
\\[_{10}C_3 = _{10}C_7 = 120\\]
<br>

10人から3人選ぶ = 10人から7人選ぶ<br>
<br>

<b>例2:</b><br>
\\[_{100}C_{98} = _{100}C_2 = \\frac{100 \\times 99}{2 \\times 1} = 4950\\]
<br>

100個から98個選ぶ計算は大変<br>
→ 2個選ぶ計算に変換すると簡単!<br>
<br>

<b>例3:</b><br>
\\[_nC_0 = _nC_n = 1\\]
<br>

• 何も選ばない方法: 1通り<br>
• すべて選ぶ方法: 1通り<br>
• 対称性から同じ<br>
<br>

<hr>

<b>【対称性の活用: 計算の簡略化】</b><br>
<br>

<b>原則: rが大きい場合、n-rで計算</b><br>
<br>

<b>判断基準:</b><br>
• r > n/2 の場合 → n-rで計算する方が楽<br>
<br>

<b>例題: 52C50を計算</b><br>
<br>

<b>愚直な計算:</b><br>
\\[_{52}C_{50} = \\frac{52!}{50! \\times 2!}\\]
<br>

分子が膨大な数になる...<br>
<br>

<b>対称性を使う:</b><br>
\\[_{52}C_{50} = _{52}C_2 = \\frac{52 \\times 51}{2 \\times 1} = \\frac{2652}{2} = 1326\\]
<br>

一瞬で計算できる!<br>
<br>

<hr>

<b>【性質2: パスカルの三角形（Pascal's Triangle）】</b><br>
<br>

<b>公式:</b><br>
\\[\\binom{n}{r} = \\binom{n-1}{r-1} + \\binom{n-1}{r}\\]
<br>

<b>意味:</b><br>
1つの要素に注目して場合分けすると導出できる<br>
<br>

<b>証明の考え方:</b><br>
<br>

n個から r個選ぶ問題を、特定の1つ（Aとする）に注目して分ける<br>
<br>

• <b>ケース1: Aを含む</b><br>
  - 残りn-1個からr-1個選ぶ → n-1Cr-1<br>
<br>

• <b>ケース2: Aを含まない</b><br>
  - 残りn-1個からr個選ぶ → n-1Cr<br>
<br>

2つのケースは排反なので:<br>
\\[\\binom{n}{r} = \\binom{n-1}{r-1} + \\binom{n-1}{r}\\]
<br>

<hr>

<b>【パスカルの三角形の構造】</b><br>
<br>

<pre style="font-size:16px;">
                    1                    (0C0)
                  1   1                  (1C0, 1C1)
                1   2   1                (2C0, 2C1, 2C2)
              1   3   3   1              (3C0, 3C1, 3C2, 3C3)
            1   4   6   4   1            (4C0, 4C1, 4C2, 4C3, 4C4)
          1   5  10  10   5   1          (5C0, 5C1, 5C2, 5C3, 5C4, 5C5)
        1   6  15  20  15   6   1        (6C0〜6C6)
</pre>
<br>

<b>規則:</b><br>
• 両端は常に1<br>
• 内側の数は、上の2つの数の和<br>
• n行目がnCrの値<br>
• 左右対称（対称性の視覚的表現）<br>
<br>

<b>具体例: 6C2を求める</b><br>
<br>

パスカルの三角形の6行目、2番目の値を見る<br>
→ 15<br>
<br>

または公式から:<br>
\\[_6C_2 = _5C_1 + _5C_2 = 5 + 10 = 15\\]
<br>

<hr>

<b>【パスカルの三角形の応用】</b><br>
<br>

<b>二項定理との関係:</b><br>
<br>

\\[(a + b)^n = \\sum_{r=0}^n \\binom{n}{r} a^{n-r} b^r\\]
<br>

パスカルの三角形の各行が二項展開の係数<br>
<br>

<b>例: (a + b)³</b><br>
\\[(a + b)^3 = 1a^3 + 3a^2b + 3ab^2 + 1b^3\\]
<br>

係数: 1, 3, 3, 1 → パスカルの三角形の3行目<br>
<br>

<b>各行の和:</b><br>
\\[\\sum_{r=0}^n \\binom{n}{r} = 2^n\\]
<br>

例: 1 + 4 + 6 + 4 + 1 = 16 = 2⁴<br>
<br>

<hr>

<b>【性質3: その他の重要な関係式】</b><br>
<br>

<b>①nCr = nPr / r!</b><br>
順列と組み合わせの基本関係<br>
<br>

<b>②nC1 = n</b><br>
n個から1個選ぶ → n通り<br>
<br>

<b>③nCn = 1</b><br>
すべて選ぶ → 1通り<br>
<br>

<b>④nC0 = 1</b><br>
何も選ばない → 1通り<br>
<br>

<b>⑤和の公式:</b><br>
\\[\\sum_{k=0}^n _nC_k = 2^n\\]
<br>

全ての組み合わせの総数（部分集合の数）<br>
<br>

<hr>

<b>【実践問題での活用】</b><br>
<br>

<b>問題: 20C18 + 20C19を計算せよ</b><br>
<br>

<b>方法1: 対称性を使う</b><br>
\\[_{20}C_{18} = _{20}C_2 = 190\\]
\\[_{20}C_{19} = _{20}C_1 = 20\\]
\\[190 + 20 = 210\\]
<br>

<b>方法2: パスカルの三角形を使う</b><br>
\\[_{20}C_{18} + _{20}C_{19} = _{21}C_{19} = _{21}C_2 = 210\\]
<br>

どちらも同じ答え!<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>対称性で計算を簡略化</b><br>
  - r > n/2なら n-rで計算<br>
  - 大幅に計算量が減る<br>
<br>

• <b>パスカルの三角形の理解</b><br>
  - 二項定理の係数<br>
  - 組み合わせの再帰的構造<br>
  - 確率の問題でも応用<br>
<br>

• <b>統計検定2級では</b><br>
  - 対称性を使った計算問題<br>
  - パスカルの三角形の概念理解<br>
  - 二項分布との関連<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「Cの使い方」<br>
一般的な数学教材<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'counting', 'combination', 'symmetry', 'pascal-triangle']
        },

        # カード7: 確率計算における場合の数の活用
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【確率計算と場合の数】<br>白3個・赤7個のボールから<br>3個取り出す確率は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【場合の数と確率の基本】</b><br>
<br>

<b>確率の基本公式:</b><br>
\\[P(A) = \\frac{事象Aの場合の数}{全体の場合の数}\\]
<br>

場合の数は<b>確率計算の基礎</b><br>
→ 順列・組み合わせが重要<br>
<br>

<hr>

<b>【問題設定】</b><br>
<br>

<b>白3個、赤7個、計10個のボールがある</b><br>
この中から無作為に3個を取り出す<br>
<br>

<b>条件:</b><br>
• ボールはすべて区別できる<br>
• 同時に3個取り出す（順序を考えない）<br>
• 非復元抽出（戻さない）<br>
<br>

→ <b>組み合わせ（C）</b>を使う<br>
<br>

<hr>

<b>【全体の場合の数】</b><br>
<br>

10個から3個を選ぶ:<br>
\\[_{10}C_3 = \\frac{10 \\times 9 \\times 8}{3 \\times 2 \\times 1} = \\frac{720}{6} = 120\\]
<br>

<hr>

<b>【問1: 全て赤である確率】</b><br>
<br>

<b>求める事象: 赤3個</b><br>
<br>

赤7個から3個選ぶ:<br>
\\[_7C_3 = \\frac{7 \\times 6 \\times 5}{3 \\times 2 \\times 1} = \\frac{210}{6} = 35\\]
<br>

<b>確率:</b><br>
\\[P(全て赤) = \\frac{35}{120} = \\frac{7}{24} \\\approx 0.292\\]
<br>

<b>約29.2%</b><br>
<br>

<hr>

<b>【問2: 白1個、赤2個である確率】</b><br>
<br>

<b>求める事象: 白1個 かつ 赤2個</b><br>
<br>

<b>ステップ1: 白1個を選ぶ</b><br>
白3個から1個:<br>
\\[_3C_1 = 3\\]
<br>

<b>ステップ2: 赤2個を選ぶ</b><br>
赤7個から2個:<br>
\\[_7C_2 = \\frac{7 \\times 6}{2 \\times 1} = 21\\]
<br>

<b>ステップ3: 両方が起こる（積の法則）</b><br>
\\[3 \\times 21 = 63\\]
<br>

<b>確率:</b><br>
\\[P(白1, 赤2) = \\frac{63}{120} = \\frac{21}{40} = 0.525\\]
<br>

<b>52.5%</b><br>
<br>

<hr>

<b>【問3: 白2個、赤1個である確率】</b><br>
<br>

白3個から2個:<br>
\\[_3C_2 = 3\\]
<br>

赤7個から1個:<br>
\\[_7C_1 = 7\\]
<br>

両方が起こる:<br>
\\[3 \\times 7 = 21\\]
<br>

<b>確率:</b><br>
\\[P(白2, 赤1) = \\frac{21}{120} = \\frac{7}{40} = 0.175\\]
<br>

<b>17.5%</b><br>
<br>

<hr>

<b>【問4: 全て白である確率】</b><br>
<br>

白3個から3個:<br>
\\[_3C_3 = 1\\]
<br>

<b>確率:</b><br>
\\[P(全て白) = \\frac{1}{120} \\\approx 0.0083\\]
<br>

<b>約0.83%</b>（非常に低い）<br>
<br>

<hr>

<b>【検証: 確率の和は1】</b><br>
<br>

白の個数で場合分け:<br>
<br>

• 白0個（赤3個）: 7/24 = 35/120<br>
• 白1個（赤2個）: 21/40 = 63/120<br>
• 白2個（赤1個）: 7/40 = 21/120<br>
• 白3個（赤0個）: 1/120<br>
<br>

<b>合計:</b><br>
\\[\\frac{35 + 63 + 21 + 1}{120} = \\frac{120}{120} = 1\\]
<br>

✓ 正しい!<br>
<br>

<hr>

<b>【重要な考え方】</b><br>
<br>

<b>①組み合わせを使う理由</b><br>
• 「同時に取り出す」→ 順序を考えない<br>
• 「3個のボール」を選ぶだけ → 組み合わせ<br>
<br>

<b>②積の法則の使用</b><br>
• 「白から選ぶ」AND「赤から選ぶ」<br>
• 独立した選択 → 掛け算<br>
<br>

<b>③全体の場合の数</b><br>
• すべての確率計算で分母は同じ<br>
• 10C3 = 120通り<br>
<br>

<hr>

<b>【Excel関数での計算】</b><br>
<br>

<b>全体の場合の数:</b><br>
=COMBIN(10, 3) → 120<br>
<br>

<b>白1個・赤2個の場合の数:</b><br>
=COMBIN(3, 1) * COMBIN(7, 2) → 63<br>
<br>

<b>確率:</b><br>
=COMBIN(3,1)*COMBIN(7,2)/COMBIN(10,3) → 0.525<br>
<br>

<hr>

<b>【類題: カードの問題】</b><br>
<br>

<b>問題: 52枚のトランプから5枚引く</b><br>
<br>

全体:<br>
\\[_{52}C_5 = 2598960\\]
<br>

<b>例: スペード2枚、ハート3枚の確率</b><br>
<br>

スペード13枚から2枚:<br>
\\[_{13}C_2 = 78\\]
<br>

ハート13枚から3枚:<br>
\\[_{13}C_3 = 286\\]
<br>

両方:<br>
\\[78 \\times 286 = 22308\\]
<br>

確率:<br>
\\[\\frac{22308}{2598960} \\\approx 0.00858\\]
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

• <b>順序の有無を判断</b><br>
  - 同時に取り出す → 組み合わせ<br>
  - 1個ずつ順に取り出す → 順列<br>
<br>

• <b>複数条件は積の法則</b><br>
  - 「AかつB」→ 掛け算<br>
  - 「AまたはB」→ 足し算（排反の場合）<br>
<br>

• <b>確率の和の検証</b><br>
  - すべての場合を足すと1<br>
  - 計算ミスのチェックに有効<br>
<br>

• <b>統計検定2級では</b><br>
  - この種の計算問題が頻出<br>
  - 正確な場合の数の計算が必須<br>
  - Excelでの計算も覚えておく<br>
<br>

<hr>

<b>【Excel関数まとめ】</b><br>
<br>

• <b>PERMUT(n, r)</b>: nPrを計算<br>
• <b>COMBIN(n, r)</b>: nCrを計算<br>
• <b>FACT(n)</b>: n!を計算<br>
<br>

<b>例:</b><br>
• =PERMUT(6, 3) → 120<br>
• =COMBIN(6, 3) → 20<br>
• =FACT(5) → 120<br>
• =COMBIN(10,3) → 120<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「確率の計算」<br>
統計WEB「順列と組み合わせ」<br>
bellcurve.jp
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'counting', 'probability', 'combination', 'application', 'excel']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("場合の数 - 検証済みAnkiカード生成")
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
    cards = create_counting_principles_cards(deck_name, model_name)
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
    print("✨ 場合の数カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 順列と組み合わせの基本的な違い")
    print("  カード2: 階乗と0の階乗")
    print("  カード3: 円順列と数珠順列")
    print("  カード4: 同じものを含む順列")
    print("  カード5: 重複順列と重複組み合わせ")
    print("  カード6: nCrの性質（対称性とパスカルの三角形）")
    print("  カード7: 確率計算における場合の数の活用")
    print()


if __name__ == "__main__":
    main()
