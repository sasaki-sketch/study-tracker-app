#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
度数分布・累積度数分布・スタージェス公式・幹葉表示 - シンプル版
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


def create_distribution_cards(deck_name, model_name):
    """度数分布カードを作成（シンプル版）"""

    cards = [
        # カード1: 度数分布表の5つの要素
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【度数分布表】の<br>5つの要素とは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>1. 階級（Class）</b><br>
• データを集計するための区間<br>
• 例: 0〜50未満、50〜100未満<br>
<br>
<b>2. 階級値（Class value）</b><br>
• その階級を代表する値<br>
• 階級の真ん中の値<br>
• 例: 0〜50未満 → 階級値25<br>
<br>
<b>3. 度数（Frequency）</b><br>
• 各階級に含まれるデータ数<br>
<br>
<b>4. 相対度数（Relative frequency）</b><br>
• 各階級の度数が全体に占める割合<br>
• 計算: 度数 ÷ 全データ数<br>
<br>
<b>5. 累積相対度数</b><br>
• その階級までの相対度数の合計<br>
• 最終値は必ず1.0000
</div>''',
            'tags': ['distribution', 'frequency']
        },

        # カード2: 度数分布とヒストグラム
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【度数分布表】と<br>【ヒストグラム】の関係は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>度数分布表:</b><br>
• データを階級ごとに表形式でまとめたもの<br>
<br>
<b>ヒストグラム:</b><br>
• 度数分布表をグラフ化したもの<br>
• 横軸: 階級<br>
• 縦軸: 度数<br>
<br>
<hr>
<b>メリット:</b><br>
• データの分布を視覚的に理解できる<br>
• ばらつきや偏りが一目でわかる<br>
<br>
<hr>
<b>注意点:</b><br>
• 階級幅が異なる場合は【度数密度】を使う<br>
• 度数密度 = 度数 ÷ 階級幅
</div>''',
            'tags': ['distribution', 'histogram']
        },

        # カード3: スタージェスの公式
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【スタージェスの公式】とは?<br>何に使う?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
ヒストグラムの階級数を決めるための公式<br>
<br>
<b>公式:</b><br>
k = 1 + log₂ n<br>
<br>
k = 階級数<br>
n = データ数<br>
<br>
<hr>
<b>別の表記:</b><br>
k = 1 + 3.3 × log₁₀ n<br>
<br>
<hr>
<b>具体例:</b><br>
データ数が50個の場合<br>
<br>
k = 1 + log₂ 50<br>
  = 1 + 5.64<br>
  ≈ 6.64<br>
  → <b>階級数は7</b>（小数点以下切り上げ）<br>
