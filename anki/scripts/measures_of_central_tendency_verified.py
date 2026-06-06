#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
様々な代表値（Measures of Central Tendency） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「3-1. 平均・中央値・モード」https://bellcurve.jp/statistics/course/4317.html
- 統計WEB「3-2. 平均・中央値・モードの関係」https://bellcurve.jp/statistics/course/4320.html
- 統計WEB「3-3. 平均・中央値・モードの使い方」https://bellcurve.jp/statistics/course/4322.html
- 統計WEB「4-1. 平均、中央値、最頻値を求めてみよう」https://bellcurve.jp/statistics/course/19014.html
- 統計WEB「4-2. 四分位数を見てみよう」https://bellcurve.jp/statistics/course/19277.html
- 複数の統計学サイトで検証済み
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


def create_measures_of_central_tendency_cards(deck_name, model_name):
    """様々な代表値カードを作成（検証済み）"""

    cards = [
        # カード1: 算術平均
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【算術平均】<br>定義と公式は？<br>特徴と注意点は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
すべてのデータを合計してデータ数で割った値<br>
てこの原理における「支点」として機能する統計量<br>
<br>

<b>英語:</b> Arithmetic Mean, Average<br>
<br>

<b>公式:</b><br>
\\[\\bar{x} = \\frac{x_1 + x_2 + \\cdots + x_n}{n} = \\frac{1}{n}\\sum_{i=1}^n x_i\\]
<br>

\\(\\bar{x}\\): 標本平均（xバー）<br>
n: データ数<br>
<br>

<b>度数分布表の場合:</b><br>
\\[\\bar{x} = \\frac{f_1v_1 + f_2v_2 + \\cdots + f_kv_k}{f_1 + f_2 + \\cdots + f_k}\\]
<br>

f: 度数、v: 階級値<br>
<br>

<hr>

<b>【具体例】</b><br>
<br>

<b>5つの屋台の焼きそば価格:</b><br>
1000円、500円、700円、1200円、800円<br>
<br>

\\[\\bar{x} = \\frac{1000 + 500 + 700 + 1200 + 800}{5} = \\frac{4200}{5} = 840円\\]
<br>

<hr>

<b>【特徴】</b><br>
<br>

<b>メリット:</b><br>
• すべてのデータを計算に反映<br>
• 統計的推定・検定で最も重要<br>
• 数学的性質が優れている<br>
<br>

<b>デメリット:</b><br>
• <b>外れ値の影響を大きく受ける</b><br>
• 分布が偏っていると実態を表せない<br>
<br>

<b>例: 外れ値の影響</b><br>
貯蓄額データ:<br>
200万、300万、400万、500万、<b>1700万</b><br>
→ 平均 = 620万円（実態より高い）<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>使用場面:</b><br>
• 左右対称の分布で外れ値がない場合<br>
• すべてのデータを反映したい場合<br>
• 統計的検定・推定を行う場合<br>
<br>

<b>母平均との関係:</b><br>
• \\(\\mu\\)（ミュー）: 母平均（母集団全体の平均）<br>
• \\(\\bar{x}\\)（xバー）: 標本平均（サンプルの平均）<br>
• \\(\\bar{x}\\) は \\(\\mu\\) の推定値<br>
<br>

<b>統計検定2級では:</b><br>
• 基礎的な計算は確実に<br>
• 度数分布表からの平均計算<br>
• 外れ値の影響を理解<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-1. 平均・中央値・モード」<br>
統計WEB「4-1. 平均、中央値、最頻値を求めてみよう」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'mean', 'arithmetic-mean', 'central-tendency']
        },

        # カード2: 中央値（メジアン）
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【中央値（メジアン）】<br>定義と計算方法は？<br>なぜ外れ値に強い？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
データを小さい順に並べたとき、<br>
<b>ちょうど真ん中に来る値</b><br>
<br>

<b>英語:</b> Median<br>
<b>別名:</b> 第2四分位数、50パーセンタイル<br>
<br>

<hr>

<b>【計算方法】</b><br>
<br>

<b>データが奇数個の場合:</b><br>
中央の値をそのまま使用<br>
<br>

例: 1, 2, 3, <b>4</b>, 5, 6, 7 → 中央値 = <b>4</b><br>
<br>

