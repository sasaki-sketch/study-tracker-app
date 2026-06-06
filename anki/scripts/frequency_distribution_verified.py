#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
度数分布（Frequency Distribution） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「度数分布と累積度数分布」https://bellcurve.jp/statistics/course/1625.html
- 統計WEB「ヒストグラム」https://bellcurve.jp/statistics/course/1639.html
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


def create_histogram_graph():
    """ヒストグラムのグラフを生成してBase64エンコード"""
    # 日本語フォント設定
    plt.rcParams['font.family'] = 'Hiragino Sans'

    # サンプルデータ（試験の点数を想定）
    data = [45, 52, 58, 63, 67, 68, 70, 72, 73, 75,
            76, 78, 79, 80, 81, 82, 83, 84, 85, 86,
            87, 88, 89, 90, 91, 92, 93, 94, 95, 98]

    # 階級の設定
    bins = [40, 50, 60, 70, 80, 90, 100]
    bin_labels = ['40-50', '50-60', '60-70', '70-80', '80-90', '90-100']

    # グラフ作成
    fig, ax = plt.subplots(figsize=(10, 6))

    # ヒストグラム
    n, bins_edge, patches = ax.hist(data, bins=bins, edgecolor='black',
                                      alpha=0.7, color='steelblue')

    # 軸とラベル
    ax.set_xlabel('点数（階級）', fontsize=14)
    ax.set_ylabel('度数（人数）', fontsize=14)
    ax.set_title('試験の点数分布（ヒストグラム）', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')

    # x軸の目盛り
    ax.set_xticks(bins)

    # 各階級の度数を表示
    for i, (count, x) in enumerate(zip(n, bins[:-1])):
        if count > 0:
            ax.text(x + 5, count + 0.3, f'{int(count)}人',
                   ha='center', fontsize=11, fontweight='bold')

    plt.tight_layout()

    # Base64エンコード
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()

    return image_base64


def create_frequency_distribution_cards(deck_name, model_name):
    """度数分布カードを作成（検証済み）"""

    # グラフ生成
    print("📊 ヒストグラムのグラフを生成中...")
    histogram_graph = create_histogram_graph()
    print("✅ グラフ生成完了")

    cards = [
        # カード1: 度数分布の基本概念
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【度数分布】<br>基本用語の定義は？</b><br>
    <br>
    階級、階級値、度数、<br>
    相対度数、累積度数
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>度数分布とは:</b><br>
データをある幅ごとに区切り、<br>
各区間に含まれるデータの個数を示す方法<br>
<br>

<hr>

<b>【基本用語】</b><br>
<br>

<b>階級（かいきゅう）:</b><br>
• データを集計するための区間<br>
• 例: 「0以上50未満」「50以上100未満」<br>
<br>

<b>階級値:</b><br>
• その階級を代表する値<br>
• <b>階級の真ん中の値</b><br>
• 例: 「0以上50未満」の階級値 = 25<br>
• 計算: (0 + 50) / 2 = 25<br>
<br>

<b>度数:</b><br>
• 各階級に含まれるデータ数<br>
• 例: 「0以上50未満」に5個のデータ → 度数 = 5<br>
<br>

<b>相対度数:</b><br>
• 各階級の度数が全体に占める割合<br>
\\[相対度数 = \\frac{その階級の度数}{全体のデータ数}\\]
<br>

<b>累積度数:</b><br>
• その階級までの度数の合計<br>
• 最初の階級から順に足し上げていく<br>
<br>

<b>累積相対度数:</b><br>
• その階級までの相対度数の合計<br>
• 最後の階級では1.0（100%）になる<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>階級の幅:</b><br>
• スタージェスの公式で階級数を決定<br>
• 階級幅 = (最大値 - 最小値) / 階級数<br>
<br>

<b>統計検定2級では:</b><br>
• 度数分布表から平均値を計算<br>
• 相対度数・累積度数の計算<br>
• ヒストグラムの読み取り<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「2-1. 度数分布と累積度数分布」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'frequency-distribution', 'definition']
        },

        # カード2: 度数分布表の作り方とヒストグラム
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【度数分布とヒストグラム】<br>度数分布表の作り方と<br>ヒストグラムとは？</b>
</div>
''',
            'back': f'''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>度数分布表の作り方:</b><br>
<br>

<b>ステップ1: 階級数を決定</b><br>
スタージェスの公式: k = 1 + log₂ n<br>
<br>

<b>ステップ2: 階級幅を計算</b><br>
h = (最大値 - 最小値) / 階級数<br>
<br>

<b>ステップ3: 階級を設定</b><br>
最小値から階級幅ずつ区切る<br>
<br>

