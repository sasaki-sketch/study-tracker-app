"""
Ankiカード: 相補効果と相乗効果
科目: 中小企業診断士_企業経営理論
セクション: 03_成長戦略・国際経営
作成日: 2026-03-15
"""

import genanki
import sys
sys.path.insert(0, '/Users/sasaki')
from anki_card_css_template import CARD_CSS

# モデル定義
model_id = 1703080001
deck_id = 1703080002

my_model = genanki.Model(
    model_id,
    '中小企業診断士_企業経営理論_相補効果と相乗効果',
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
    '中小企業診断士_企業経営理論::03_成長戦略・国際経営::相補効果と相乗効果'
)

# カード内容
question = '''多角化における「相乗効果」「相補効果」「範囲の経済性」の<span class="important">定義の違い</span>と、それぞれの具体例を答えよ'''

answer = '''<b>Synergy / Complementary Effect / Economies of Scope</b>

<p>多角化によって得られる3つの異なる効果。混同しやすいが、メカニズムが異なる。</p>

<div class="formula">
<table>
<tr><th></th><th>相乗効果</th><th>相補効果</th><th>範囲の経済性</th></tr>
<tr><td><b>英語</b></td><td>Synergy</td><td>Complementary Effect</td><td>Economies of Scope</td></tr>
<tr><td><b>イメージ</b></td><td>1+1 &gt; 2</td><td>1+1 = 2</td><td>コスト削減</td></tr>
<tr><td><b>相互作用</b></td><td><span class="important">直接的</span></td><td><span class="important">間接的</span>（なし）</td><td>資源共有</td></tr>
<tr><td><b>着目点</b></td><td>売上・価値の増幅</td><td>遊休資源の補完</td><td>コスト効率</td></tr>
</table>
</div>

<div class="example">
<b>具体例:</b><br>
・<b>相乗効果</b>: TAC（講座×出版）― 講義データがテキスト開発を強化し、テキストの質がブランドを向上させる。<b>事業間に直接的な相互作用</b>がある<br><br>
・<b>相補効果</b>: 二毛作（夏にじゃがいも、冬にほうれん草）、スキー場の夏季キャンプ場営業 ― 事業間に直接の関連はないが、<b>遊休資源を時間的に補完</b>して活用<br><br>
・<b>範囲の経済性</b>: シャープの液晶技術（TV・スマホ・車載等に応用）― 既存の技術・設備を<b>複数事業で共有</b>しコストを削減
</div>

<p><b>注意</b>: 相乗効果は特定の事業の「組み合わせ」が重要（AとBだから生まれる）。相補効果は組み合わせ自体に意味はなく、遊休期間を埋められれば別の事業でもよい。範囲の経済性は売上増ではなくコスト効率の概念である。</p>

<div class="source">出典: たかぴーの中小企業診断士試験攻略ブログ、東大OCW 経営戦略講義資料</div>'''

my_note = genanki.Note(
    model=my_model,
    fields=[question, answer]
)

my_deck.add_note(my_note)

# .apkg出力
output_path = '/Users/sasaki/study_app/anki/scripts/smec/km/smec_km_0308_相補効果と相乗効果_verified.apkg'
genanki.Package(my_deck).write_to_file(output_path)
print(f"Generated: {output_path}")