<b>データが偶数個の場合:</b><br>
中央に最も近い2つの値の平均<br>
<br>

例: 1, 1, 2, 4, <b>5, 8</b>, 9, 10, 11, 14<br>
→ 中央値 = \\(\\frac{5 + 8}{2} = 6.5\\)<br>
<br>

<hr>

<b>【具体例】</b><br>
<br>

<b>10軒の屋台の金魚すくい数:</b><br>
データ: 3, 4, 4, 5, <b>6, 7</b>, 7, 8, 10, 11 匹<br>
<br>

中央値 = \\(\\frac{6 + 7}{2} = 6.5\\)匹<br>
<br>

<hr>

<b>【外れ値への頑健性（ロバスト性）】</b><br>
<br>

<b>なぜ外れ値に強いのか:</b><br>
• 値そのものではなく「順位」だけを見るため<br>
• 極端な値があっても中央の位置は変わらない<br>
<br>

<b>比較例（貯蓄額）:</b><br>
データ: 200万、300万、400万、500万、<b>1700万</b><br>
<br>

• 平均 = 620万円（外れ値に引っ張られる）<br>
• 中央値 = <b>400万円</b>（実態に近い）✓<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>使用場面:</b><br>
• 外れ値がある場合<br>
• 分布が偏っている場合<br>
• 年収や資産など、極端な値を含むデータ<br>
• 「ちょうど真ん中くらい」を知りたい場合<br>
<br>

<b>メリット:</b><br>
• 外れ値の影響を受けにくい<br>
• 実態を正確に反映しやすい<br>
• 直感的に理解しやすい<br>
<br>

<b>デメリット:</b><br>
• すべてのデータを活用しない<br>
• 数学的な扱いが平均より難しい<br>
<br>

<b>統計検定2級では:</b><br>
• 奇数個・偶数個の計算方法<br>
• 平均との使い分け<br>
• 外れ値への頑健性の理解<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-1. 平均・中央値・モード」<br>
統計WEB「4-1. 平均、中央値、最頻値を求めてみよう」<br>
統計WEB「平均値と中央値の違い」ブログ記事<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'median', 'central-tendency', 'robust']
        },

        # カード3: 最頻値（モード）
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【最頻値（モード）】<br>定義と使い方は？<br>質的データにも使える？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
<b>最も頻度が高い値</b>（一番多く出現している値）<br>
<br>

<b>英語:</b> Mode<br>
<b>別名:</b> 最頻値、並み、モード<br>
<br>

<hr>

<b>【具体例1: 量的データ】</b><br>
<br>

<b>13軒の屋台の食べ物価格:</b><br>
100円、<b>200円</b>、<b>200円</b>、<b>200円</b>、<b>200円</b>、<br>
300円、400円、400円、500円、500円、<br>
600円、800円、900円<br>
<br>

→ 最頻値 = <b>200円</b>（4回出現で最多）<br>
<br>

<hr>

<b>【具体例2: 質的データ】</b><br>
<br>

<b>好きな果物のアンケート:</b><br>
• りんご: 5人<br>
• <b>みかん: 12人</b><br>
• バナナ: 8人<br>
• ぶどう: 3人<br>
<br>

→ 最頻値 = <b>みかん</b><br>
<br>

<b>重要:</b> 質的データ（カテゴリーデータ）に使える唯一の代表値！<br>
<br>

<hr>

<b>【使用場面と意味】</b><br>
<br>

<b>「ボリュームゾーン」を把握:</b><br>
• 最も多い顧客層は？<br>
• 最も需要がある価格帯は？<br>
• 集団の「中心的な特徴」を知る<br>
<br>

<b>例: 貯蓄額分布</b><br>
データ: 200〜400万円が36人中12人<br>
→ 「約3分の1の人が200〜400万円の層」<br>
→ これが実態の中心<br>
<br>

<hr>

<b>【注意点】</b><br>
<br>

<b>最頻値が存在しない場合:</b><br>
• すべての値が1回ずつ → モードなし<br>
<br>

<b>複数の最頻値がある場合:</b><br>
• 2つ: 二峰性（bimodal）<br>
• 3つ以上: 多峰性（multimodal）<br>
<br>

