#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ギリシャ文字（Greek Letters） - 検証済みAnkiカード
統計検定2級対策

情報源：
- 統計WEB「1-1. ギリシャ文字の読み方」https://bellcurve.jp/statistics/course/1547.html
- 統計WEB「ギリシャ文字による統計記号」https://bellcurve.jp/statistics/blog/14206.html
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


def create_greek_letters_cards(deck_name, model_name):
    """ギリシャ文字カードを作成（検証済み）"""

    cards = [
        # カード1: よく使う小文字のギリシャ文字
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【ギリシャ文字】<br>統計学でよく使う小文字は？<br>読み方と意味は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>統計学で頻出のギリシャ文字（小文字）:</b><br>
<br>

<table border="1" style="border-collapse:collapse; width:100%;">
<tr style="background-color:#f0f0f0;">
  <th>文字</th>
  <th>読み方</th>
  <th>英語</th>
  <th>統計での主な意味</th>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\alpha\\)</td>
  <td>アルファ</td>
  <td>alpha</td>
  <td>有意水準、第1種の過誤の確率、<br>回帰モデルの切片</td>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\beta\\)</td>
  <td>ベータ</td>
  <td>beta</td>
  <td>第2種の過誤の確率、<br>偏回帰係数</td>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\mu\\)</td>
  <td>ミュー</td>
  <td>mu</td>
  <td><b>母平均</b>（population mean）</td>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\sigma\\)</td>
  <td>シグマ</td>
  <td>sigma</td>
  <td><b>母標準偏差</b>、<br>\\(\\sigma^2\\) は母分散</td>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\rho\\)</td>
  <td>ロー</td>
  <td>rho</td>
  <td><b>母相関係数</b>（population correlation）</td>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\chi\\)</td>
  <td>カイ</td>
  <td>chi</td>
  <td>カイ二乗分布（\\(\\chi^2\\)）の検定統計量</td>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\lambda\\)</td>
  <td>ラムダ</td>
  <td>lambda</td>
  <td>ポアソン分布のパラメータ、<br>固有値、ウィルクスのラムダ</td>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\pi\\)</td>
  <td>パイ</td>
  <td>pi</td>
  <td>母比率、円周率（3.14159...）</td>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\theta\\)</td>
  <td>シータ</td>
  <td>theta</td>
  <td>母数（パラメータ）の一般表記</td>
</tr>
</table>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>母集団パラメータ vs 標本統計量:</b><br>
• ギリシャ文字 → <b>母集団</b>のパラメータ<br>
• 英文字（ローマ字）→ <b>標本</b>の統計量<br>
<br>

例:<br>
• μ（母平均）vs \\(\\bar{x}\\)（標本平均）<br>
• σ（母標準偏差）vs s（標本標準偏差）<br>
• ρ（母相関係数）vs r（標本相関係数）<br>
<br>

<b>統計検定2級では:</b><br>
• これらの文字の読み方を知ること<br>
• 母集団と標本の違いを理解すること<br>
• 公式で見たときに意味が分かること<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「1-1. ギリシャ文字の読み方」<br>
統計WEB「ギリシャ文字による統計記号」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'greek-letters', 'lowercase', 'symbols']
        },

        # カード2: 大文字のギリシャ文字と特殊記号
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【ギリシャ文字】<br>大文字と特殊記号は？<br>読み方と意味は？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>大文字のギリシャ文字（統計でよく使う）:</b><br>
<br>

<table border="1" style="border-collapse:collapse; width:100%;">
<tr style="background-color:#f0f0f0;">
  <th>文字</th>
  <th>読み方</th>
  <th>英語</th>
  <th>統計での主な意味</th>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\Sigma\\)</td>
  <td>シグマ</td>
  <td>Sigma</td>
  <td><b>総和</b>（summation）<br>\\(\\sum_{i=1}^n x_i\\) = 合計</td>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\Pi\\)</td>
  <td>パイ</td>
  <td>Pi</td>
  <td><b>総乗</b>（product）<br>\\(\\prod_{i=1}^n x_i\\) = 積</td>
</tr>
<tr>
  <td style="font-size:24px; text-align:center;">\\(\\Delta\\)</td>
  <td>デルタ</td>
  <td>Delta</td>
  <td>差、変化量</td>
</tr>
</table>
<br>

<hr>

<b>【ハット記号（^）の意味】</b><br>
<br>

文字の上に「^」（ハット）が付く場合:<br>
→ <b>推定量</b>を示す<br>
<br>

<table border="1" style="border-collapse:collapse; width:100%;">
<tr style="background-color:#f0f0f0;">
  <th>記号</th>
  <th>読み方</th>
  <th>意味</th>
</tr>
<tr>
  <td style="font-size:20px; text-align:center;">\\(\\hat{\\mu}\\)</td>
  <td>ミューハット</td>
  <td>母平均の推定値（= 標本平均 \\(\\bar{x}\\)）</td>
</tr>
<tr>
  <td style="font-size:20px; text-align:center;">\\(\\hat{\\sigma}\\)</td>
  <td>シグマハット</td>
  <td>母標準偏差の推定値</td>
</tr>
<tr>
  <td style="font-size:20px; text-align:center;">\\(\\hat{\\beta}\\)</td>
  <td>ベータハット</td>
  <td>回帰係数の推定値</td>
</tr>
<tr>
  <td style="font-size:20px; text-align:center;">\\(\\hat{y}\\)</td>
  <td>yハット</td>
  <td>yの予測値（回帰分析）</td>
</tr>
</table>
<br>

<hr>

<b>【バー記号（¯）の意味】</b><br>
<br>

