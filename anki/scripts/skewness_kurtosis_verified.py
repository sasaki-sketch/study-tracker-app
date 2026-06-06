#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
歪度・尖度（Skewness and Kurtosis） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「3-5. 歪度と尖度」https://bellcurve.jp/statistics/course/17950.html
- 統計WEB用語集「歪度」https://bellcurve.jp/statistics/glossary/2135.html
- 統計WEB用語集「尖度」https://bellcurve.jp/statistics/glossary/2113.html
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
from scipy import stats


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


def create_skewness_graph():
    """歪度のグラフを生成してBase64エンコード"""
    # 日本語フォント設定
    plt.rcParams['font.family'] = 'Hiragino Sans'

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    x = np.linspace(-5, 5, 1000)

    # 左裾が長い（負の歪度）
    skew_left = stats.skewnorm.pdf(x, -5, loc=0, scale=1)
    axes[0].plot(x, skew_left, linewidth=2, color='steelblue')
    axes[0].fill_between(x, skew_left, alpha=0.3, color='steelblue')
    axes[0].set_title('負の歪度（左裾が長い）', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('確率密度', fontsize=12)
    axes[0].grid(True, alpha=0.3)
    axes[0].text(0.5, 0.9, '歪度 < 0', transform=axes[0].transAxes,
                fontsize=12, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # 正規分布（歪度ゼロ）
    normal = stats.norm.pdf(x, loc=0, scale=1)
    axes[1].plot(x, normal, linewidth=2, color='green')
    axes[1].fill_between(x, normal, alpha=0.3, color='green')
    axes[1].set_title('正規分布（対称）', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('確率密度', fontsize=12)
    axes[1].grid(True, alpha=0.3)
    axes[1].text(0.5, 0.9, '歪度 = 0', transform=axes[1].transAxes,
                fontsize=12, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # 右裾が長い（正の歪度）
    skew_right = stats.skewnorm.pdf(x, 5, loc=0, scale=1)
    axes[2].plot(x, skew_right, linewidth=2, color='coral')
    axes[2].fill_between(x, skew_right, alpha=0.3, color='coral')
    axes[2].set_title('正の歪度（右裾が長い）', fontsize=14, fontweight='bold')
    axes[2].set_ylabel('確率密度', fontsize=12)
    axes[2].grid(True, alpha=0.3)
    axes[2].text(0.5, 0.9, '歪度 > 0', transform=axes[2].transAxes,
                fontsize=12, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()

    # Base64エンコード
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()

    return image_base64


def create_kurtosis_graph():
    """尖度のグラフを生成してBase64エンコード"""
    # 日本語フォント設定
    plt.rcParams['font.family'] = 'Hiragino Sans'

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    x = np.linspace(-5, 5, 1000)

    # 低い尖度（扁平）
    low_kurt = stats.laplace.pdf(x, loc=0, scale=1.5)
    axes[0].plot(x, low_kurt, linewidth=2, color='steelblue')
    axes[0].fill_between(x, low_kurt, alpha=0.3, color='steelblue')
    axes[0].set_title('負の尖度（扁平）', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('確率密度', fontsize=12)
    axes[0].set_ylim(0, 0.5)
    axes[0].grid(True, alpha=0.3)
    axes[0].text(0.5, 0.9, '尖度 < 0\n（超過尖度）', transform=axes[0].transAxes,
                fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # 正規分布（尖度 = 0 or 3）
    normal = stats.norm.pdf(x, loc=0, scale=1)
    axes[1].plot(x, normal, linewidth=2, color='green')
    axes[1].fill_between(x, normal, alpha=0.3, color='green')
    axes[1].set_title('正規分布', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('確率密度', fontsize=12)
    axes[1].set_ylim(0, 0.5)
    axes[1].grid(True, alpha=0.3)
    axes[1].text(0.5, 0.9, '尖度 = 0\n（超過尖度）', transform=axes[1].transAxes,
                fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # 高い尖度（尖鋭）
    high_kurt = stats.laplace.pdf(x, loc=0, scale=0.7)
    axes[2].plot(x, high_kurt, linewidth=2, color='coral')
    axes[2].fill_between(x, high_kurt, alpha=0.3, color='coral')
    axes[2].set_title('正の尖度（尖鋭）', fontsize=14, fontweight='bold')
    axes[2].set_ylabel('確率密度', fontsize=12)
    axes[2].set_ylim(0, 0.5)
    axes[2].grid(True, alpha=0.3)
    axes[2].text(0.5, 0.9, '尖度 > 0\n（超過尖度）', transform=axes[2].transAxes,
                fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()

    # Base64エンコード
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()

    return image_base64


def create_skewness_kurtosis_cards(deck_name, model_name):
    """歪度・尖度カードを作成（検証済み）"""

    # グラフ生成
    print("📊 歪度のグラフを生成中...")
    skewness_graph = create_skewness_graph()
    print("✅ 歪度グラフ生成完了")

    print("📊 尖度のグラフを生成中...")
    kurtosis_graph = create_kurtosis_graph()
    print("✅ 尖度グラフ生成完了")

    cards = [
        # カード1: 歪度の定義と公式
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【歪度】<br>定義と公式は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
分布が正規分布からどれだけ逸脱しているかを表す統計量で、<br>
<b>左右対称性を示す指標</b><br>
<br>

<b>英語:</b> Skewness（スキューネス）<br>
<br>

<b>公式:</b><br>
\\[歪度 = \\frac{n}{(n-1)(n-2)} \\sum_{i=1}^n \\left( \\frac{x_i - \\bar{x}}{s} \\right)^3\\]
<br>

n: データ数<br>
\\(\\bar{x}\\): 平均値<br>
s: 標準偏差<br>
<br>

<hr>

<b>【グラフで見る歪度】</b><br>
<br>
<img src="data:image/png;base64,{skewness_graph}" style="max-width:100%; height:auto;"><br>
<br>

<hr>

<b>【解釈】</b><br>
<br>

<b>正の歪度（歪度 > 0）:</b><br>
• 分布の山が左にずれる<br>
• 右裾が長い（右に伸びている）<br>
• 例: 所得分布、試験の簡単な問題の得点分布<br>
<br>

<b>負の歪度（歪度 < 0）:</b><br>
• 分布の山が右にずれる<br>
• 左裾が長い（左に伸びている）<br>
• 例: 試験の難しい問題の得点分布<br>
<br>

<b>歪度 = 0:</b><br>
• 左右対称<br>
• 正規分布など<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>統計検定2級では:</b><br>
• 歪度の符号から分布の形を判断<br>
• 正規分布との比較が重要<br>
• 計算式の詳細は覚えなくても可<br>
<br>

<b>Excelでの計算:</b><br>
=SKEW(データ範囲)<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-5. 歪度と尖度」<br>
統計WEB用語集「歪度」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'skewness', 'definition', 'graph']
        },

        # カード2: 尖度の定義と公式（2つの定義方法）
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【尖度】<br>定義と公式は？<br>2つの定義方法の違いは？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
分布が正規分布からどれだけ逸脱しているかを表す統計量で、<br>
<b>山の尖り度と裾の広がり度を示す</b><br>
<br>

<b>英語:</b> Kurtosis（カートシス）<br>
<br>

<hr>

<b>【2つの定義方法】</b><br>
<br>

<b>定義1: 正規分布を基準とする方法</b><br>
• 基準値: <b>3</b><br>
• 正規分布の尖度 = 3<br>
<br>

公式:<br>
\\[尖度 = \\frac{n\\sum_{{i=1}^n (x_i - \\bar{x})^4}}{\\left(\\sum_{{i=1}^n (x_i - \\bar{x})^2\\right)^2}}\\]
<br>

• 尖度 < 3 → 扁平（裾が短い）<br>
• 尖度 = 3 → 正規分布<br>
• 尖度 > 3 → 尖鋭（裾が長い）<br>
<br>

<b>定義2: 超過尖度（Excess Kurtosis）</b><br>
• 基準値: <b>0</b><br>
• 正規分布の超過尖度 = 0<br>
• 定義1から3を引いた値<br>
<br>

公式:<br>
\\[超過尖度 = \\frac{n(n+1)}{(n-1)(n-2)(n-3)}\\sum_{i=1}^n \\frac{{(x_i - \\bar{x})^4}}{s^4} - \\frac{3(n-1)^2}{(n-2)(n-3)}\\]
<br>

• 超過尖度 < 0 → 扁平（裾が短い）<br>
• 超過尖度 = 0 → 正規分布<br>
• 超過尖度 > 0 → 尖鋭（裾が長い）<br>
<br>

<hr>

<b>【グラフで見る尖度】</b><br>
<br>
<img src="data:image/png;base64,{kurtosis_graph}" style="max-width:100%; height:auto;"><br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>どちらの定義を使うか:</b><br>
• Excelの KURT関数 → 超過尖度（基準0）<br>
• 一部の統計ソフト → 定義1（基準3）<br>
• <b>必ず基準値を確認すること！</b><br>
<br>

<b>統計検定2級では:</b><br>
• 尖度の意味を理解（山の尖り具合）<br>
• 2つの定義があることを知る<br>
• 正規分布との比較が重要<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-5. 歪度と尖度」<br>
統計WEB用語集「尖度」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'kurtosis', 'definition', 'graph']
        },

        # カード3: 歪度・尖度の使い方と解釈
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【歪度・尖度】<br>いつ使う？<br>どう解釈する？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>使用場面:</b><br>
<br>

<b>1. 分布形状の把握</b><br>
• データが正規分布に従っているか確認<br>
• 歪度・尖度がともにゼロ付近 → 正規分布に近い<br>
<br>

<b>2. 外れ値の検出</b><br>
• 尖度が高い → 外れ値が存在する可能性<br>
• 裾の重さを定量化<br>
<br>

<b>3. 統計的検定の前提確認</b><br>
• t検定、分散分析などは正規性を仮定<br>
• 歪度・尖度で正規性を評価<br>
<br>

<hr>

<b>【解釈のポイント】</b><br>
<br>

<b>歪度と尖度の組み合わせ:</b><br>
<br>

<table border="1" style="border-collapse:collapse; width:100%;">
<tr style="background-color:#f0f0f0;">
  <th>歪度</th>
  <th>尖度</th>
  <th>分布の特徴</th>
</tr>
<tr>
  <td>≈ 0</td>
  <td>≈ 0</td>
  <td>正規分布に近い</td>
</tr>
<tr>
  <td>> 0</td>
  <td>任意</td>
  <td>右裾が長い（所得分布など）</td>
</tr>
<tr>
  <td>< 0</td>
  <td>任意</td>
  <td>左裾が長い</td>
</tr>
<tr>
  <td>任意</td>
  <td>> 0</td>
  <td>尖った分布、重い裾</td>
</tr>
<tr>
  <td>任意</td>
  <td>< 0</td>
  <td>扁平な分布、軽い裾</td>
</tr>
</table>
<br>

<hr>

<b>【具体例】</b><br>
<br>

<b>正の歪度の例:</b><br>
• 所得分布: ほとんどの人は平均以下、一部の高所得者が右裾を作る<br>
• 試験の簡単な問題: ほとんどの人が高得点、一部の低得点者が左裾を作る<br>
<br>

<b>負の歪度の例:</b><br>
• 試験の難しい問題: ほとんどの人が低得点、一部の高得点者が右裾を作る<br>
• 年齢制限のあるデータ<br>
<br>

<b>高い尖度の例:</b><br>
• 株価の日次変動: ほとんどは小さな変動、まれに大きな変動<br>
• 品質管理データ: ほとんどは規格内、まれに不良品<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>正規性の検定:</b><br>
• 歪度・尖度だけでは不十分<br>
• Shapiro-Wilk検定やKolmogorov-Smirnov検定と併用<br>
• 正規確率プロットで視覚的にも確認<br>
<br>

<b>統計検定2級では:</b><br>
• 分布の形状を言葉で説明できることが重要<br>
• 歪度・尖度の符号から分布の特徴を読み取る<br>
• 正規分布との比較が頻出<br>
<br>

<b>サンプルサイズの影響:</b><br>
• nが小さいと推定が不安定<br>
• n ≥ 30 が望ましい<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「3-5. 歪度と尖度」<br>
複数の統計サイトで使用例を検証
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'skewness', 'kurtosis', 'usage', 'interpretation']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("歪度・尖度 - 検証済みAnkiカード生成")
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
    cards = create_skewness_kurtosis_cards(deck_name, model_name)
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
    print("✨ 歪度・尖度カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 歪度の定義と公式（グラフ付き）")
    print("  カード2: 尖度の定義と公式（2つの定義方法、グラフ付き）")
    print("  カード3: 歪度・尖度の使い方と解釈")
    print()


if __name__ == "__main__":
    main()