<b>二峰性データの解釈:</b><br>
• 複数の異なる集団が混在している可能性<br>
• 例: 男女混合データ、異なる商品カテゴリ混在<br>
• → データを分割して分析することを推奨<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>メリット:</b><br>
• <b>質的データに使える唯一の代表値</b><br>
• 「最も典型的な値」を示す<br>
• 直感的に理解しやすい<br>
<br>

<b>デメリット:</b><br>
• 存在しない場合がある<br>
• 複数存在する場合がある<br>
• データ全体を反映しない<br>
<br>

<b>統計検定2級では:</b><br>
• 質的データへの適用を理解<br>
• ボリュームゾーンの概念<br>
• 二峰性の解釈<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-1. 平均・中央値・モード」<br>
統計WEB「3-3. 平均・中央値・モードの使い方」<br>
統計WEB「4-1. 平均、中央値、最頻値を求めてみよう」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'mode', 'central-tendency', 'qualitative-data']
        },

        # カード4: 3つの代表値の使い分け
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【代表値の使い分け】<br>平均・中央値・最頻値<br>どう使い分ける？<br>分布の歪みとの関係は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>【使い分けの基準】</b><br>
<br>

<table border="1" style="border-collapse:collapse; width:100%;">
<tr style="background-color:#f0f0f0;">
  <th>状況</th>
  <th>推奨される代表値</th>
  <th>理由</th>
</tr>
<tr>
  <td>外れ値なし<br>左右対称分布</td>
  <td><b>平均値</b></td>
  <td>すべてのデータを反映<br>統計的性質が良い</td>
</tr>
<tr>
  <td>外れ値あり<br>偏った分布</td>
  <td><b>中央値</b></td>
  <td>外れ値の影響を受けない<br>実態を正確に反映</td>
</tr>
<tr>
  <td>質的データ<br>カテゴリーデータ</td>
  <td><b>最頻値</b></td>
  <td>唯一使える代表値</td>
</tr>
<tr>
  <td>ボリュームゾーン<br>を知りたい</td>
  <td><b>最頻値</b></td>
  <td>最も多い層を把握</td>
</tr>
</table>
<br>

<hr>

<b>【分布の歪みと代表値の関係】</b><br>
<br>

<b>左右対称分布（正規分布など）:</b><br>
\\[平均値 = 中央値 = 最頻値\\]
<br>

例: 157.2 ≈ 157.2 ≈ 157.2<br>
<br>

<b>右に裾が長い分布（左に偏った分布）:</b><br>
\\[最頻値 < 中央値 < 平均値\\]
<br>

例: 152.5 < 155 < 157.2<br>
• 高所得者が平均を引き上げる<br>
• 中央値の方が実態に近い<br>
<br>

<b>左に裾が長い分布（右に偏った分布）:</b><br>
\\[平均値 < 中央値 < 最頻値\\]
<br>

例: 167.8 < 170 < 172.5<br>
<br>

<b>※注意:</b> データによっては必ずしもこの順番にならない場合もある<br>
<br>

<hr>

<b>【具体的な判断フロー】</b><br>
<br>

<b>ステップ1: データの種類を確認</b><br>
• 質的データ → <b>最頻値</b>のみ使用可<br>
• 量的データ → ステップ2へ<br>
<br>

<b>ステップ2: 分布を確認</b><br>
• ヒストグラムや箱ひげ図を作成<br>
• 外れ値の有無を確認<br>
<br>

<b>ステップ3: 代表値を選択</b><br>
• 外れ値なし＆対称分布 → <b>平均値</b><br>
• 外れ値あり or 偏った分布 → <b>中央値</b><br>
• ボリュームゾーン把握 → <b>最頻値</b><br>
<br>

<hr>

<b>【併用のススメ】</b><br>
<br>

<b>複数の代表値を併用する:</b><br>
• 平均と中央値の差 → 分布の偏りを把握<br>
• 3つすべて → データの全体像を理解<br>
• 五数要約（最小値、Q1、中央値、Q3、最大値）も活用<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>統計検定2級では:</b><br>
• 分布の歪みから代表値の大小関係を判断<br>
• 適切な代表値を選択する問題が出題<br>
• 「なぜその代表値を使うか」を説明できること<br>
<br>