<b>ステップ4: 度数を数える</b><br>
各階級に含まれるデータ数を集計<br>
<br>

<hr>

<b>ヒストグラム:</b><br>
<br>

<b>定義:</b><br>
度数分布表をグラフ化したもの<br>
<br>

• <b>横軸</b>: 階級<br>
• <b>縦軸</b>: 度数<br>
• <b>特徴</b>: 柱と柱の間に隙間がない<br>
<br>

<b>グラフ例:</b><br>
<img src="data:image/png;base64,{histogram_graph}" style="max-width:100%; height:auto;"><br>
<br>

<hr>

<b>【ヒストグラムの見方】</b><br>
<br>

<b>分布の形状:</b><br>
• <b>右裾が長い</b>: 山が左に偏り、右になだらか<br>
• <b>左裾が長い</b>: 山が右に偏り、左になだらか<br>
• <b>左右対称</b>: 山が中央にある<br>
<br>

<b>棒グラフとの違い:</b><br>
• ヒストグラム: 量的データ専用、隙間なし<br>
• 棒グラフ: 質的データも可、隙間あり<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>統計検定2級では:</b><br>
• ヒストグラムから分布の特徴を読み取る<br>
• データの偏り（歪度）を判断<br>
• 累積相対度数の折れ線を重ねる問題<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「2-2. ヒストグラム」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'frequency-distribution', 'histogram', 'graph']
        },

        # カード3: 相対度数と累積度数の計算
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【度数分布】<br>計算例</b><br>
    <br>
    以下の度数分布表から<br>
    相対度数と累積度数を計算
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>問題:</b><br>
<br>

| 階級 | 度数 |
|------|------|
| 0-10 | 2 |
| 10-20 | 5 |
| 20-30 | 8 |
| 30-40 | 3 |
| 40-50 | 2 |
| 合計 | 20 |
<br>

<hr>

<b>解答:</b><br>
<br>

<b>ステップ1: 相対度数を計算</b><br>
相対度数 = 各階級の度数 / 全体のデータ数<br>
<br>

| 階級 | 度数 | 相対度数 |
|------|------|----------|
| 0-10 | 2 | 2/20 = 0.10 |
| 10-20 | 5 | 5/20 = 0.25 |
| 20-30 | 8 | 8/20 = 0.40 |
| 30-40 | 3 | 3/20 = 0.15 |
| 40-50 | 2 | 2/20 = 0.10 |
| 合計 | 20 | 1.00 |
<br>

<b>ステップ2: 累積度数を計算</b><br>
累積度数 = その階級までの度数の合計<br>
<br>

| 階級 | 度数 | 累積度数 |
|------|------|----------|
| 0-10 | 2 | 2 |
| 10-20 | 5 | 2+5 = 7 |
| 20-30 | 8 | 7+8 = 15 |
| 30-40 | 3 | 15+3 = 18 |
| 40-50 | 2 | 18+2 = 20 |
<br>

<b>ステップ3: 累積相対度数を計算</b><br>
累積相対度数 = その階級までの相対度数の合計<br>
<br>

| 階級 | 相対度数 | 累積相対度数 |
|------|----------|--------------|
| 0-10 | 0.10 | 0.10 |
| 10-20 | 0.25 | 0.10+0.25 = 0.35 |
| 20-30 | 0.40 | 0.35+0.40 = 0.75 |
| 30-40 | 0.15 | 0.75+0.15 = 0.90 |
| 40-50 | 0.10 | 0.90+0.10 = 1.00 |
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>検算:</b><br>
• 相対度数の合計 = 1.00<br>
• 累積度数の最後 = 全体のデータ数<br>
• 累積相対度数の最後 = 1.00<br>
<br>

<b>度数分布表からの平均値:</b><br>
\\[\\bar{x} = \\frac{\\sum (階級値 \\times 度数)}{全体のデータ数}\\]
<br>

例:<br>
\\[\\bar{x} = \\frac{5 \\times 2 + 15 \\times 5 + 25 \\times 8 + 35 \\times 3 + 45 \\times 2}{20}\\]
\\[= \\frac{10 + 75 + 200 + 105 + 90}{20} = \\frac{480}{20} = 24\\]
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「2-1. 度数分布と累積度数分布」<br>
計算結果を検算して検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'frequency-distribution', 'calculation', 'example']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("度数分布 - 検証済みAnkiカード生成")
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
    cards = create_frequency_distribution_cards(deck_name, model_name)
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
    print("✨ 度数分布カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 度数分布の基本概念（用語の定義）")
    print("  カード2: 度数分布表の作り方とヒストグラム（グラフ付き）")
    print("  カード3: 相対度数と累積度数の計算")
    print()


if __name__ == "__main__":
    main()
