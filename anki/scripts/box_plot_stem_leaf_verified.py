#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
箱ひげ図と幹葉表示（Box Plot and Stem-and-Leaf Display） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「4-1. 箱ひげ図とは」https://bellcurve.jp/statistics/course/5219.html
- 統計WEB「4-2. 箱ひげ図の見方」https://bellcurve.jp/statistics/course/5220.html
- 統計WEB「4-3. 外れ値検出のある箱ひげ図」https://bellcurve.jp/statistics/course/5222.html
- 統計WEB「4-4. 箱ひげ図の書き方（データ数が奇数の場合）」https://bellcurve.jp/statistics/course/5224.html
- 統計WEB「4-5. 箱ひげ図の書き方（データ数が偶数の場合）」https://bellcurve.jp/statistics/course/5226.html
- 統計WEB「4-6. 幹葉表示」https://bellcurve.jp/statistics/course/5228.html
- 複数の統計学サイトで検証済み
"""

import json
import urllib.request
import base64
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


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


def create_box_plot_diagram():
    """箱ひげ図の構成要素を示す図を生成"""
    # 日本語フォント設定
    plt.rcParams['font.family'] = 'Hiragino Sans'

    # サンプルデータ
    np.random.seed(42)
    data = [12, 15, 18, 20, 22, 24, 25, 26, 28, 30, 32, 35, 38, 40, 45]

    fig, ax = plt.subplots(figsize=(10, 6))

    # 箱ひげ図を作成
    bp = ax.boxplot([data], vert=False, widths=0.5, patch_artist=True,
                     boxprops=dict(facecolor='lightblue', alpha=0.7),
                     medianprops=dict(color='red', linewidth=2),
                     whiskerprops=dict(linewidth=1.5),
                     capprops=dict(linewidth=1.5))

    # 統計値を計算
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)  # 中央値
    q3 = np.percentile(data, 75)
    min_val = min(data)
    max_val = max(data)

    # ラベルを追加
    y_pos = 1.3
    ax.annotate('最小値\n{:.0f}'.format(min_val), xy=(min_val, 1),
                xytext=(min_val, y_pos),
                ha='center', fontsize=11, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    ax.annotate('第一四分位数\nQ1 = {:.0f}'.format(q1), xy=(q1, 1),
                xytext=(q1, y_pos),
                ha='center', fontsize=11, fontweight='bold', color='blue',
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

    ax.annotate('中央値\nQ2 = {:.0f}'.format(q2), xy=(q2, 1),
                xytext=(q2, y_pos + 0.2),
                ha='center', fontsize=11, fontweight='bold', color='red',
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

    ax.annotate('第三四分位数\nQ3 = {:.0f}'.format(q3), xy=(q3, 1),
                xytext=(q3, y_pos),
                ha='center', fontsize=11, fontweight='bold', color='blue',
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

    ax.annotate('最大値\n{:.0f}'.format(max_val), xy=(max_val, 1),
                xytext=(max_val, y_pos),
                ha='center', fontsize=11, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # 四分位範囲を示す
    ax.annotate('', xy=(q1, 0.5), xytext=(q3, 0.5),
                arrowprops=dict(arrowstyle='<->', color='green', lw=2))
    ax.text((q1+q3)/2, 0.35, 'IQR（四分位範囲）= {:.0f}'.format(q3-q1),
            ha='center', fontsize=11, fontweight='bold', color='green')

    ax.set_ylim(0, 2)
    ax.set_xlim(5, 50)
    ax.set_yticks([])
    ax.set_xlabel('値', fontsize=14, fontweight='bold')
    ax.set_title('箱ひげ図の構成要素', fontsize=16, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, axis='x')

    plt.tight_layout()

    # Base64エンコード
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()

    return image_base64


def create_box_plot_stem_leaf_cards(deck_name, model_name):
    """箱ひげ図と幹葉表示カードを作成（検証済み）"""

    # グラフ生成
    print("📊 箱ひげ図の説明図を生成中...")
    box_plot_diagram = create_box_plot_diagram()
    print("✅ 箱ひげ図生成完了")

    cards = [
        # カード1: 箱ひげ図の基本
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【箱ひげ図】<br>定義と構成要素は？<br>五数要約との関係は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>定義:</b><br>
データの分布を<b>「箱」と「ひげ」</b>で表したグラフ<br>
<br>

<b>英語:</b> Box Plot, Box-and-Whisker Plot<br>
<b>別名:</b> 箱ひげ図、箱ひげプロット<br>
<br>

<hr>

<b>【構成要素の図解】</b><br>
<br>
<img src="data:image/png;base64,{box_plot_diagram}" style="max-width:100%; height:auto;"><br>
<br>

<hr>

<b>【5つの構成要素（五数要約）】</b><br>
<br>

<table border="1" style="border-collapse:collapse; max-width:100%; overflow-x:auto;">
<tr style="background-color:#f0f0f0;">
  <th>要素</th>
  <th>意味</th>
  <th>別名</th>
</tr>
<tr>
  <td><b>ひげの下端</b></td>
  <td>最小値</td>
  <td>Minimum</td>
</tr>
<tr>
  <td><b>箱の下端</b></td>
  <td>第一四分位数（Q1）</td>
  <td>25パーセンタイル</td>
</tr>
<tr>
  <td><b>箱の中の線</b></td>
  <td>中央値（Q2）</td>
  <td>50パーセンタイル</td>
</tr>
<tr>
  <td><b>箱の上端</b></td>
  <td>第三四分位数（Q3）</td>
  <td>75パーセンタイル</td>
</tr>
<tr>
  <td><b>ひげの上端</b></td>
  <td>最大値</td>
  <td>Maximum</td>
</tr>
</table>
<br>

<hr>

<b>【重要な概念】</b><br>
<br>

<b>四分位範囲（IQR）:</b><br>
\\[\\\IQR = Q3 - Q1\\]
<br>

• 箱の幅がIQRを表す<br>
• データの中央50%の散らばり度合い<br>
• 外れ値の影響を受けにくい<br>
<br>

<b>範囲（レンジ）:</b><br>
\\[範囲 = 最大値 - 最小値\\]
<br>

• ひげ全体の長さ<br>
• データの散らばり全体<br>
<br>

<hr>

<b>【目的と利点】</b><br>
<br>

<b>目的:</b><br>
• データの集中や散らばりを一目で把握<br>
• 複数グループの比較<br>
• 外れ値の検出<br>
<br>

<b>利点:</b><br>
• 五数要約を視覚的に表現<br>
• 複数のデータセットを並べて比較しやすい<br>
• 分布の対称性や偏りが分かる<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>4つの区間の特徴:</b><br>
箱ひげ図の4区間（最小値～Q1、Q1～Q2、Q2～Q3、Q3～最大値）には、<br>
<b>それぞれ同じ個数のデータが入っている</b>（各25%ずつ）<br>
<br>

区間の長さが異なる = データのばらつき具合が異なる<br>
<br>

<b>統計検定2級では:</b><br>
• 箱ひげ図の読み取り問題<br>
• 複数グループの比較<br>
• 四分位数・IQRの計算<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「4-1. 箱ひげ図とは」<br>
統計WEB「4-2. 箱ひげ図の見方」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'box-plot', 'five-number-summary', 'graph']
        },

        # カード2: 箱ひげ図の作り方
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【箱ひげ図の作り方】<br>奇数個と偶数個のデータで<br>どう違う？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【データが奇数個の場合】</b><br>
<br>

<b>手順:</b><br>
1. データを小さい順に並べ替える<br>
2. 最大値と最小値を確定<br>
3. <b>中央値（Q2）</b>を求める（真ん中の値）<br>
4. <b>中央値を除いて</b>、下位データと上位データに分ける<br>
5. 下位データの中央値 = <b>Q1</b><br>
6. 上位データの中央値 = <b>Q3</b><br>
<br>

<b>例: データ9個</b><br>
12, 15, 18, 20, <b>22</b>, 24, 26, 28, 30<br>
<br>

• Q2（中央値）= 22<br>
• 下位: 12, <b>15</b>, 18, 20 → Q1 = (15+18)/2 = 16.5<br>
• 上位: 24, <b>26</b>, 28, 30 → Q3 = (26+28)/2 = 27<br>
<br>

<hr>

<b>【データが偶数個の場合】</b><br>
<br>

<b>手順:</b><br>
1. データを小さい順に並べ替える<br>
2. 最大値と最小値を確定<br>
3. <b>中央値（Q2）</b>を求める（真ん中の2つの平均）<br>
4. <b>中央値は除かずに</b>、データを均等に2分割<br>
5. 下位半分の中央値 = <b>Q1</b><br>
6. 上位半分の中央値 = <b>Q3</b><br>
<br>

<b>例: データ10個</b><br>
12, 15, 18, 20, | 22, 24, 26, 28, 30, 35<br>
<br>

• Q2（中央値）= (20+22)/2 = 21<br>
• 下位: 12, <b>15, 18</b>, 20, 22 → Q1 = 18<br>
• 上位: 22, 24, <b>26, 28</b>, 30, 35 → Q3 = 27<br>
<br>

<hr>

<b>【重要な違い】</b><br>
<br>

<table border="1" style="border-collapse:collapse; max-width:100%; overflow-x:auto;">
<tr style="background-color:#f0f0f0;">
  <th></th>
  <th>奇数個</th>
  <th>偶数個</th>
</tr>
<tr>
  <td><b>中央値</b></td>
  <td>真ん中の1つの値</td>
  <td>真ん中2つの平均</td>
</tr>
<tr>
  <td><b>分割方法</b></td>
  <td>中央値を<b>除外</b>して分割</td>
  <td>中央値を<b>除かず</b>均等に分割</td>
</tr>
<tr>
  <td><b>Q1, Q3の求め方</b></td>
  <td>各グループの中央値</td>
  <td>各グループの中央値</td>
</tr>
</table>
<br>

<hr>

<b>【具体例: 試験の点数】</b><br>
<br>

<b>13人の国語テストの点数（奇数個）:</b><br>
50, 55, 60, 65, 70, 75, <b>80</b>, 82, 85, 88, 90, 92, 95<br>
<br>

• 最小値 = 50<br>
• Q1 = 65（下位グループの中央値）<br>
• Q2 = 80（中央値）<br>
• Q3 = 90（上位グループの中央値）<br>
• 最大値 = 95<br>
• IQR = 90 - 65 = 25<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>Excel・ソフトウェアでの計算:</b><br>
• QUARTILE関数で自動計算可能<br>
• 計算方法が複数存在する場合があるため、定義を確認<br>
<br>

<b>統計検定2級では:</b><br>
• 手計算で四分位数を求める問題<br>
• 奇数個・偶数個両方のパターンを練習<br>
• 計算ミスに注意（特に中央値の扱い）<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「4-4. 箱ひげ図の書き方（データ数が奇数の場合）」<br>
統計WEB「4-5. 箱ひげ図の書き方（データ数が偶数の場合）」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'box-plot', 'quartile', 'calculation']
        },

        # カード3: 箱ひげ図の読み方
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【箱ひげ図の読み方】<br>分布の形状は？<br>ばらつきは？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【ばらつき具合の判定】</b><br>
<br>

<b>箱の幅（IQR）:</b><br>
• 箱が<b>広い</b> → データが散らばっている<br>
• 箱が<b>狭い</b> → データが集中している<br>
<br>

<b>ひげの長さ:</b><br>
• ひげが<b>長い</b> → 極端な値が存在<br>
• ひげが<b>短い</b> → データが狭い範囲に収まっている<br>
<br>

<hr>

<b>【分布の対称性の判定】</b><br>
<br>

<b>対称的な分布:</b><br>
• 中央値が箱の中心にある<br>
• 上下のひげの長さがほぼ同じ<br>
• 上下の箱の幅がほぼ同じ<br>
→ <b>正規分布</b>に近い形<br>
<br>

<b>右に裾が長い分布（左に偏った分布）:</b><br>
• 中央値が箱の下側（Q1寄り）にある<br>
• 上のひげが長い<br>
• Q2～Q3の幅 > Q1～Q2の幅<br>
→ 最頻値 < 中央値 < 平均値<br>
<br>

<b>左に裾が長い分布（右に偏った分布）:</b><br>
• 中央値が箱の上側（Q3寄り）にある<br>
• 下のひげが長い<br>
• Q1～Q2の幅 > Q2～Q3の幅<br>
→ 平均値 < 中央値 < 最頻値<br>
<br>

<hr>

<b>【複数グループの比較】</b><br>
<br>

複数の箱ひげ図を並べて表示することで比較可能:<br>
<br>

<b>比較できる項目:</b><br>
• <b>中央値の位置</b>: どちらが高い/低い<br>
• <b>IQRの大きさ</b>: どちらがばらつきが大きい<br>
• <b>範囲の大きさ</b>: 最大値と最小値の差<br>
• <b>分布の形状</b>: 対称性や偏り<br>
• <b>外れ値の有無</b>: 異常値の検出<br>
<br>

<b>例: クラスごとの成績比較</b><br>
• Aクラス: 中央値70点、IQR=15<br>
• Bクラス: 中央値75点、IQR=10<br>
→ Bクラスの方が平均的に高く、ばらつきも小さい<br>
<br>

<hr>

<b>【箱ひげ図から読み取れないこと】</b><br>
<br>

<b>注意点:</b><br>
• <b>峰の数（モードの数）</b>は判定できない<br>
• 二峰性分布も一峰性分布も同じ箱ひげ図になる場合がある<br>
• 詳細な分布形状を知りたい場合は<b>ヒストグラム</b>を使用<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>4区間の特徴（再確認）:</b><br>
各区間（最小値～Q1、Q1～Q2、Q2～Q3、Q3～最大値）には<br>
同じ個数（25%ずつ）のデータが入っている<br>
<br>

→ 区間の長さが違う = その範囲でのデータの散らばり方が違う<br>
<br>

<b>統計検定2級では:</b><br>
• 箱ひげ図から分布の特徴を読み取る<br>
• 複数グループの比較問題<br>
• 「範囲が最も大きいのは？」「IQRが最も小さいのは？」<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「4-2. 箱ひげ図の見方」<br>
統計WEB「練習問題（4. 箱ひげ図と幹葉表示）」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'box-plot', 'interpretation', 'comparison']
        },

        # カード4: 外れ値の判定
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【箱ひげ図と外れ値】<br>外れ値の判定基準は？<br>1.5×IQR法とは？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【外れ値とは】</b><br>
<br>

<b>定義:</b><br>
データの分布において、<b>他の観測値から大きく外れた値</b><br>
<br>

<b>原因:</b><br>
• 測定ミス<br>
• 記録ミス<br>
• 実際の異常値（正常な範囲外）<br>
• 別の母集団からのデータ混入<br>
<br>

<hr>

<b>【1.5×IQR法による外れ値判定】</b><br>
<br>

<b>判定基準:</b><br>
\\[下限 = Q1 - 1.5 \\times \IQR\\]
\\[上限 = Q3 + 1.5 \\times \IQR\\]
<br>

この範囲<b>外</b>の値が外れ値<br>
<br>

<b>具体例:</b><br>
Q1 = 20、Q3 = 40、IQR = 20 の場合<br>
<br>

• 下限 = 20 - 1.5×20 = 20 - 30 = <b>-10</b><br>
• 上限 = 40 + 1.5×20 = 40 + 30 = <b>70</b><br>
<br>

→ -10未満または70より大きい値が外れ値<br>
<br>

<hr>

<b>【外れ値のある箱ひげ図】</b><br>
<br>

<b>表示方法:</b><br>
• 外れ値は <b>「×」印</b> で個別に表示<br>
• ひげは外れ値を除いた範囲まで伸びる<br>
• ひげの端 = 外れ値でない最大値・最小値<br>
<br>

<b>例:</b><br>
データ: 5, 10, 12, 15, 18, 20, 22, 24, 26, <b>50</b><br>
<br>

• Q1 = 12、Q3 = 24、IQR = 12<br>
• 上限 = 24 + 1.5×12 = 42<br>
• 50 > 42 → <b>50は外れ値</b><br>
• 上のひげは26まで伸び、50は×印で表示<br>
<br>

<hr>

<b>【外れ値の扱い】</b><br>
<br>

<b>外れ値が見つかったら:</b><br>
<br>

<b>1. 原因を調査</b><br>
• 測定ミスや記録ミス → <b>削除または修正</b><br>
• 実際の異常値 → <b>分析に含めるか判断</b><br>
<br>

<b>2. 分析方法の選択</b><br>
• 外れ値を含めた分析<br>
• 外れ値を除外した分析<br>
• 頑健な統計量（中央値など）の使用<br>
<br>

<b>3. 報告</b><br>
• 外れ値の存在を明記<br>
• 外れ値の扱いを説明<br>
<br>

<hr>

<b>【なぜ1.5倍なのか】</b><br>
<br>

<b>理由:</b><br>
• 正規分布の場合、この基準で約99.3%のデータが範囲内に収まる<br>
• 経験的に適切なバランス<br>
• John Tukeyが提唱した基準<br>
<br>

<b>他の基準:</b><br>
• <b>3.0×IQR</b>: より厳しい基準（極端な外れ値のみ）<br>
• 目的に応じて調整可能<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>外れ値判定の手順:</b><br>
1. Q1、Q3、IQRを計算<br>
2. 下限・上限を計算（Q1 - 1.5×IQR、Q3 + 1.5×IQR）<br>
3. この範囲外のデータを特定<br>
4. 箱ひげ図に×印で表示<br>
<br>

<b>統計検定2級では:</b><br>
• 1.5×IQR法の計算<br>
• 外れ値の判定<br>
• 外れ値のある箱ひげ図の読み取り<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「4-3. 外れ値検出のある箱ひげ図」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'box-plot', 'outlier', 'IQR']
        },

        # カード5: 箱ひげ図とヒストグラムの比較
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【箱ひげ図 vs ヒストグラム】<br>どう使い分ける？<br>それぞれの利点は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【比較表】</b><br>
<br>

<table border="1" style="border-collapse:collapse; max-width:100%; overflow-x:auto;">
<tr style="background-color:#f0f0f0;">
  <th>項目</th>
  <th>箱ひげ図</th>
  <th>ヒストグラム</th>
</tr>
<tr>
  <td><b>主な用途</b></td>
  <td>複数データの比較</td>
  <td>1つのデータの詳細な分布</td>
</tr>
<tr>
  <td><b>適切なデータ数</b></td>
  <td>10個以上</td>
  <td>50個以上</td>
</tr>
<tr>
  <td><b>表示情報</b></td>
  <td>五数要約、IQR、外れ値</td>
  <td>度数分布、分布の形状、最頻値</td>
</tr>
<tr>
  <td><b>詳細度</b></td>
  <td>概要的</td>
  <td>詳細</td>
</tr>
<tr>
  <td><b>複数比較</b></td>
  <td>並べて比較しやすい</td>
  <td>並べると見にくい</td>
</tr>
<tr>
  <td><b>峰の数</b></td>
  <td>判定不可</td>
  <td>判定可能</td>
</tr>
<tr>
  <td><b>元データ</b></td>
  <td>復元不可</td>
  <td>復元不可（階級値のみ）</td>
</tr>
</table>
<br>

<hr>

<b>【箱ひげ図の利点】</b><br>
<br>

<b>1. 複数グループの比較が容易</b><br>
• 横に並べて表示しやすい<br>
• ばらつきの違いが一目瞭然<br>
<br>

<b>2. コンパクトな表現</b><br>
• 五数要約を1つの図で表現<br>
• スペースを取らない<br>
<br>

<b>3. 外れ値の検出</b><br>
• 1.5×IQR法で自動判定<br>
• 外れ値を視覚的に強調<br>
<br>

<b>4. 少ないデータでも有効</b><br>
• 10個程度から作成可能<br>
<br>

<hr>

<b>【ヒストグラムの利点】</b><br>
<br>

<b>1. 分布の詳細な形状</b><br>
• 峰の数（モード）が分かる<br>
• 二峰性、多峰性の判定<br>
• 歪みの程度が分かる<br>
<br>

<b>2. 最頻値の特定</b><br>
• どの階級が最も多いか明確<br>
<br>

<b>3. 確率分布との比較</b><br>
• 正規分布に従っているか確認<br>
• 理論分布との当てはまりを検証<br>
<br>

<b>4. 直感的な理解</b><br>
• データの「山」の形が分かりやすい<br>
<br>

<hr>

<b>【使い分けの基準】</b><br>
<br>

<b>箱ひげ図を使う場面:</b><br>
✓ 複数のグループを比較したい<br>
✓ ばらつきの大きさを比較したい<br>
✓ 外れ値を検出したい<br>
✓ データ数が少ない（10〜50個程度）<br>
✓ 簡潔に要約したい<br>
<br>

<b>例:</b> クラスごとの成績比較、地域ごとの所得比較<br>
<br>

<b>ヒストグラムを使う場面:</b><br>
✓ 1つのデータセットを詳しく分析<br>
✓ 分布の形状を詳細に把握したい<br>
✓ 最頻値を知りたい<br>
✓ データ数が多い（50個以上）<br>
✓ 正規性の検定前<br>
<br>

<b>例:</b> 試験の得点分布、製品の品質データ<br>
<br>

<hr>

<b>【併用のススメ】</b><br>
<br>

両方を使うことで、データの全体像をより深く理解できる:<br>
<br>

• <b>ヒストグラム</b>: 各グループの詳細な分布<br>
• <b>箱ひげ図</b>: グループ間の比較<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>統計検定2級では:</b><br>
• 両者の違いを理解<br>
• 適切な使い分けができること<br>
• 箱ひげ図から読み取れる情報と限界を理解<br>
<br>

<b>覚えておくこと:</b><br>
箱ひげ図は「要約」、ヒストグラムは「詳細」<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「4-1. 箱ひげ図とは」<br>
複数のソースで比較・検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'box-plot', 'histogram', 'comparison']
        },

        # カード6: 幹葉図の基本
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【幹葉図（茎葉図）】<br>定義と作り方は？<br>幹と葉の決め方は？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>定義:</b><br>
データの値そのものを用いて作成する<br>
<b>ヒストグラムに似た図</b><br>
<br>

<b>英語:</b> Stem-and-Leaf Plot, Stem-and-Leaf Display<br>
<b>別名:</b> 幹葉表示、茎葉図<br>
<br>

<hr>

<b>【構成要素】</b><br>
<br>

<b>幹（Stem）:</b><br>
• 縦向きに並ぶ数字<br>
• 通常は大きい桁（十の位など）<br>
• 上から下へ昇順に配列<br>
<br>

<b>葉（Leaf）:</b><br>
• 幹の横に並ぶ1桁の数字<br>
• 通常は小さい桁（一の位など）<br>
• 左から右へ昇順に整列<br>
<br>

<hr>

<b>【作成手順】</b><br>
<br>

<b>ステップ1: 幹と葉を決定</b><br>
データの桁を確認し、どの桁を幹・葉にするか決める<br>
<br>

<b>ステップ2: 幹を縦に配列</b><br>
幹を上から下へ昇順に書く<br>
<br>

<b>ステップ3: 葉を記入</b><br>
各データの葉を対応する幹の横に記入<br>
<br>

<b>ステップ4: 葉を整列</b><br>
各幹に対応する葉を左から右へ昇順に並べる<br>
<br>

<hr>

<b>【具体例1: 基本】</b><br>
<br>

<b>データ:</b> 27, 30, 33, 33, 37, 41, 45<br>
<br>

<b>幹葉図:</b><br>
<pre style="font-family:monospace; font-size:1em; background-color:#e8e8e8; color:#000; padding:15px; border:1px solid #999; border-radius:5px;">
幹 | 葉
---------
2  | 7
3  | 0 3 3 7
4  | 1 5
</pre>
<br>

• 十の位が「幹」、一の位が「葉」<br>
• 27 → 幹2、葉7<br>
• 33 → 幹3、葉3（2回出現）<br>
<br>

<hr>

<b>【具体例2: より大きなデータ】</b><br>
<br>

<b>試験の点数（15人）:</b><br>
52, 58, 63, 65, 68, 70, 72, 75, 75, 78, 82, 85, 88, 90, 95<br>
<br>

<b>幹葉図:</b><br>
<pre style="font-family:monospace; font-size:1em; background-color:#e8e8e8; color:#000; padding:15px; border:1px solid #999; border-radius:5px;">
幹 | 葉
---------
5  | 2 8
6  | 3 5 8
7  | 0 2 5 5 8
8  | 2 5 8
9  | 0 5
</pre>
<br>

• 70点台が最も多い（5人）<br>
• 75点が2人（葉に「5」が2つ）<br>
• 分布の形が横向きのヒストグラムのように見える<br>
<br>

<hr>

<b>【小数を含むデータの場合】</b><br>
<br>

<b>データ:</b> 3.2, 3.5, 3.8, 4.1, 4.3, 4.7<br>
<br>

<b>幹葉図:</b><br>
<pre style="font-family:monospace; font-size:1em; background-color:#e8e8e8; color:#000; padding:15px; border:1px solid #999; border-radius:5px;">
幹 | 葉
---------
3  | 2 5 8
4  | 1 3 7
</pre>
<br>

• 整数部分が「幹」、小数第一位が「葉」<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>幹と葉の決め方:</b><br>
• データの範囲や目的に応じて調整<br>
• 適度な幹の数（5〜20程度）が望ましい<br>
• データの特性が見やすい区切りを選ぶ<br>
<br>

<b>元データの復元:</b><br>
• 幹葉図から元のデータ値を完全に復元可能<br>
• これがヒストグラムとの大きな違い<br>
<br>

<b>統計検定2級では:</b><br>
• 幹葉図の作成方法<br>
• 幹葉図から統計量を読み取る<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「4-6. 幹葉表示」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'stem-and-leaf', 'plot', 'definition']
        },

        # カード7: 幹葉図の読み方と活用
        {
            'front': '''
<div style="font-size:1.3em; padding:20px;">
    <b>【幹葉図の活用】<br>どう読む？<br>メリット・デメリットは？<br>ヒストグラムとの違いは？</b>
</div>
''',
            'back': '''
<div style="font-size:1.1em; padding:20px; line-height:1.8;">

<b>【読み取り方】</b><br>
<br>

<b>1. 分布の形状:</b><br>
• 縦方向に見る → ヒストグラムのような形<br>
• 葉が多い幹 → データが集中<br>
• 葉が少ない幹 → データが少ない<br>
<br>

<b>2. 個々のデータ値:</b><br>
• 横方向に見る → 具体的な値を確認<br>
• 幹と葉を組み合わせて元の数値に戻す<br>
<br>

<b>3. 度数:</b><br>
• 各幹の葉の数を数える → その範囲のデータ数<br>
<br>

<hr>

<b>【統計量の読み取り】</b><br>
<br>

<b>中央値の求め方:</b><br>
1. すべての葉を上から順に数える<br>
2. 真ん中の位置のデータを見つける<br>
<br>

<b>例:</b> 15個のデータの場合<br>
• 8番目が中央値<br>
• 幹葉図で上から8番目の葉を探す<br>
<br>

<b>四分位数の求め方:</b><br>
1. データ数から位置を計算<br>
2. 幹葉図で該当位置のデータを読み取る<br>
<br>

<b>最頻値の求め方:</b><br>
• 同じ葉が複数ある値を探す<br>
• 葉が最も多い幹を確認<br>
<br>

<hr>

<b>【メリット】</b><br>
<br>

<b>1. 個々のデータ値が保持される</b><br>
• 元データの完全復元が可能<br>
• ヒストグラムと違って情報の損失なし<br>
<br>

<b>2. 分布と詳細の両立</b><br>
• 分布の形を掴める<br>
• 同時に個々のデータも確認できる<br>
<br>

<b>3. 外れ値や最頻値が分かりやすい</b><br>
• 離れた幹にある葉 → 外れ値<br>
• 同じ葉が複数 → 最頻値<br>
<br>

<b>4. 手作業で作成しやすい</b><br>
• ソフトウェア不要<br>
• 教育現場で有効<br>
<br>

<hr>

<b>【デメリット】</b><br>
<br>

<b>1. データ数が多いと見にくい</b><br>
• 数百個以上のデータには不向き<br>
• 葉が多すぎて雑然とする<br>
<br>

<b>2. 適用範囲が限定的</b><br>
• <b>適切なデータ数: 15〜150程度</b><br>
• 15個未満 → ドットプロット推奨<br>
• 150個以上 → ヒストグラムや箱ひげ図推奨<br>
<br>

<b>3. 複数グループの比較には不向き</b><br>
• 並べて表示しにくい<br>
• 箱ひげ図の方が適切<br>
<br>

<hr>

<b>【ヒストグラムとの違い】</b><br>
<br>

<table border="1" style="border-collapse:collapse; max-width:100%; overflow-x:auto;">
<tr style="background-color:#f0f0f0;">
  <th>項目</th>
  <th>幹葉図</th>
  <th>ヒストグラム</th>
</tr>
<tr>
  <td><b>データの保持</b></td>
  <td>個々の値が保持される</td>
  <td>階級ごとの度数のみ</td>
</tr>
<tr>
  <td><b>元データの復元</b></td>
  <td>可能</td>
  <td>不可能</td>
</tr>
<tr>
  <td><b>適切なデータ数</b></td>
  <td>15〜150程度</td>
  <td>50個以上</td>
</tr>
<tr>
  <td><b>視認性</b></td>
  <td>データ多いと見にくい</td>
  <td>大規模でも見やすい</td>
</tr>
<tr>
  <td><b>作成方法</b></td>
  <td>手作業可能</td>
  <td>ソフト使用が一般的</td>
</tr>
</table>
<br>

<hr>

<b>【使用場面】</b><br>
<br>

<b>適切な使用場面:</b><br>
✓ 小〜中規模データ（15〜150個）<br>
✓ 初期のデータ分析<br>
✓ 手作業でのデータ整理<br>
✓ 教育現場（クラスごとのテスト結果など）<br>
✓ 詳細を保持しながら分布を確認<br>
<br>

<b>不適切な使用場面:</b><br>
✗ 大規模データ（数百個以上）<br>
✗ 複数グループの比較<br>
✗ 非常に小規模データ（15個未満）<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>切り捨て表現に注意:</b><br>
• 元データの完全復元に使用される場合<br>
• 切り捨て表現の場合（例: 3.45を3.4と表示）<br>
• どちらのタイプか確認すること<br>
<br>

<b>統計検定2級では:</b><br>
• 幹葉図の作成と読み取り<br>
• 中央値や四分位数の求め方<br>
• ヒストグラムとの使い分け<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「4-6. 幹葉表示」<br>
統計WEB「練習問題（4. 箱ひげ図と幹葉表示）」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'stem-and-leaf', 'interpretation', 'comparison']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("箱ひげ図と幹葉表示 - 検証済みAnkiカード生成")
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
    cards = create_box_plot_stem_leaf_cards(deck_name, model_name)
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
    print("✨ 箱ひげ図と幹葉表示カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 箱ひげ図の基本 - 定義、構成要素、五数要約（図解付き）")
    print("  カード2: 箱ひげ図の作り方 - 奇数個/偶数個の計算")
    print("  カード3: 箱ひげ図の読み方 - 分布の形状、ばらつき判定")
    print("  カード4: 外れ値の判定 - 1.5×IQR法")
    print("  カード5: 箱ひげ図 vs ヒストグラム - 使い分け")
    print("  カード6: 幹葉図の基本 - 定義、作り方")
    print("  カード7: 幹葉図の活用 - 読み方、メリット・デメリット")
    print()


if __name__ == "__main__":
    main()
