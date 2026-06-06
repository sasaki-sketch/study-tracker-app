#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級 - 標本と抽出法（検証済み）
===================================================
トピック: 母集団と標本、標本抽出法、研究デザイン
検証日: 2026-01-20
出典: 統計WEB、統計検定2級対策教材、複数の統計学サイト
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


def create_cards():
    """標本と抽出法カードを作成"""
    cards = [
    # ===== 母集団と標本 =====
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【母集団と標本】母集団、標本、抽出とは何か？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
<b>母集団</b>: 本来知りたいと思っている集団全体<br>
例: 日本に住む女性全員<br>
<br>
<b>標本</b>: 母集団の情報を推測するために選ばれた一部の集団<br>
例: 調査のために選ばれた1000人の女性<br>
<br>
<b>抽出</b>: 母集団から一部を選んで標本とするプロセス<br>
<br>

<hr>

<b>有限母集団と無限母集団:</b><br>
・<b>有限母集団</b>: 有限の要素からなる母集団（例: 日本在住女性）<br>
・<b>無限母集団</b>: 無限の要素からなる母集団（例: サイコロ投げの結果）<br>
<br>

<b>推測統計学:</b><br>
抽出された標本を用いて、母集団の性質を推測する統計学の分野<br>
↔ 記述統計学: 取得済みデータの特徴を表やグラフで明示<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・母集団と標本は推測統計の最も基本的な概念<br>
・有限母集団では「有限母集団修正」を適用して推定値の偏りを補正<br>
・標本から母集団を推測するには、適切な抽出方法が必要<br>
・統計検定2級では、ほぼ全ての問題の前提知識として重要<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「16-1. 母集団と標本」<br>
・総務省統計局「Data StaRt データ・スタート」<br>
・複数の統計学教材で検証済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'population', 'sample', 'grade2']
    },

    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【調査方法】全数調査と標本調査の違いは？それぞれの長所・短所は？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
<b>全数調査</b>: 調査対象となる母集団を全て調べる方法<br>
例: 国勢調査<br>
<br>
<b>標本調査</b>: 母集団の一部を取り出して調べる方法<br>
例: 工場の抜き取り検査、街頭アンケート<br>
<br>

<hr>

<b>比較表:</b><br>
<table style="border-collapse: collapse; width: 100%;">
<tr style="background-color: #f0f0f0;">
<th style="border: 1px solid #ccc; padding: 8px;"></th>
<th style="border: 1px solid #ccc; padding: 8px;">全数調査</th>
<th style="border: 1px solid #ccc; padding: 8px;">標本調査</th>
</tr>
<tr>
<td style="border: 1px solid #ccc; padding: 8px;"><b>長所</b></td>
<td style="border: 1px solid #ccc; padding: 8px;">正確な情報が得られる</td>
<td style="border: 1px solid #ccc; padding: 8px;">低コスト・短期間で実施可能</td>
</tr>
<tr>
<td style="border: 1px solid #ccc; padding: 8px;"><b>短所</b></td>
<td style="border: 1px solid #ccc; padding: 8px;">時間・費用が膨大</td>
<td style="border: 1px solid #ccc; padding: 8px;">推測値に誤差の可能性</td>
</tr>
</table>
<br>

<hr>

<b>単純無作為抽出:</b><br>
標本調査の基本的な抽出方法で、母集団から「完全に」「ランダムに」標本を抽出します。<br>
誰もが選ばれる確率が等しく、偏りのない推測が可能になります。<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・現実には全数調査は困難なため、標本調査が一般的<br>
・標本調査では適切な抽出方法が重要（偏りを避ける）<br>
・乱数を用いた抽出が基本<br>
・統計検定2級では、調査方法の選択理由が問われる<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「16-2. 全数調査と標本調査」<br>
・統計検定2級対策教材で検証済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'census', 'sample-survey', 'grade2']
    },

    # ===== 標本抽出法 =====
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【層化抽出法】層化抽出法とは？特徴と長所・短所は？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
母集団を複数の層（グループ）に分け、各層から必要な数の調査対象を無作為に抽出する方法<br>
<br>

<b>手順:</b><br>
1. 母集団を性別、年齢、地域などの特性で層に分ける<br>
2. 各層の中から必要な数を無作為に抽出<br>
3. 各層から一部ずつ標本を得る<br>
<br>

<hr>

<b>具体例:</b><br>
全国の高校生を対象とする調査で、都道府県ごとに層を作り、各都道府県から人口比に応じて学生を抽出する。<br>
→ 各都道府県の特徴を反映した標本が得られる<br>
<br>

<hr>

<b>長所:</b><br>
・推定精度が高い（単純無作為抽出より精度向上）<br>
・母集団内の層間比較が可能（年齢別、地域別など）<br>
・各層の特徴を確実に反映できる<br>
<br>