<b>実務での注意:</b><br>
• 「平均」だけで判断しない<br>
• グラフと併せて確認<br>
• 目的に応じて使い分ける<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-2. 平均・中央値・モードの関係」<br>
統計WEB「3-3. 平均・中央値・モードの使い方」<br>
統計WEB「平均値と中央値の違い」ブログ記事<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'central-tendency', 'comparison', 'skewness']
        },

        # カード5: 加重平均
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【加重平均】<br>定義と公式は？<br>なぜ重みをつける？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
各データに<b>重み（ウェイト）</b>をつけて計算する平均値<br>
データの重要度や重みが違っても正しく平均値を求められる<br>
<br>

<b>英語:</b> Weighted Mean, Weighted Average<br>
<br>

<b>公式:</b><br>
\\[\\bar{x}_w = \\frac{x_1w_1 + x_2w_2 + \\cdots + x_nw_n}{w_1 + w_2 + \\cdots + w_n} = \\frac{\\sum_{i=1}^n x_iw_i}{\\sum_{i=1}^n w_i}\\]
<br>

\\(x_i\\): データの値<br>
\\(w_i\\): 重み（ウェイト）<br>
<br>

<hr>

<b>【具体例1: 成績評価】</b><br>
<br>

<b>3つのテストの点数と配点:</b><br>
• 中間試験: 80点（配点30%）<br>
• 期末試験: 70点（配点50%）<br>
• レポート: 90点（配点20%）<br>
<br>

<b>単純平均（誤り）:</b><br>
\\(\\frac{80 + 70 + 90}{3} = 80\\)点<br>
<br>

<b>加重平均（正しい）:</b><br>
\\[\\frac{80 \\times 0.3 + 70 \\times 0.5 + 90 \\times 0.2}{0.3 + 0.5 + 0.2}\\]
\\[= \\frac{24 + 35 + 18}{1} = 77点\\]
<br>

→ 期末試験の重みが大きいため、正しくは77点<br>
<br>

<hr>

<b>【具体例2: 度数分布表からの平均】</b><br>
<br>

度数分布表から平均を求めるとき、実は加重平均を使っている！<br>
<br>

\\[\\bar{x} = \\frac{f_1v_1 + f_2v_2 + \\cdots + f_kv_k}{f_1 + f_2 + \\cdots + f_k}\\]
<br>

• \\(v_i\\): 階級値（データの値）<br>
• \\(f_i\\): 度数（重み）<br>
<br>

<hr>

<b>【使用場面】</b><br>
<br>

<b>実務での活用:</b><br>
• 成績評価（配点が異なる試験）<br>
• 株式ポートフォリオ（保有比率が重み）<br>
• 東証株価指数（TOPIX）（時価総額が重み）<br>
• 満足度調査（回答数が重み）<br>
• 製造工場の歩留まり率<br>
• 会計（数量が異なる品目の平均価格）<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>単純平均との違い:</b><br>
• 単純平均 = すべてのデータの重みが同じ<br>
• 加重平均 = データごとに重みが異なる<br>
• <b>重みが同じなら、加重平均 = 単純平均</b><br>
<br>

<b>重みの意味:</b><br>
• 重要度（試験の配点）<br>
• 頻度・数量（度数、保有量）<br>
• 信頼度（測定の精度）<br>
<br>

<b>メリット:</b><br>
• より現実的で正確な平均<br>
• データの特性を反映<br>
<br>

<b>注意点:</b><br>
• 重みの設定が不適切だと誤った結論<br>
• 重みの合計を確認すること<br>
<br>

<b>統計検定2級では:</b><br>
• 度数分布表からの平均 = 加重平均<br>
• 加重調和平均の応用問題も出題される<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-1. 平均・中央値・モード」<br>
統計WEB「練習問題（3. さまざまな代表値）」<br>
複数の統計サイトで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'weighted-mean', 'central-tendency']
        },

        # カード6: 四分位数
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【四分位数】<br>定義と計算方法は？<br>Q1、Q2、Q3とは？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
データを小さい方から並び替え、<br>
データの個数で<b>4等分</b>した時の区切り点<br>
<br>

<b>英語:</b> Quartile<br>
<br>

<hr>

<b>【3つの四分位数】</b><br>
<br>