<br>
<hr>
<b>重要:</b><br>
• あくまで【目安】であり、絶対ではない<br>
• データの性質によって調整してOK
</div>''',
            'tags': ['distribution', 'sturges']
        },

        # カード4: スタージェスの公式の計算
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>スタージェスの公式で<br>log₂が計算できない場合は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>方法1: 常用対数（log₁₀）を使う</b><br>
<br>
log₂ n = log₁₀ n ÷ log₁₀ 2<br>
<br>
log₁₀ 2 ≈ 0.301<br>
<br>
よって:<br>
log₂ n ≈ log₁₀ n ÷ 0.301<br>
     ≈ 3.32 × log₁₀ n<br>
<br>
<hr>
<b>方法2: 公式を変換</b><br>
<br>
k = 1 + log₂ n<br>
  = 1 + 3.3 × log₁₀ n<br>
<br>
<hr>
<b>具体例: n = 50の場合</b><br>
<br>
log₁₀ 50 ≈ 1.699<br>
<br>
k = 1 + 3.3 × 1.699<br>
  = 1 + 5.61<br>
  ≈ 6.61<br>
  → <b>階級数は7</b>
</div>''',
            'tags': ['distribution', 'sturges', 'calculation']
        },

        # カード5: 累積度数分布
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【累積度数分布】とは?<br>何に使う?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
その階級までの度数の累積合計<br>
<br>
<hr>
<b>累積相対度数:</b><br>
その階級までの相対度数の合計<br>
最終値は必ず1.0000（100%）<br>
<br>
<hr>
<b>用途:</b><br>
• 中央値の推定<br>
• パーセンタイルの計算<br>
• 「〜以下」のデータが何%かを知る<br>
<br>
<hr>
<b>具体例:</b><br>
累積相対度数が0.50となる階級<br>
→ その階級に中央値が含まれる<br>
<br>
<hr>
<b>グラフ:</b><br>
• 累積度数折れ線グラフ<br>
• オジーブ（累積度数曲線）
</div>''',
            'tags': ['distribution', 'cumulative']
        },

        # カード6: 幹葉表示（基本）
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>【幹葉表示】<br>（Stem-and-Leaf Plot）とは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>定義:</b><br>
データの値そのものを用いて作成する<br>
ヒストグラムに似た図<br>
<br>
<hr>
<b>構造:</b><br>
• <b>幹（Stem）:</b> 上位の桁（十の位など）<br>
• <b>葉（Leaf）:</b> 下位の桁（一の位など）<br>
<br>
<hr>
<b>例: 27, 30, 33, 33, 37, 41, 45</b><br>
<br>
幹 | 葉<br>
---+------<br>
 2 | 7<br>
 3 | 0 3 3 7<br>
 4 | 1 5<br>
<br>
<hr>
<b>読み方:</b><br>
• 2|7 → 27<br>
• 3|0 3 3 7 → 30, 33, 33, 37<br>
• 4|1 5 → 41, 45
</div>''',
            'tags': ['distribution', 'stem-leaf']
        },

        # カード7: 幹葉表示のメリット
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>幹葉表示の<br>メリットは?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【メリット1】個別データを保持</b><br>
• ヒストグラムと違い、元のデータ値が残る<br>
• データの詳細情報が失われない<br>
<br>
<b>【メリット2】分布形状の把握</b><br>
• データの分布パターンを視覚的に理解できる<br>
• 偏りや外れ値が一目でわかる<br>
<br>
<b>【メリット3】統計量の抽出</b><br>
• 中央値を直接読み取れる<br>
• 四分位数も簡単に計算できる<br>
<br>
<hr>
<b>【デメリット】</b><br>
• データ数が多いと見づらい<br>
• 100個以上のデータには不向き<br>
<br>
<hr>
<b>【統計検定での注意】</b><br>
• データ数が少ない（20〜50個程度）<br>
• 簡単に作成できる問題が出題される
</div>''',
            'tags': ['distribution', 'stem-leaf', 'benefits']
        },

        # カード8: 幹葉表示の作成手順
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>幹葉表示の作成手順は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>ステップ1: 幹の決定</b><br>
• 上位の桁を幹にする<br>
• 通常は十の位<br>
<br>
<b>ステップ2: 幹を縦に並べる</b><br>
• 小さい順に上から下へ<br>
<br>
<b>ステップ3: 葉を追加</b><br>
• 各データの下位の桁を横に並べる<br>
• 小さい順に左から右へ<br>
<br>
<hr>
<b>具体例: 64, 73, 63, 68, 44</b><br>
<br>
<b>手順:</b><br>
1. 幹: 4, 6, 7<br>
2. データを分類:<br>
   • 4台: 44<br>
   • 6台: 64, 63, 68<br>
   • 7台: 73<br>
3. 葉を小さい順に:<br>
<br>
幹 | 葉<br>
---+------<br>
 4 | 4<br>
 6 | 3 4 8<br>
 7 | 3
</div>''',
            'tags': ['distribution', 'stem-leaf', 'how-to']
        },

        # カード9: 中央値を累積度数から求める
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>累積度数分布から<br>中央値を求める方法は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>ステップ1: 累積相対度数が0.5となる階級を見つける</b><br>
<br>
データ数がn個の場合<br>
→ n/2番目のデータが含まれる階級<br>
<br>
<hr>
<b>ステップ2: その階級の階級値が中央値の推定値</b><br>
<br>
<hr>
<b>具体例:</b><br>
データ数50個、階級0〜50, 50〜100, ...<br>
<br>
累積度数:<br>
0〜50: 20個（累積相対度数0.4）<br>
50〜100: 35個（累積相対度数0.7）<br>
<br>
→ 50/2 = 25番目は50〜100の階級<br>
→ 中央値の推定値 = <b>階級値75</b><br>
<br>
<hr>
<b>より正確な計算:</b><br>
線形補間を使って階級内の位置を推定
</div>''',
            'tags': ['distribution', 'median', 'practice']
        },

        # カード10: 度数分布の注意点
        {
            'front': '<div style="font-size:24px; padding:20px;"><b>度数分布表作成時の<br>注意点は?</b></div>',
            'back': '''<div style="font-size:20px; padding:20px; line-height:1.8;">
<b>【注意1】階級幅</b><br>
• 等間隔が原則<br>
• 異なる場合は度数密度を使う<br>
<br>
<b>【注意2】階級数</b><br>
• 多すぎ → データが分散して見づらい<br>
• 少なすぎ → 分布の特徴が見えない<br>
• 目安: スタージェスの公式<br>
<br>
<b>【注意3】階級の境界</b><br>
• 0〜50、50〜100のように書く<br>
• 「以上〜未満」を明確に<br>
<br>
<b>【注意4】データの範囲</b><br>
• すべてのデータが含まれるように<br>
• 最小値〜最大値をカバー<br>
<br>
<hr>
<b>【統計検定のポイント】</b><br>
• 階級値 = 階級の中央値<br>
• 相対度数の合計 = 1.0000<br>
• 累積相対度数は単調増加
</div>''',
            'tags': ['distribution', 'tips']
        }
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("度数分布・スタージェス・幹葉表示 - シンプル版カード生成")
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
    cards = create_distribution_cards(deck_name, model_name)
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
    print("✨ 度数分布カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()


if __name__ == "__main__":
    main()