<b>短所:</b><br>
・事前に母集団の構成情報が必要<br>
・層の設定に専門知識が必要<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・<b>各層から一部を抽出</b>する点がクラスター抽出法と異なる<br>
・統計検定2級で最も頻出の抽出方法<br>
・キーワード: 「層」「グループに分けて各グループから」<br>
・比例配分（人口比）と最適配分（層の分散考慮）がある<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「16-3. 標本の抽出方法」<br>
・Qiita「[統計検定2級] 6つの抽出法について」<br>
・複数の統計学教材で検証済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'stratified-sampling', 'grade2']
    },

    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【クラスター抽出法】クラスター抽出法（集落抽出法）とは？層化抽出法との違いは？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>定義:</b><br>
母集団を小集団（クラスター）に分割し、いくつかのクラスターを無作為に選び、選ばれたクラスター内の<b>全員</b>を調査する方法<br>
<br>

<b>手順:</b><br>
1. 母集団をクラスター（小集団）に分ける<br>
2. いくつかのクラスターを無作為に選ぶ<br>
3. 選ばれたクラスター内の<b>全員</b>を標本とする<br>
<br>

<hr>

<b>具体例:</b><br>
全国の小学校を対象とする調査で、学校をクラスターとし、いくつかの学校を無作為に選び、選ばれた学校の<b>全生徒</b>を調査する。<br>
<br>

<hr>

<b>層化抽出法との違い:</b><br>
<table style="border-collapse: collapse; width: 100%;">
<tr style="background-color: #f0f0f0;">
<th style="border: 1px solid #ccc; padding: 8px;"></th>
<th style="border: 1px solid #ccc; padding: 8px;">層化抽出法</th>
<th style="border: 1px solid #ccc; padding: 8px;">クラスター抽出法</th>
</tr>
<tr>
<td style="border: 1px solid #ccc; padding: 8px;"><b>選び方</b></td>
<td style="border: 1px solid #ccc; padding: 8px;"><b>各層から一部</b>を抽出</td>
<td style="border: 1px solid #ccc; padding: 8px;">選ばれたクラスターの<b>全員</b></td>
</tr>
<tr>
<td style="border: 1px solid #ccc; padding: 8px;"><b>精度</b></td>
<td style="border: 1px solid #ccc; padding: 8px;">高い</td>
<td style="border: 1px solid #ccc; padding: 8px;">偏りが生じやすい</td>
</tr>
<tr>
<td style="border: 1px solid #ccc; padding: 8px;"><b>コスト</b></td>
<td style="border: 1px solid #ccc; padding: 8px;">高い</td>
<td style="border: 1px solid #ccc; padding: 8px;">低い（効率的）</td>
</tr>
</table>
<br>

<hr>

<b>長所:</b><br>
・時間と労力を節約できる<br>
・クラスター情報（学校名など）があれば実施しやすい<br>
<br>

<b>短所:</b><br>
・同一クラスター内のメンバーは似た特性を持つため、標本に偏りが生じやすい<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・キーワード: 「クラスター」「選ばれたグループの全員を調査」<br>
・層化抽出法との違いを問う問題が頻出<br>
・統計検定2級では文章からどちらの抽出法かを判定する問題が多い<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「16-3. 標本の抽出方法」<br>
・複数の統計学教材で層化抽出法との違いを検証
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'cluster-sampling', 'grade2']
    },

    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【その他の抽出法】系統抽出法、多段抽出法、二相抽出法とは？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>1. 系統抽出法（Systematic Sampling）:</b><br>
通し番号付き名簿から、最初の対象を無作為選択後、一定間隔で抽出<br>
<br>
例: 100人の名簿から10人を選ぶ場合、1〜10番からランダムに1人（例: 3番）を選び、その後10人ごと（3, 13, 23, ...）を抽出<br>
<br>
・長所: 単純無作為抽出より手間が少ない<br>
・短所: 名簿に周期性があると偏りが生じる<br>
<br>

<hr>

<b>2. 多段抽出法（Multi-stage Sampling）:</b><br>
複数段階にわたって階層的に無作為抽出を繰り返す方法<br>
<br>
例: 全国調査で、①都道府県を抽出 → ②市町村を抽出 → ③学校を抽出 → ④学生を抽出<br>
<br>
・長所: 段階的絞り込みでコスト低減、抽出効率が高い<br>
・短所: 小規模サンプルで偏りのリスク<br>
<br>

<hr>