文字の上に「¯」（バー）が付く場合:<br>
→ <b>平均</b>を示す<br>
<br>

例:<br>
• \\(\\bar{x}\\)（xバー）= 標本平均<br>
• \\(\\bar{y}\\)（yバー）= yの標本平均<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>Σ（シグマ）の使い方:</b><br>
\\[\\sum_{i=1}^n x_i = x_1 + x_2 + \\cdots + x_n\\]
<br>

• i = 1 から n まで、xi を全て足す<br>
• 統計で最も頻繁に使う記号<br>
<br>

<b>Π（パイ）の使い方:</b><br>
\\[\\prod_{i=1}^n x_i = x_1 \\times x_2 \\times \\cdots \\times x_n\\]
<br>

• i = 1 から n まで、xi を全て掛ける<br>
• 幾何平均や確率の計算で使用<br>
<br>

<b>統計検定2級では:</b><br>
• Σ記号の読み方と計算が重要<br>
• ハット記号は「推定値」を意味<br>
• バー記号は「平均」を意味<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「1-1. ギリシャ文字の読み方」<br>
統計WEB「ギリシャ文字による統計記号」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'greek-letters', 'uppercase', 'hat', 'bar', 'sigma']
        },

        # カード3: ギリシャ文字の覚え方と使い分け
        {
            'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【ギリシャ文字】<br>覚え方と使い分けのコツは？</b>
</div>
''',
            'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>ギリシャ文字の覚え方:</b><br>
<br>

<b>【頻出度別】</b><br>
<br>

<b>★★★ 超重要（必須）:</b><br>
• \\(\\mu\\)（ミュー）- 母平均<br>
• \\(\\sigma\\)（シグマ）- 母標準偏差<br>
• \\(\\alpha\\)（アルファ）- 有意水準<br>
• \\(\\Sigma\\)（大文字シグマ）- 総和<br>
<br>

<b>★★ 重要:</b><br>
• \\(\\rho\\)（ロー）- 母相関係数<br>
• \\(\\chi^2\\)（カイ二乗）- カイ二乗検定<br>
• \\(\\beta\\)（ベータ）- 回帰係数<br>
<br>

<b>★ 知っておくと良い:</b><br>
• \\(\\lambda\\)（ラムダ）- ポアソン分布<br>
• \\(\\theta\\)（シータ）- パラメータ一般<br>
• \\(\\pi\\)（パイ）- 母比率、円周率<br>
<br>

<hr>

<b>【使い分けのコツ】</b><br>
<br>

<b>母集団 vs 標本:</b><br>
<br>

| 概念 | 母集団（全体）| 標本（一部）|<br>
|------|--------------|------------|<br>
| 平均 | \\(\\mu\\)（ミュー）| \\(\\bar{x}\\)（xバー）|<br>
| 標準偏差 | \\(\\sigma\\)（シグマ）| s |<br>
| 分散 | \\(\\sigma^2\\)（シグマ二乗）| \\(s^2\\) |<br>
| 相関係数 | \\(\\rho\\)（ロー）| r |<br>
| 比率 | \\(\\pi\\)（パイ）| p |<br>
<br>

<b>ルール:</b><br>
• ギリシャ文字 = 母集団のパラメータ（真の値、未知）<br>
• 英文字 = 標本統計量（計算で求める値）<br>
<br>

<hr>

<b>【ギリシャ文字アルファベット順】</b><br>
<br>

よく使う順（統計学）:<br>
1. α（アルファ）<br>
2. β（ベータ）<br>
3. γ（ガンマ）<br>
4. δ（デルタ）<br>
5. ε（イプシロン）<br>
6. θ（シータ）<br>
7. λ（ラムダ）<br>
8. μ（ミュー）<br>
9. π（パイ）<br>
10. ρ（ロー）<br>
11. σ（シグマ）<br>
12. χ（カイ）<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
<br>

<b>文脈で意味が変わる:</b><br>
• 同じギリシャ文字でも分野で意味が違う<br>
• 例: π = 円周率 or 母比率<br>
• 例: λ = ポアソン分布のパラメータ or 固有値<br>
<br>

<b>大文字・小文字の違い:</b><br>
• Σ（大文字）= 総和<br>
• σ（小文字）= 標準偏差<br>
• 全く異なる意味なので注意！<br>
<br>

<b>統計検定2級では:</b><br>
• 公式に出てくる記号の意味を理解<br>
• μ, σ, α, Σ は絶対に覚える<br>
• 母集団と標本の記号を区別<br>
• 問題文を読めば文脈で判断できる<br>
<br>

<b>覚え方のヒント:</b><br>
• α（アルファ）→ 「ある程度」→ 有意水準（5%など）<br>
• μ（ミュー）→ meanのm → 平均<br>
• σ（シグマ）→ standardのs → 標準偏差<br>
• ρ（ロー）→ relationのr → 相関<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
統計WEB「1-1. ギリシャ文字の読み方」<br>
統計WEB「ギリシャ文字による統計記号」<br>
複数のソースで検証済み
</div>

</div>
''',
            'tags': ['statistics', 'verified', 'greek-letters', 'memorization', 'tips']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("ギリシャ文字 - 検証済みAnkiカード生成")
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
    cards = create_greek_letters_cards(deck_name, model_name)
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
    print("✨ ギリシャ文字カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: よく使う小文字のギリシャ文字（一覧表）")
    print("  カード2: 大文字のギリシャ文字と特殊記号（Σ, ^, ¯）")
    print("  カード3: ギリシャ文字の覚え方と使い分けのコツ")
    print()


if __name__ == "__main__":
    main()
