#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統計検定2級対策：標本と抽出法
出典：統計学の時間 | 統計WEB (https://bellcurve.jp/)
      総務省統計局 (https://www.stat.go.jp/)
"""

import genanki
import random

# デッキIDとモデルIDを生成
DECK_ID = random.randrange(1 << 30, 1 << 31)
MODEL_ID = random.randrange(1 << 30, 1 << 31)

# Ankiモデルの定義
model = genanki.Model(
    MODEL_ID,
    '統計検定2級モデル',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div style="font-size: 20px; text-align: center;">{{Question}}</div>',
            'afmt': '''
                <div style="font-size: 20px; text-align: center;">{{Question}}</div>
                <hr id="answer">
                <div style="font-size: 18px;">{{Answer}}</div>
            ''',
        },
    ],
    css='''
        .card {
            font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro W3", Meiryo, メイリオ, Osaka, "MS PGothic", arial, helvetica, sans-serif;
            text-align: left;
            color: black;
            background-color: white;
            padding: 20px;
        }
        .mjx-math {
            font-size: 1.2em;
        }
    '''
)

# デッキの作成
deck = genanki.Deck(DECK_ID, '統計検定2級::標本と抽出法')

# カード1: 母集団と標本の定義
note1 = genanki.Note(
    model=model,
    fields=[
        '母集団（Population）と標本（Sample）の定義を説明してください。',
        '''<b>母集団（Population）</b><br>
本来知りたいと思っている調査対象の集団全体のこと。<br><br>

<b>例</b>：日本に住む女性全員の平均身長を調べる場合、日本全国の女性全体が母集団<br><br>

<b>標本（Sample）</b><br>
母集団の情報を推測するために選ばれた一部の集団のこと。<br><br>

<b>抽出（Sampling）</b><br>
母集団から一部を選んで標本とすることを「抽出」という。<br><br>

<b>母集団の種類</b><br>
・<b>有限母集団</b>：要素数が限定される（例：日本の女性）<br>
・<b>無限母集団</b>：無限に繰り返される現象（例：サイコロの試行）<br><br>

<small>出典：統計WEB「母集団と標本」</small>'''
    ]
)
deck.add_note(note1)

# カード2: 全数調査と標本調査の比較
note2 = genanki.Note(
    model=model,
    fields=[
        '全数調査と標本調査の違い、メリット・デメリットを説明してください。',
        '''<b>全数調査（悉皆調査）</b><br>
調査対象となる母集団を全て調べること。<br><br>

<b>メリット</b>：<br>
・母集団全体を把握でき、推測誤差がない<br>
・正確な結果が得られる<br><br>

<b>デメリット</b>：<br>
・時間と費用が莫大にかかる<br>
・実務的に困難な場合が多い<br><br>

<b>例</b>：国勢調査<br><br>

<hr>

<b>標本調査（サンプル調査）</b><br>
調査対象となる母集団の一部を取り出して調べること。<br><br>

<b>メリット</b>：<br>
・効率的で現実的<br>
・コスト削減が可能<br>
・時間がかからない<br><br>

<b>デメリット</b>：<br>
・標本誤差が生じる<br>
・抽出方法に偏りがあると正確な推測ができない<br><br>

<b>例</b>：工場での抜き取り検査、街頭アンケート<br><br>

<small>出典：統計WEB「全数調査と標本調査」、総務省統計局</small>'''
    ]
)
deck.add_note(note2)

# カード3: 単純無作為抽出法
note3 = genanki.Note(
    model=model,
    fields=[
        '単純無作為抽出法（Simple Random Sampling）とは何ですか？',
        '''<b>定義</b><br>
母集団から「完全に」・「ランダムに」標本を抽出する最も基本的な方法。<br>
すべての要素が等しい確率で選ばれることを保証する。<br><br>

<b>特徴</b><br>
・最も基本的な抽出方法<br>
・母集団の各要素が等確率で選ばれる<br>
・無作為抽出の原則に最も忠実<br><br>

<b>方法</b><br>
・<b>復元抽出法</b>：抽出後、標本を母集団に戻す<br>
・<b>非復元抽出法</b>：抽出後、標本は戻さない<br><br>

<b>メリット</b><br>
・偏りのない標本が得られる<br>
・統計的な理論に基づいた推測が可能<br><br>

<b>デメリット</b><br>
・母集団の情報を事前に完全に把握する必要がある<br><br>

<small>出典：統計WEB「標本の抽出方法」、総務省統計局</small>'''
    ]
)
deck.add_note(note3)

# カード4: 層化抽出法
note4 = genanki.Note(
    model=model,
    fields=[
        '層化抽出法（層別抽出法、Stratified Sampling）とは何ですか？',
        '''<b>定義</b><br>
母集団を事前にいくつかの層（グループ）に分割し、各層の中から必要な数の調査対象を無作為に抽出する方法。<br><br>

<b>特徴</b><br>
・比例配分法により、層の大きさに応じた配分が可能<br>
・各層の特性を反映した標本が得られる<br><br>

<b>メリット</b><br>
・推定精度が高まる<br>
・母集団内の情報（年齢別、性別など）の比較が可能<br>
・層ごとの分析ができる<br><br>

<b>デメリット</b><br>
・母集団の構成情報を事前に把握する必要がある<br>
・層の分け方によって結果が変わる可能性がある<br><br>

<b>具体例</b><br>
ある大学で学生の意識調査を行う場合、1年生・2年生・3年生・4年生という層に分けて、各学年から同じ割合で学生を無作為抽出する。<br><br>

<small>出典：統計WEB「標本の抽出方法」</small>'''
    ]
)
deck.add_note(note4)

# カード5: 集落抽出法
note5 = genanki.Note(
    model=model,
    fields=[
        '集落抽出法（クラスター抽出法、Cluster Sampling）とは何ですか？',
        '''<b>定義</b><br>
母集団を小集団（クラスター）に分割し、そこから無作為抽出したクラスターについて全数調査を実施する方法。<br><br>

<b>特徴</b><br>
・クラスター単位で抽出を行う<br>
・選ばれたクラスター内は全数調査<br><br>

<b>メリット</b><br>
・調査が効率的に実施できる<br>
・コストを抑えられる<br>
・地理的に分散している場合に有効<br><br>

<b>デメリット</b><br>
・同一クラスター内の対象は似た性質を持つため、標本に偏りが生じるリスクがある<br>
・クラスター間のばらつきが大きいと精度が低下する<br><br>

<b>具体例</b><br>
全国の小学校を対象とした調査で、学校をクラスターとして一部の学校を無作為に選び、選ばれた学校の全児童を調査する。<br><br>

<small>出典：統計WEB「標本の抽出方法」</small>'''
    ]
)
deck.add_note(note5)

# カード6: 系統抽出法
note6 = genanki.Note(
    model=model,
    fields=[
        '系統抽出法（Systematic Sampling）とは何ですか？',
        '''<b>定義</b><br>
通し番号をつけた名簿を作成し、1番目の調査対象を無作為に選び、2番目以降の調査対象を一定の間隔で抽出する方法。<br><br>

<b>特徴</b><br>
・一定間隔（k番目ごと）に系統的に抽出<br>
・スタート番号は無作為に選択<br><br>

<b>抽出間隔の計算</b><br>
抽出間隔 k = 母集団の大きさ N ÷ 標本の大きさ n<br><br>

<b>メリット</b><br>
・実施が簡単で手間が削減できる<br>
・乱数発生器が使えない状況でも人力で実施可能<br>
・母集団全体に均等に分散した標本が得られる<br><br>

<b>デメリット</b><br>
・名簿に周期性がある場合、偏りが生じるリスクがある<br>
・特定のパターンと抽出間隔が一致すると問題が発生<br><br>

<b>具体例</b><br>
1000人の名簿から100人を抽出する場合、k=10として、最初に1〜10の中から無作為に番号（例：3）を選び、その後13、23、33...と10番目ごとに抽出する。<br><br>

<small>出典：統計WEB「標本の抽出方法」、総務省統計局</small>'''
    ]
)
deck.add_note(note6)

# カード7: 多段抽出法
note7 = genanki.Note(
    model=model,
    fields=[
        '多段抽出法（Multistage Sampling）とは何ですか？',
        '''<b>定義</b><br>
グループの段階的な無作為抽出を繰り返し、最終段階で個別の調査対象を抽出する手法。<br><br>

<b>特徴</b><br>
・複数の段階（段）に分けて抽出を行う<br>
・各段階で無作為抽出を実施<br><br>

<b>メリット</b><br>
・コストを低く抑えられる<br>
・大規模な調査に適している<br>
・実務的に効率が良い<br><br>

<b>デメリット</b><br>
・サンプルサイズが小さい場合は偏りが生じる可能性がある<br>
・段数が多くなるごとに精度の低下につながりやすい<br><br>

<b>具体例</b><br>
全国調査の場合：<br>
第1段：都道府県を無作為抽出<br>
第2段：選ばれた都道府県内の市区町村を無作為抽出<br>
第3段：選ばれた市区町村内の個人を無作為抽出<br><br>

<small>出典：統計WEB「標本の抽出方法」</small>'''
    ]
)
deck.add_note(note7)

# カード8: 二相抽出法
note8 = genanki.Note(
    model=model,
    fields=[
        '二相抽出法（Two-phase Sampling）とは何ですか？',
        '''<b>定義</b><br>
母集団の情報がない場合に、まず初期標本から情報を取得し、その情報をもとに層化抽出を行う二段階の手法。<br><br>

<b>特徴</b><br>
・第1相で母集団の情報を収集<br>
・第2相で層化抽出を実施<br><br>

<b>使用する場面</b><br>
・層化抽出を行いたいが母集団の情報がない場合<br>
・母集団の構造が不明な場合<br><br>

<b>メリット</b><br>
・効率性に優れる<br>
・母集団の事前情報が不要<br>
・層化抽出の利点を活用できる<br><br>

<b>デメリット</b><br>
・サンプルサイズが小さいと偏りが生じやすい<br>
・二段階のプロセスが必要<br><br>

<b>具体例</b><br>
ある地域の住民の健康調査を行う場合：<br>
第1相：一部の住民から年齢構成などの基本情報を収集<br>
第2相：得られた年齢構成に基づいて層を作り、各層から詳細な健康調査の対象者を抽出<br><br>

<small>出典：統計WEB「標本の抽出方法」</small>'''
    ]
)
deck.add_note(note8)

# カード9: 実験研究
note9 = genanki.Note(
    model=model,
    fields=[
        '実験研究とは何ですか？主な種類を挙げてください。',
        '''<b>定義</b><br>
研究対象に対して何らかの介入（投薬や治療など）を行い、その効果を検証するための研究デザイン。<br><br>

<b>主な種類</b><br><br>

<b>1. ランダム化比較試験（RCT: Randomized Controlled Trial）</b><br>
実験群と対照群への割り付けをランダムに行う前向き研究。<br>
・医師の選別バイアスや参加者の期待効果などの偏りが両群で等確率で発生<br>
・差異は介入効果として解釈できる<br>
・エビデンスレベルが最も高い<br><br>

<b>2. クロスオーバー試験</b><br>
対象者を2群に分け、介入実施後に群を入れ替えて再度実施する前向き研究。<br>
・同じ対象者で比較できる利点<br>
・持ち越し効果（先の介入の効果が残る）が課題<br><br>

<b>特徴</b><br>
・因果関係の検証に適している<br>
・高いエビデンスレベル<br>
・倫理的配慮が必要<br><br>

<small>出典：統計WEB「研究デザイン」</small>'''
    ]
)
deck.add_note(note9)

# カード10: 観察研究
note10 = genanki.Note(
    model=model,
    fields=[
        '観察研究とは何ですか？主な種類を挙げてください。',
        '''<b>定義</b><br>
研究対象に対して介入を行わずに、観察によってデータを集めて解析を行う研究デザイン。<br><br>

<b>主な種類</b><br><br>

<b>1. 横断研究（Cross-sectional Study）</b><br>
ある1時点における断面的調査。<br>
・要因と結果の関連を調べる<br>
・過去や未来への調査拡張はない<br>
・実施が比較的容易<br><br>

<b>2. コホート研究（Cohort Study）</b><br>
特定の特性を持つ群と持たない群を時系列で観察し、疾患発生との関係を調べる。<br>
・前向き研究と後ろ向き研究の両方がある<br>
・因果関係の推定が可能<br><br>

<b>3. ケースコントロール研究（症例対照研究）</b><br>
患者群（症例）と対照群の既往歴や特性を遡行調査し、関連性を検討する後ろ向き研究。<br>
・稀な疾患研究に適している<br>
・比較的短期間で実施可能<br><br>

<b>特徴</b><br>
・倫理的な制約が少ない<br>
・実施が比較的容易<br>
・因果関係の特定には限界がある<br><br>

<small>出典：統計WEB「研究デザイン」</small>'''
    ]
)
deck.add_note(note10)

# カード11: 研究デザインのエビデンスレベル
note11 = genanki.Note(
    model=model,
    fields=[
        '研究デザインのエビデンスレベルを高い順に並べてください。',
        '''<b>エビデンスレベル（高い順）</b><br><br>

<b>1. システマティックレビュー／メタアナリシス</b><br>
複数の研究結果を統合的に分析<br><br>

<b>2. ランダム化比較試験（RCT）</b><br>
無作為割付による実験研究<br><br>

<b>3. 分析的観察研究</b><br>
・コホート研究<br>
・ケースコントロール研究<br><br>

<b>4. 記述的研究</b><br>
・横断研究<br>
・症例報告<br><br>

<b>重要な注意点</b><br>
・エビデンスレベルが高い＝良い研究、ではない<br>
・研究目的、臨床的な問題、必要なエビデンスレベル、研究の実施可能性を考慮して選択すべき<br>
・適切な研究デザインの選択が重要<br><br>

<small>出典：統計WEB「研究デザイン」</small>'''
    ]
)
deck.add_note(note11)

# カード12: 抽出方法の比較
note12 = genanki.Note(
    model=model,
    fields=[
        '6つの主要な標本抽出方法を比較してください。',
        '''<b>標本抽出方法の比較</b><br><br>

<table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
<tr>
<th>抽出方法</th>
<th>特徴</th>
<th>主な利点</th>
<th>主な欠点</th>
</tr>
<tr>
<td><b>単純無作為抽出</b></td>
<td>完全にランダムに抽出</td>
<td>偏りがない</td>
<td>母集団情報が必要</td>
</tr>
<tr>
<td><b>層化抽出</b></td>
<td>層に分けて各層から抽出</td>
<td>推定精度が高い</td>
<td>事前の層情報が必要</td>
</tr>
<tr>
<td><b>集落抽出</b></td>
<td>クラスター単位で抽出</td>
<td>効率的・低コスト</td>
<td>偏りが生じやすい</td>
</tr>
<tr>
<td><b>系統抽出</b></td>
<td>一定間隔で抽出</td>
<td>実施が簡単</td>
<td>周期性に注意</td>
</tr>
<tr>
<td><b>多段抽出</b></td>
<td>段階的に抽出</td>
<td>大規模調査向き</td>
<td>精度が低下しやすい</td>
</tr>
<tr>
<td><b>二相抽出</b></td>
<td>2段階で抽出</td>
<td>事前情報不要</td>
<td>プロセスが複雑</td>
</tr>
</table>
<br>

<b>使い分けのポイント</b><br>
・母集団情報が十分 → 単純無作為抽出、層化抽出<br>
・大規模調査 → 多段抽出、集落抽出<br>
・効率重視 → 系統抽出、集落抽出<br>
・精度重視 → 層化抽出<br><br>

<small>出典：統計WEB「標本の抽出方法」</small>'''
    ]
)
deck.add_note(note12)

# .apkgファイルとして保存
output_file = '/Users/sasaki/sample_and_sampling_verified.apkg'
genanki.Package(deck).write_to_file(output_file)
print(f"Ankiパッケージが作成されました: {output_file}")
print(f"カード枚数: {len(deck.notes)}")