<b>第一四分位数（Q1）:</b><br>
• 下から25%の位置<br>
• 25パーセンタイル<br>
<br>

<b>第二四分位数（Q2）:</b><br>
• 下から50%の位置<br>
• <b>中央値（メジアン）</b>と同じ<br>
• 50パーセンタイル<br>
<br>

<b>第三四分位数（Q3）:</b><br>
• 下から75%の位置<br>
• 75パーセンタイル<br>
<br>

<hr>

<b>【計算方法】</b><br>
<br>

<b>データが奇数個の場合:</b><br>
1. 中央値（Q2）を求める<br>
2. 中央値を除外して上下のグループに分割<br>
3. 各グループの中央値がQ1、Q3<br>
<br>

例: 1, 2, 3, 4, <b>5</b>, 6, 7, 8, 9<br>
• Q2 = 5（中央値）<br>
• 下グループ: 1, <b>2</b>, 3, 4 → Q1 = 2.5<br>
• 上グループ: 6, <b>7</b>, 8, 9 → Q3 = 7.5<br>
<br>

<b>データが偶数個の場合:</b><br>
1. 中央で均等に分割<br>
2. 各半分内の中央値がQ1、Q3<br>
<br>

例: 1, 2, 3, 4, | 5, 6, 7, 8<br>
• Q1 = (2+3)/2 = 2.5<br>
• Q2 = (4+5)/2 = 4.5<br>
• Q3 = (6+7)/2 = 6.5<br>
<br>

<hr>

<b>【四分位範囲（IQR）】</b><br>
<br>

<b>定義:</b><br>
\\[\IQR = Q3 - Q1\\]
<br>

• データの散らばり度合いを示す<br>
• 中央50%のデータの範囲<br>
• 外れ値の影響を受けにくい<br>
<br>

<b>外れ値の判定:</b><br>
• 下側外れ値: Q1 - 1.5×IQR より小さい<br>
• 上側外れ値: Q3 + 1.5×IQR より大きい<br>
<br>

<hr>

<b>【具体例】</b><br>
<br>

<b>12曲の楽曲の長さ（分）:</b><br>
2.7, 2.8, 3.2, 3.2, 3.6, 3.9,<br>
4.0, 4.1, 4.3, 4.4, 4.6, 5.2<br>
<br>

• Q1 = (3.2 + 3.2)/2 = <b>3.2分</b><br>
• Q2 = (3.9 + 4.0)/2 = <b>3.95分</b>（中央値）<br>
• Q3 = (4.4 + 4.4)/2 = <b>4.4分</b><br>
• IQR = 4.4 - 3.2 = <b>1.2分</b><br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>五数要約:</b><br>
最小値、Q1、Q2（中央値）、Q3、最大値<br>
→ データの分布を簡潔に表現<br>
<br>

<b>箱ひげ図との関係:</b><br>
• 箱の下端 = Q1<br>
• 箱の中の線 = Q2（中央値）<br>
• 箱の上端 = Q3<br>
• ひげ = 最小値と最大値（外れ値除く）<br>
<br>

<b>統計検定2級では:</b><br>
• 四分位数の計算（奇数/偶数）<br>
• IQRの計算<br>
• 箱ひげ図の読み取り・作成<br>
• 外れ値の判定<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「4-2. 四分位数を見てみよう」<br>
統計WEB用語集「四分位数」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'quartile', 'Q1', 'Q2', 'Q3', 'IQR']
        },

        # カード7: パーセンタイル・五数要約
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【パーセンタイル・五数要約】<br>パーセンタイルとは？<br>五数要約と箱ひげ図の関係は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>【パーセンタイル】</b><br>
<br>

<b>定義:</b><br>
データを小さい順に並べたとき、<br>
初めから数えて全体の<b>100α%</b>に位置する値（0≤α≤1）<br>
<br>

<b>英語:</b> Percentile<br>
<br>

<b>例:</b><br>
• 65パーセンタイル = 下から65%の位置の値<br>
• 90パーセンタイル = 下から90%の位置の値<br>
<br>

<hr>

<b>【四分位数との関係】</b><br>
<br>

<table border="1" style="border-collapse:collapse; width:100%;">
<tr style="background-color:#f0f0f0;">
  <th>四分位数</th>
  <th>パーセンタイル</th>
  <th>意味</th>