<b>3. 二相抽出法（Two-phase Sampling）:</b><br>
第一相で母集団情報を取得後、第二相で層化抽出を実施<br>
<br>
例: 第一相で簡単なアンケートを実施し、その結果を元に層を作り、第二相で詳細調査<br>
<br>
・長所: 事前情報がない場合に効率的<br>
・短所: 小規模サンプルで偏りが生じる可能性<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・系統抽出: キーワード「一定間隔」「等間隔」<br>
・多段抽出: キーワード「段階的」「複数段階」<br>
・二相抽出: キーワード「二相」「第一相・第二相」<br>
・統計検定2級では、文章から抽出法を判定する問題が頻出<br>
・層化抽出とクラスター抽出ほど頻出ではないが、知識として重要<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「16-3. 標本の抽出方法」<br>
・Qiita「[統計検定2級] 6つの抽出法について」<br>
・複数の統計学教材で検証済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'systematic-sampling', 'multistage-sampling', 'two-phase-sampling', 'grade2']
    },

    # ===== 研究デザイン =====
    {
        'front': '''
<div style="font-size:24px; padding:20px;">
    <b>【研究デザイン】実験研究と観察研究の違いは？主な研究デザインは？</b>
</div>
''',
        'back': '''
<div style="font-size:20px; padding:20px; line-height:1.8;">

<b>実験研究 vs 観察研究:</b><br>
<br>
<b>実験研究</b>: 対象者に介入（投薬・治療など）を加えて効果を検証<br>
例: 新薬の効果を調べるために、患者に新薬を投与する<br>
<br>
<b>観察研究</b>: 介入を行わず、観察によってデータを集めて解析<br>
例: 喫煙者と非喫煙者の健康状態を比較する<br>
<br>

<hr>

<b>主な研究デザイン:</b><br>
<br>

<b>1. ランダム化比較試験（RCT）</b> - 実験研究<br>
実験群と対照群への割り付けをランダムに行い、介入の効果を調べる<br>
・エビデンスレベル: 最高<br>
・特徴: バイアスを最小化、因果関係を明確に示せる<br>
<br>

<b>2. コホート研究</b> - 観察研究<br>
異なる集団を時間経過で追跡し、特性と疾患発生の関係を調べる<br>
・前向き研究: 現在から未来へ追跡<br>
・統計指標: 相対リスク（RR）<br>
・特徴: 時間軸に沿って因果関係を調べられる<br>
<br>

<b>3. ケースコントロール研究（症例対照研究）</b> - 観察研究<br>
患者群と対照群で過去の特性を比較する後ろ向き研究<br>
・後ろ向き研究: 過去を振り返る<br>
・統計指標: オッズ比（OR）<br>
・特徴: 稀な病気の研究に適している<br>
<br>

<b>4. 横断研究</b> - 観察研究<br>
ある1時点において断面的調査を行い、要因と結果の関連を調べる<br>
・特徴: 過去や未来への調査は含まない<br>
<br>

<hr>

<b>【重要ポイント・注意点】</b><br>
・エビデンスの強さ: RCT > コホート研究 > ケースコントロール研究<br>
・統計検定2級では、研究デザインの違いと適用場面が頻出<br>
・バイアスと因果推論の理解が重要<br>
・前向き vs 後ろ向きの区別を理解する<br>
<br>

<div style="font-size:14px; color:#666; margin-top:20px;">
<b>出典:</b><br>
・統計WEB「16-4. 研究デザイン」<br>
・医学統計学の教材で検証済み<br>
・複数の統計学・疫学教材で検証済み
</div>

</div>
''',
        'tags': ['statistics', 'verified', 'research-design', 'RCT', 'cohort', 'case-control', 'grade2']
    },
    ]

    return cards


def main():
    """メイン実行"""
    print("=" * 70)
    print("統計検定2級 - 標本と抽出法（検証済み）")
    print("=" * 70)
    print()

    # AnkiConnect接続確認
    print("🔌 AnkiConnectに接続中...")
    version = invoke_anki('version')
    if version is None:
        print("❌ Ankiが起動していないか、AnkiConnectがインストールされていません")
        print("   Ankiを起動してから再度実行してください。")
        return

    print(f"✅ AnkiConnect接続成功")
    print()

    # デッキとモデル名
    deck_name = "統計学v2"
    model_name = "Basic"

    # カード作成
    cards = create_cards()
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
                    'allowDuplicate': False
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
    print("✨ 標本と抽出法 カード追加完了!")
    print("=" * 70)
    print()
    print(f"📊 結果:")
    print(f"  ✅ 追加成功: {cards_added}枚")
    print()
    print("=" * 70)
    print("📋 カード内容サマリ:")
    print("=" * 70)
    print("  カード1: 母集団と標本")
    print("  カード2: 全数調査と標本調査")
    print("  カード3: 層化抽出法")
    print("  カード4: クラスター抽出法")
    print("  カード5: その他の抽出法（系統・多段・二相）")
    print("  カード6: 研究デザイン（RCT、コホート、ケースコントロール）")
    print()
    print("【検証情報】")
    print("・統計WEB（bellcurve.jp）で定義と特徴を検証")
    print("・統計検定2級対策教材（Qiita等）で頻出度を確認")
    print("・複数の統計学教材で正確性を確認")
    print("・医学統計学教材で研究デザインを検証")
    print()
    print("【重要度】")
    print("・母集団と標本: ★★★★★（最重要）")
    print("・層化抽出法: ★★★★★（最重要・最頻出）")
    print("・全数調査と標本調査: ★★★★（高重要度）")
    print("・クラスター抽出法: ★★★★（高重要度）")
    print("・研究デザイン: ★★★★（高重要度）")
    print("・その他の抽出法: ★★★（中重要度）")


if __name__ == "__main__":
    main()
