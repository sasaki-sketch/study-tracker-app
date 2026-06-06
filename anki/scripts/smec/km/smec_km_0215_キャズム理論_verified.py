"""
Ankiカード: キャズム理論（タニワタリ軍団）
科目: 中小企業診断士_企業経営理論
セクション: 02_競争戦略
作成日: 2026-04-23
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki/02_Personal/anki')
from anki_card_css_template import CARD_CSS

model_id = 1702150001
deck_id = 1702150002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_キャズム理論',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
        },
    ],
    css=CARD_CSS
)

my_deck = genanki.Deck(
    deck_id,
    '中小企業診断士_企業経営理論::02_競争戦略::キャズム理論'
)

question = '''<span class="important">タニワタリ軍団</span>が渡る「<b>深い谷</b>」とは？<br><br>・<b>提唱者と著作（発表年）</b>は？<br>・<b>5購買層と%（イノベーター理論）</b>は？<br>・<b>キャズムが発生する理由</b>は？<br>・「戦士かつイベント運営」の<b>二重役</b>の意味は？'''

answer = '''<b>Crossing the Chasm</b>（キャズム理論）

<div class="formula">
<b>■ 提唱</b><br>
<b>Geoffrey A. Moore</b>（ジェフリー・ムーア）<br>
『<b>Crossing the Chasm</b>』<b>1991年</b>出版<br>
→ E.Rogersの『<b>イノベーション普及理論</b>』（1962）を土台に<br>
　ハイテク製品特有の「断絶」を追加
</div>

<div class="example">
<b>■ 5購買層（Rogers のイノベーター理論）と割合</b>
<table>
<tr><th>段階</th><th>名称</th><th>%</th><th>価値観</th></tr>
<tr><td>①</td><td>Innovators（革新者）</td><td><b>2.5%</b></td><td>技術そのものが好き</td></tr>
<tr><td>②</td><td>Early Adopters（初期採用者）</td><td><b>13.5%</b></td><td>「<b>新しさ</b>」・先見性</td></tr>
<tr><td colspan="4" style="text-align:center; background:#ffecb3; color:#d32f2f;">★<b>キャズム（深い谷）</b>★</td></tr>
<tr><td>③</td><td>Early Majority（前期追随層）</td><td><b>34%</b></td><td>「<b>安心感・実績</b>」</td></tr>
<tr><td>④</td><td>Late Majority（後期追随層）</td><td><b>34%</b></td><td>周りが使っているから</td></tr>
<tr><td>⑤</td><td>Laggards（遅延者）</td><td><b>16%</b></td><td>変化を嫌う</td></tr>
</table>
</div>

<div class="example">
<b>■ なぜキャズムが生まれる？</b><br>
<b>② Early Adopters</b>: 「<b>新しさ</b>」を評価（先見性・冒険心）<br>
<b>③ Early Majority</b>: 「<b>安心感・実績</b>」を評価（保守的・慎重）<br>
→ <b>価値基準が断絶</b>している！<br>
→ 2.5% + 13.5% = <b>16%の壁</b>を越えられず頓挫する製品が多い<br>
　（多くのハイテクスタートアップの死因）
</div>

<div class="example">
<b>■ タニワタリ軍団の「二重役」</b><br>
【<b>戦士モード</b>】自らもキャズムを渡る<br>
　例: Zoomがパンデミックで一気に大衆化 / ChatGPT<br><br>
【<b>イベント運営モード</b>】他の6戦士が主流化する際に<b>橋を架ける</b><br>
　└ ハタタテ開拓者の旗 → 大衆化には軍団の橋が必要<br>
　└ アオウミ海賊のニッチ王国 → 主流市場進出には軍団の橋<br>
　└ ハカイ錬金術師の破壊技術 → 市場テイクオフに軍団の橋
</div>

<div class="example">
<b>■ キャズムを渡る方法（Mooreの処方箋）</b><br>
・<b>一点集中</b>: 特定ニッチ市場（ボウリングのピン1本目）を制覇<br>
・<b>ホールプロダクト</b>: 関連サービスも含めた<b>完成品</b>として提供<br>
・<b>実績・事例</b>の可視化で Early Majority の不安を解消<br>
・<b>口コミ連鎖</b>で1つの市場から隣接市場へ転がす（ボウリング・アレー）
</div>

<div class="source">出典: Geoffrey A. Moore『キャズム』（翔泳社、原著1991年・改訂版2014年）、E.Rogers『Diffusion of Innovations』(1962); スタディング 中小企業診断士 マーケティング関連解説</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

output_path = '/Users/sasaki/02_Personal/anki/anki/scripts/smec/km/smec_km_0215_キャズム理論_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