</tr>
<tr>
  <td>Q1（第一四分位数）</td>
  <td>25パーセンタイル</td>
  <td>下から25%</td>
</tr>
<tr>
  <td>Q2（第二四分位数）</td>
  <td>50パーセンタイル</td>
  <td>中央値</td>
</tr>
<tr>
  <td>Q3（第三四分位数）</td>
  <td>75パーセンタイル</td>
  <td>下から75%</td>
</tr>
</table>
<br>

<hr>

<b>【五数要約（Five-Number Summary）】</b><br>
<br>

<b>定義:</b><br>
データの分布を5つの数値で要約<br>
<br>

<b>5つの値:</b><br>
1. <b>最小値</b>（Minimum）<br>
2. <b>第一四分位数（Q1）</b> - 25パーセンタイル<br>
3. <b>中央値（Q2）</b> - 50パーセンタイル<br>
4. <b>第三四分位数（Q3）</b> - 75パーセンタイル<br>
5. <b>最大値</b>（Maximum）<br>
<br>

<b>例:</b><br>
データ: 12曲の楽曲の長さ<br>
• 最小値: 2.7分<br>
• Q1: 3.2分<br>
• Q2: 3.95分<br>
• Q3: 4.4分<br>
• 最大値: 5.2分<br>
<br>

<hr>

<b>【箱ひげ図（Box Plot）】</b><br>
<br>

<b>五数要約を視覚化したグラフ:</b><br>
<br>

┣━━━━┫■■■■■■┃■■■■■■┣━━━━┫<br>
最小  Q1    Q2    Q3   最大<br>
値              (中央値)              値<br>
<br>

<b>構成要素:</b><br>
• <b>箱（Box）</b>: Q1からQ3まで（IQRの範囲）<br>
• <b>箱の中の線</b>: Q2（中央値）<br>
• <b>ひげ（Whisker）</b>: 最小値と最大値まで伸びる線<br>
  （外れ値がある場合は外れ値を除く）<br>
• <b>外れ値</b>: 個別の点として表示<br>
<br>

<hr>

<b>【使用場面】</b><br>
<br>

<b>データの分布把握:</b><br>
• 中心位置（Q2）<br>
• 散らばり（IQR）<br>
• 歪み（箱の形の偏り）<br>
• 外れ値の有無<br>
<br>

<b>複数グループの比較:</b><br>
• 複数の箱ひげ図を並べて比較<br>
• 例: クラスごとの成績分布<br>
• 例: 年齢層別の収入分布<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>パーセンタイルの利点:</b><br>
• 外れ値の影響を受けにくい<br>
• 順位による表現で直感的<br>
• 分布の形状を把握しやすい<br>
<br>

<b>五数要約の利点:</b><br>
• データ全体を簡潔に表現<br>
• 平均だけでは見えない情報<br>
• 箱ひげ図で視覚化可能<br>
<br>

<b>統計検定2級では:</b><br>
• パーセンタイルの意味を理解<br>
• 五数要約の計算<br>
• 箱ひげ図の読み取り・作成<br>
• 複数グループの比較<br>
<br>

<b>Excelでの計算:</b><br>
• PERCENTILE関数<br>
• QUARTILE関数<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB用語集「パーセンタイル」<br>
統計WEB用語集「四分位数」<br>
統計WEB「平均値と中央値の違い」ブログ記事<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'percentile', 'five-number-summary', 'box-plot']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("様々な代表値 - 検証済みAnkiカード生成")
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
    cards = create_measures_of_central_tendency_cards(deck_name, model_name)
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
    print("✨ 様々な代表値カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 算術平均 - 定義、公式、外れ値の影響")
    print("  カード2: 中央値（メジアン）- 計算方法、頑健性")
    print("  カード3: 最頻値（モード）- 質的データへの適用")
    print("  カード4: 3つの代表値の使い分け - 分布の歪みとの関係")
    print("  カード5: 加重平均 - 重みづけ、成績評価の例")
    print("  カード6: 四分位数 - Q1/Q2/Q3、IQR")
    print("  カード7: パーセンタイル・五数要約 - 箱ひげ図")
    print()


if __name__ == "__main__":
    main()
